import ssl

ssl._create_default_https_context = ssl._create_unverified_context

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import random
import time
from utils.cache import cache
from core.config import settings
import logging

logger = logging.getLogger(__name__)


def get_html(url: str) -> str:
    """Obtém o conteúdo HTML de uma URL com cache"""

    cached_content = cache.get(url)
    if cached_content:
        return cached_content

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }

    request = Request(url)
    for key, value in headers.items():
        request.add_header(key, value)

    try:
        time.sleep(random.uniform(2.0, 5.0))

        response = urlopen(request)
        html = response.read().decode("utf-8", errors="ignore")

        cache.set(url, html)

        return html

    except Exception as e:
        logger.error(f"Erro ao obter HTML de {url}: {str(e)}")

        return None
