from adafruit_circuitplayground import cp
import time

while True:
   cp.pixels.fill((0,0,10))
   cp.play_tone(500,0.5)
   time.sleep(0.5)
   cp.pixels.fill((10,0,0))
   cp.play_tone(900,0.5)