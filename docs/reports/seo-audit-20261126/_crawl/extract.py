#!/usr/bin/env python3
"""Extract granular on-page SEO data from crawled Emplowise Phase I HTML files."""
import json, os, re, sys
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse, urldefrag

BASE = "https://diocese-trees.github.io/Emplowise-Website-Phase-I/"
FILES = ["index","what-we-are","what-we-do","what-we-are-building","why-emplowise",
         "emplostart","faq","contact","free-hr-audit","terms","privacy",
         "company-profile","portfolio","docs","pitch-deck"]

class PageParser(HTMLParser):
    def __init__(self, page_url):
        super().__init__(convert_charrefs=True)
        self.page_url = page_url
        self.title_parts = []
        self.metas = []
        self.links = []          # <link rel=...>
        self.headings = []       # (level, text)
        self.images = []         # (src, alt, width, height, loading, decoding)
        self.anchors = []        # (href, text)
        self.ldjson = []         # raw JSON-LD strings
        self.og = {}
        self.twitter = {}
        self.body_parts = []
        self._in_title = False
        self._in_heading = None
        self._heading_buf = []
        self._in_anchor = False
        self._anchor_buf = []
        self._anchor_href = None
        self._in_ldjson = False
        self._ld_buf = []
        self._in_body = False
        self._skip = 0           # inside script/style/svg
        self._buf = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            name = (a.get("name") or "").lower()
            prop = (a.get("property") or "").lower()
            content = a.get("content", "")
            self.metas.append({"name": name or None, "property": prop or None, "content": content})
            if prop.startswith("og:"): self.og[prop] = content
            if name.startswith("twitter:"): self.twitter[name] = content
        elif tag == "link":
            self.links.append(a)
        elif tag in ("h1","h2","h3","h4","h5","h6"):
            self._in_heading = int(tag[1]); self._heading_buf = []
        elif tag == "img":
            self.images.append({
                "src": a.get("src",""), "alt": a.get("alt"),
                "width": a.get("width"), "height": a.get("height"),
                "loading": a.get("loading"), "decoding": a.get("decoding"),
                "srcset": a.get("srcset")})
        elif tag == "a":
            self._in_anchor = True; self._anchor_buf = []
            self._anchor_href = a.get("href")
        elif tag == "script":
            if (a.get("type") or "").lower() == "application/ld+json":
                self._in_ldjson = True; self._ld_buf = []
            else:
                self._skip += 1
        elif tag in ("style","svg","noscript"):
            self._skip += 1
        elif tag == "body":
            self._in_body = True

    def handle_startendtag(self, tag, attrs):
        if tag == "img":
            a = dict(attrs)
            self.images.append({
                "src": a.get("src",""), "alt": a.get("alt"),
                "width": a.get("width"), "height": a.get("height"),
                "loading": a.get("loading"), "decoding": a.get("decoding"),
                "srcset": a.get("srcset")})

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag in ("h1","h2","h3","h4","h5","h6"):
            if self._in_heading is not None:
                txt = re.sub(r"\s+", " ", "".join(self._heading_buf)).strip()
                if txt: self.headings.append({"level": self._in_heading, "text": txt})
            self._in_heading = None; self._heading_buf = []
        elif tag == "a":
            if self._in_anchor:
                txt = re.sub(r"\s+", " ", "".join(self._anchor_buf)).strip()
                self.anchors.append({"href": self._anchor_href, "text": txt})
            self._in_anchor = False; self._anchor_buf = []; self._anchor_href = None
        elif tag == "script":
            if self._in_ldjson:
                self.ldjson.append("".join(self._ld_buf)); self._in_ldjson = False; self._ld_buf = []
            elif self._skip > 0: self._skip -= 1
        elif tag in ("style","svg","noscript"):
            if self._skip > 0: self._skip -= 1

    def handle_data(self, data):
        if self._in_title: self.title_parts.append(data)
        if self._in_heading is not None: self._heading_buf.append(data)
        if self._in_anchor: self._anchor_buf.append(data)
        if self._in_ldjson: self._ld_buf.append(data)
        if self._in_body and self._skip == 0:
            s = data.strip()
            if s: self.body_parts.append(s)


