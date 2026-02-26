import json # to read JSON files
import csv # to write into CSV file
import shutil # for file copying
import logging # to log the ingestion process
from pathlib import Path #for handling file paths


def convert_json_to_csv(json_path, csv_path, fieldnames):
    """Convert a JSON list of objects into a CSV file."""
    with open(json_path, "r") as f:
        data = json.load(f)

    with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            writer.writerow(row)


def ingest_raw_data():
    logging.info("Starting Bronze Layer Ingestion (with JSON → CSV conversion)...")

    data_dir = Path("Input_data")
    bronze_dir = Path("bronze")

    # 1. Copy EHR CSV directly
    ehr_src = data_dir / "ehr.csv"
    ehr_dest = bronze_dir / "ehr.csv"

    if ehr_src.exists():
        shutil.copy(ehr_src, ehr_dest)
        logging.info("Copied: ehr.csv")
    else:
        logging.error("Missing: ehr.csv")

    # 2. Convert vitals.json → vitals.csv
    vitals_json = data_dir / "vitals.json"
    vitals_csv = bronze_dir / "vitals.csv"

    if vitals_json.exists():
        convert_json_to_csv(
            vitals_json,
            vitals_csv,
            fieldnames=["patientId", "timestamp", "hr", "ox", "sys", "dia"]
        )
        logging.info("Converted: vitals.json → vitals.csv")
    else:
        logging.error("Missing: vitals.json")

    # 3. Convert labs.json → labs.csv
    labs_json = data_dir / "labs.json"
    labs_csv = bronze_dir / "labs.csv"

    if labs_json.exists():
        convert_json_to_csv(
            labs_json,
            labs_csv,
            fieldnames=["patient_id", "test", "value", "timestamp"]
        )
        logging.info("Converted: labs.json → labs.csv")
    else:
        logging.error("Missing: labs.json")

    logging.info("Bronze Layer Ingestion Completed.")