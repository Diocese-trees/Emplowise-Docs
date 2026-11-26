#!/usr/bin/env python3
"""Produce a full granular per-page markdown dump for Phase 1 backup."""
import json, os, re
from urllib.parse import urljoin, urlparse

D = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(D, "extracted.json")))
BASE = "https://diocese-trees.github.io/Emplowise-Website-Phase-I/"
ORDER = ["index","what-we-are","what-we-do","what-we-are-building","why-emplowise",
         "emplostart","faq","contact","free-hr-audit","company-profile","portfolio",
         "docs","pitch-deck","terms","privacy"]
SITEMAP = {BASE, BASE+"what-we-are/", BASE+"what-we-do/", BASE+"what-we-are-building/",
           BASE+"why-emplowise/", BASE+"emplostart/", BASE+"faq/", BASE+"contact/",
           BASE+"free-hr-audit/", BASE+"terms/", BASE+"privacy/", BASE+"company-profile/",
           BASE+"portfolio/", BASE+"docs/"}

def nav_footer(r):
    # reconstruct nav/footer by heading/section isn't reliable; use anchor order & classes are lost.
    # Instead list all internal anchors with text, grouped by href target label.
    return r["internal_links"]

def schema_types(ld):
    out=[]
    def walk(node):
        if isinstance(node, dict):
            t=node.get("@type")
            if t: out.append(t if isinstance(t,str) else "+".join(t))
            for v in node.values(): walk(v)
        elif isinstance(node, list):
            for v in node: walk(v)
    walk(ld); return out

def deep_get(d, keys):
    res=[]
    def walk(node, path):
        if isinstance(node, dict):
            for k,v in node.items():
                if k in keys and not isinstance(v,(dict,list)): res.append((path+"/"+k, v))
                walk(v, path+"/"+k)
        elif isinstance(node, list):
            for i,v in enumerate(node): walk(v, f"{path}[{i}]")
    walk(d, "")
    return res

lines=[]
for name in ORDER:
    r = data[name]
    lines.append(f"\n\n================ PAGE: /{'' if name=='index' else name+'/'}  (file {name}.html) ================")
    lines.append(f"URL: {r['page_url']}")
    lines.append(f"In sitemap: {'YES' if r['page_url'] in SITEMAP else 'NO'}")
    lines.append(f"Title ({r['title_len']}): {r['title']}")
    lines.append(f"Meta description ({r['desc_len']}): {r['meta_description']}")
    lines.append(f"Meta robots: {r['meta_robots']}")
    lines.append(f"Canonical: {r['canonical']}")
    lines.append(f"Viewport: {r['viewport']} | theme-color: {r['theme_color']}")
    lines.append(f"OG: {json.dumps(r['og'], ensure_ascii=False)}")
    lines.append(f"Twitter: {json.dumps(r['twitter'], ensure_ascii=False)}")
    lines.append(f"Word count (body, JS-rendered excluded): {r['body_word_count']}")
    lines.append("--- Headings (H1-H3) ---")
    for h in r["headings"]:
        lines.append(f"  H{h['level']}: {h['text']}")
    lines.append("--- Images (src basename | alt | w x h | loading) ---")
    for im in r["images"]:
        src=im['src']; b=src.split('?')[0].split('/')[-1]
        lines.append(f"  {b} | alt={im['alt']!r} | {im['width']}x{im['height']} | loading={im['loading']}")
    lines.append(f"  images missing alt: {len(r['img_no_alt'])}")
    lines.append("--- Internal links (resolved path | anchor text) ---")
    seen=set()
    for il in r["internal_links"]:
        key=(il['resolved'], il['text'])
        if key in seen: continue
        seen.add(key)
        pp = il['resolved'].replace(BASE,'/')
        lines.append(f"  {pp} | {il['text']!r}")
    if r["external_links"]:
        lines.append("--- External links ---")
        for ex in r["external_links"]:
            lines.append(f"  {ex['href']} | {ex['text']!r}")
    if r["mailto_tel"]:
        lines.append("--- mailto/tel ---")
        for m in r["mailto_tel"]:
            lines.append(f"  {m['href']} | {m['text']!r}")
    lines.append(f"--- JSON-LD blocks: {len(r['ldjson'])} ---")
    for i,ld in enumerate(r["ldjson"]):
        st = schema_types(ld)
        lines.append(f"  [{i}] @types found: {sorted(set(st))}")
        dates = deep_get(ld, {"datePublished","dateModified","dateCreated","uploadDate"})
        auths = deep_get(ld, {"author","name","legalName","founder","employee","sameAs"})
        for path,v in dates: lines.append(f"      DATE {path} = {v}")
        # print schema compact
        lines.append("      JSON: " + json.dumps(ld, ensure_ascii=False)[:1500])
    lines.append("--- BODY TEXT (full) ---")
    lines.append(r["body_text"])

open(os.path.join(D,"..","_crawl","detailed_dump.txt"),"w").write("\n".join(lines))
print("wrote detailed_dump.txt", len("\n".join(lines)), "chars")
