import ctypes
import random
import time

# Load required Windows libraries
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# Get screen dimensions
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

# Get desktop device context
hdc = user32.GetDC(0)

# Function to draw random squares
def draw_random_squares(count=2000):
    for _ in range(count):
        x1 = random.randint(0, screen_width)
        y1 = random.randint(0, screen_height)
        x2 = x1 + random.randint(10, 200)
        y2 = y1 + random.randint(10, 200)
        color = random.randint(0, 0xFFFFFF)
        brush = gdi32.CreateSolidBrush(color)
        gdi32.SelectObject(hdc, brush)
        gdi32.Rectangle(hdc, x1, y1, x2, y2)
        gdi32.DeleteObject(brush)


# Function to create "melt" effect
def melt_screen(steps=5000):
    for _ in range(steps):
        x = random.randint(0, screen_width - 1)
        y = random.randint(0, screen_height - 1)
        w = random.randint(1, 50)
        h = random.randint(1, 50)
        gdi32.BitBlt(hdc, x, y + 5, w, h, hdc, x, y, 0x00CC0020)  # SRCCOPY
        time.sleep(0.01)

# Run effects in sequence
try:
    draw_random_squares(2000)
    rainbow_flash(3)
    melt_screen(2000)
except KeyboardInterrupt:
    print("\nStopping GDI effects...")
finally:
    # Release device context
    user32.ReleaseDC(0, hdc)
    print("GDI cleanup complete.")
