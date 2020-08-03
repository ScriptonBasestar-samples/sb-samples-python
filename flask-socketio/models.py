from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Tick:
    """Class for mark price"""
    t: int  # time
    p: float  # price
    v: float  # volume


@dataclass_json
@dataclass
class Candle:
    """Class for candle data"""
    t: int  # time
    o: float  # open
    h: float  # high
    l: float  # low
    c: float  # close
    v: float  # volume
