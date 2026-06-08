from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from database import AsyncSessionLocal
from core.config import settings
from models import User
from core.security import verifier_access_token

async def get_db():
    async with AsyncSessionLocal as session:
        yield session

