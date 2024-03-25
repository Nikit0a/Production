import board
import neopixel
import time

# LED strip configuration
LED_PIN = board.D18
NUM_LEDS = 300
led_strip = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=0.2, auto_write=False)

# Colors for reducing the emotion of fear
COLOR_CALM = (0, 255, 100)  # Soft green
COLOR_PEACE = (0, 155, 255)  # Sky blue

def breathe(color, cycles=5, max_brightness=0.5, min_brightness=0.1, speed=0.035):
    step = (max_brightness - min_brightness) / 30  # Brightness change step
    for _ in range(cycles):
        # Gradual increase in brightness
        brightness = min_brightness
        while brightness < max_brightness:
            led_strip.fill(tuple(int(c * brightness) for c in color))
            led_strip.show()
            brightness += step
            time.sleep(speed)
        
        # Gradual decrease in brightness
        while brightness > min_brightness:
            led_strip.fill(tuple(int(c * brightness) for c in color))
            led_strip.show()
            brightness -= step
            time.sleep(speed)
            
    # Return the strip to the initial state
    led_strip.fill((0, 0, 0))
    led_strip.show()

if __name__ == '__main__':
    # Switching between two colors to create a "breathing" effect
    while True:
        breathe(COLOR_CALM, cycles=1)
        breathe(COLOR_PEACE, cycles=1)
