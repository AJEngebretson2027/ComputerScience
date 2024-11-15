from adafruit_circuitplayground import cp
import time
import random
shake = 2.0
cp.pixels.brightness =0.1
while True:
   x, y, z = cp.acceleration
   if abs(z) <= shake:
      for i in range(10):
         gambling = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
         cp.pixels[i] = (gambling)