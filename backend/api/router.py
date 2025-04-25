from fastapi import APIRouter
from api.endpoints import match, team, debug

router = APIRouter()

router.include_router(match.router)
router.include_router(team.router)
router.include_router(debug.router)


@router.get("/")
def root():
    return {
        "message": "FURIA CS2 API",
        "version": "1.0.0",
        "documentation": "/api/docs",
        "endpoints": {
            "/api/furia/next_match": "Próxima partida da FURIA",
            "/api/furia/results": "Resultados recentes da FURIA",
            "/api/furia/roster": "Elenco atual",
            "/api/furia/coach": "Informações do técnico",
            "/api/furia/ranking": "Informações de ranking",
            "/api/furia/info": "Informações gerais da equipe",
            "/api/furia/achievements": "Conquistas da FURIA",
            "/api/furia/debug_html": "Debug de qualquer URL (para analise de estrutura)",
        },
    }
