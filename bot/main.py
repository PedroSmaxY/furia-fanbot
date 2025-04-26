from dotenv import load_dotenv
from os import getenv

load_dotenv()

print(getenv('API_KEY'))