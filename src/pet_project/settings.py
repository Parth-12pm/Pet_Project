from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="app_",
    )

    # MongoDB
    MONGO_DB_URL: str
    MONGO_DB_NAME: str


settings = AppSettings()
