import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:

    entsoe_api_key: str = os.getenv("ENTSOE_API_KEY", "")
    country: str = os.getenv("COUNTRY", "PL")


settings = Settings()
