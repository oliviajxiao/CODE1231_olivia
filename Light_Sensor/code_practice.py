# fading light

import time
import board
from analogio import AnalogOut
import digitalio

led = AnalogOut(board.A0)
MAX_CYCLE = 2 ** 16

button = digitalio.DigitalInOut(board.BUTTON_A)
button.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    for i in range(0, MAX_CYCLE, 64):
        led.value = i
        time.sleep(0.01)
    for i in range(MAX_CYCLE-1, 0, -64):
        led.value = i
        time.sleep(0.01)
        break


# Changing colours red, green, blue
# The Circuit Playground Express has 10 onboard RGB LEDs called NeoPixels. This code changes their colours

import time
import board
import neopixel
# Set up the NeoPixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.3)
while True:
    pixels.fill((255, 0, 0)) # Red
    time.sleep(1)
    pixels.fill((0, 255, 0)) # Green
    time.sleep(1)
    pixels.fill((0, 0, 255)) # Blue
    time.sleep(1)


# Simple Blinking LEDS
# This example makes your onboard lEDs blink!
import time
import board
import digitalio
led = digitalio.DigitalInOut(board.D13) # Onboard LED
led.direction = digitalio.Direction.OUTPUT
while True:
 led.value = True # Turn on the LED
 time.sleep(1) # Wait for 1 second
 led.value = False # Turn off the LED
 time.sleep(1) # Wait for 1 second


 #Light turns on when button is pressed
import time
import board
import digitalio
import neopixel
button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.DOWN
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2)
while True:
 if button_a.value: # If button A is pressed
    pixels.fill((255, 0, 0)) # Turn all NeoPixels red
 else:
    pixels.fill((0, 0, 0)) # Turn off all NeoPixels
 time.sleep(0.1)

 #senses the brightness of the light
import time
import board
import analogio
# Create an analog input for the light sensor
light = analogio.AnalogIn(board.LIGHT)
while True:
 light_level = light.value
 print("Light level:", light_level)
 time.sleep(1)

 #when light is too bright, neopixels turn on
 import time
import board
import analogio
import neopixel
# Create an analog input for the light sensor
light = analogio.AnalogIn(board.LIGHT)
# Set up the NeoPixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2)
# Function to convert raw sensor data to voltage
def get_voltage(pin):
 return (pin.value * 3.3) / 65536
while True:
 light_level = get_voltage(light)
 print("Light level:", light_level)

 # If it's bright, turn on the NeoPixels white, else turn them off
 if light_level > 1.5:
    pixels.fill((255, 255, 255)) # White if bright
 else:
    pixels.fill((0, 0, 0)) # Off if dark
 time.sleep(0.1)

