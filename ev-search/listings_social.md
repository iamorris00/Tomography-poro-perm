# Used Electric SUV Hunt — Social Channels (Bogotá + 40km ring)

Search date: 2026-09-26
Buyer baseline: new Chery/Omoda E5 Luxury (~COP 120-140M), looking for a BETTER-DEAL used EV SUV,
MY 2025-2027, 100% electric, 360° camera, comfort ≥ E5, price COP 70-150M.
Target area: Bogotá, Chía, Cajicá, Zipaquirá, Sopó, La Calera, Cota, Funza, Mosquera.

## 0. Access status (read this first)

- **Facebook (all subdomains, marketplace, groups, pages) and Instagram are BLOCKED at the
  network egress/proxy level in this environment** — not just a login wall. Every `WebFetch`
  attempt to `facebook.com` or `instagram.com` failed with `EGRESS_BLOCKED` before even reaching
  Facebook's login page. So no Marketplace search results page, group post, or IG post could be
  opened or scraped directly in this session.
- `WebSearch` (Google-style indexed search) still surfaces some Facebook Marketplace URLs and
  titles because they're publicly indexed, but clicking through to read price/km/description is
  not possible here (WebFetch blocked). Titles alone are given below, clearly marked "snippet-only,
  unverified."
- TikTok and X/Twitter: no TikTok car-sale posts were indexed by search. X/Twitter turned up only
  official dealer/brand accounts (BYD Auto Colombia, Metrokia), not private used-car listings.
- No public, unauthenticated, scrapable social listing meeting the buyer's exact criteria
  (used, 2025-2027, SUV, 100% EV, Bogotá-area, COP 70-150M) was confirmed in this session.

## 1. Snippet-only leads (found via search engine indexing, NOT verified, NOT confirmed to match all criteria)

| # | Channel | Title as indexed | Model/Trim | Year | Km | Price | City | Seller type | 360 cam | URL | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Facebook Marketplace | "2025 KIA EV5 WIND 100% ELECTRICO" | Kia EV5 Wind | 2025 | 0 km (per snippet) | unknown (not captured by search index) | **Medellín**, not Bogotá | Dealership ("VENTA POR CONCESIONARIO") | unknown | https://www.facebook.com/marketplace/item/2102121583578021/ | Looks like NEW dealer stock, not a used private sale, and wrong city. Listed only as a lead to re-check manually. |
| 2 | Facebook Marketplace | "2025 ByD Dolphin Mini" | BYD Dolphin Mini | 2025 | unknown | unknown | unknown (not confirmed Bogotá) | unknown | unknown | https://www.facebook.com/marketplace/item/955019066012376/ | Dolphin Mini is a hatchback, not an SUV/crossover — does not meet the SUV requirement even if verified. Included only for completeness. |
| 3 | Facebook Group | "BYD YUAN UP COLOMBIA" | — | — | — | — | — | Community group | — | https://www.facebook.com/groups/783724820598956/ | A group to search manually for owner resale posts (Yuan Up is an SUV and a good fit model). Content not readable in this session. |
| 4 | X/Twitter | Metrokia (@KiaMetroKia) | Kia EV5 (dealer stock, mentions "immediate delivery", "$6M benefits") | 2025 | — | — | Bogotá, Envigado, Villavicencio | Official dealer | unknown | https://twitter.com/KiaMetroKia | This is a NEW-car dealer account, not a used listing — relevant only as a channel to watch for dealer trade-ins. |
| 5 | X/Twitter | BYD Auto Colombia (@bydautocolombia) | — | — | — | — | Colombia (national) | Official brand account | — | https://x.com/bydautocolombia | Brand account; monitor for any resale/consignment posts, none found currently. |

**None of the above is a confirmed, price-verified, criteria-matching used listing.** They are
starting points for the buyer to open manually while logged into Facebook/Instagram.

## 2. What was explicitly ruled out / not found

