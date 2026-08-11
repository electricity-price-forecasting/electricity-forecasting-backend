import os
from entsoe import EntsoePandasClient
from src.settings import settings


class EntsoeLoader:

    def __init__(self, country=settings.country) -> None:
        api_key = os.getenv("ENTSOE_API_KEY")
        if not api_key:
            raise ValueError("Environment variable ENTSOE_API_KEY is not set.")
        self.client = EntsoePandasClient(api_key=api_key)
        self.country = country