import os
from starlette.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=os.environ.get("ALLOWED_ORIGINS", "*"),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

app = FastAPI(middleware=middleware)

from app.login import router as login_router
from app.register import router as register_router
from app.user import router as user_router

app.include_router(login_router)
app.include_router(register_router)
app.include_router(user_router)
