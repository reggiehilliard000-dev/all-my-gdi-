import time
import GDI_effects.GDI as GDI

# This script creates visual effects without damaging the system.
# GDI_effects handles the Win32 API calls safely.

def run_harmless_prank():
    print("Starting GDI Effect... (Press Ctrl+C in this console to stop, or close the window)")
    
    # 1. Effect: Screen Melting
    # Simulates the screen dripping down
    GDI.melt_screen(speed=10, intensity=5)
    
    # 2. Effect: Screen Invert
    # Inverts the colors of the screen
    GDI.invert_screen()
    time.sleep(2)
    GDI.invert_screen() # Invert back

    # 3. Effect: Text Drawing
    # Draws "GDI Prank" on the screen at random locations 100 times
    GDI.type_text("GDI EFFECT", 100)
    
    # 4. Effect: Screen Shaking
    GDI.shake_screen(intensity=10, duration=5)

    print("Effect Finished.")

if __name__ == "__main__":
    # Give the user a moment before the prank starts
    time.sleep(1)
    run_harmless_prank()
