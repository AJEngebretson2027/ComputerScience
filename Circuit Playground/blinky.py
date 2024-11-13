from adafruit_circuitplayground import cp
import time

while True: 
   cp.pixels.fill((0, 0, 10))
   time.sleep(0.367)
   cp.pixels.fill((0,0,0))
   time.sleep(0.367)