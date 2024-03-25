import board
import neopixel
import time

# LED Strip Configuration
LED_PIN = board.D18
NUM_LEDS = 300
INITIAL_BRIGHTNESS = 0.5  # Initial brightness from 0.0 to 1.0

led_strip = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=INITIAL_BRIGHTNESS, auto_write=False)

def fade_to_black(step_delay=0.05, steps=100):
    # Calculate the brightness reduction step at each step of the cycle
    decrement = INITIAL_BRIGHTNESS / steps

    for step in range(steps, -1, -1):
        # Gradually reduce the brightness
        led_strip.brightness = step * decrement
        led_strip.show()
        time.sleep(step_delay)
    
    # Make sure that all the LEDs are turned off at the end
    led_strip.fill((0, 0, 0))
    led_strip.show()

if __name__ == '__main__':
    fade_to_black()
