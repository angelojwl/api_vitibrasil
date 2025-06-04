from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth.jwt_handler import decode_jwt

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
    
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Usuário de autenticação inválido.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Token inválido ou expirado.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Credenciais de autenticação não fornecidas.")
    
    def verify_jwt(self, jwtoken: str) -> bool:
        payload = decode_jwt(jwtoken)
        return payload is not None