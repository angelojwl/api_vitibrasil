from fastapi import Depends
from app.auth.jwt_handler import sign_jwt
from app.models.user import User

@app.post("/login")
def login(user: User):
    if user.username == "admin" and user.password == "admin":
        return sign_jwt(user.username)
    return {"error": "Usuário inválido"}