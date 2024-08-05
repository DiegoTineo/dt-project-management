import datetime
from fastapi import HTTPException, Request, status
from functools import wraps

from app.utils.jwt import validateJWT

# def createJWT():
#     payload = {
#         "user_id": 123,
#         "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
#     }
#     token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
#     return token

# def validateJWT(token):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#         return payload
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Token has expired",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     except jwt.InvalidTokenError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

def get_token_header(request: Request):
    auth_header = request.headers.get("Authorization")
    if auth_header is None or not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization header",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = auth_header.split(" ")[1]
    return token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = kwargs.get('token', None)
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token is missing",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        validation_response = validateJWT(token)
        if isinstance(validation_response, str):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=validation_response,
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        return f(*args, **kwargs)
    return decorated