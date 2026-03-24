import polars as pl

from ohlc_dss_model.config import config


# for sorting data based on column name
def sort_data(
    df: pl.DataFrame, col: str = config.schema.datetime, descending: bool = False
) -> pl.DataFrame:
    return df.sort(col, descending=descending)
