import random as random
import math

def calculate_pi():
    total = 199900
    r = 1.0
    inside = 0
    for i in range(0, total):
        x2 = random.random()**2
        y2 = random.random()**2
        if math.sqrt(x2+y2) <= r:
            inside+=1
    
    pi = 4 * inside/total
    return pi

print(calculate_pi())