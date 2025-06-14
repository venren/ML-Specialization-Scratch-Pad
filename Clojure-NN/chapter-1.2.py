## Matrix operations with activation functions
# 
import numpy as np 

def input():
    inp = np.array([[0.3, 0.6],[0.1, 2],[0.9, 3.7 ],[0, 1]])
    return inp

def weight():
    w = np.array([0.3, 0.9])
    return w

def threshold():
    return np.array([0.7, 0.2, 1.1, 2])


def relu_process():
    input_val = input()
    weight_val = weight()
    threshold_val = threshold()

    weighted = np.matmul(input_val, weight_val)
    #threshold_val = np.maximum(weighted, threshold_val)
    sub = np.subtract(weighted, threshold_val )
    print(sub)


relu_process()