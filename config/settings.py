import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Config values
CSV_FILE_PATH = os.getenv("CSV_FILE_PATH", "data/Online_Sales_Data.csv")

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "password"),  # Loaded securely
    "database": os.getenv("DB_NAME", "prefect_db")
}
