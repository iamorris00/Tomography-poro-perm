"""Scrape Autogermana Usados (usadosautogermana.com, a VTEX storefront for BMW/MINI
certified pre-owned) for used electric vehicles.

The storefront runs on VTEX IO, which exposes a public, unauthenticated REST
catalog API at vtexcommercestable.com.br. Product search results already
include structured specs (Combustible/Precio/Kilometraje/Ubicación/Modelo) as
facet-style fields, so no JS rendering or HTML scraping is needed.

Usage: python3 autogermana.py [out.csv]
"""
import csv
import json
import sys
import time
import urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36"
BASE = "https://usadosautogermana.vtexcommercestable.com.br/api/catalog_system/pub/products/search/compra-vehiculos/carros-y-camionetas"
PAGE_SIZE = 50
DELAY = 1.5


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def field(p, name):
    v = p.get(name)
    return v[0] if isinstance(v, list) and v else (v or "")


def main(out):
    rows = []
    start = 0
    while True:
        url = f"{BASE}?_from={start}&_to={start + PAGE_SIZE - 1}"
        try:
            page = fetch(url)
        except Exception as e:
            print(f"WARN {url}: {e}", file=sys.stderr)
            break
        if not page:
            break
        for p in page:
            fuel = field(p, "Combustible").strip().lower()
            if fuel != "eléctrico" and fuel != "electrico":
                continue
            rows.append(dict(
                site="autogermana",
                title=p.get("productName", ""),
                price_cop=field(p, "Precio"),
                year=field(p, "Modelo"),
                km=field(p, "Kilometraje"),
                location=field(p, "Ubicación"),
                url=p.get("link", ""),
            ))
        if len(page) < PAGE_SIZE:
            break
        start += PAGE_SIZE
        time.sleep(DELAY)
    with open(out, "w", newline="", encoding="utf-8") as f:
        fields = ["site", "title", "price_cop", "year", "km", "location", "url"]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} listings -> {out}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "autogermana_raw.csv")
