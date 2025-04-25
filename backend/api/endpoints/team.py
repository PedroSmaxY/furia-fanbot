from fastapi import APIRouter, HTTPException
from bs4 import BeautifulSoup
from core.scraper import get_html
from core.config import settings
from datetime import datetime
from typing import Dict, Any
import re


PLAYER_NAMES = {
    "FalleN": "Gabriel Toledo",
    "yuurih": "Yuri Santos",
    "YEKINDAR": "Mareks Gaļinskis",
    "KSCERATO": "Kaike Cerato",
    "molodoy": "Bogdan Valovskiy",
    "chelo": "Marcelo Cespedes",
    "skullz": "Eduardo Teles",
    "sidde": "Pedro Bittencourt",  # Coach
}


router = APIRouter(prefix="/api/furia", tags=["team"])


@router.get("/roster", summary="Elenco atual da FURIA")
async def get_roster() -> Dict[str, Any]:
    """Retorna o elenco atual da FURIA com informações detalhadas"""
    try:
        html = get_html(settings.TEAM_FURIA_URL + "#tab-rosterBox")

        if not html:
            raise HTTPException(
                status_code=503, detail="Não foi possível obter dados do HLTV"
            )

        soup = BeautifulSoup(html, "html.parser")

        players = []
        players_table = soup.select("table.players-table")

        if players_table:
            rows = players_table[0].select("tr")

            for row in rows[1:]:

                cells = row.select("td")
                if len(cells) >= 5:

                    player_cell = cells[0]

                    player_link = player_cell.select_one("a")
                    if not player_link:
                        continue

                    nickname_elem = player_cell.select_one(
                        ".text-ellipsis.bold, .playersBox-playernick"
                    )
                    nickname = (
                        nickname_elem.text.strip()
                        if nickname_elem
                        else player_link.text.strip()
                    )
                    nickname = nickname.split("\n")[0].strip()

                    flag = player_cell.select_one("img.flag")
                    country = flag.get("title", "Brasil") if flag else "Brasil"

                    status = cells[1].text.strip() if len(cells) > 1 else "N/A"

                    time_on_team = cells[2].text.strip() if len(cells) > 2 else "N/A"

                    maps_played = cells[3].text.strip() if len(cells) > 3 else "N/A"

                    rating = cells[4].text.strip() if len(cells) > 4 else "N/A"

                    players.append(
                        {
                            "nickname": nickname,
                            "name": PLAYER_NAMES.get(nickname, "Não disponível"),
                            "country": country,
                            "status": status,
                            "time_on_team": time_on_team,
                            "maps_played": maps_played,
                            "rating": rating,
                        }
                    )

        if not players:
            player_elements = soup.select(".text-ellipsis.nickname-container")

            if not player_elements:
                player_elements = soup.select(".playerFlagName")

            if not player_elements and soup.select_one(".bodyshot-team"):
                bodyshot_text = soup.select_one(".bodyshot-team").text.strip()
                names = [
                    name.strip() for name in bodyshot_text.split("\n") if name.strip()
                ]

                for name in names:
                    players.append(
                        {
                            "nickname": name,
                            "name": PLAYER_NAMES.get(name, "Não disponível"),
                            "country": "Não disponível",
                            "status": "Não disponível",
                            "time_on_team": "Não disponível",
                            "maps_played": "Não disponível",
                            "rating": "Não disponível",
                        }
                    )

                return {"status": "success", "data": {"roster": players}}

            for elem in player_elements:
                nickname = elem.text.strip()
                if nickname:
                    flag = None

                    if elem.parent:
                        flag = elem.parent.select_one("img.flag") or elem.select_one(
                            "img.flag"
                        )

                    country = flag.get("title", "Brasil") if flag else "Brasil"

                    players.append(
                        {
                            "nickname": nickname,
                            "name": PLAYER_NAMES.get(nickname, "Não disponível"),
                            "country": country,
                            "status": "Não disponível",
                            "time_on_team": "Não disponível",
                            "maps_played": "Não disponível",
                            "rating": "Não disponível",
                        }
                    )

        return {"status": "success", "data": {"roster": players}}
    except Exception as e:
        print(f"Erro ao processar roster: {str(e)}")
        return {"status": "error", "message": str(e)}


