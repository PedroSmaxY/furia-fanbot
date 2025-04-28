from dotenv import load_dotenv
from os import getenv
import httpx
from src.models.pandascore_models import Team, PlayerDetail

load_dotenv()

PANDASCORE_API_KEY = getenv('PANDASCORE_API_KEY')
BASE_URL = 'https://api.pandascore.co'


def get_pandascore_data(endpoint, params=None):
    headers = {
        'accept': 'application/json',
        'authorization': 'Bearer ' + PANDASCORE_API_KEY
    }

    response = httpx.get(f"{BASE_URL}/{endpoint}", headers=headers, params=params)

    response.raise_for_status()

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro: {response.status_code} - {response.text}")
        return None


def get_team() -> Team:
    team = get_pandascore_data(endpoint="/teams/furia")
    return Team.from_dict(team)


def get_team_matches():
    team = get_pandascore_data(endpoint="/teams/furia/matches?future=true&page=&per_page=25")
    return team


def get_player(id_or_slug: str) -> PlayerDetail:
    player = get_pandascore_data(endpoint=f"/players/{id_or_slug}")
    return PlayerDetail.from_dict(player)


if __name__ == "__main__":
    print(get_player("fallen"))
