from dagster import Definitions
from .assets.create import create as create_assets

defs = Definitions(assets=create_assets())
