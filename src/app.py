from typing import Dict

from fastapi import FastAPI

from src.api.v1.router import router as router_v1

app = FastAPI()


@app.get("/ping", tags=["Ping"])
async def ping() -> Dict[str, str]:
    return {"ping": "ok"}


app.include_router(router=router_v1)
