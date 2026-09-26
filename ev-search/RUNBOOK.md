# Used EV SUV hunt — Bogotá (recurring runbook)

This folder is the state for a recurring search. Each run follows this runbook.

## Buyer's goal
The buyer is about to buy a **new Chery/Omoda E5 Luxury** (see `baseline.md` for price and equipment).
Find **used** cars that are a better deal than that purchase:

- Model year **2025, 2026 or 2027**
- **SUV / crossover**, **100% electric** (no HEV / PHEV)
- Comfort **equal or better** than the E5 Luxury: **360° camera is mandatory**, plus ADAS, big screen,
  wireless CarPlay/Android Auto, sunroof, powered seats, fast DC charging (CCS2 preferred), V2L, etc.
- **Better value**: a better brand or a higher-tier car that has depreciated
  (e.g. COP 140M new, now ~90M used). Always compare against the **E5 Luxury** trim (not Comfort),
  which costs **~COP 90M new** (see `baseline.md`).
- **Price band: COP 70M – 101M** (set by the buyer). Units slightly above 101M go in a short
  "just over budget" list only when they are clearly a tier above the E5.
- Also watch 2024 units that are otherwise excellent and label them "2024 – outside year filter".
- Location: **Bogotá** or nearby (Chía, Cajicá, Zipaquirá, Sopó, La Calera, Cota, Funza, Mosquera, Soacha).

## Sources (one Sonnet subagent per group, run in parallel)
1. **TuCarro / MercadoLibre** (`listings_tucarro.md`)
2. **Other marketplaces and dealers**: Carroya, Vendetunave, Autocosmos, Kavak, dealer "seminuevos"
   programs (BYD, Kia, Hyundai, Volvo Selekt, Autogermana, Casa Toro, Los Coches, Localiza…)
   (`listings_other_sites.md`)
3. **Social**: Facebook Marketplace and groups, Instagram dealers, Clasificados El Tiempo
   (`listings_social.md`). Marketplace is behind a login wall, so this agent relies on search-engine
   snippets and lists manual search recipes.

Model watch list: BYD Yuan Plus/Atto 3, Yuan Up, Sealion 7, Song; Kia EV3/EV5/EV6/Niro EV;
Hyundai Kona EV/Ioniq 5; Volvo EX30/EX40/C40; Zeekr X/7X; Geely EX5; Deepal S07; Leapmotor C10/B10;
Chevrolet Equinox EV/Blazer EV; BMW iX1; Mercedes EQA/EQB; Audi Q4 e-tron; Mustang Mach-E;
Nissan Ariya; Toyota bZ4X; Renault Megane E-Tech; Peugeot e-2008; MG ZS EV/Marvel R; Omoda E5
(used, for price reference); Tesla Model Y (from ~COP 120M new, so used 2025 units may fall near 100M);
MG S5 EV; GAC Aion V/UT; Geely EX2. Add any new model that meets the criteria.

## Known access limits
In this cloud environment the network proxy blocks tucarro.com.co, carroya.com, vendetunave.co,
autocosmos.com.co, casatoro.com, loscoches.com, autogermana, facebook.com and instagram.com
(EGRESS_BLOCKED). Until the environment's network access is widened, agents have to use search-engine snippets,
so every listing is a lead to verify by phone or in person.

## Rules for agents
- Never invent listings. Only report listings actually seen on a fetched page or a search snippet
  (mark snippet-only data as such).
- For each listing record: source, model, trim, year, km, price COP, city, seller type,
  360 camera (confirmed / likely / unknown), URL, listing date if visible.
- Note blocked sites and login walls explicitly.

## Each run
1. Read `baseline.md`, `seen_listings.csv` and the latest `REPORT.md`.
2. Launch the three source agents (Sonnet), refresh the three `listings_*.md` files.
3. Merge into `seen_listings.csv` (columns: `first_seen,last_seen,source,model,trim,year,km,price_cop,city,cam360,url`),
   keyed by URL. Update `last_seen` and price for known URLs; flag price drops.
4. Write `REPORT.md` (and a copy at `history/YYYY-MM-DD.md`): top 10 best-value cars,
   **NEW since last run**, **price drops**, listings that disappeared (probably sold), and
   a short "buy the new E5 or this?" verdict.
5. Commit and push to branch `claude/ev-comparison-shopping-i6qptr`.
