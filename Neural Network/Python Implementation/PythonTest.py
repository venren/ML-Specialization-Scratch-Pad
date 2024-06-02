import numpy as np

layers = np.array([10,30,10])
numberOfLayers  = len(layers)
neurons = layers
weight = [np.random.randn(y,1) for y in layers[1:]]
bias = [np.random.randn(y, x)
                for x, y in zip(layers[:-1], layers[1:])]
print("I am here!!!")