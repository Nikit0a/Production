import time
import board
import neopixel

# LED strip initialization
num_leds = 300
pixels = neopixel.NeoPixel(board.D18, num_leds, auto_write=False)

def smooth_turn_on(target_brightness=0.4, duration=2):
    steps = int(duration * 50)  # Approximate number of steps for smoothness
    initial_brightness = 0.1
    pixels.brightness = initial_brightness
    step_increase = (target_brightness - initial_brightness) / steps
    
    for i in range(steps):
        pixels.brightness += step_increase
        pixels.fill((255, 182, 193))  # Using light pink for turning on
        pixels.show()
        time.sleep(duration / steps)

def gradient_flow(colors, cycle_duration=2):
    steps_per_color = int(cycle_duration / len(colors) * 100)  # Number of steps per color
    total_steps = steps_per_color * len(colors)
    
    while True:
        for i in range(total_steps):
            color_index = (i // steps_per_color) % len(colors)
            next_color_index = (color_index + 1) % len(colors)
            
            fraction = (i % steps_per_color) / steps_per_color
            r = int(colors[color_index][0] + (colors[next_color_index][0] - colors[color_index][0]) * fraction)
            g = int(colors[color_index][1] + (colors[next_color_index][1] - colors[color_index][1]) * fraction)
            b = int(colors[color_index][2] + (colors[next_color_index][2] - colors[color_index][2]) * fraction)
            
            for pixel in range(num_leds):
                pixels[pixel] = (r, g, b)
            pixels.show()
            time.sleep(cycle_duration / total_steps)

# Definition of pink shades
colors = [
    (255, 182, 193),  # Light pink
    (255, 105, 180),  # Medium pink
    (219, 112, 147)   # Dark pink
]

try:
    smooth_turn_on()
    gradient_flow(colors)
except KeyboardInterrupt:
    pixels.fill((0, 0, 0))
    pixels.show()
