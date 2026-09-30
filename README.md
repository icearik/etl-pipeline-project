# API-to-SQLite ETL Pipeline

A modular Python ETL pipeline that extracts data from a public API, transforms it with Pandas, and loads it into a local SQLite database.

This project demonstrates fundamental data engineering practices, including:

- Extract, transform, and load pipeline design
- Python virtual environments
- API data extraction
- Data cleaning with Pandas
- SQL database loading
- Configuration management
- Logging
- Git version control
- Reproducible local development

## Architecture

```text
JSONPlaceholder API
        |
        v
     Extract
     Requests
        |
        v
 Raw JSON file
 data/raw_posts.json
        |
        v
    Transform
      Pandas
        |
        v
 Transformed CSV
data/transformed_posts.csv
        |
        v
      Load
    SQLAlchemy
        |
        v
 SQLite database
data/etl_pipeline.db


**Pipeline stages:**
1. **Extract** (`src/extract.py`) — Pulls raw JSON data from a public API, saves a local copy for reproducibility/debugging
2. **Transform** (`src/transform.py`) — Cleans and reshapes data using Pandas (deduplication, null handling, derived columns)
3. **Load** (`src/load.py`) — Writes the cleaned data into a SQL database via SQLAlchemy
4. **Orchestration** (`src/main.py`) — Runs all three stages in sequence with logging

---

## 🧱 Architecture Decisions

**Database: SQLite (instead of Postgres)**

Originally planned to run Postgres via Docker, but switched to SQLite due to
corporate machine restrictions on Docker/virtualization access. SQLAlchemy is
used as an abstraction layer, so this pipeline can be migrated to Postgres,
MySQL, or any other SQL backend later by changing only the connection string
in `get_engine()` — no other code changes required.

**Why this matters:** Writing database-agnostic code is a real-world best
practice. Production data pipelines are often designed to be portable across
environments (local dev, staging, cloud) without rewriting business logic.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11+ | Core language |
| Pandas | Data transformation |
| Requests | API extraction |
| SQLAlchemy | Database-agnostic ORM/connection layer |
| SQLite | Local database (no external dependencies) |
| python-dotenv | Environment variable / config management |
| Git | Version control |

---

## 📂 Project Structure
etl-pipeline-project/
├── src/
│ ├── extract.py # Pulls data from API
│ ├── transform.py # Cleans and reshapes data
│ ├── load.py # Writes data to SQLite
│ └── main.py # Orchestrates the full pipeline
├── data/ # Raw + transformed data, SQLite DB (gitignored)
├── logs/ # Log output (gitignored)
├── .env # Local config (gitignored, not committed)
├── .gitignore
├── requirements.txt
└── README.md
