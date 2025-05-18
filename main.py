from prefect import flow
from tasks.ingest import ingest_data
from tasks.transform import clean_data
from tasks.load import load_to_mysql
import logging


@flow(name="CSV to MySQL Pipeline")
def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    logging.info("Starting Prefect pipeline...")

    df = ingest_data()
    cleaned = clean_data(df)
    load_to_mysql(cleaned)

    logging.info("Pipeline complete.")


if __name__ == "__main__":
    main()
