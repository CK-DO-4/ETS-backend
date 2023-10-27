from typing import Annotated, Dict

from fastapi import Depends, FastAPI, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.v1.router import router as router_v1
from src.database import get_async_session

app = FastAPI()


@app.get("/ping", tags=["Ping"], status_code=status.HTTP_200_OK)
async def ping(
    session: Annotated[AsyncSession, Depends(get_async_session)],
) -> Dict[str, str]:
    return {"ping": "ok"}


app.include_router(router=router_v1)
