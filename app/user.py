from fastapi import Depends, APIRouter
from dotenv import load_dotenv
from app.utils.jwt import get_current_user

load_dotenv()

router = APIRouter()


@router.get("/users/me")
def read_users_me(current_user: str = Depends(get_current_user)):
    return {"user": current_user}
