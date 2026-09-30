import requests
import logging
import json
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def extract_data(url: str) -> list:
    """ Fetch data from API and return JSON"""
    logger.info(f"Fetching data from {url}")
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    logger.info(f"Data fetched successfully from {url}")
    return data

def save_raw_data(data: list, filepath: str):
    """ Save raw data to a JSON file"""
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f"Raw data saved to {filepath}")

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    raw_data = extract_data(url)
    save_raw_data(raw_data, "data/raw_posts.json")