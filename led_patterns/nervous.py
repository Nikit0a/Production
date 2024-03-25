import time
import board
import neopixel

# LED strip initialization
num_leds = 300
pixels = neopixel.NeoPixel(board.D18, num_leds, brightness=0.5, auto_write=False)

def chase_effect(main_color, background_color, chase_size=5, wait=0.05):
    while True:
        for i in range(num_leds + chase_size):
            # Set background color
            pixels.fill(background_color)
            
            # Determine the position of the chasing LEDs
            for j in range(chase_size):
                pixel_index = (i - j) % num_leds
                pixels[pixel_index] = main_color
            
            pixels.show()
            time.sleep(wait)

# Define colors
main_color = (255, 182, 193)  # Yellow-green
background_color = (50, 50, 50)  # Dark grey

try:
    chase_effect(main_color, background_color)
except KeyboardInterrupt:
    pixels.fill((0, 0, 0))
    pixels.show()
