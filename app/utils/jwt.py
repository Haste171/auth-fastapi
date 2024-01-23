import jwt
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends, HTTPException
from dotenv import load_dotenv

load_dotenv()


# CHANGE THESE TO ENV VAR!!!!!!
JWT_SECRET_KEY = "your-secret-key"
JWT_ALGORITHM = "HS256"

bearer_scheme = HTTPBearer()


def create_access_token(data: dict):
    encoded_jwt = jwt.encode(data, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt


def get_bearer_token(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
):
    if credentials:
        return credentials.credentials
    else:
        raise HTTPException(
            status_code=401, detail="Invalid authentication credentials"
        )


def get_current_user(token: str = Depends(get_bearer_token)):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=401, detail="Invalid authentication credentials"
            )
        return username
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=401, detail="Invalid authentication credentials"
        )
