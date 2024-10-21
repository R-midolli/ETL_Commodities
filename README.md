# Commodities ETL Pipeline and Data Warehouse

## Overview

This project implements an ETL (Extract, Transform, Load) pipeline for commodities data and sets up a Data Warehouse using dbt (data build tool). It extracts financial data from Yahoo Finance (yfinance), performs transformations, and loads the processed data into a PostgreSQL database for further analysis.

```mermaid
graph TD
A[Start] --> B[Extract Commodity Data]
B --> C[Transform Commodity Data]
C --> D[Load Data into PostgreSQL]
D --> E[DBT Transformations]
E --> F[Final Data Models]
F --> G[End]

    subgraph Extract
        B1[Fetch Data from yfinance]
        B2[Process Raw Data]
    end

    subgraph Transform
        C1[Clean and Format Data]
        C2[Apply Business Logic]
    end

    subgraph Load
        D1[Insert into Staging Tables]
    end

    subgraph DBT
        E1[Run Staging Models]
        E2[Run Mart Models]
    end

    B --> B1
    B1 --> B2
    B2 --> C
    C --> C1
    C1 --> C2
    C2 --> D
    D --> D1
    D1 --> E
    E --> E1
    E1 --> E2
    E2 --> F
```

## Features

- Data extraction from Yahoo Finance using the yfinance library
- Data transformation and modeling with dbt
- Pandas for intermediate data manipulation
- PostgreSQL as the data warehouse
- Poetry for dependency management
- Environment variable management with python-dotenv

## Prerequisites

- Python 3.12+
- PostgreSQL
- dbt 1.8+
- Poetry (optional, but recommended)

## Installation

You have two options for setting up this project: using Poetry (recommended) or using pip.

### Option 1: Using Poetry (Recommended)

If you already have Poetry installed:

1. Clone this repository:

   ```
   git clone https://github.com/your-username/commodities-etl-pipeline.git
   cd commodities-etl-pipeline
   ```

2. Install dependencies using Poetry:

   ```
   poetry install
   ```

3. Activate the virtual environment:
   ```
   poetry shell
   ```

If you don't have Poetry installed, you can install it by following the instructions at [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)

### Option 2: Using pip

If you prefer not to use Poetry:

1. Clone this repository:

   ```
   git clone https://github.com/your-username/commodities-etl-pipeline.git
   cd commodities-etl-pipeline
   ```

2. Create a virtual environment:

   ```
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

After installation, proceed with the setup of dbt:

5. Set up dbt:
   ```
   dbt init
   ```
   Follow the prompts to configure your dbt project.

Note: This project requires Python 3.12 or higher.

## Configuration

1. Create a `.env` file in the project root and add your database credentials:

   ```
   DB_HOST=your_host
   DB_PORT=your_port
   DB_NAME=your_database_name
   DB_USER=your_username
   DB_PASSWORD=your_password
   ```

2. Update the `profiles.yml` file in your dbt configuration directory (usually `~/.dbt/`) with your database connection details.

## Usage

1. Run the data extraction and initial load script:

   ```
   python scripts/extract_load_data.py
   ```

2. Run dbt models:

   ```
   dbt run
   ```

3. Test dbt models:
   ```
   dbt test
   ```

## Project Structure

```
commodities-etl-pipeline/
├── dbt_project.yml
├── models/
│   ├── staging/
│   │   ├── stg_commodities.sql
│   │   ├── stg_commodities_transactions.sql
│   │   └── schema.yml
│   └── mart/
│       ├── dm_commodities.sql
│       └── schema.yml
├── scripts/
│   └── extract_load_data.py
├── tests/
├── seeds/
│   └── commodities_transactions.csv
├── macros/
├── analyses/
├── .env
├── README.md
└── requirements.txt
```

## Data Models

- **Staging Models**:
  - `stg_commodities`: Processes raw commodity data
  - `stg_commodities_transactions`: Processes transaction data
- **Mart Models**:
  - `dm_commodities`: Integrates commodity and transaction data for analysis

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - your.email@example.com

Project Link: [https://github.com/your-username/commodities-etl-pipeline](https://github.com/your-username/commodities-etl-pipeline)