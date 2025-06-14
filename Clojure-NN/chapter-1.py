## matrix operations with activation function

import numpy as np 

def x():
    return np.array([0, 2 ,7])

def threshold():
    return np.array([1, 2, 3])

def max(x, t):
    return np.maximum(x, t)

def subtract(t, x):
    return x - t

def signum(x):
    return np.sign(x)

def main():
    x_val = x()
    threshold_val = threshold()
    return signum(subtract(threshold_val, max(x_val, threshold_val)))


print(main())


    

