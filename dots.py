import ctypes
import math
import time
import random

# Load GDI and User32
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# Get desktop device context
hDC = user32.GetDC(0)

# Screen size
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

# Function to create RGB color
def rgb(r, g, b):
    return r | (g << 8) | (b << 16)

# Animation loop
t = 0
try:
    while True:
        for y in range(0, height, 5):
            for x in range(0, width, 5):
                r = int((math.sin(x / 50 + t) + 1) * 127)
                g = int((math.sin(y / 50 + t) + 1) * 127)
                b = int((math.sin((x + y) / 50 + t) + 1) * 127)
                color = rgb(r, g, b)
                gdi32.SetPixel(hDC, x, y, color)
        t += 0.1
        time.sleep(0.000000000000000000000000000000000000000000000000001)
except KeyboardInterrupt:
    pass

# Release DC
user32.ReleaseDC(0, hDC)