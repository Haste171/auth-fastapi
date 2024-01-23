from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi import Depends, APIRouter
from app.utils.pwd import hash_password
from app.utils.models import User
from app.utils.database import get_db

router = APIRouter()


class UserCreate(BaseModel):
    username: str
    password: str


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(username=user.username, hashed_password=hash_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"username": db_user.username}
