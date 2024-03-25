import time
import board
import neopixel

# LED strip initialization
num_leds = 300
pixels = neopixel.NeoPixel(board.D18, num_leds, brightness=0.2, auto_write=False)

# Function to create a "snake" effect
def snake_effect(snake_color, background_color, snake_length, wait):
    # Set the background color for the entire strip
    pixels.fill(background_color)
    pixels.show()

    while True:
        # Moving the "snake" forward
        for i in range(num_leds + snake_length):
            # Setting the colors for the "snake"
            for j in range(snake_length):
                # Calculating the current LED index
                pixel_index = (i - j) % num_leds
                pixels[pixel_index] = snake_color

            # Returning the last LED to the background color
            if i >= snake_length:
                tail_index = (i - snake_length) % num_leds
                pixels[tail_index] = background_color

            pixels.show()
            time.sleep(wait)

        # Brief pause before moving backward
        time.sleep(0.5)

        # Moving the "snake" backward
        for i in range(num_leds + snake_length - 1, -1, -1):
            # Setting the colors for the "snake"
            for j in range(snake_length):
                # Calculating the current LED index
                pixel_index = (i - j) % num_leds
                pixels[pixel_index] = snake_color

            # Returning the last LED to the background color
            if i < num_leds:
                tail_index = (i + 1) % num_leds
                pixels[tail_index] = background_color

            pixels.show()
            time.sleep(wait)

        # Brief pause before the next cycle
        time.sleep(0.5)

# Colors for the "snake" effect
snake_color = (0, 0, 255)  # Blue snake color
background_color = (50, 72, 160)  # Light blue background color

# Start the "snake" effect with a different shade of blue background
snake_effect(snake_color, background_color, 30, 0.05)  # Snake length of 30 LEDs, delay of 0.05 seconds