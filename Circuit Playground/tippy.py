from adafruit_circuitplayground import cp
import time
while True:
    x, y, z = cp.acceleration
    if x > 1:
        for i in range(1,4):
            cp.pixels[i] = (0,0,10)
        for n in range(6,9):
            cp.pixels[n] = (0,0,0)
    elif x < -1:
        for i in range(1,4):
            cp.pixels[i] = (0,0,0)
        for n in range(6,9):
            cp.pixels[n] = (0,0,10)