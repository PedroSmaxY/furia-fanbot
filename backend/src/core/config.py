import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_TITLE: str = "FURIA CS2 API"
    API_DESCRIPTION: str = "API para obter informações sobre o time FURIA de CS2"
    API_VERSION: str = "1.0.0"

    HLTV_BASE_URL: str = "https://www.hltv.org"
    TEAM_FURIA_URL: str = "https://www.hltv.org/team/8297/furia"

    CACHE_EXPIRY: int = 3600

    SSL_VERIFY: bool = False


settings = Settings()
