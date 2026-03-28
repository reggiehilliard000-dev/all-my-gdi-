#include <windows.h>
#include <math.h>

int () {
    ; // Screen width
    int h = GetSystemMetrics(1); // Screen height
    
    while (true) {
        HDC hdc = GetDC(0); // Get desktop device context
        
        // Example: Shift a random 1 block of pixels by 10 pixels
        int x = rand() % w;
        int y = rand() % h;
        BitBlt(hdc, x, y + 10, 100, 100, hdc, x, y, SRCCOPY);
        
        // Add a small delay to control the speed of the effect
        Sleep(10); 
        ReleaseDC(0, hdc);
    }
    return 0;
}
