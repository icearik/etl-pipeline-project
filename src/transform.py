import pandas as pd
import logging
import json

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def load_raw_data(filepath: str) -> list:
    with open(filepath, 'r') as f:
        return json.load(f)


def transform_data(raw_data: list) -> pd.DataFrame:
    """ Transform raw data into a DataFrame"""
    df = pd.DataFrame(raw_data)

    df['title'] = df['title'].str.strip().str.capitalize()
    df['body_legth'] = df['body'].str.len()
    df = df.drop_duplicates(subset='id', keep='first')
    df = df.dropna(subset=['title', 'body'])

    logger.info("Data transformation complete")
    return df

if __name__ == "__main__":
    raw = load_raw_data("data/raw_posts.json")
    df = transform_data(raw)
    df.to_csv("data/transformed_posts.csv", index=False)
    logger.info("Transformed data saved to data/transformed_posts.csv")