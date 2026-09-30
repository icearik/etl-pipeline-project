import logging
from extract import extract_data, save_raw_data
from transform import load_raw_data, transform_data
from load import get_engine, load_data

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def run_pipeline():
    logger.info("Starting ETL pipeline")

    # Extract
    url = "https://jsonplaceholder.typicode.com/posts"
    raw_data = extract_data(url)
    save_raw_data(raw_data, "data/raw_posts.json")

    # Transform
    raw_data = load_raw_data("data/raw_posts.json")
    transformed_data = transform_data(raw_data)
    transformed_data.to_csv("data/transformed_posts.csv", index=False)

    # Load
    engine = get_engine()
    load_data(transformed_data, "posts", engine)

    logger.info("ETL pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()