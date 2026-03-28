import ctypes
import time
import random

# Load user32 and gdi32 DLLs
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# Get desktop device context
hDC = user32.GetDC(0)
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

try:
    while True:
        # Random shrink factor for tunnel effect
        shrink = random.randint(1, 100)

        # StretchBlt parameters:
        # (destDC, x, y, width, height, srcDC, srcX, srcY, srcWidth, srcHeight, rop)
        gdi32.StretchBlt(
            hDC,
            shrink, shrink,
            screen_width - shrink * 2,
            screen_height - shrink * 2,
            hDC,
            0, 0,
            screen_width,
            screen_height,
            0xCC0020  # SRCCOPY
        )

        time.sleep(0)

except KeyboardInterrupt:
    pass

# Release DC
user32.ReleaseDC(0, hDC)
from mingus.core import scales

# Get the notes for a Whole Tone scale starting on C
modern_scale = scales.WholeTone("C").ascending()
import numpy as np
import sounddevice as sd

# Settings
sps = 44100       # Samples per second
duration_s = 3.0  # Length of sound
carrier_hz = 440.0 # Base pitch
modulator_hz = 5.0 # How fast it "wobbles"
wobble_depth = 50.0 # How much the pitch swings

# Generate time samples
t_samples = np.arange(duration_s * sps)

# Frequency Modulation formula
# This creates a "sliding" pitch effect typical of sci-fi sounds
carrier = 2 * np.pi * t_samples * carrier_hz / sps
modulator = wobble_depth * np.sin(2 * np.pi * t_samples * modulator_hz / sps)
output = np.cos(carrier + modulator)

# Play the sound
print("Playing alien wobble...")
sd.play(output, sps)
sd.wait()
