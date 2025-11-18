"""Template scraper that returns sample/static data.

Use this as a starting point when adding real scrapers for each store.
"""
from datetime import datetime
from typing import List, Dict

from .base import BaseScraper


class TemplateScraper(BaseScraper):
    store_name = "TemplateStore"

    def get_prices(self, products: List[str]) -> List[Dict]:
        """Return a small sample for each requested product."""
        records = []
        now = datetime.utcnow().isoformat()
        for p in products:
            records.append(
                {
                    "date": now,
                    "store": self.store_name,
                    "product": p,
                    "brand": "Generic",
                    "pack_size": "1",
                    "unit_price": 9.99,
                    "total_price": 9.99,
                    "unit": "each",
                    "pack_count": 1,
                    "url": "",
                    "notes": "sample data",
                }
            )
        return records
