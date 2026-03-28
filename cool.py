import ctypes
import random
import time

# Load GDI and User32
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# Get desktop device context
hdc = user32.GetDC(0)

# Get screen size
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

try:
    while True:
        # Random rectangle position and size
        x = random.randint(0, screen_width - 100)
        y = random.randint(0, screen_height - 100)
        w = random.randint(50, 300)
        h = random.randint(50, 300)

        # Random offset for glitch effect
        dx = x + random.randint(-50, 50)
        dy = y + random.randint(-50, 50)

        # BitBlt with SRCINVERT for color cycling glitch
        gdi32.BitBlt(hdc, dx, dy, w, h, hdc, x, y, 0x00660046)

        time.sleep(0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)  # Control speed
except KeyboardInterrupt:
    pass
finally:
    user32.ReleaseDC(0, hdc)