from audio import get_metronome_ticks
from bpm import calculate_bpm
from typing import List, Dict, Final
from numpy import float64

INITIAL_TIME: Final[int] = 0
INITIAL_TICK: Final[int] = 0
INITIAL_BPM: Final[int] = 120

def generate_chart(audio_path: str) -> None:
    print('Loading audio...')
    times = get_metronome_ticks(audio_path)
    print('Syncing track...')
    track = sync_track(times)
    print('Generating chart file...')
    print(track)


def sync_track(times: List[float64]) -> List[Dict]:
    track: List[Dict] = []
    
    prev_time = INITIAL_TIME
    current_tick = INITIAL_TICK
    current_bpm = INITIAL_BPM

    for current_time in times:
        data = calculate_bpm(current_bpm, current_tick, prev_time, current_time)
        track.append(data)

        current_bpm = data["next_bpm"]
        current_tick = data["next_tick"]
        prev_time = current_time
    
    return track