@router.get("/coach", summary="Técnico atual da FURIA")
async def get_coach() -> Dict[str, Any]:
    """Retorna informações do técnico atual da FURIA"""
    try:
        html = get_html(settings.TEAM_FURIA_URL + "#tab-rosterBox")

        if not html:
            raise HTTPException(
                status_code=503, detail="Não foi possível obter dados do HLTV"
            )

        soup = BeautifulSoup(html, "html.parser")

        # Buscar a tabela de técnico
        coach_table = soup.select("table.coach-table")
        coach_data = {}

        if coach_table:
            rows = coach_table[0].select("tr")

            if len(rows) > 1:
                # Pular o cabeçalho e pegar a primeira linha
                cells = rows[1].select("td")

                if len(cells) >= 5:
                    # Célula do técnico (primeira coluna)
                    coach_cell = cells[0]

                    # Nome do técnico
                    coach_link = coach_cell.select_one("a")
                    if coach_link:
                        nickname = coach_link.text.strip()

                        # País
                        flag = coach_cell.select_one("img.flag")
                        country = flag.get("title", "Brasil") if flag else "Brasil"

                        # Outras informações
                        time_on_team = (
                            cells[1].text.strip() if len(cells) > 1 else "N/A"
                        )
                        maps_coached = (
                            cells[2].text.strip() if len(cells) > 2 else "N/A"
                        )
                        trophies = cells[3].text.strip() if len(cells) > 3 else "N/A"
                        winrate = cells[4].text.strip() if len(cells) > 4 else "N/A"

                        coach_data = {
                            "nickname": nickname,
                            "name": PLAYER_NAMES.get(nickname, "Não disponível"),
                            "country": country,
                            "time_on_team": time_on_team,
                            "maps_coached": maps_coached,
                            "trophies": trophies,
                            "winrate": winrate,
                        }

        # Se não encontrou dados do técnico
        if not coach_data:
            coach_data = {
                "nickname": "sidde",
                "name": "Pedro Bittencourt",
                "country": "Brasil",
                "time_on_team": "Não disponível",
                "maps_coached": "Não disponível",
                "trophies": "Não disponível",
                "winrate": "Não disponível",
            }

        return {"status": "success", "data": {"coach": coach_data}}
    except Exception as e:
        print(f"Erro ao processar informações do técnico: {str(e)}")
        return {"status": "error", "message": str(e)}


@router.get("/ranking", summary="Informações de ranking da FURIA")
async def get_ranking() -> Dict[str, Any]:
    """Retorna informações de ranking da FURIA"""

    try:
        html = get_html(settings.TEAM_FURIA_URL)

        if not html:
            raise HTTPException(
                status_code=503, detail="Não foi possível obter dados do HLTV"
            )

        soup = BeautifulSoup(html, "html.parser")

        world_ranking = "Não disponível"

        world_ranking_header = soup.find(text="World ranking")

        if world_ranking_header and world_ranking_header.parent:
            span_right = world_ranking_header.parent.find_next("span", class_="right")

            if span_right:
                ranking_link = span_right.select_one("a")

                if ranking_link:
                    rank_text = ranking_link.text.strip()
                    rank_match = re.search(r"#?(\d+)", rank_text)
                    if rank_match:
                        world_ranking = rank_match.group(1)
                else:
                    world_ranking = span_right.text.strip()

        if world_ranking == "Não disponível":
            ranking_link = soup.select_one('a[href^="/ranking/teams/"]')

            if ranking_link:
                rank_text = ranking_link.text.strip()

                rank_match = re.search(r"#?(\d+)", rank_text)
                if rank_match:
                    world_ranking = rank_match.group(1)

        return {
            "status": "success",
            "data": {
                "world_ranking": world_ranking,
                "region": "Brazil",
                "last_updated": datetime.now().strftime("%d/%m/%Y"),
            },
        }

    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Erro ao processar ranking: {str(e)}")
        return {"status": "error", "message": str(e)}


@router.get("/achievements", summary="Conquistas da FURIA")
async def get_achievements() -> Dict[str, Any]:
    """Retorna todas as conquistas (achievements) da FURIA"""

    try:
        html = get_html(settings.TEAM_FURIA_URL + "#tab-achievementsBox")

        if not html:
            raise HTTPException(
                status_code=503, detail="Não foi possível obter dados do HLTV"
            )

        soup = BeautifulSoup(html, "html.parser")

        achievement_tables = soup.select(".achievement-table")

        all_achievements = []

        for table in achievement_tables:
            rows = table.select("tbody tr")

            for row in rows:
                cells = row.select("td")
                if len(cells) >= 3:
                    placement = cells[0].text.strip()

                    tournament_cell = cells[1]
                    tournament_name = tournament_cell.text.strip()
                    tournament_link = None

                    tournament_a = tournament_cell.select_one("a")
                    if tournament_a and tournament_a.has_attr("href"):
                        tournament_link = f"https://www.hltv.org{tournament_a['href']}"

                    date_cell = cells[2]
                    date = date_cell.text.strip()

                    achievement = {
                        "placement": placement,
                        "tournament": tournament_name,
                        "date": date,
                        "tournament_link": tournament_link,
                    }

                    all_achievements.append(achievement)

        return {"status": "success", "data": {"achievements": all_achievements}}
    except Exception as e:
        print(f"Erro ao processar conquistas: {str(e)}")
        return {"status": "error", "message": str(e)}


@router.get("/info", summary="Informações gerais da FURIA")
async def get_info() -> Dict[str, Any]:
    """Retorna informações gerais da FURIA com conquistas atualizadas"""
    return {
        "name": "FURIA Esports",
        "founded": "2017",
        "location": "Brazil",
        "website": "https://www.furia.gg/",
    }
