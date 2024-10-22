#plays two tones
# Write your code here :-)
from adafruit_circuitplayground import cp
cp.play_tone(262, 1)
cp.play_tone(294, 1)

#plays tones when press buttons
from adafruit_circuitplayground import cp
while True:
 if cp.button_a:
    cp.play_tone(262, 1)
 if cp.button_b:
    cp.play_tone(294, 1)

#Press button A. Now, press button B. Each button plays a tone, but only while it's being pressed
from adafruit_circuitplayground import cp
while True:
 if cp.button_a:
    cp.start_tone(262)
 elif cp.button_b:
    cp.start_tone(294)
 else:
    cp.stop_tone()

#read temperature
import time
import board
import microcontroller
while True:
 temperature = microcontroller.cpu.temperature # Get CPU temperature
 print(f"Temperature: {temperature:.2f} °C")
 time.sleep(1)