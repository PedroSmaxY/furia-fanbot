from dotenv import load_dotenv
from os import getenv
import httpx

load_dotenv()

PANDASCORE_API_KEY = getenv('PANDASCORE_API_KEY')


def get_matches():
    url = 'https://api.pandascore.co/matches?sort=-modified_at&token=' + PANDASCORE_API_KEY
    client = httpx.Client()
    response = client.get(url)
    response.raise_for_status()
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_matches())
