from numpy import float64
from typing import Final
from math import floor

BEAT_TICKS: Final[int] = 192

def nearest_beat(bpm: int, time: float64) -> float:
    beat_seconds: float = 60 / bpm
    return time / beat_seconds

def nearest_tick(bpm: int, time: float64) -> int:
    return floor(nearest_beat(bpm, time)) * BEAT_TICKS

def nearest_compass(bpm: int, time: float64) -> float:
    return nearest_beat(bpm, time) / 4

def nearest_compass_tick(bpm: int, time: float64) -> int:
    return floor(nearest_compass(bpm, time)) * BEAT_TICKS