def parse(path, page_url):
    with open(path, encoding="utf-8", errors="replace") as f:
        html = f.read()
    p = PageParser(page_url)
    p.feed(html)
    title = re.sub(r"\s+"," ", "".join(p.title_parts)).strip()
    desc = next((m["content"] for m in p.metas if m["name"]=="description"), None)
    robots_meta = next((m["content"] for m in p.metas if m["name"]=="robots"), None)
    canonical = next((l.get("href") for l in p.links if (l.get("rel") or "").lower()=="canonical"), None)
    viewport = next((m["content"] for m in p.metas if m["name"]=="viewport"), None)
    theme = next((m["content"] for m in p.metas if m["name"]=="theme-color"), None)
    body_text = " ".join(p.body_parts)
    # internal vs external links
    internal, external, anchors, mailto_tel = [], [], [], []
    for a in p.anchors:
        href = a["href"] or ""
        if href.startswith("#"): anchors.append(a); continue
        if href.startswith("mailto:") or href.startswith("tel:"): mailto_tel.append(a); continue
        absu = urljoin(page_url, href)
        du = urlparse(defrag := urldefrag(absu)[0])
        if du.netloc == urlparse(BASE).netloc:
            internal.append({"href": href, "resolved": defrag, "text": a["text"]})
        else:
            external.append({"href": defrag, "text": a["text"]})
    # ldjson parse
    parsed_ld = []
    for raw in p.ldjson:
        try: parsed_ld.append(json.loads(raw))
        except Exception as e: parsed_ld.append({"_parse_error": str(e), "_raw_head": raw[:400]})
    return {
        "page_url": page_url,
        "title": title, "title_len": len(title),
        "meta_description": desc, "desc_len": len(desc) if desc else 0,
        "meta_robots": robots_meta, "canonical": canonical,
        "viewport": viewport, "theme_color": theme,
        "og": p.og, "twitter": p.twitter,
        "headings": p.headings,
        "h_counts": {f"h{i}": sum(1 for h in p.headings if h["level"]==i) for i in range(1,7)},
        "images": p.images,
        "img_no_alt": [im["src"] for im in p.images if not im.get("alt")],
        "internal_links": internal,
        "external_links": external,
        "anchor_links": anchors,
        "mailto_tel": mailto_tel,
        "ldjson_raw_count": len(p.ldjson),
        "ldjson": parsed_ld,
        "body_text": body_text,
        "body_word_count": len(body_text.split()),
        "css_links": [l.get("href") for l in p.links if (l.get("rel") or "").lower()=="stylesheet"],
        "preloads": [l.get("href") for l in p.links if (l.get("rel") or "").lower()=="preload"],
        "icons": [l.get("href") for l in p.links if "icon" in (l.get("rel") or "").lower()],
    }

results = {}
all_internal = {}
for name in FILES:
    path = os.path.join(os.path.dirname(__file__), name + ".html")
    page_url = BASE + ("" if name=="index" else name + "/")
    r = parse(path, page_url)
    results[name] = r
    for il in r["internal_links"]:
        all_internal.setdefault(il["resolved"], 0)
        all_internal[il["resolved"]] += 1

with open(os.path.join(os.path.dirname(__file__), "extracted.json"), "w") as f:
    json.dump(results, f, indent=1)

print("PAGES:", len(results))
for name in FILES:
    r = results[name]
    print(f"[{name}] title={r['title_len']} desc={r['desc_len']} H1={r['h_counts']['h1']} H2={r['h_counts']['h2']} H3={r['h_counts']['h3']} imgs={len(r['images'])} noalt={len(r['img_no_alt'])} int={len(r['internal_links'])} ext={len(r['external_links'])} ld={r['ldjson_raw_count']} words={r['body_word_count']} robots={r['meta_robots']}")
print("\nDISCOVERED INTERNAL URLS (resolved, count):")
for u,c in sorted(all_internal.items(), key=lambda x:-x[1]):
    print(f"  {c:3d}  {u}")
