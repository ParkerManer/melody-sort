import numpy as np
import pyaudio

def generate_tone(frequency, duration, fade_duration=0.01):
    # Constants
    sample_rate = 44100  # Sample rate (samples/second)
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)  # Time array

    # Generate sine wave with fade-in and fade-out
#    fade_samples = int(sample_rate * fade_duration)
#    fade_in = np.linspace(0, 1, fade_samples)
#    fade_out = np.linspace(1, 0, fade_samples)
    sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t).astype(np.float32)
#    sine_wave[:fade_samples] *= fade_in
#    sine_wave[-fade_samples:] *= fade_out

    return sine_wave


def play_tone(frequency, duration, buffer_size=1024):
    p = pyaudio.PyAudio()

    tone = generate_tone(frequency, duration)

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=96000,
                    output=True,
                    frames_per_buffer=buffer_size)  # Specify the buffer size

    stream.write(tone.tobytes())
    stream.stop_stream()
    stream.close()

    p.terminate()

if __name__ == "__main__":
    # Set the frequency (in Hz) and duration (in seconds) of the tone
    frequency = 440  # 440 Hz is A4
    duration = 2  # 2 seconds

    # Increase the buffer size to a suitable value (e.g., 4096 or 8192)
    buffer_size = 2048

    play_tone(frequency, duration, buffer_size)


    
