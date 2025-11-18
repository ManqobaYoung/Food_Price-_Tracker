"""CLI wrapper to run the price collection script."""
import sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))

from src.collector import main


if __name__ == "__main__":
    main()
