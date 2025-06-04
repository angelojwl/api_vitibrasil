from fastapi import FastAPI
from app.routes import vitibrasil
from app.auth.auth_bearer import JWTBearer
from fastapi import Depends


app = FastAPI(title="VitiBrasil API", description="API pública para webscrapping dos dados de vitivinicultura da Embrapa", version="1.0.0")

app.include_router(vitibrasil.router, dependencies=[Depends(JWTBearer())])
