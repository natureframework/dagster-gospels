from pandas import DataFrame, read_csv
from dagster import asset


@asset
def matthew() -> DataFrame:
    return read_csv(
        "https://raw.githubusercontent.com"
        "/ivandustin/bible/main/data/new/01-matthew.csv"
    )
