from argparse import ArgumentParser
from charter import generate_chart

parser = ArgumentParser("bpm-charter")
parser.add_argument("-m", "--metronome", help="Path to metronome (mp3 file)", type=str, required=True)
parser.add_argument("-s", "--start", help="Number of the beat where the song starts", type=int, default=0)
args = parser.parse_args()

generate_chart(args.metronome, args.start)