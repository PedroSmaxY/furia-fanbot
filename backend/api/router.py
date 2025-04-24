from fastapi import APIRouter
from api.endpoints import match, team

router = APIRouter()

router.include_router(match.router)
router.include_router(team.router)

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
            "/api/furia/ranking": "Informações de ranking"
        }
    }