from adafruit_circuitplayground import cp
import time
import random
count = 0
while True:
   if cp.button_b:
      cp.pixels[count] = (0,0,0)
      count = count - 1
      for i in range(count):
         cp.pixels[i] = (0,0,10)
      while cp.button_b:
            pass
   elif cp.button_a:
      count += 1
      for i in range(count):
         cp.pixels[i] = (0,0,10)
      while cp.button_a:
            pass