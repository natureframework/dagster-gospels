from dagster import Definitions
from .assets.matthew import matthew
from .assets.mark import mark
from .assets.luke import luke
from .assets.john import john

defs = Definitions(assets=[matthew, mark, luke, john])
