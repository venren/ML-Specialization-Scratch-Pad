import numpy as np
import random

"""
A simple neural network implementation from scratch using Python.
"""
class Network:
    def __init__(self, epochs: int, X : np.ndarray, y : np.ndarray, layers: np.array):
        self.inputSize = X.shape[1]
        self.input = X
        self.actualOuput = y
        self.layers = len(layers)
        self.weight = [np.random.randn(y,1) for y in layers[1:]]
        self.bias = [np.random.randn(y, x)
                        for x, y in zip(layers[:-1], layers[1:])]
        self.epochs = epochs

    def sigmoid(z: int):
        return 1/(1+np.exp(-z))
    
    def forwardProp(self):
        result = self.input
        for weight, bias in zip(self.weight, self.bias):
            result = np.dot(self.result,weight) + bias
            result = np.array([self.sigmoid(x) for x in result])
        return result
    
    def expectedVsActual(activation, actual):
        return(activation - y)
    
    def sigmoid_prime(z):
        """Derivative of the sigmoid function."""
        return sigmoid(z)*(1-sigmoid(z))

    """
        1. Forward propogation 
    """
    def gradientDescent(self):
        batchSize = 100
        for epoch in range(self.epochs):
            random.shuffle(self.input)
            miniBatchX = [self.input[x : x+batchSize] for x in range(0, len(self.input), batchSize)]
            miniBatchY = [self.input[x : x+batchSize] for x in range(0, len(self.actualOuput), batchSize)]

            for batch in zip(miniBatchX, miniBatchY):
                nabla_w = [np.zeros(w.shape) for w in self.weight]
                nabla_b = [np.zeros(b.shape) for b in self.bias]
                
                for x, y in batch:
                    nabla_minbatch_w = [np.zeros(w.shape) for w in self.weight]
                    nabla_minbatch_b = [np.zeros(b.shape) for b in self.bias]

                    activation = x
                    activations = [x]
                    zs = []

                    for w, b in zip(self.weight, self.bias):
                        z = np.dot(x,w) + b
                        zs.append(z)
                        activation = self.sigmoid(z)
                        activations.append(activation)

                    delta = self.expectedVsActual(activations[-1], y) * sigmoid_prime(zs[-1])                       





        
    
    

    