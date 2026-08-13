import pandas as pd


def normalize_timezone(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts the DataFrame index to the UTC timezone.
    If the index is timezone-naive, it localizes it to UTC.
    """
    if df.empty:
        return df

    if df.index.tz is None:
        df.index = df.index.tz_localize("UTC")
    else:
        df.index = df.index.tz_convert("UTC")

    return df


def resample_to_15min(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts hourly data resolution to 15-minute intervals.
    Applies linear interpolation based on time to ensure smooth transitions.
    """
    if df.empty:
        return df

    return df.resample("15min").interpolate(method="time").round(2)