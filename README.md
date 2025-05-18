# 📊 Prefect Data Pipeline

A modular and scalable data pipeline built with [Prefect](https://www.prefect.io/), designed to ingest, transform, and load CSV data into a MySQL database. The project leverages `uv` for efficient package and environment management.

---

## 🚀 Features

- **Prefect 2.x**: Orchestrates the data pipeline with robust task management.
- **Modular Structure**: Separates concerns into distinct modules for ingestion, transformation, and loading.
- **Environment Configuration**: Utilizes `.env` files for secure and flexible configuration.
- **MySQL Integration**: Loads processed data into a MySQL database.
- **`uv` Package Manager**: Manages dependencies and virtual environments efficiently.

---

## 🗂️ Project Structure

```
Prefect-data-pipeline/
├── config/
│   └── settings.py          # Configuration settings loaded from .env
├── data/
│   └── sample.csv           # Sample CSV data file
├── tasks/
│   ├── ingest.py            # Task to ingest CSV data
│   ├── transform.py         # Task to clean and transform data
│   └── load.py              # Task to load data into MySQL
├── .env                     # Environment variables
├── .gitignore               # Git ignore file
├── main.py                  # Entry point to run the Prefect flow
├── pyproject.toml           # Project metadata and dependencies
├── uv.lock                  # Lock file for uv
└── README.md                # Project documentation
```

---

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) installed
- MySQL server running and accessible

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Nanji-Freddy/Prefect-data-pipeline.git
   cd Prefect-data-pipeline
   ```

2. **Create and activate a virtual environment using `uv`:**

   ```bash
   uv venv
   .venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**

   ```bash
   uv pip install -r requirements.txt
   ```

4. **Configure environment variables:**

   Create a `.env` file in the root directory with the following content:

   ```env
   CSV_FILE_PATH=data/sample.csv
   DB_HOST=localhost
   DB_PORT=3306
   DB_USER=your_mysql_user
   DB_PASSWORD=your_mysql_password
   DB_NAME=your_database_name
   ```

   Replace the placeholders with your actual MySQL credentials and desired database name.

---

## 🏃 Running the Pipeline

Ensure your MySQL server is running and the specified database exists. Then, execute the pipeline:

```bash
uv run main.py
```

This command will:

1. Ingest data from the specified CSV file.
2. Clean and transform the data.
3. Load the processed data into the specified MySQL database.

---

## 🔧 Configuration Details

- **CSV_FILE_PATH**: Path to the input CSV file.
- **DB_HOST**: Hostname of the MySQL server.
- **DB_PORT**: Port number of the MySQL server (default is 3306).
- **DB_USER**: Username for the MySQL database.
- **DB_PASSWORD**: Password for the MySQL database.
- **DB_NAME**: Name of the MySQL database to load data into.

---

## 🧪 Sample Data

A sample CSV file is provided at `data/Online_Sales_Data.csv` to test the pipeline. Ensure this file exists or replace it with your own data, updating the `CSV_FILE_PATH` in the `.env` file accordingly.

---

## 📚 Learn More

- [Prefect Documentation](https://docs.prefect.io/)
- [uv Documentation](https://github.com/astral-sh/uv)
- [MySQL Documentation](https://dev.mysql.com/doc/)

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
