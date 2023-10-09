import numpy as np
import pyaudio

def generate_tone(frequency, duration):
    # Constants
    sample_rate = 44100  # Sample rate (samples/second)
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)  # Time array

    # Generate sine wave
    sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t).astype(np.float32)

    return sine_wave

def play_tone(frequency, duration):
    p = pyaudio.PyAudio()

    tone = generate_tone(frequency, duration)

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=44100,
                    output=True)

    stream.write(tone.tobytes())
    stream.stop_stream()
    stream.close()

    p.terminate()

if __name__ == "__tone_generator__":
    # Set the frequency (in Hz) and duration (in seconds) of the tone
    frequency = 440  # 440 Hz is A4
    duration = 2  # 2 seconds

    play_tone(frequency, duration)
