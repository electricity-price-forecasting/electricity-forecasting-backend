import os
from entsoe import EntsoePandasClient
from entsoe.exceptions import NoMatchingDataError

from src.settings import settings
import pandas as pd


class EntsoeLoader:

    def __init__(self, country=settings.country) -> None:
        api_key = os.getenv("ENTSOE_API_KEY")
        if not api_key:
            raise ValueError("Environment variable ENTSOE_API_KEY is not set.")
        self.client = EntsoePandasClient(api_key=api_key)
        self.country = country

    @staticmethod
    def _prepare_dataframe(df: pd.DataFrame | pd.Series) -> pd.DataFrame:
        if isinstance(df, pd.Series):
            df = df.to_frame()

        df.index = pd.to_datetime(df.index, utc=True)
        return df.sort_index()

    def get_prices(self, start: pd.Timestamp, end: pd.Timestamp) -> pd.DataFrame:
        try:
            prices = self.client.query_day_ahead_prices(
                country_code=self.country, start=start, end=end
            ).to_frame(name="price")
            prices = prices.resample("15min").interpolate(method="time").round(2)
            return self._prepare_dataframe(prices)
        except NoMatchingDataError:
            return pd.DataFrame(columns=["price"])
