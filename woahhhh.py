import win32gui
import win32api
import win32con
import random
import time

def salien_melt():
    # Get the handle to the entire desktop screen
    hdc = win32gui.GetDC(0)
    
    # Get screen dimensions
    sw = win32api.GetSystemMetrics(0)
    sh = win32api.GetSystemMetrics(1)
    
    try:
        while True:
            # Pick a random x-coordinate for the vertical strip
            x = random.randint(0, sw)
            # Pick a random width for the strip (e.g., between 5 and 100 pixels)
            width = random.randint(5, 100)
            
            # BitBlt: Copy a strip and paste it 5 pixels lower
            # hdc: destination, (x, 5): destination top-left, (width, sh): size, 
            # hdc: source, (x, 0): source top-left, SRCCOPY: operation
            win32gui.BitBlt(hdc, x, 5, width, sh, hdc, x, 0, win32con.SRCCOPY)
            
            # Control the speed of the effect
            time.sleep(0)
            
    except KeyboardInterrupt:
        # Release the DC handle to avoid memory leaks
        win32gui.ReleaseDC(0, hdc)

if __name__ == "__main__":
    salien_melt()
