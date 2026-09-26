"""Scrape TuCarro (MercadoLibre Colombia) search results for used EVs near Bogotá / Cajicá.

Usage: python3 tucarro.py [out.csv]
Writes one row per listing card: title, price_cop, year, km, location, region, url.
"""
import csv
import html
import re
import sys
import time
import urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
PRICE = "_PriceRange_70000000-101000000"
# Bogotá D.C. and Cundinamarca (Cajicá, Chía, Cota, Zipaquirá, Sopó, Tocancipá, Funza...).
REGIONS = ["bogota-dc", "cundinamarca"]
PAGE_SIZE = 48


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "es-CO,es;q=0.9"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def text(fragment):
    t = re.sub(r"<[^>]+>", "|", fragment)
    return [html.unescape(p).strip() for p in t.split("|") if p.strip()]


def parse(page, region):
    rows = []
    for card in page.split("poly-card")[1:]:
        m = re.search(r'poly-component__title"[^>]*>([^<]+)', card)
        u = re.search(r'href="(https://(?:articulo|auto)\.tucarro\.com\.co/[^"#?]+)', card)
        if not (m and u):
            continue
        parts = text(card[:6000])
        title = html.unescape(m.group(1)).strip()
        price = year = km = loc = ""
        for i, p in enumerate(parts):
            if p == "$" and not price and i + 1 < len(parts):
                price = parts[i + 1].replace(".", "")
            elif re.fullmatch(r"(19|20)\d\d", p) and not year:
                year = p
            elif p.endswith("Km") and not km:
                km = p.replace(" Km", "").replace(".", "")
                if i + 1 < len(parts):
                    loc = parts[i + 1]
        rows.append(dict(title=title, price_cop=price, year=year, km=km,
                         location=loc, region=region, url=u.group(1)))
    return rows


def main(out):
    seen, rows = set(), []
    for region in REGIONS:
        for start in range(0, PAGE_SIZE * 10, PAGE_SIZE):
            desde = f"_Desde_{start + 1}" if start else ""
            url = f"https://carros.tucarro.com.co/electrico/{region}/2024-2027/{desde}{PRICE}_NoIndex_True"
            try:
                got = parse(fetch(url), region)
            except Exception as e:  # keep going on one bad page
                print(f"WARN {url}: {e}", file=sys.stderr)
                break
            new = [r for r in got if r["url"] not in seen]
            if not new:
                break
            seen.update(r["url"] for r in new)
            rows += new
            time.sleep(1.5)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["title"])
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} listings -> {out}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "tucarro_raw.csv")
