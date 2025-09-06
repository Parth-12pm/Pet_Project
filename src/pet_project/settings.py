from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    # Mongodb
    MONGO_DB_URL: str
    MONGO_DB_NAME: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="App_",
    )


settings = AppSettings()
