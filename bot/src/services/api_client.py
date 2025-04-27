import httpx
import os
from dotenv import load_dotenv
from src.models.models import Summary, Roster

load_dotenv()
API_URL = os.getenv("API_URL")


def get_summary() -> Summary:
    client = httpx.Client()
    response = client.get(f"{API_URL}/team/summary")
    response.raise_for_status()
    data = response.json()
    return Summary.from_dict(data)


def get_roster() -> Roster:
    client = httpx.Client()
    response = client.get(f"{API_URL}/team/roster")
    response.raise_for_status()
    data = response.json()
    return Roster.from_dict(data)


if __name__ == "__main__":
    info = get_roster()
    print(info)
