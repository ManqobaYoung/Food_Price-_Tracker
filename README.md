# Food_Price-_Tracker

Compare prices of essential grocery products across major South African supermarkets:
Spar, Checkers, Boxer, Shoprite and Woolworths.

## Purpose
Collect and compare prices for a set of essential products to monitor price differences,
track inflation, and identify the cheapest retailer for each item.

## Stores
- Spar
- Checkers
- Boxer
- Shoprite
- Woolworths

## Essential products
Organized by category. Add/remove items to match your needs.

- Staples
  - White bread (loaf)
  - Maize meal (2.5 kg)
  - Rice (2 kg)
  - All-purpose flour (1–2 kg)
  - Sugar (2 kg)
- Dairy & Eggs
  - Milk (1 L)
  - Eggs (dozen)
  - Butter / Margarine (250 g)
  - Cheese (block)
- Proteins
  - Chicken portions (1 kg)
  - Beef mince (1 kg)
  - Canned pilchards / pilchard (400 g)
  - Dried beans / lentils (1 kg)
- Fresh produce
  - Potatoes (1 kg)
  - Onions (1 kg)
  - Tomatoes (1 kg)
  - Carrots (1 kg)
- Cooking & condiments
  - Cooking oil (2 L)
  - Salt (500 g)
  - Instant coffee / tea
- Pantry & convenience
  - Pasta (500 g)
  - Canned tomatoes (410 g)
  - Breakfast cereal (medium box)
- Household & personal care (optional)
  - Toilet paper (4 pack)
  - Bar soap / liquid soap
  - Dishwashing liquid (750 ml)

## Data format / CSV columns
When saving price records, use a consistent CSV/JSON schema. Example CSV columns:
date, store, product, brand, pack_size, unit_price, total_price, unit, pack_count, url, notes

## Frequency
- Recommended: weekly or monthly snapshots depending on resources.

## How to run
1. Install dependencies:
```sh
pip install -r requirements.txt
```
2. Add or implement a scraper or data-collection script that writes to CSV/DB using the schema above.

## Contribution
- Add missing essential products or local brand variants.
- Improve scrapers per store page structure.

## License
Specify a license (e.g., MIT) if you plan to share the project.

## Contact
Open issues or pull requests in this repository.

