"""Acceptance pass for the internal executive report.

Builds nothing itself: run generators/report-ui/build.py first, then

    python3 generators/report-ui/test_report.py [--shots /tmp/report-shots]

It serves reports/ on a free local port, drives the page with Playwright and
system Chromium at 1440x900 and 360x780 in both themes, and exits non-zero on
any failed check, console error or page error.
"""

import argparse, functools, http.server, json, pathlib, socket, sys, tempfile, threading
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[2]
REPORTS = ROOT / "reports"
STEM = "Emplowise-Executive-Report-2026"

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--shots", default=None, help="directory for screenshots (default: a temp dir)")
args = parser.parse_args()
SHOTS = pathlib.Path(args.shots) if args.shots else pathlib.Path(tempfile.mkdtemp(prefix="report-shots-"))
SHOTS.mkdir(parents=True, exist_ok=True)

if not (REPORTS / f"{STEM}.html").exists():
    sys.exit("build the report first: python3 generators/report-ui/build.py")

handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(REPORTS))
httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
threading.Thread(target=httpd.serve_forever, daemon=True).start()
URL = f"http://127.0.0.1:{httpd.server_address[1]}/{STEM}.html"

errors, results = [], []

def check(name, cond, extra=""):
    results.append((name, bool(cond), extra))