- No indexed TikTok posts selling used EV SUVs in Bogotá.
- No indexed Instagram dealer/reseller posts matching the target models (IG itself is unscrapable
  here; Google's index of Instagram is thin for this vertical).
- No OLX Colombia individual listing surfaced (OLX's used-car section for Bogotá returns mostly
  a generic category page, `https://www.olx.com.co/carros_c378/q-electrico`, no item-level results
  indexed).
- Clasificados El Tiempo shows BYD listings in Bogotá but the ones indexed are older BYD combustion
  models (2019-2021), not the electric SUV segment requested.
- Classifieds/marketplace **aggregator sites** (Mercado Libre, TuCarro, Carroya, Autocosmos) DO show
  real inventory of used 2025 BYD Yuan/Yuan Up/Seagull in Bogotá in the COP 85-127M band, and a
  Volvo EX30 Core E40 (2025, 102 km, COP 158M, Bogotá) — but these are classifieds sites, not the
  "social" channels this task was scoped to, so they are reported here only as context, not as the
  deliverable. Recommend a **separate pass over Mercado Libre / TuCarro** if the buyer wants full
  coverage beyond social channels — those sites are not blocked and returned real inventory.

## 3. Manual search recipe for the buyer (run while logged into Facebook)

### Facebook Marketplace — set filters every time
- Location: **Bogotá**, radius **40 km** (captures Chía, Cajicá, Zipaquirá, Sopó, La Calera, Cota,
  Funza, Mosquera)
- Category: Vehicles → Cars & Trucks (or "SUVs" sub-filter if offered)
- Year: min **2025**, max **2027**
- Price: **COP 70,000,000 – 150,000,000**
- Fuel type filter if available: Electric

### Exact query strings to paste into Marketplace search box (one at a time)
1. `BYD Yuan Plus`
2. `BYD Yuan Up`
3. `BYD Atto 3`
4. `BYD Sealion 7`
5. `Kia EV3`
6. `Kia EV5`
7. `Kia EV6`
8. `Kia Niro EV`
9. `Hyundai Kona eléctrico`
10. `Hyundai Ioniq 5`
11. `Volvo EX30`
12. `Volvo EX40`
13. `Volvo C40`
14. `Zeekr X`
15. `Zeekr 7X`
16. `Geely EX5`
17. `Deepal S07`
18. `Leapmotor C10`
19. `Chevrolet Equinox EV`
20. `BMW iX1`
21. `Mercedes EQA`
22. `Mercedes EQB`
23. `Audi Q4 e-tron`
24. `Ford Mustang Mach-E`
25. `Nissan Ariya`
26. `Toyota bZ4X`
27. `Renault Megane E-Tech`
28. `Peugeot e-2008`
29. `MG ZS EV`
30. `Omoda E5` (to benchmark against comparable used units)

For each hit, check: seller type (dealer vs. private), km, whether photos show a 360°/around-view
badge or rear+front+side cameras, and cross-check VIN/plate history if the seller shares it.

### Facebook Groups to join and search internally (search box inside each group, same query list above)
- "Carros eléctricos Colombia"
- "BYD Colombia propietarios"
- "BYD YUAN UP COLOMBIA" (found, public metadata only — https://www.facebook.com/groups/783724820598956/)
- "Compra venta carros Bogotá"
- "Kia EV Colombia"
- "Vehículos eléctricos Colombia usados"
- "Compra y venta de carros eléctricos Colombia"
- "Carros usados Bogotá y Sabana" (Chía/Cajicá/Zipaquirá often trade here)

### Instagram
- Search hashtags: `#bydcolombia`, `#kiaev5colombia`, `#carroelectricousado`, `#autoelectricobogota`
- Check dealer/consignment accounts: search "seminuevos eléctricos Bogotá", "autos eléctricos usados Colombia"
- DM any account posting a matching unit to ask for price, km, and confirm 360° camera before an in-person visit.

### X/Twitter
- Search: `vendo eléctrico Bogotá SUV` (Latest tab, not Top)
- Search: `"BYD Yuan" OR "Kia EV5" OR "Ioniq 5" usado Bogotá`

### TikTok
- Search: `carro eléctrico usado Bogotá`, `vendo BYD Bogotá`, `seminuevos eléctricos Colombia`
- Check TikTok Shop / linked WhatsApp catalog in bio of dealer accounts.

### WhatsApp catalog pages (Google-indexed)
- Search: `site:wa.me OR site:api.whatsapp.com BYD OR Kia EV OR eléctrico usado Bogotá`
- Search: `"catálogo" "eléctrico" "Bogotá" wa.me`

## 4. Recommendation given the block

Because Facebook/Instagram cannot be fetched from this environment at all (network egress block,
confirmed twice), the buyer should run the query list in Section 3 manually — it takes ~15-20
minutes on Marketplace with the filters set once. For a channel-agnostic view, also run a
Mercado Libre / TuCarro pass (not blocked here) for the same model list, since it already shows
real inventory (used 2025 BYD Yuan-family units at COP 85-127M, and a 2025 Volvo EX30 Core E40 in
Bogotá at COP 158M — slightly above the buyer's ceiling but worth a negotiation attempt).
