import time
import board
import neopixel

num_leds = 300
pixels = neopixel.NeoPixel(board.D18, num_leds, brightness=0.5, auto_write=False)

def interpolate_color(color_start, color_end, step, total_steps):
    """Interpolates between two colors."""
    r_start, g_start, b_start = color_start
    r_end, g_end, b_end = color_end
    
    r = r_start + (r_end - r_start) * step / total_steps
    g = g_start + (g_end - g_start) * step / total_steps
    b = b_start + (b_end - b_start) * step / total_steps
    
    return int(r), int(g), int(b)

def smooth_transition():
    color_start = (255, 50, 0)  # Yellow beginning
    color_end = (244, 100, 0)  # Orange 
    steps = 100
    for step in range(steps + 1):
        color = interpolate_color(color_start, color_end, step, steps)
        pixels.fill(color)
        pixels.show()
        time.sleep(0.05)

smooth_transition()
