import polars as pl

from ohlc_dss_model.config import Volatility_cfg

def yang_zhang(df: pl.DataFrame, mode: str, n: int = Volatility_cfg.n) -> pl.DataFrame:
    k = 0.34 / (1.34 + (n + 1) / (n - 1))

    log_overnight = (pl.col("O_Asia") / pl.col("C_New York").shift(1)).log()

    if mode == "historical":
        log_oc = (pl.col("C_New York") / pl.col("O_Asia")).log()
        h = pl.max_horizontal("H_Asia", "H_London", "H_New York")
        l = pl.min_horizontal("L_Asia", "L_London", "L_New York")
        o = pl.col("O_Asia")
        c = pl.col("C_New York")

    elif mode == "today":
        log_oc = (pl.col("C_London") / pl.col("O_Asia")).log()
        h = pl.max_horizontal("H_Asia", "H_London")
        l = pl.min_horizontal("L_Asia", "L_London")
        o = pl.col("O_Asia")
        c = pl.col("C_London")

    rs = (h / c).log() * (h / o).log() + (l / c).log() * (l / o).log()
    df = df.with_columns([
        log_overnight.alias("_log_overnight"),
        log_oc.alias("_log_oc"),
        rs.alias("_rs"),
    ])

    yz = (
        pl.col("_log_overnight").rolling_var(n)
        + k * pl.col("_log_oc").rolling_var(n)
        + (1 - k) * pl.col("_rs").rolling_mean(n)
    )

    label = "Sigma_Historical" if mode == "historical" else "Sigma_Today"

    return df.with_columns(
        yz.sqrt().alias(label)
    ).drop(["_log_overnight", "_log_oc", "_rs"])