import numpy as np

def tanhActivation(x):
    return np.tanh(x)

def sigmoidActivation(x):
    return 1 / (1 + np.exp(-x))

## simple nn to accept or reject credit card application
## simple data with 3 input features - income, age, education_level
## input  - 5 input with 3 featues (5x3)
## layer 1 - 5 neurons --> weights()
## output 1 - 5 output 


input = np.array([[10000, 35, 3],[15000, 25, 2],[45000, 38, 4],[75000, 41, 2],[75000, 29, 5]])
weights1 = np.array([[0.50, 0.35, 0.15],[0.45, 0.25, 0.3],[0.9, 0.05, 0.05],[0.85,0.10, 0.05],[0.25,0.25,0.5]])

layer1 = input @ weights1.T

weights2 = np.array([[0.25, 0.25, 0.25, 0.25, 0.25]])
layer2 = layer1 @ weights2.T
print(layer2)

print(tanhActivation(layer2))

