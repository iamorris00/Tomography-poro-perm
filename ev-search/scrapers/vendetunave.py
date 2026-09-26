"""Scrape Vendetunave.co for used electric SUV/crossover listings.

Strategy: the site's sitemap (sitemap-vehicles.xml) lists every listing URL as a
static XML file, with brand/model in the path. We filter that list to known EV
SUV/crossover model names (excluding tiny city cars and DM-i/PHEV hybrids by
URL text), then fetch each candidate's detail page. Each detail page is a
Next.js page embedding a `__NEXT_DATA__` JSON blob with the full listing
record (price, km, year, city, department, fuel type), which we parse
directly -- no JS rendering needed.

Usage: python3 vendetunave.py [out.csv]
"""
import csv
import json
import re
import sys
import time
import urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36"
SITEMAP = "https://www.vendetunave.co/sitemap-vehicles.xml"
DELAY = 1.0

# SUV/crossover EV model name fragments (case-insensitive), used to filter the
# sitemap's listing URLs before fetching detail pages.
SUV_KEYWORDS = [
    "song", "yuan", "atto", "tang", "ex30", "ex40", "c40", "kona", "niro",
    "marvel", "zeekr", "deepal", "leapmotor", "ariya", "mach-e", "id.4",
    "id4", "bz4x", "equinox", "blazer", "eqa", "eqb", "eqc", "eqs", "ev6",
    "ev5", "ev3", "ev9", "ioniq", "e-2008",
]
# Drop plug-in hybrid variants (not 100% electric) by URL text.
HYBRID_EXCLUDE = ["dmi", "dm-i", "hibrid", "phev", "hybrid"]

TARGET_CITIES = {
    "bogota", "bogotá", "cajica", "cajicá", "chia", "chía", "cota",
    "zipaquira", "zipaquirá", "sopo", "sopó", "tocancipa", "tocancipá",
    "tenjo", "tabio", "la calera", "funza", "mosquera",
}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "es-CO,es;q=0.9"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def candidate_urls():
    xml = fetch(SITEMAP)
    locs = re.findall(r"<loc>([^<]+)</loc>", xml)
    cands = []
    for u in locs:
        ul = u.lower()
        if not any(k in ul for k in SUV_KEYWORDS):
            continue
        if not re.search(r"-\d+$", u):
            continue  # skip bare brand/model category pages (no listing id)
        if any(h in ul for h in HYBRID_EXCLUDE):
            continue
        cands.append(u)
    return sorted(set(cands))


def parse_detail(url):
    try:
        html = fetch(url)
    except Exception as e:
        print(f"WARN {url}: {e}", file=sys.stderr)
        return None
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    if not m:
        return None
    try:
        data = json.loads(m.group(1))
        v = data["props"]["pageProps"]["data"]["vehiculo"]
    except (KeyError, TypeError, json.JSONDecodeError):
        return None
    fuel = str(v.get("fuel_label", "")).strip().lower()
    if fuel != "eléctrico" and fuel != "electrico":
        return None  # skip hybrids/gas that slipped through URL filter
    city = str(v.get("city_label", "")).strip()
    dept = str(v.get("department_label", "")).strip()
    if city.lower() not in TARGET_CITIES and dept.lower() not in ("cundinamarca", "bogota d.c.", "bogotá d.c."):
        return None
    return dict(
        site="vendetunave",
        title=v.get("title", ""),
        price_cop=v.get("precio", ""),
        year=v.get("ano", ""),
        km=v.get("kilometraje", ""),
        location=f"{city}, {dept}".strip(", "),
        url=url,
    )


def main(out):
    rows = []
    try:
        cands = candidate_urls()
    except Exception as e:
        print(f"FATAL fetching sitemap: {e}", file=sys.stderr)
        cands = []
    print(f"{len(cands)} candidate URLs from sitemap", file=sys.stderr)
    for i, url in enumerate(cands):
        row = parse_detail(url)
        if row:
            rows.append(row)
        if i % 25 == 0:
            print(f"...{i}/{len(cands)}", file=sys.stderr)
        time.sleep(DELAY)
    with open(out, "w", newline="", encoding="utf-8") as f:
        fields = ["site", "title", "price_cop", "year", "km", "location", "url"]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} listings -> {out}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "vendetunave_raw.csv")
