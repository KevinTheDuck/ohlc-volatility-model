from dataclasses import dataclass


# Expected column names from broker
@dataclass(frozen=True)
class Schema_cfg:
    datetime: str = "DateTime"


# Intraday Session Settings
@dataclass(frozen=True)
class Session_cfg:
    asian_session: tuple = ((18, 0), (3, 0))
    london_session: tuple = ((3, 0), (8, 30))
    # including am + pm sessions
    new_york_session: tuple = ((8, 30), (17, 0))


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
    session: Session_cfg = Session_cfg()


config = Project()
