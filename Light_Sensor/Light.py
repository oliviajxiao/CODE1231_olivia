#turn light on with button

import board
import digitalio
import time
from adafruit_circuitplayground import cp

# Set up GPIO pin A1 for the external LED
led = digitalio.DigitalInOut(board.A1)
led.direction = digitalio.Direction.OUTPUT

# Main loop
while True:
    # Check if button A is pressed
    if cp.button_a:
        led.value = True  # Turn on the external LED
    else:
        led.value = False  # Turn off the external LED

    time.sleep(0.1)  # Short delay to debounce button


#Pulsing light when button is pressed
import time
import board
from analogio import AnalogOut
import digitalio

# Set up AnalogOut on pin A0 for the external LED
led = AnalogOut(board.A0)

# Maximum cycle for smooth analog fading
MAX_CYCLE = 2 ** 16 - 1

# Set up button A input
button = digitalio.DigitalInOut(board.BUTTON_A)
button.switch_to_input(pull=digitalio.Pull.DOWN)

# Main loop
while True:
    if button.value:  # Check if button A is pressed
        # Fade in
        for i in range(0, MAX_CYCLE, 1000):
            led.value = i
            time.sleep(0.01)
        # Fade out
        for i in range(MAX_CYCLE - 1, 0, -1000):
            led.value = i
            time.sleep(0.01)
    else:
        led.value = 0  # Turn off the LED when button A is not pressed


#swapping lights when button is pressed
import board
import digitalio
import time
from adafruit_circuitplayground import cp

# Set up GPIO pins for the LEDs
led1 = digitalio.DigitalInOut(board.A1)  # Default LED
led1.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.A2)  # LED that lights up when button A is pressed
led2.direction = digitalio.Direction.OUTPUT

# Main loop
while True:
    if cp.button_a:  # Check if button A is pressed
        led1.value = False  # Turn off LED1
        led2.value = True   # Turn on LED2
    else:
        led1.value = True   # Turn on LED1 (default)
        led2.value = False  # Turn off LED2

    time.sleep(0.1)  # Short delay for debounce

#swapping lights when button is pressed, but second light also pulses
import time
import board
from analogio import AnalogOut
import digitalio

# Set up DigitalOut for LED1 on pin A1 (default LED)
led1 = digitalio.DigitalInOut(board.A1)
led1.direction = digitalio.Direction.OUTPUT

# Set up AnalogOut on pin A0 for LED2 (pulsing LED)
led2 = AnalogOut(board.A0)

# Maximum cycle for smooth analog fading
MAX_CYCLE = 2 ** 16 - 1

# Set up button A input
button = digitalio.DigitalInOut(board.BUTTON_A)
button.switch_to_input(pull=digitalio.Pull.DOWN)

# Main loop
while True:
    if button.value:  # Check if button A is pressed
        led1.value = False  # Turn off LED1 (default)

        # Pulse LED2
        for i in range(0, MAX_CYCLE, 2000):
            led2.value = i
            time.sleep(0.01)
        for i in range(MAX_CYCLE - 1, 0, -2000):
            led2.value = i
            time.sleep(0.01)
    else:
        led1.value = True  # Turn on LED1 (default)
        led2.value = 0     # Turn off LED2

#Same as last, but uses neopixels on the circuit playground
import time
from adafruit_circuitplayground import cp

# Set up NeoPixel colors
LED_COLOR_GREEN = (0, 25, 0)  # Green color for default state
LED_COLOR_RED_MAX = (50, 0, 0)  # Red color for pulsing (max brightness reduced)
LED_COLOR_OFF = (0, 0, 0)  # Off state for pulsing

# Main loop
while True:
    if cp.button_a:  # Check if button A is pressed
        # Turn off all NeoPixels initially
        cp.pixels.fill(LED_COLOR_OFF)
        
        # Pulse all NeoPixels in red
        for brightness in range(0, 100, 5):  # Larger step size for quicker transitions
            scale = brightness / 100.0
            red_level = int(LED_COLOR_RED_MAX[0] * scale)  # Scale the red level
            cp.pixels.fill((red_level, 0, 0))  # Adjust red intensity
            cp.pixels.show()
            time.sleep(0.01)

        for brightness in range(100, 0, -5):  # Decreasing step size for fade-out
            scale = brightness / 100.0
            red_level = int(LED_COLOR_RED_MAX[0] * scale)  # Scale the red level
            cp.pixels.fill((red_level, 0, 0))  # Adjust red intensity
            cp.pixels.show()
            time.sleep(0.01)

    else:
        # Set all NeoPixels to green by default when button A is not pressed
        cp.pixels.fill(LED_COLOR_GREEN)
        cp.pixels.show()
