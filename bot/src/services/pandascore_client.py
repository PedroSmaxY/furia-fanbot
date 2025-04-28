from dotenv import load_dotenv
from os import getenv
import httpx
import time
from src.models.pandascore_models import Team, PlayerDetail, MatchList

load_dotenv()

PANDASCORE_API_KEY = getenv('PANDASCORE_API_KEY')
BASE_URL = 'https://api.pandascore.co'

_cache = {}
DEFAULT_CACHE_EXPIRY = 30 * 60


def get_pandascore_data(endpoint, params=None, cache_ttl=DEFAULT_CACHE_EXPIRY):
    cache_key = f"{endpoint}:{str(params)}"

    current_time = time.time()
    if cache_key in _cache and _cache[cache_key][1] > current_time:
        print(f"Usando dados em cache para {endpoint}")
        return _cache[cache_key][0]

    headers = {
        'accept': 'application/json',
        'authorization': 'Bearer ' + PANDASCORE_API_KEY
    }

    response = httpx.get(f"{BASE_URL}/{endpoint}", headers=headers, params=params)

    print(f"Requisição à API para {response.url}")

    response.raise_for_status()

    if response.status_code == 200:
        data = response.json()
        expiry_time = current_time + cache_ttl
        _cache[cache_key] = (data, expiry_time)
        return data
    else:
        print(f"Erro: {response.status_code} - {response.text}")
        return None


def get_team(cache_ttl=DEFAULT_CACHE_EXPIRY) -> Team:
    team = get_pandascore_data(endpoint="/teams/furia", cache_ttl=cache_ttl)
    return Team.from_dict(team)


def get_future_matches(team_id_or_slug="furia", cache_ttl=DEFAULT_CACHE_EXPIRY) -> MatchList:
    params = {
        'filter[future]': True,
        'sort': 'begin_at',
        'per_page': 10
    }

    matches = get_pandascore_data(
        endpoint=f"/teams/{team_id_or_slug}/matches",
        params=params,
        cache_ttl=cache_ttl
    )

    return MatchList.from_dict(matches)


def get_player(id_or_slug: str, cache_ttl=DEFAULT_CACHE_EXPIRY) -> PlayerDetail:
    player = get_pandascore_data(endpoint=f"/players/{id_or_slug}", cache_ttl=cache_ttl)
    return PlayerDetail.from_dict(player)


def clear_cache():
    global _cache
    _cache = {}
    print("Cache limpo com sucesso")


if __name__ == "__main__":
    print(get_future_matches())
