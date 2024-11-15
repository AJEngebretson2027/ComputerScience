from adafruit_circuitplayground import cp
import time
import random
while True:
   if cp.button_a:
      dice = (random.randint(0,10))
      cp.pixels.fill((0,0,0))
      for i in range(dice):
         cp.pixels[i] = (0,0,10)
         while cp.button_a:
            pass
   if cp.button_b:
      cp.pixels.fill((0,0,0))