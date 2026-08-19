from typing import ClassVar

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    entsoe_api_key: str = Field(validation_alias="ENTSOE_API_KEY")
    country: str = Field(default="PL", validation_alias="COUNTRY")

    PROJECT_NAME: str = "Electricity Price Forecasting"
    BASE_DIR: ClassVar[Path] = Path(__file__).resolve().parents[1]

    raw_file: Path = BASE_DIR / "data" / "raw" / "historical_dataset.csv"
    cache_dir: Path = BASE_DIR / "data" / "cache"

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


settings: Settings = Settings()  # type: ignore[call-arg]
