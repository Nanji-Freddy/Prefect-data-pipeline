from prefect import task
import logging


@task
def clean_data(df):
    logging.info("Cleaning data...")
    df = df.drop_duplicates()
    df = df.dropna()
    df.columns = [col.lower().strip().replace(" ", "_") for col in df.columns]
    logging.info("Data cleaned.")
    return df
