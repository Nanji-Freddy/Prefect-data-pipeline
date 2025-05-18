from prefect import task
import pandas as pd
from config.settings import CSV_FILE_PATH
import logging


@task
def ingest_data():
    logging.info(f"Reading CSV from {CSV_FILE_PATH}")
    try:
        df = pd.read_csv(CSV_FILE_PATH)
        logging.info(f"Loaded {len(df)} rows.")
        return df
    except Exception as e:
        logging.error("Error reading CSV", exc_info=True)
        raise e
