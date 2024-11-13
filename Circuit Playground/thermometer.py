from adafruit_circuitplayground import cp
import time
temp_c = cp.temperature
temp_f = (temp_c * 9 / 5) + 32
while True:
   if temp_f < 78:
      cp.pixels[0] = (0,0,1)
   elif temp_f > 78:
      for i in range(2):
         cp.pixels[i] = (0,0,1)
   elif temp_f > 79:
      for i in range(3):
         cp.pixels[i] = (0,0,1)
   elif temp_f > 80:
      for i in range(4):
         cp.pixels[i] = (1,1,0)
   elif temp_f > 81:
      for i in range(5):
         cp.pixels[i] = (1,1,0)
   elif temp_f > 82:
      for i in range(6):
         cp.pixels[i] = (1,1,0)
   elif temp_f > 83:
      for i in range(7):
         cp.pixels[i] = (1,1,0)
   elif temp_f > 84:
      for i in range(8):
         cp.pixels[i] = (1,0,0)
   elif temp_f > 85:
      for i in range(9):
         cp.pixels[i] = (1,0,0)
   elif temp_f > 86:
      for i in range(10):
         cp.pixels[i] = (1,0,0)