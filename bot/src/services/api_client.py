import httpx
import os
from dotenv import load_dotenv
from src.models.summary_model import Summary

load_dotenv()
API_URL = os.getenv("API_URL")


def get_summary() -> Summary:
    client = httpx.Client()
    response = client.get(f"{API_URL}/team/summary")
    response.raise_for_status()
    data = response.json()['summary']
    return Summary.from_dict(data)


if __name__ == "__main__":
    summary = get_summary()
    print(summary.info)
