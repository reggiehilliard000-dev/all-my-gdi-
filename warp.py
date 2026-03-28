import ctypes
import math
import time

# Load GDI functions
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# Get screen dimensions
sw = user32.GetSystemMetrics(0)
sh = user32.GetSystemMetrics(1)

# Get device context for the entire screen
hdc = user32.GetDC(0)

# Main loop
t = 0
try:
    while True:
        for y in range(0, sh, 2):  # Step by 2 for speed
            offset = int(math.sin(y / 10 + t) * 0)  # Wave distortion
            gdi32.BitBlt(hdc, offset, y, sw, 2, hdc, 100, y, 0x00CC0020)  # SRCCOPY
        t += 0.1
        time.sleep(0)
except KeyboardInterrupt:
    pass

# Release device context
user32.ReleaseDC(0, hdc)