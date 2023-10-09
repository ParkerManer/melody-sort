from pydub import AudioSegment
from pydub.generators import Sine

class MusicGenerator:
    def __init__(self):
        # Define a mapping of musical notes to frequencies (Hz)
        self.note_mapping = {
            'C': 261.63,  # Middle C
            'D': 293.66,
            'E': 329.63,
            'F': 349.23,
            'G': 392.00,
            'A': 440.00,
            'B': 493.88,
        }

    def generate_tone(self, note, duration_ms=100):
        if note in self.note_mapping:
            frequency = self.note_mapping[note]
            tone = Sine(frequency)
            audio = tone.to_audio_segment(duration=duration_ms)
            return audio
        else:
            return AudioSegment.silent(duration=duration_ms)
