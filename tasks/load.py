from prefect import task
from config.settings import DB_CONFIG
import sqlalchemy
import logging


@task
def load_to_mysql(df, table_name="cleaned_data"):
    logging.info(f"Loading data to MySQL table: {table_name}")
    try:
        conn_str = (
            f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
            f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        )
        engine = sqlalchemy.create_engine(conn_str)
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        logging.info("Load successful.")
    except Exception as e:
        logging.error("MySQL load failed.", exc_info=True)
        raise e
