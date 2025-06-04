from fastapi import FastAPI
from app.routes import vitibrasil

app = FastAPI(
    title="VitiBrasil API",
    description="API pública para dados de vitivinicultura da Embrapa",
    version="1.0.0"
)

app.include_router(vitibrasil.router)