import pytest

from utils.validation import validate_dates
import pandas as pd


def test_validate_dates_rejects_invalid_range():
    with pytest.raises(ValueError):
        validate_dates(
            pd.Timestamp("2026-01-02"),
            pd.Timestamp("2026-01-01"),
        )
