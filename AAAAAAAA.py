import win32gui
import win32api
import win32con
import random
import time

def glitch_effect():
    hdc = win32gui.GetDC(0)
    sw = win32api.GetSystemMetrics(0)
    sh = win32api.GetSystemMetrics(1)
    
    try:
        # Run for 15 seconds
        end_time = time.time() + 60
        while time.time() < end_time:
            # Randomly pick a source area
            x1, y1 = random.randint(0, sw), random.randint(0, sh)
            # Randomly pick a destination area
            x2, y2 = random.randint(0, sw), random.randint(0, sh)
            
            # Pick a random size for the "chunk"
            w, h = random.randint(50, 400), random.randint(50, 400)
            
            # Teleport the pixels from (x1, y1) to (x2, y2)
            win32gui.BitBlt(
                hdc, x2, y2, w, h, 
                hdc, x1, y1, win32con.SRCCOPY
            )
            
            # High speed for that "digital noise" feel
            time.sleep(0.005)
            
    finally:
        win32gui.ReleaseDC(0, hdc)

if __name__ == "__main__":
    print("Glitching screen... refresh your desktop to clear.")
    glitch_effect()
