import numpy as np
import random

"""
A simple neural network implementation from scratch using Python.
"""
class Network:
    def __init__(self, epoch: int, X : np.ndarray, y : np.ndarray, layers: np.array):
        self.inputSize = X.shape[1]
        self.input = X
        self.actualOuput = y
        self.layers = len(layers)
        self.weight = [np.random.randn(y,1) for y in layers[1:]]
        self.bias = [np.random.randn(y, x)
                        for x, y in zip(layers[:-1], layers[1:])]

    def sigmoid(z: int):
        return 1/(1+np.exp(-z))
    
    def forwardProp(self):
        result = self.input
        for weight, bias in zip(self.weight, self.bias):
            result = np.dot(self.result,weight) + bias
            result = np.array([self.sigmoid(x) for x in result])
        return result
        
    
    

    