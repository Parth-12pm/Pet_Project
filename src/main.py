from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .api.views import router as api_router
from .db.util import close_db_client, get_db_client
from .pet_project.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # set up mongodb
    client = get_db_client()
    app.state.mongodb = client.get_database(settings.MONGO_DB_NAME)
    yield
    close_db_client()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "Hello World this is my first FastAPI application"}
