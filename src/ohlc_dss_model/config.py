from dataclasses import dataclass


# Expected column names from broker
@dataclass(frozen=True)
class Schema_cfg:
    datetime: str = "DateTime"


# Timezone properties to be used in time related operations
@dataclass(frozen=True)
class Timezone_cfg:
    eod_close_hour: int = 17
    broker: str = "EET"
    # desired data timezone, recommended to leave this be
    target: str = "America/New_York"


# Aliases
@dataclass(frozen=True)
class Project:
    schema: Schema_cfg = Schema_cfg()
    timezone: Timezone_cfg = Timezone_cfg()


config = Project()
