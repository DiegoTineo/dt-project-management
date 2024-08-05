import jwt
import datetime

SECRET_KEY = "your_secret_key"

def createJWT():
    payload = {
        "user_id": 123,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def validateJWT(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return "Token has expired"
    except jwt.InvalidTokenError:
        return "Invalid token"