import httpx
import os
from dotenv import load_dotenv
from src.models.models import Summary, Roster, MatchesResponse, NewsResponse

load_dotenv()
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:3000/api/v1/furia")


def get_api_data(endpoint: str) -> dict:
    client = httpx.Client()
    response = client.get(f"{API_BASE_URL}/{endpoint}")
    response.raise_for_status()
    return response.json()


def get_summary() -> Summary:
    summary = get_api_data("team/summary")
    return Summary.from_dict(summary)


def get_roster() -> Roster:
    roster = get_api_data("team/roster")
    return Roster.from_dict(roster)


def get_matches() -> MatchesResponse:
    matches = get_api_data("team/stats/matches")
    return MatchesResponse.from_dict(matches)


def get_news() -> NewsResponse:
    news = get_api_data("team/news")
    return NewsResponse.from_dict(news)


if __name__ == "__main__":
    info = get_roster()
    print(info)
