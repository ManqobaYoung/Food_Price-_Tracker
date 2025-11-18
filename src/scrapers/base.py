"""Base scraper interface for store scrapers."""
from typing import List, Dict


class BaseScraper:
    """Abstract base scraper.

    Implementations should provide a `get_prices` method that accepts a list
    of product names and returns a list of dictionaries with at least the
    following keys: date, store, product, unit_price, total_price, unit, notes
    """

    store_name: str = ""

    def __init__(self):
        if not self.store_name:
            raise ValueError("Scraper must define store_name")

    def get_prices(self, products: List[str]) -> List[Dict]:
        """Return price records for the requested products.

        Each record must be a dict. Implementations may fetch data from the
        web or local fixtures.
        """
        raise NotImplementedError()
