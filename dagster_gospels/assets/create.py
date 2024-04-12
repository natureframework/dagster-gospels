from ..constants.urls import MATTHEW, MARK, LUKE, JOHN
from ..asset.create import create as create_asset


def create():
    names = ["matthew", "mark", "luke", "john"]
    urls = [MATTHEW, MARK, LUKE, JOHN]
    assets = [create_asset(name, url) for name, url in zip(names, urls)]
    return assets
