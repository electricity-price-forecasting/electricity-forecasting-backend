import unittest
import pandas as pd
from unittest.mock import Mock, patch
import sys

# =====================================================================
# ВАЖНО: Заглушка (Mock) для модуля настроек.
# Должна стоять ДО импорта HistoricalDatasetBuilder.
# Это не даст Pydantic упасть с ошибкой ValidationError из-за базы данных.
# =====================================================================
mock_settings = Mock()
mock_settings.country = "PL"  # Задаем дефолтную страну, чтобы лоудер не ругался

mock_settings_module = Mock()
mock_settings_module.settings = mock_settings

# Обманываем Python: когда кто-то попытается сделать "from config.settings import settings",
# он получит наш фейковый объект вместо падения Pydantic.
sys.modules["config"] = Mock()
sys.modules["config.settings"] = mock_settings_module
sys.modules["app.config"] = Mock()
sys.modules["app.config.settings"] = mock_settings_module
# =====================================================================

# Теперь можно безопасно импортировать наш класс
from app.services.dataset_builder import HistoricalDatasetBuilder


class TestHistoricalDatasetBuilder(unittest.TestCase):

    def test_merge_energy_data_outer_join(self):
        """
        Test that the merge uses an outer join and does not drop rows
        if data is missing in one of the DataFrames.
        """
        # Create a mock prices DataFrame (only 10:00 and 10:30)
        prices_index = pd.to_datetime(["2026-01-01 10:00", "2026-01-01 10:30"], utc=True)
        prices_df = pd.DataFrame({"price": [100.0, 150.0]}, index=prices_index)

        # Create a mock load DataFrame (only 10:00 and 10:15)
        load_index = pd.to_datetime(["2026-01-01 10:00", "2026-01-01 10:15"], utc=True)
        load_df = pd.DataFrame({"load": [1000.0, 1100.0]}, index=load_index)

        # Execute the merge
        result = HistoricalDatasetBuilder.merge_energy_data(prices_df, load_df)

        # Assertions
        # Must preserve all 3 unique timestamps (10:00, 10:15, 10:30)
        self.assertEqual(len(result), 3)

        # Missing values should be filled with NaN
        self.assertTrue(pd.isna(result.loc["2026-01-01 10:15", "price"]))
        self.assertTrue(pd.isna(result.loc["2026-01-01 10:30", "load"]))

        # Existing values should merge correctly
        self.assertEqual(result.loc["2026-01-01 10:00", "price"], 100.0)
        self.assertEqual(result.loc["2026-01-01 10:00", "load"], 1000.0)

    @patch("app.services.dataset_builder.get_cached_or_fetch")
    def test_build_trims_data_to_exact_dates(self, mock_get_cached):
        """
        Test that the builder correctly trims the full month cached data
        down to the exact requested dates.
        """
        # 1. Setup mock data (full August 2026)
        full_month_index = pd.date_range("2026-08-01", "2026-08-31", freq="15min", tz="UTC")
        mock_df = pd.DataFrame({"dummy_col": 1}, index=full_month_index)

        # Make the cache wrapper return the full month
        mock_get_cached.return_value = mock_df

        # 2. Initialize the builder with a dummy loader
        builder = HistoricalDatasetBuilder(loader=Mock())

        # 3. Request data strictly from Aug 10 to Aug 15
        start_req = "2026-08-10"
        end_req = "2026-08-15"

        result = builder.build(start_date=start_req, end_date=end_req)

        # 4. Assertions for accurate trimming
        # First row must be exactly Aug 10 00:00 UTC
        expected_start = pd.Timestamp(start_req, tz="UTC")
        self.assertEqual(result.index.min(), expected_start)

        # Last row must be exactly Aug 15 00:00 UTC
        expected_end = pd.Timestamp(end_req, tz="UTC")
        self.assertEqual(result.index.max(), expected_end)

        # Verify chronological sorting
        self.assertTrue(result.index.is_monotonic_increasing)


if __name__ == "__main__":
    unittest.main()