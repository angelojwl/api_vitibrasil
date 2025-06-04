import time
import jwt

SECRET_KEY = "senha_123_api"
ALGORITHM = "HS256"
EXPIRATION_TIME = 3600  # 1 hora

def sign_jwt(user_id: str):
    payload = {
        "user_id": user_id,
        "expires": time.time() + EXPIRATION_TIME
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_jwt(token: str):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return None