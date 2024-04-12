from pandas import DataFrame, read_csv
from dagster import asset


def create(name, url):
    @asset(name=name)
    def function() -> DataFrame:
        return read_csv(url)

    return function
