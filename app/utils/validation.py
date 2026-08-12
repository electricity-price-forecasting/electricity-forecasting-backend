import pandas as pd


def validate_dates(start, end):
    start = pd.Timestamp(start)
    end = pd.Timestamp(end)
    if start >= end:
        raise ValueError("Start date must be before end date")
    return start, end
