## simple matrix operations

import numpy as np 

def x():
    return np.array([[0.3, 0.6],[0.1, 2], [0.9, 3.7], [0.0, 1.0] ])

def weight():
    return np.array([0.3, 0.9])

def threshold():
    return np.array([0.7, 0.2, 1.1, 2])

def max(x, t):
    return np.maximum(x, t)

def subtract(t, x):
    return x - t

def signum(x):
    return np.sign(x)

def main():
    x_val = x()
    weight_val = weight()
    threshold_val = threshold()
    result = np.matmul(x_val, weight_val)
    return signum(subtract(threshold_val, max(result, threshold_val)))


print(main())


    

