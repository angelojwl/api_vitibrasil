from fastapi import APIRouter, HTTPException
from app.services.scraper import scrape_data
from app.utils.fallback import load_fallback_data

router = APIRouter(prefix="/vitibrasil", tags=["VitiBrasil"])

@router.get("/{ano}/{categoria}/{subcategoria}")
async def get_data(ano: int, categoria: str, subcategoria: str):
    try:
        data = scrape_data(ano, categoria, subcategoria)
        return {"ano": ano, "categoria": categoria, "subcategoria": subcategoria, "dados": data}
    except Exception as e:
        fallback_data = load_fallback_data(ano, categoria, subcategoria)
        if fallback_data:
            return {"ano": ano, "categoria": categoria, "subcategoria": subcategoria, "dados": fallback_data, "fonte": "fallback"}
        raise HTTPException(status_code=500, detail=str(e))
