from adafruit_circuitplayground import cp
import time

while True: 
   if cp.switch:
      for i in range(5):
        cp.pixels[i] = (0,0,10)
      for n in range(5,10):
           cp.pixels[n] = (0,0,0)
   else:
      for i in range(5):
        cp.pixels[i] = (0,0,0)
      for n in range(5,10):
           cp.pixels[n] = (0,0,10)