from src.utils import setup_logger
from src.bronze import ingest_raw_data

if __name__ == "__main__":
    setup_logger()

    print("🚀 Pipeline Started")
    ingest_raw_data()
    print("🥉 Bronze Layer Completed")