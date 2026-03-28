import win32gui
import win32api
import win32con
import time
import colorsys

def rainbow_effect():
    # Get handle to the entire desktop window
    hdc = win32gui.GetDC(0)
    
    # Get screen dimensions
    sw = win32api.GetSystemMetrics(0)
    sh = win32api.GetSystemMetrics(1)
    
    hue = 0
    try:
        while True:
            # Convert HSV color to RGB for a smooth rainbow transition
            # hue cycles from 0 to 1
            rgb = colorsys.hsv_to_rgb(hue, 1, 1)
            color = win32api.RGB(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))
            
            # Create a solid brush with the current color
            brush = win32gui.CreateSolidBrush(color)
            
            # Select the brush into the device context
            obj = win32gui.SelectObject(hdc, brush)
            
            # Apply the color to the screen using BitBlt or PatBlt
            # PATINVERT (0x5A0049) creates a "ghostly" inverted rainbow effect
            # DSTINVERT (0x00550009) inverts the current screen colors
            win32gui.PatBlt(hdc, 0, 0, sw, sh, win32con.PATINVERT)
            
            # Cleanup brush to prevent memory leak
            win32gui.SelectObject(hdc, obj)
            win32gui.DeleteObject(brush)
            
            # Increment hue and loop
            hue += 0.01
            if hue > 1: hue = 0
            
            time.sleep(0.01)
            
    except KeyboardInterrupt:
        # Release the DC and refresh screen
        win32gui.ReleaseDC(0, hdc)
        win32gui.InvalidateRect(0, None, True)
        print("Effect stopped.")

if __name__ == "__main__":
    rainbow_effect()
