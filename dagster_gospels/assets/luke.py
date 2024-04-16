from pandas import DataFrame, read_csv
from dagster import asset


@asset
def luke() -> DataFrame:
    return read_csv(
        "https://raw.githubusercontent.com/ivandustin/bible/main/data/new/03-luke.csv"
    )
