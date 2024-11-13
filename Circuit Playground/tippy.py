from adafruit_circuitplayground import cp
import time
while True:
   for i in range(1,3):
      cp.pixels[i] = (0,10,0)
   for n in range(6,8):
      cp. pixels[n] = (0,0,0)