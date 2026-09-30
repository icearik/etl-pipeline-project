import pandas as pd
import logging
import os
from pathlib import Path
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)  

def get_engine():
    """ Create a SQLAlchemy engine using environment variables"""
    db_path = os.getenv("DB_PATH", "data/etl_pipeline.db")
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
    engine = create_engine(f"sqlite:///{db_path}")
    return engine

def load_data(df: pd.DataFrame, table_name: str, engine):
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    logger.info(f"Data loaded into table '{table_name}' in the database")   

if __name__ == "__main__":
    df = pd.read_csv("data/transformed_posts.csv")
    engine = get_engine()
    load_data(df, "posts", engine)
    