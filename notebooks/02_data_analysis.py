# %%
import polars as pl

from ohlc_dss_model.data.integrity import sort_data
from ohlc_dss_model.utils.dt_utils import convert_to_timezone

# %%
data_path = "../data/raw/NAS100_30m.parquet"

# %%
df = pl.read_parquet(data_path)
df = convert_to_timezone(df)
print(df.head(5))

# %%
# The data is inverted so we must resort them so it goes from earliest -> latest
# This will make our job easier later on
df = sort_data(df)
print(df.head())

# %%
# We will then check for any duplicated rows
print(df.filter(df.is_duplicated()))
# Theres seem to be no duplicated rows so we can move on

# %%
# Next we will determine how we will define the interval for a single trading day

candle_timeframe = (
    df.select(pl.col("DateTime").dt.time().alias("TimeOfDay"))
    .unique()
    .sort("TimeOfDay")
)

print(candle_timeframe)
