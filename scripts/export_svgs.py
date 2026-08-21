#!/usr/bin/env python3
"""Optional: export SVG snapshots of dashboard diagrams into assets/diagrams/.
Requires: pip install playwright && playwright install chromium
Run after generate.py. Not part of CI by default."""
import os, asyncio
from playwright.async_api import async_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
async def main():
    out = os.path.join(ROOT, "assets", "diagrams"); os.makedirs(out, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width":1500,"height":900})
        await pg.goto("file://" + os.path.join(ROOT, "site", "index.html"))
        await pg.click('#nav button[data-v="bpml"]')
        targets = ["L0"] + [f"L1:{i:02d}" for i in range(1,11)]
        # add all L2 ids
        l2 = await pg.evaluate("[...new Set(DATA.rows.map(r=>r.l1id))]")
        targets += [f"L2:{x}" for x in l2]
        for t in targets:
            await pg.evaluate(f"bpmlSel='{t}'; renderBpml()")
            svg = await pg.evaluate("document.querySelector('#bpmlsvg').innerHTML")
            name = t.replace(":","-").replace(".","_")
            open(os.path.join(out, f"bpml-{name}.svg"),"w").write(svg)
        for fl in ["UC3","UC2","UC1","UC4","CLD","INV"]:
            await pg.evaluate(f"curFlow='{fl}'; renderFlow()")
            svg = await pg.evaluate("document.querySelector('#flowsvg').innerHTML")
            open(os.path.join(out, f"e2e-{fl}.svg"),"w").write(svg)
        await b.close()
    print("SVGs exported to assets/diagrams/")
asyncio.run(main())
