from motor.motor_asyncio import AsyncIOMotorClient

from ..pet_project.settings import settings

_mongodb_client: AsyncIOMotorClient | None = None


def get_db_client() -> AsyncIOMotorClient:
    """Get a singleton MongoDB client instance."""
    global _mongodb_client
    if _mongodb_client is None:
        _mongodb_client = AsyncIOMotorClient(settings.MONGO_DB_URL)
    return _mongodb_client


def close_db_client() -> None:
    """Close the singleton MongoDB client instance."""
    global _mongodb_client
    if _mongodb_client:
        _mongodb_client.close()
        _mongodb_client = None
