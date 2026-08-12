from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    entsoe_api_key: str
    country: str = "PL"

    PROJECT_NAME: str = "Electricity Price Forecasting"

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    POSTGRES_ECHO: bool = False

    REDIS_PORT: int
    REDIS_HOST: str

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


settings: Settings = Settings()  # type: ignore[call-arg]