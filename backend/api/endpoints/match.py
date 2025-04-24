from fastapi import APIRouter, HTTPException
from bs4 import BeautifulSoup
from core.scraper import get_html
from core.config import settings
from typing import Dict, Any
from datetime import datetime
import re


router = APIRouter(prefix="/api/furia", tags=["matches"])


@router.get("/debug-results", summary="Analisa o HTML da página de resultados")
def debug_results() -> Dict[str, Any]:
    """Endpoint para depurar o HTML da página de resultados da FURIA"""
    try:
        # URL específica para resultados da FURIA
        results_url = f"{settings.HLTV_BASE_URL}/results?team=8297"
        html = get_html(results_url)
        
        if not html:
            return {"status": "error", "message": "Não foi possível obter o HTML"}
            
        soup = BeautifulSoup(html, "html.parser")
        
        debug_info = {}
        
        # Título da página para confirmar que estamos na página correta
        title = soup.find("title")
        debug_info["title"] = title.text if title else None
        
        # Encontrar containers de resultados
        result_containers = soup.select(".results-sublist")
        container_info = []
        
        for i, container in enumerate(result_containers[:2]):  # Analisar apenas os 2 primeiros para não sobrecarregar
            # Data do grupo de resultados
            date_header = container.select_one(".standard-headline")
            date_text = date_header.text.strip() if date_header else "Data não encontrada"
            
            # Resultados individuais
            match_results = container.select(".result-con")
            matches = []
            
            for j, match in enumerate(match_results[:3]):  # Primeiros 3 resultados de cada data
                match_data = {
                    "index": j,
                    "html_structure": str(match)[:200] + "...",  # Primeiros 200 caracteres
                    "teams": [team.text.strip() for team in match.select(".team")],
                    "score": match.select_one(".result-score").text.strip() if match.select_one(".result-score") else None,
                    "event": match.select_one(".event-name").text.strip() if match.select_one(".event-name") else None,
                    "map": match.select_one(".map-text").text.strip() if match.select_one(".map-text") else None,
                    "importance": len(match.select(".stars i")),
                    "classes": match.get("class", [])
                }
                
                # Verificar link da partida
                match_link = match.select_one("a")
                if match_link and match_link.has_attr("href"):
                    match_data["link"] = match_link["href"]
                
                matches.append(match_data)
            
            container_info.append({
                "container_index": i,
                "date": date_text,
                "match_count": len(match_results),
                "sample_matches": matches
            })
        
        debug_info["result_containers"] = container_info
        
        # Analisar estrutura de elementos importantes
        element_samples = {}
        
        # Tags importantes para análise
        important_selectors = [
            ".results-holder", 
            ".results-sublist",
            ".result-con", 
            ".team", 
            ".event-name",
            ".map-text",
            ".result-score",
            ".stars"
        ]
        
        for selector in important_selectors:
            elements = soup.select(selector)
            if elements:
                element_samples[selector] = {
                    "count": len(elements),
                    "example": str(elements[0])[:150] + "..." if elements else "Não encontrado"
                }
        
        debug_info["element_samples"] = element_samples
        
        return {
            "status": "success",
            "data": {
                "debug_info": debug_info,
                "base_url": results_url
            }
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

@router.get("/results", summary="Histórico de resultados da FURIA")
def get_results_history(limit: int = 10) -> Dict[str, Any]:
    """
    Retorna o histórico detalhado de resultados das partidas da FURIA.
    
    Args:
        limit: Número máximo de resultados a retornar (padrão: 10)
    """
    try:
        results_url = f"{settings.HLTV_BASE_URL}/results?team=8297"
        html = get_html(results_url)
        
        if not html:
            raise HTTPException(status_code=503, detail="Não foi possível obter dados do HLTV")
        
        soup = BeautifulSoup(html, "html.parser")
        
        results = []
        result_containers = soup.select(".results-sublist")
        
        # Para cada grupo de resultados (agrupados por data)
        for container in result_containers:
            # Extrai a data do grupo
            date_header = container.select_one(".standard-headline")
            date_str = date_header.text.strip() if date_header else "Data não disponível"
            
            # Para cada resultado de partida
            match_results = container.select(".result-con")
            for match in match_results:
                if len(results) >= limit:
                    break
                
                # Extrair times
                team_elements = match.select(".team")
                if len(team_elements) < 2:
                    continue  # Pular se não encontrar os dois times
                    
                team1 = team_elements[0].text.strip()
                team2 = team_elements[1].text.strip()
                
                # Extrair placar
                score_element = match.select_one(".result-score")
                if not score_element:
                    continue  # Pular se não encontrar o placar
                
                # Processa o placar para extrair pontuação de cada time
                score_text = score_element.text.strip()
                score_parts = score_text.split('-')
                
                team1_score = score_parts[0].strip()
                team2_score = score_parts[1].strip()
                
                # Evento
                event_element = match.select_one(".event-name")
                event = event_element.text.strip() if event_element else "Evento desconhecido"
                
                # Formato da partida (BO3, BO1, etc)
                map_element = match.select_one(".map-text")
                match_format = map_element.text.strip() if map_element else "Formato desconhecido"
                
                # Importância do jogo (quantidade de estrelas)
                stars_elements = match.select(".stars i")
                importance = len(stars_elements)
                
                # Link da partida
                match_link = None
                match_link_element = match.select_one("a.a-reset")
                if match_link_element and match_link_element.has_attr("href"):
                    match_link = f"{settings.HLTV_BASE_URL}{match_link_element['href']}"
                
                # Determina se a FURIA ganhou ou perdeu
                furia_is_team1 = "FURIA" in team1
                furia_score = team1_score if furia_is_team1 else team2_score
                opponent_score = team2_score if furia_is_team1 else team1_score
                opponent_name = team2 if furia_is_team1 else team1
                
                # Determinando o resultado
                if int(furia_score) > int(opponent_score):
                    result = "vitória"
                elif int(furia_score) < int(opponent_score):
                    result = "derrota"
                else:
                    result = "empate"
                
                # Adiciona o resultado processado à lista
                results.append({
                    "date": date_str,
                    "opponent": opponent_name,
                    "score": {
                        "furia": int(furia_score),
                        "opponent": int(opponent_score),
                        "text": f"{furia_score}:{opponent_score}"
                    },
                    "result": result,
                    "event": event,
                    "format": match_format,
                    "importance": importance,
                    "match_url": match_link
                })
                
                if len(results) >= limit:
                    break
        
        return {
            "status": "success",
            "data": {
                "results": results,
                "count": len(results)
            }
        }
    
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Erro ao processar resultados: {str(e)}")
        return {"status": "error", "message": str(e)}

@router.get("/next_match", summary="Próxima partida da FURIA")
def get_next_furia_match() -> Dict[str, Any]:
    """Retorna informações sobre a próxima partida da FURIA"""
    
    try:
        html = get_html(settings.TEAM_FURIA_URL)
        
        if not html:
            raise HTTPException(status_code=503, detail="Não foi possível obter dados do HLTV")
        
        soup = BeautifulSoup(html, "html.parser")
        
        upcoming_match = soup.select_one(".upcoming-match")
        
        if not upcoming_match:
            return {"status": "success", "data": None, "message": "Nenhuma partida agendada encontrada"}
        
        opponent = upcoming_match.select_one(".team-logo")
        opponent_name = opponent.get("title", "TBD") if opponent else "TBD"
        
        date_element = upcoming_match.select_one(".date")
        match_date = date_element.text.strip() if date_element else "Data não disponível"
        
        event_element = upcoming_match.select_one(".event-name")
        event = event_element.text.strip() if event_element else "Evento não especificado"
        
        return {
            "status": "success",
            "data": {
                "opponent": opponent_name,
                "date": match_date,
                "event": event,
                "team": "FURIA"
            }
        }
    
    except HTTPException as e:
        raise e
    except Exception as e:
        return {"status": "error", "message": str(e)}
