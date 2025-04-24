from fastapi import APIRouter, HTTPException
from bs4 import BeautifulSoup
from core.scraper import get_html
from core.config import settings
from datetime import datetime
from typing import Dict, Any


PLAYER_NAMES = {
    "FalleN": "Gabriel Toledo",
    "yuurih": "Yuri Santos",
    "YEKINDAR": "Mareks Gaļinskis",
    "KSCERATO": "Kaike Cerato",
    "molodoy": "Bogdan Valovskiy",
    "chelo": "Marcelo Cespedes",
    "skullz": "Eduardo Teles",
    "sidde": "Pedro Bittencourt" # Coach
}


router = APIRouter(prefix="/api/furia", tags=["team"])


@router.get("/roster", summary="Elenco atual da FURIA")
def get_roster() -> Dict[str, Any]:
    """Retorna o elenco atual da FURIA com informações detalhadas"""
    try:
        # Com base na análise, sabemos que precisamos acessar a tab rosterBox
        html = get_html(settings.TEAM_FURIA_URL + "#tab-rosterBox")
        
        if not html:
            raise HTTPException(status_code=503, detail="Não foi possível obter dados do HLTV")
        
        soup = BeautifulSoup(html, "html.parser")
        
        # Vamos buscar a tabela de jogadores que identificamos na análise
        players = []
        players_table = soup.select("table.players-table")
        
        # Se encontrou a tabela de jogadores
        if players_table:
            rows = players_table[0].select("tr")
            
            # Pular o cabeçalho
            for row in rows[1:]:
                # Extrair células
                cells = row.select("td")
                if len(cells) >= 5:
                    # Célula do jogador (primeira coluna)
                    player_cell = cells[0]
                    
                    # Nome do jogador
                    player_link = player_cell.select_one("a")
                    if not player_link:
                        continue
                        
                    # Nickname está no link ou em um span específico
                    nickname_elem = player_cell.select_one(".text-ellipsis.bold, .playersBox-playernick")
                    nickname = nickname_elem.text.strip() if nickname_elem else player_link.text.strip()
                    nickname = nickname.split("\n")[0].strip()  # Limpar quebras de linha
                    
                    # País
                    flag = player_cell.select_one("img.flag")
                    country = flag.get("title", "Brasil") if flag else "Brasil"
                    
                    # Status (STARTER, BENCHED, etc)
                    status = cells[1].text.strip() if len(cells) > 1 else "N/A"
                    
                    # Tempo no time
                    time_on_team = cells[2].text.strip() if len(cells) > 2 else "N/A"
                    
                    # Mapas jogados
                    maps_played = cells[3].text.strip() if len(cells) > 3 else "N/A"
                    
                    # Rating
                    rating = cells[4].text.strip() if len(cells) > 4 else "N/A"
                    
                    # Adicionar jogador ao roster
                    players.append({
                        "nickname": nickname,
                        "name": PLAYER_NAMES.get(nickname, "Não disponível"),
                        "country": country,
                        "status": status,
                        "time_on_team": time_on_team,
                        "maps_played": maps_played,
                        "rating": rating
                    })
        
        # Se não encontrou jogadores na tabela, tenta o método anterior que já está funcionando
        if not players:
            player_elements = soup.select(".text-ellipsis.nickname-container")
            
            if not player_elements:
                player_elements = soup.select(".playerFlagName")
                
            if not player_elements and soup.select_one(".bodyshot-team"):
                bodyshot_text = soup.select_one(".bodyshot-team").text.strip()
                names = [name.strip() for name in bodyshot_text.split("\n") if name.strip()]
                
                for name in names:
                    players.append({
                        "nickname": name,
                        "name": PLAYER_NAMES.get(name, "Não disponível"),
                        "country": "Não disponível",
                        "status": "Não disponível",
                        "time_on_team": "Não disponível",
                        "maps_played": "Não disponível",
                        "rating": "Não disponível"
                    })
                
                return {"status": "success", "data": {"roster": players}}
            
            for elem in player_elements:
                nickname = elem.text.strip()
                if nickname:
                    flag = None
                    
                    if elem.parent:
                        flag = elem.parent.select_one("img.flag") or elem.select_one("img.flag")
                    
                    country = flag.get("title", "Brasil") if flag else "Brasil"
                    
                    players.append({
                        "nickname": nickname,
                        "name": PLAYER_NAMES.get(nickname, "Não disponível"),
                        "country": country,
                        "status": "Não disponível",
                        "time_on_team": "Não disponível",
                        "maps_played": "Não disponível",
                        "rating": "Não disponível"
                    })
        
        return {"status": "success", "data": {"roster": players}}
    except Exception as e:
        print(f"Erro ao processar roster: {str(e)}")
        return {"status": "error", "message": str(e)}


@router.get("/coach", summary="Técnico atual da FURIA")
def get_coach() -> Dict[str, Any]:
    """Retorna informações do técnico atual da FURIA"""
    try:
        html = get_html(settings.TEAM_FURIA_URL + "#tab-rosterBox")
        
        if not html:
            raise HTTPException(status_code=503, detail="Não foi possível obter dados do HLTV")
        
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
                        time_on_team = cells[1].text.strip() if len(cells) > 1 else "N/A"
                        maps_coached = cells[2].text.strip() if len(cells) > 2 else "N/A"
                        trophies = cells[3].text.strip() if len(cells) > 3 else "N/A"
                        winrate = cells[4].text.strip() if len(cells) > 4 else "N/A"
                        
                        coach_data = {
                            "nickname": nickname,
                            "name": PLAYER_NAMES.get(nickname, "Não disponível"),
                            "country": country,
                            "time_on_team": time_on_team,
                            "maps_coached": maps_coached,
                            "trophies": trophies,
                            "winrate": winrate
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
                "winrate": "Não disponível"
            }
        
        return {"status": "success", "data": {"coach": coach_data}}
    except Exception as e:
        print(f"Erro ao processar informações do técnico: {str(e)}")
        return {"status": "error", "message": str(e)}


@router.get("/ranking", summary="Informações de ranking da FURIA")
def get_ranking() -> Dict[str, Any]:
    """Retorna informações de ranking da FURIA"""
    
    try:
        html = get_html(settings.TEAM_FURIA_URL)
        
        if not html:
            raise HTTPException(status_code=503, detail="Não foi possível obter dados do HLTV")
        
        soup = BeautifulSoup(html, "html.parser")
        
        # Tentar encontrar o rank mundial
        ranking_elem = soup.select_one(".profile-team-stat .right")
        world_ranking = ranking_elem.text.strip() if ranking_elem else "Não disponível"
        
        return {
            "status": "success", 
            "data": {
                "world_ranking": world_ranking,
                "region": "Brasil",
                "last_updated": datetime.now().strftime("%d/%m/%Y")
            }
        }
    
    except HTTPException as e:
        raise e
    except Exception as e:
        return {"status": "error", "message": str(e)}