with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/chromium", args=["--no-sandbox"])
    for width, height, theme in ((1440, 900, "light"), (1440, 900, "dark"), (360, 780, "light"), (360, 780, "dark")):
        ctx = b.new_context(viewport={"width": width, "height": height}, device_scale_factor=1)
        pg = ctx.new_page()
        pg.on("console", lambda m: errors.append(f"[{width}/{theme}] console {m.type}: {m.text}") if m.type == "error" else None)
        pg.on("pageerror", lambda e: errors.append(f"[{width}/{theme}] pageerror: {e}"))
        pg.goto(URL, wait_until="load")
        pg.wait_for_timeout(600)
        tag = f"{width}/{theme}"
        if theme == "dark":
            pg.click("#theme-toggle")
            pg.wait_for_timeout(200)
        check(tag + " theme attr", pg.get_attribute("html", "data-theme") == theme)

        # populated content
        check(tag + " copy blocks", pg.locator("#copy-grid .copy-block").count() == 12, str(pg.locator("#copy-grid .copy-block").count()))
        check(tag + " lint clean", "12 of 12" in pg.inner_text("#lint-summary"), pg.inner_text("#lint-summary"))
        check(tag + " months", pg.locator("#month-list .month").count() == 6)
        check(tag + " rows", pg.locator("#emp-body tr").count() == 22, str(pg.locator("#emp-body tr").count()))
        check(tag + " dept chart bars", pg.locator("#chart-dept svg rect").count() > 8)
        check(tag + " trend chart", pg.locator("#chart-trend svg circle").count() == 6)
        check(tag + " spark", pg.locator("#retention-spark polyline").count() == 1)
        check(tag + " checks", pg.locator("#comp-list .check").count() == 8)
        check(tag + " schema json", "employee_id" in pg.inner_text("#json-schema"))
        check(tag + " csv sample", pg.inner_text("#csv-sample").startswith("employee_id,name"))

        # no horizontal page overflow
        ow = pg.evaluate("document.documentElement.scrollWidth")
        check(tag + " no page overflow", ow <= width + 1, f"scrollWidth={ow}")
        # element overflow beyond viewport
        bad = pg.evaluate("""() => {
          const out=[]; const w=document.documentElement.clientWidth;
          document.querySelectorAll('main *, header *, footer *').forEach(el=>{
            const r=el.getBoundingClientRect();
            if(r.width>0 && (r.right>w+2 || r.left<-2)) {
              const p=el.closest('.table-scroll,.code-card,svg,.header-nav,.drawer');
              if(!p) out.push(el.tagName+'.'+(el.className||'').toString().slice(0,40)+' right='+Math.round(r.right));
            }
          });
          return out.slice(0,10);
        }""")
        check(tag + " no element overflow", not bad, json.dumps(bad))

        # KPI live values
        vals = pg.evaluate("""() => ({risk:document.getElementById('risk-value').textContent,
          ret:document.getElementById('retention-value').textContent,
          perf:document.getElementById('perf-count').textContent,
          comp:document.getElementById('comp-pass').textContent,
          flag:document.getElementById('flag-contract-text').textContent})""")
        results.append((tag + " KPI values", True, json.dumps(vals)))

        # control interactions
        before = pg.inner_text("#risk-value")
        pg.eval_on_selector("#w-contract", "el=>{el.value=100;el.dispatchEvent(new Event('input',{bubbles:true}))}")
        pg.wait_for_timeout(120)
        after = pg.inner_text("#risk-value")
        check(tag + " weight slider live", before != after, f"{before}->{after}")
        pg.eval_on_selector("#perf-floor", "el=>{el.value=80;el.dispatchEvent(new Event('input',{bubbles:true}))}")
        pg.wait_for_timeout(120)
        check(tag + " perf floor live", pg.inner_text("#perf-count") != vals["perf"], pg.inner_text("#perf-count"))
        pg.click("#threshold-up"); pg.wait_for_timeout(80)
        check(tag + " threshold stepper", pg.inner_text("#threshold-out") == "60", pg.inner_text("#threshold-out"))
        pg.select_option("#notice-floor", "8"); pg.wait_for_timeout(120)
        check(tag + " notice floor select", pg.inner_text("#risk-value") != after)
        pg.select_option("#review-window", "12"); pg.wait_for_timeout(120)
        pg.select_option("#filter-dept", "Sales"); pg.wait_for_timeout(120)
        check(tag + " dept filter", pg.locator("#emp-body tr").count() == 4, str(pg.locator("#emp-body tr").count()))
        pg.fill("#emp-search", "Kamran"); pg.wait_for_timeout(150)
        check(tag + " search", pg.locator("#emp-body tr").count() == 1)
        pg.fill("#emp-search", ""); pg.select_option("#filter-dept", "all"); pg.wait_for_timeout(120)
        pg.click("#reset-model"); pg.wait_for_timeout(200)
        pg.click("label[for=flagged-only]"); pg.wait_for_timeout(150)
        flagged = pg.locator("#emp-body tr").count()
        check(tag + " flagged filter", 0 < flagged < 22, str(flagged))
        pg.click("label[for=flagged-only]"); pg.wait_for_timeout(120)
        pg.click("label[for=density]"); pg.wait_for_timeout(120)
        pg.click("label[for=density]"); pg.wait_for_timeout(120)
        pg.select_option("#sort-by", "salary_desc"); pg.wait_for_timeout(120)
        check(tag + " sort", "Bilal" in pg.inner_text("#emp-body tr:first-child"))
        pg.click("#emp-table th[data-sort='name']"); pg.wait_for_timeout(120)
        check(tag + " header sort", pg.get_attribute("#emp-table th[data-sort='name']", "aria-sort") in ("ascending", "descending"))

        # selection + bulk review + undo
        pg.check("#select-all"); pg.wait_for_timeout(120)
        check(tag + " bulk enabled", pg.is_enabled("#bulk-review"))
        ret_before = pg.inner_text("#retention-value")
        pg.click("#bulk-review"); pg.wait_for_timeout(200)
        check(tag + " bulk review changes index", pg.inner_text("#retention-value") != ret_before,
              f'{ret_before}->{pg.inner_text("#retention-value")}')
        check(tag + " undo enabled", pg.is_enabled("#undo-btn"))
        pg.click("#undo-btn"); pg.wait_for_timeout(200)
        check(tag + " undo restores", pg.inner_text("#retention-value") == ret_before)

        # drawer edit / save / delete / undo
        pg.click("#emp-body tr:first-child"); pg.wait_for_timeout(450)
        check(tag + " drawer open", "is-open" in (pg.get_attribute("#drawer", "class") or ""))
        check(tag + " drawer fields", pg.locator("#drawer-body input").count() >= 9)
        pg.fill("#d-salary", "99000")
        pg.fill("#d-perf", "44")
        pg.click("#drawer-save"); pg.wait_for_timeout(450)
        check(tag + " drawer closed after save", "is-open" not in (pg.get_attribute("#drawer", "class") or ""))
        check(tag + " saved value visible", "99,000" in pg.inner_text("#emp-body"))
        pg.click("#undo-btn"); pg.wait_for_timeout(200)
        check(tag + " undo edit", "99,000" not in pg.inner_text("#emp-body"))

        # invalid save rejected
        pg.click("#emp-body tr:first-child"); pg.wait_for_timeout(400)
        pg.fill("#d-perf", "150"); pg.click("#drawer-save"); pg.wait_for_timeout(200)
        check(tag + " invalid save blocked", "is-open" in (pg.get_attribute("#drawer", "class") or ""))
        pg.fill("#d-perf", "70")
        pg.click("#drawer-delete"); pg.wait_for_timeout(400)
        check(tag + " delete works", pg.locator("#emp-body tr").count() == 21, str(pg.locator("#emp-body tr").count()))
        pg.click("#undo-btn"); pg.wait_for_timeout(200)
        check(tag + " undo delete", pg.locator("#emp-body tr").count() == 22)

        # add employee
        pg.click("#add-employee"); pg.wait_for_timeout(450)
        check(tag + " add employee", pg.locator("#emp-body tr").count() == 23)
        pg.fill("#d-name", "Test Person"); pg.click("#drawer-save"); pg.wait_for_timeout(400)
        check(tag + " new person saved", "Test Person" in pg.inner_text("#emp-body"))
        pg.click("#undo-btn"); pg.wait_for_timeout(150); pg.click("#undo-btn"); pg.wait_for_timeout(200)
        check(tag + " undo add", pg.locator("#emp-body tr").count() == 22)

        # compliance toggle
        comp_before = pg.inner_text("#comp-pass")
        pg.click("#comp-list .check:nth-child(4)"); pg.wait_for_timeout(200)
        check(tag + " compliance toggle", pg.inner_text("#comp-pass") != comp_before,
              f'{comp_before}->{pg.inner_text("#comp-pass")}')
        pg.click("#undo-btn"); pg.wait_for_timeout(200)

        # simulate + reset
        pg.click("#simulate"); pg.wait_for_timeout(250)
        check(tag + " simulate advances date", "Dec 2026" in pg.inner_text("#dash-sub"), pg.inner_text("#dash-sub"))
        pg.click("#undo-btn"); pg.wait_for_timeout(200)
        pg.click("#reset-model"); pg.wait_for_timeout(250)
        check(tag + " reset model", pg.inner_text("#w-contract-out") == "45" and pg.inner_text("#threshold-out") == "55")

        # saved views
        pg.select_option("#filter-dept", "Design")
        pg.click("#save-view"); pg.wait_for_timeout(200)
        check(tag + " saved view chip", pg.locator("#saved-views .view-chip").count() >= 2)
        pg.select_option("#filter-dept", "all"); pg.wait_for_timeout(100)
        pg.click("#saved-views .view-chip:first-child"); pg.wait_for_timeout(200)
        check(tag + " saved view applies", pg.input_value("#filter-dept") == "Design")
        pg.click("#saved-views .view-chip:nth-child(2)"); pg.wait_for_timeout(150)
        pg.select_option("#filter-dept", "all"); pg.wait_for_timeout(100)

        # timeline
        pg.eval_on_selector("#month-slider", "el=>{el.value=4;el.dispatchEvent(new Event('input',{bubbles:true}))}")
        pg.wait_for_timeout(150)
        check(tag + " timeline scrub", pg.inner_text("#month-readout") == "Month 4 of 6")
        check(tag + " timeline flags", pg.locator("#month-list .flag").count() == 4)
        pg.click("#month-play"); pg.wait_for_timeout(3200)
        check(tag + " timeline play", pg.inner_text("#month-readout") in ("Month 3 of 6", "Month 4 of 6"), pg.inner_text("#month-readout"))
        pg.click("#month-reset"); pg.wait_for_timeout(150)
        check(tag + " timeline reset", pg.inner_text("#month-readout") == "Month 1 of 6")

        # CSV import: invalid then valid
        pg.fill("#csv-input", "employee_id,name\nX1,Test")
        pg.click("#csv-load"); pg.wait_for_timeout(200)
        check(tag + " import rejects bad header", pg.get_attribute("#import-result", "data-state") == "error")
        pg.click("#csv-fill"); pg.wait_for_timeout(150)
        pg.click("#csv-load"); pg.wait_for_timeout(250)
        check(tag + " import valid", pg.get_attribute("#import-result", "data-state") == "ok", pg.inner_text("#import-result"))
        bad = "employee_id,name,role,department,salary,start_date,contract_status,notice_period_weeks,performance_score,last_review_date,manager_id,risk_flags\n"
        bad += "E1,A,Role,Sales,-5,2026-01-01,permanent,4,50,,,\nE1,B,Role,Sales,5000,2026-13-01,unknown,99,150,,E9,\n"
        pg.fill("#csv-input", bad); pg.click("#csv-load"); pg.wait_for_timeout(200)
        check(tag + " import validation rules", pg.get_attribute("#import-result", "data-state") == "error", pg.inner_text("#import-result")[:160])
        pg.click("#csv-restore"); pg.wait_for_timeout(250)
        check(tag + " restore register", pg.locator("#emp-body tr").count() == 22)

        # exports
        for btn, name in (("#export-csv", ".csv"), ("#export-json", ".json"), ("#hero-export", ".csv"),
                          ("#download-schema", ".json"), ("#download-csv-sample", ".csv")):
            with pg.expect_download(timeout=8000) as dl:
                pg.click(btn)
            d = dl.value
            check(tag + " download " + btn, d.suggested_filename.endswith(name), d.suggested_filename)

        # copy buttons (clipboard permission granted below)
        ctx.grant_permissions(["clipboard-read", "clipboard-write"])
        pg.click("#copy-all"); pg.wait_for_timeout(250)
        clip = pg.evaluate("navigator.clipboard.readText()")
        check(tag + " copy all", "absence of HR" in clip or "Senior HR" in clip, clip[:60])
        pg.click("[data-copy-block='0']"); pg.wait_for_timeout(250)
        check(tag + " copy block", "already pays for HR" in pg.evaluate("navigator.clipboard.readText()"))

        # nav + progress
        pg.click("a[data-nav='dashboard']"); pg.wait_for_timeout(2200)
        check(tag + " nav current", pg.get_attribute("a[data-nav='dashboard']", "aria-current") == "true")
        rect = pg.evaluate("()=>{const r=document.getElementById('dashboard').getBoundingClientRect();return r.top}")
        check(tag + " anchor clears header", rect >= 0 and rect < 200, str(rect))
        check(tag + " progress fill", pg.evaluate("parseFloat(document.getElementById('progress-fill').style.width)") > 5)

        # reveals visible after scroll through
        pg.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        pg.wait_for_timeout(700)
        hidden = pg.evaluate("Array.from(document.querySelectorAll('.reveal')).filter(n=>getComputedStyle(n).opacity<0.9).length")
        check(tag + " reveals shown", hidden == 0, str(hidden))

        # contrast sample of key pairs
        contrast = pg.evaluate("""() => {
          function lum(c){const [r,g,b]=c.map(v=>{v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4)});return 0.2126*r+0.7152*g+0.0722*b}
          function parse(s){const m=s.match(/[\\d.]+/g).map(Number);return m.slice(0,3)}
          function bgOf(el){let n=el;while(n){const c=getComputedStyle(n).backgroundColor;const m=c.match(/[\\d.]+/g);if(m&&(m.length<4||+m[3]>0.5))return parse(c);n=n.parentElement}return [255,255,255]}
          const sel=['.kpi .meta','.kpi .name','.control .hint','.table-note','.copy-text','.month p','.priority .accept','.metric .src','tbody td','.check','.view-chip'];
          return sel.map(s=>{const el=document.querySelector(s);if(!el)return [s,null];const fg=parse(getComputedStyle(el).color);const bg=bgOf(el);
            const l1=lum(fg),l2=lum(bg);const ratio=(Math.max(l1,l2)+0.05)/(Math.min(l1,l2)+0.05);return [s,+ratio.toFixed(2),+getComputedStyle(el).fontSize.replace('px','')]});
        }""")
        results.append((tag + " contrast", True, json.dumps(contrast)))

        # touch targets
        small = pg.evaluate("""() => Array.from(document.querySelectorAll('button,input[type=checkbox],select')).filter(el=>{
          const r=el.getBoundingClientRect(); if(r.width===0) return false;
          if(el.closest('.check')) return false;
          return r.height<30;
        }).map(el=>el.id||el.className.toString().slice(0,30)).slice(0,12)""")
        results.append((tag + " small targets", True, json.dumps(small)))

        pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(300)
        pg.screenshot(path=str(SHOTS / f"{width}-{theme}-top.png"))
        pg.evaluate("document.getElementById('dashboard').scrollIntoView()"); pg.wait_for_timeout(600)
        pg.screenshot(path=str(SHOTS / f"{width}-{theme}-dash.png"))
        pg.evaluate("document.getElementById('case').scrollIntoView()"); pg.wait_for_timeout(500)
        pg.screenshot(path=str(SHOTS / f"{width}-{theme}-case.png"))
        ctx.close()
    b.close()

fails = [r for r in results if not r[1]]
for n, ok, extra in results:
    print(("PASS " if ok else "FAIL ") + n + ("  " + extra if extra else ""))
print("\nconsole/page errors:", len(errors))
for e in errors[:20]:
    print("  ", e)
print("screenshots:", SHOTS)
print("FAILURES:", len(fails))
sys.exit(1 if fails or errors else 0)