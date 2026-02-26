# src/utils.py

import logging
from pathlib import Path

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def ensure_dirs():
    dirs = ["data", "bronze", "silver", "gold", "visualizations"]
    for d in dirs:
        Path(d).mkdir(exist_ok=True)

