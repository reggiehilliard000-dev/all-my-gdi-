import ctypes
import random
import time

# Load required Windows libraries
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# Get the desktop device context
hdc = user32.GetDC(0)

# Get screen dimensions
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

try:
    for _ in range(100):  # Draw 100 rectangles
        # Random position and size
        left = random.randint(0, screen_width - 50)
        top = random.randint(0, screen_height - 50)
        right = left + random.randint(20, 200)
        bottom = top + random.randint(20, 200)

        # Random color
        color = gdi32.CreateSolidBrush(random.randint(0, 0xFFFFFF))

        # Select brush and draw
        gdi32.SelectObject(hdc, color)
        gdi32.Rectangle(hdc, left, top, right, bottom)

        # Clean up brush
        gdi32.DeleteObject(color)

        time.sleep(0.05)  # Small delay for visible effect

finally:
    # Release the device context
    user32.ReleaseDC(0, hdc)