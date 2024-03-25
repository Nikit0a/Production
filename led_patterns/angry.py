import time
import board
import neopixel

# Initialization of the LED stripnum_leds = 300
num_leds = 300
pixels = neopixel.NeoPixel(board.D18, num_leds, auto_write=False)

# Defining colors for the emotion "Anger"
colors = [
    (255, 78, 87),  # Dark red
    (255, 69, 40),  # Red
    (219, 81, 21)  # Orange
]

# Function for the "Breathing" effect
def breathing(color, min_brightness=0.1, max_brightness=0.9, cycle_duration=2):
    fade_steps = int(cycle_duration / 2 * 100)  # Divide the cycle duration in half and by 100 for the steps
    step_duration = cycle_duration / (fade_steps * 2)  # Total time for one step
    
    # Smooth increase in brightness
    for step in range(fade_steps):
        brightness = min_brightness + (max_brightness - min_brightness) * (step / fade_steps)
        pixels.brightness = brightness
        pixels.fill(color)
        pixels.show()
        time.sleep(step_duration)
    
    # Smooth decrease in brightness
    for step in range(fade_steps, 0, -1):
        brightness = min_brightness + (max_brightness - min_brightness) * (step / fade_steps)
        pixels.brightness = brightness
        pixels.fill(color)
        pixels.show()
        time.sleep(step_duration)

# An endless cycle of changing colors with smooth "breathing"
try:
    while True:
        for color in colors:
            breathing(color)
except KeyboardInterrupt:
    pixels.fill((0, 0, 0))
    pixels.show()
