from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session

from .repo import UserRepo
from .service import UserService


async def get_user_repo(
    session: Annotated[AsyncSession, Depends(get_async_session)],
) -> UserRepo:
    return UserRepo(session)


async def get_user_service(
    user_repo: Annotated[UserRepo, Depends(get_user_repo)],
) -> UserService:
    return UserService(user_repo)
