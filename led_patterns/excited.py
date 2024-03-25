import time
import board
import neopixel
import random

# Initialization of the LED strip
num_leds = 300
pixels = neopixel.NeoPixel(board.D18, num_leds, auto_write=False)

# A list of colors for random selection
colors = [
    (255, 30, 0),  # Red 1
    (255, 27, 12),  # Red 2
    (107, 5, 4)    # Dark red
]

def smooth_flicker(min_brightness=0.1, max_brightness=0.5):
    fade_steps = 100  # The number of steps for a smooth transition
    while True:
        color = random.choice(colors)  # Random color selection
        # Gradual increase in brightness
        for step in range(fade_steps):
            brightness = min_brightness + (max_brightness - min_brightness) * (step / fade_steps)
            pixels.brightness = brightness
            pixels.fill(color)
            pixels.show()
            time.sleep(0.02)  # Control the speed of the brightness change
            
        # Gradual decrease in brightness
        for step in range(fade_steps, 0, -1):
            brightness = min_brightness + (max_brightness - min_brightness) * (step / fade_steps)
            pixels.brightness = brightness
            pixels.fill(color)
            pixels.show()
            time.sleep(0.02)  # Control the speed of the brightness change

try:
    smooth_flicker()
except KeyboardInterrupt:
    # Clear the strip on interrupt
    pixels.fill((0, 0, 0))
    pixels.show()
