"""Collector orchestration for scraping and saving prices."""
from typing import List, Dict, Optional
import os
from pathlib import Path
import pandas as pd

from .config import STORES, ESSENTIAL_PRODUCTS
from .scrapers.template_scraper import TemplateScraper


def _all_products() -> List[str]:
    # flatten categories into a single list
    items = []
    for cat, prods in ESSENTIAL_PRODUCTS.items():
        items.extend(prods)
    return items


def run_collection(output_csv: Optional[str] = None, scrapers: Optional[List] = None) -> str:
    """Run the collection using provided scrapers and write a CSV.

    If scrapers is None, uses TemplateScraper for demonstration.
    Returns the output path.
    """
    if output_csv is None:
        output_csv = os.path.join("data", "processed", "prices.csv")

    products = _all_products()

    if scrapers is None:
        scrapers = [TemplateScraper()]

    records = []
    for scraper in scrapers:
        try:
            recs = scraper.get_prices(products)
            records.extend(recs)
        except Exception as e:
            # Log and continue with next scraper
            print(f"Error running scraper {getattr(scraper, 'store_name', str(scraper))}: {e}")

    # Ensure output directory exists
    out_path = Path(output_csv)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if records:
        df = pd.DataFrame.from_records(records)
        df.to_csv(out_path, index=False)
    else:
        # create empty CSV with expected columns
        df = pd.DataFrame(columns=["date", "store", "product", "unit_price", "total_price"])
        df.to_csv(out_path, index=False)

    return str(out_path)


def main():
    path = run_collection()
    print(f"Saved prices to {path}")


if __name__ == "__main__":
    main()
