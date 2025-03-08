from typing import Final
from audio import get_metronome_ticks
from bpm import nearest_compass_tick

AUDIO_PATH: Final[str] = ""

metronome_ticks = get_metronome_ticks(AUDIO_PATH)

x = nearest_compass_tick(120, metronome_ticks[0])

print(x)