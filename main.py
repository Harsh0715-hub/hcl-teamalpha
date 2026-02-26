from src.utils import setup_logger, ensure_dirs
from src.bronze import ingest_raw_data

if __name__ == "__main__":
    setup_logger()
    ensure_dirs()

    print("🚀 Pipeline Started")
    ingest_raw_data()
    print("🥉 Bronze Layer Completed")