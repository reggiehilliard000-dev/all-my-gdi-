import ctypes

import random
import time

# Load required Windows GDI functions
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# Get the device context for the entire screen
hdc = user32.GetDC(0)

# Define POINT structure for MoveToEx and LineTo
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

# Screen dimensions
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

# Draw 1000 random lines
try:
    for _ in range(5000):
        # Random start and end points
        x1 = random.randint(0, screen_width - 1)
        y1 = random.randint(0, screen_height - 1)
        x2 = random.randint(0, screen_width - 1)
        y2 = random.randint(0, screen_height - 1)

        # Random RGB color
        color = random.randint(0, 0xFFFFFF)

        # Set pen color
        pen = gdi32.CreatePen(0, 1, color)
        gdi32.SelectObject(hdc, pen)

        # Move to start point and draw line
        gdi32.MoveToEx(hdc, x1, y1, ctypes.byref(POINT()))
        gdi32.LineTo(hdc, x2, y2)

        # Small delay so you can see the drawing
        time.sleep(0.000001)

finally:
    # Release the device context
    user32.ReleaseDC(0, hdc)
