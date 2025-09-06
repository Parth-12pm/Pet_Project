from typing import cast

from fastapi import APIRouter, Depends, HTTPException, Request, status
from motor.motor_asyncio import AsyncIOMotorDatabase

from .models import Game, StartGame

router = APIRouter(prefix="/games", tags=["Games"])


# Dependency to get the MongoDB database from the application state
def get_mongodb_database(request: Request) -> AsyncIOMotorDatabase:
    # Use cast to inform mypy of the type of the attribute on the app state
    return cast(AsyncIOMotorDatabase, request.app.state.mongodb)


@router.post("/")
async def start_new_game(
    player_data: StartGame,
    db: AsyncIOMotorDatabase = Depends(get_mongodb_database),
) -> Game:
    data = {"player_1": player_data.player, "player_2": player_data.player}

    collection = db.get_collection("games")
    insert_result = await collection.insert_one(data)

    result = await collection.find_one({"_id": insert_result.inserted_id})
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not retrieve the created game.",
        )
    return Game(**result)
