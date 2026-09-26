# Used Electric SUV/Crossover Search — Non-TuCarro Sources

Search date: 2026-09-26. Target: 100% electric SUV/crossover, 2025-2027 (2024 accepted as a flagged exception), price COP 70M-101M, ≤25,000 km, Bogotá/Cundinamarca (Cajicá, Chía, Cota, Zipaquirá, Sopó, Tocancipá, Tenjo, Tabio, La Calera, Funza, Mosquera). Buyer's reference: **new Chery E5 Luxury, COP 89.99M, with 540°/360° camera + ADAS** — so a 360° camera is mandatory; base trims lacking it are flagged.

All rows below come from data actually fetched by the scrapers in `scrapers/` — nothing here is a search-snippet guess. Raw combined data: `data_other_sites_raw.csv` (85 listings, all sources).

## Sites: what worked, what didn't

| Site | Result | How |
|---|---|---|
| **Vendetunave.co** | WORKED — 26 EV listings in Bogotá/Cundinamarca | `sitemap-vehicles.xml` lists every listing URL (brand/model in path); filtered to EV SUV model names, excluded DM-i/PHEV hybrids by URL text; each detail page is Next.js with a `__NEXT_DATA__` JSON blob holding price/km/year/city/department/fuel — no JS needed. |
| **Autogermana Usados** (`usadosautogermana.com`) | WORKED — 59 electric listings (BMW/MINI/Volvo/BYD consignments), 0 in the 70-101M SUV band | It's a VTEX IO storefront; VTEX's public `catalog_system/pub/products/search` REST API (vtexcommercestable.com.br) returns structured specs (Combustible, Precio, Kilometraje, Ubicación, Modelo) directly as JSON. |
| **Carroya.com** | SKIPPED | Pure React SPA (CRA) with no server-rendered listing data; the real search UI is loaded via webpack Module Federation remote entries and calls an AWS API Gateway (`*.execute-api.us-east-2.amazonaws.com/pro`) that returned `403 Missing Authentication Token` on every path guessed within the time budget. |
| **Autocosmos.com.co (usados)** | SKIPPED | Listing pages (`/auto/usado`, `/auto/usado/electrico`) render with jQuery via client-side AJAX; no listings present in raw HTML and no static API endpoint found in the loaded scripts within the time budget. |
| **Casa Toro Usados** (`usados.casatoro.com`) | SKIPPED | Next.js SPA; found its real API host (`https://usados.nebula.com.co/api/v1/search`, `/stock`, etc. — read from the `search` page's JS chunk) but every call (GET/POST, with/without Origin/Referer headers) returned `{"success":false,"code":500}` — likely needs an auth token or exact payload shape not recoverable in the time budget. |
| **Los Coches** | SKIPPED (no used inventory) | Found its real API (`https://loscoches.com/wp-json/wp/v2/wp-vehiculos`, a WordPress/ACF custom post type). Pulled all 184 listings — **every one is `categoria_vehiculo = carros-nuevos` (new) or motos/buggy; there is no used-car category on this site**, so it's out of scope (buyer wants used/near-new resale, not manufacturer-new stock). |
| Kia CO / Hyundai CO / BYD CO official "seminuevos" | SKIPPED | No dedicated seminuevos catalog page found on `kia.com.co`, `bydauto.com.co`, or Hyundai CO within the time budget (redirects/404s, no linked used-car section on the homepage). |
| Volvo Selekt | SKIPPED (blocked) | `volvocars.com/co/...selekt` returns `403` (bot-blocked), no workaround attempted (no JS rendering/captcha bypass). |
| Localiza Seminuevos | SKIPPED | `localiza.com.co` does not resolve (DNS failure); `localiza.com/co-es/seminuevos` returns 404. No working URL found in the time budget. |

## In-band candidates (70-101M, SUV/crossover, 100% electric)

Only **Vendetunave** produced listings inside the price band; Autogermana's cheapest electric SUV (Volvo EX30, 131.99M) is above it, and its BMW I3/MINI Cooper SE units in-budget are hatchbacks, not SUVs (excluded per scope).

| # | Title | Price COP | Year | Km | Location | 360° cam | Notes |
|---|---|---|---|---|---|---|---|
| 1 | HYUNDAI KONA LIMITED EV ELECTRICA | 98,000,000 | **2024 (exception)** | 18,000 | Bogotá | Not mentioned in listing (Limited trim usually has more kit; unverified) | Within km limit. 2024 model year — only a candidate if the deal proves strong; ~400 km range claimed, dealer warranty "5 años" claimed in ad. Verify camera/ADAS spec directly. |
| 2 | BYD yuan up | 89,990,000 | 2025 | 19,000 | Bogotá | **Not confirmed** — description is a one-liner, no spec list | Within km limit. Nearly matches the Chery E5 Luxury price point almost exactly; must verify trim (base "Up" trim historically lacks 360 cam — only Flagship/GS trims usually get it). |
| 3 | BYD Yuan Up 2025 "Full equipo, Extras exclusivos" | 89,900,000 | 2025 | 39,800 | Bogotá | **Confirmed — "Cámara 360°" explicitly listed** | **Exceeds the 25,000 km cap (39.8k km)** — flagged, not a clean match, but the only listing here with an explicitly confirmed 360° camera at this price. |
| 4 | MG Marvel R 2023 212kW 4WD | 100,900,000 | 2023 | 32,000 | Bogotá | Not mentioned in the fetched description (spec sheet focuses on drivetrain) | **Exceeds 25,000 km cap** and model year is 2023 (outside the 2024-exception allowance) — flagged as a stretch, high-power AWD but likely no clean match on mileage/year. |

## Other electric SUVs found (outside price band or km cap — for reference only)

| Title | Price COP | Year | Km | Location | Why excluded |
|---|---|---|---|---|---|
| BYD Yuan EV 400 | 65,000,000 | 2022 | 57,000 | Bogotá | Below price band; km far over cap |
| BYD Yuan Plus EV 480 (2024) | 115,800,000 | 2024 | 25,000 | Chía | Above price band (at km limit exactly) |
| BYD Yuan Plus EV | 106,900,000 | 2024 | 35,704 | Bogotá | Above band; over km cap |
| Volvo EX30 Core Range | 124,900,000 | 2024 | 20,760 | Bogotá | Above price band |
| Volvo EX30 2024 | 115,000,000 | 2024 | 22,530 | Bogotá | Above price band |
| Volvo EX30 (Autogermana) | 131,990,000 | 2025 | 15,000 | Medellín | Above band; not Bogotá/Cundinamarca |
| Hyundai Kona eléctrica 2026 | 123,000,000 | 2026 | 4,000 | Bogotá | Above price band |
| BYD Tang L / EV, Chevrolet Blazer EV / Equinox EV, Hyundai Ioniq 5, Mercedes EQA/EQS, Toyota bZ4X, Volvo EX40 | 106M-430M | 2022-2027 | varies | Bogotá/Chía | All above the 70-101M band |
| BMW I3 / I3S (Autogermana) | 68.9M-99.9M | 2019-2022 | 46k-74k | Bogotá/Medellín | Hatchback, not SUV/crossover — out of requested scope |
| MINI Cooper SE / Aceman E (Autogermana) | 85M-126M | 2022-2025 | varies | Bogotá/Medellín/Pereira | Hatchback/subcompact crossover — most below or above band, and MINI is a hatchback silhouette, not an SUV |

## Bottom line

Vendetunave is the only additional (non-TuCarro) site that surfaced real in-band candidates, and even there only 2 of the 4 near-band listings actually verify a confirmed 360° camera or fall inside every hard constraint (price + km + 2025 year) at once. None beat the new Chery E5 Luxury on a fully-verified spec+condition basis; the BYD Yuan Up "Full equipo" (89.9M, confirmed 360° cam) is the closest match but is 14,800 km over the mileage cap.
