import pygame
import pygame.gfxdraw  # Specific to ce for smoother shapes
import math
import random

# Initialise
pygame.init()
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors (Cyber-Matrix Palette)
BG = (2, 10, 5)
NEON_GREEN = (57, 255, 20)
SCAN_LINE = (0, 40, 0)

def draw_cyber_tunnel(time):
    num_rings = 15
    
    # Simulate a "system glitch" every few seconds
    glitch_offset = random.randint(-5, 5) if random.random() > 0.98 else 0
    
    for i in range(num_rings):
        # Progress from 0 (center) to 1 (edge)
        z = (i + (time % 1)) / num_rings
        
        # Exponential growth for 3D perspective
        radius = int(math.pow(z, 2) * (WIDTH / 1.5))
        
        if radius <= 0: continue

        # Dynamic Alpha (fades in from center)
        alpha = min(255, int(z * 255))
        color = (*NEON_GREEN, alpha)
        
        # Draw Smooth AA Circles using gfxdraw
        center_x = (WIDTH // 2) + glitch_offset
        center_y = (HEIGHT // 2) + glitch_offset
        
        # Main Ring
        pygame.gfxdraw.aacircle(screen, center_x, center_y, radius, color)
        
        # Draw "Data Nodes" on the rings
        for angle_deg in [0, 60, 120, 180, 240, 300]:
            rad = math.radians(angle_deg + (time * 20))
            nx = int(center_x + math.cos(rad) * radius)
            ny = int(center_y + math.sin(rad) * radius)
            
            # Pulsing node size
            node_size = int(3 * z) + 1
            pygame.draw.rect(screen, color, (nx, ny, node_size, node_size))

    # Add a horizontal "Scanner" sweep
    scan_y = int((time * 200) % HEIGHT)
    pygame.draw.line(screen, SCAN_LINE, (0, scan_y), (WIDTH, scan_y), 2)

# Main Loop
running = True
while running:
    # Use a surface with SRCALPHA for transparency/glow effects
    screen.fill(BG)
    
    t = pygame.time.get_ticks() /10.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_cyber_tunnel(t)
    
    # Add a subtle CRT scanline overlay
    for y in range(0, HEIGHT, 4):
        pygame.draw.line(screen, (0, 0, 0, 50), (0, y), (WIDTH, y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
