import time
import numpy as np 

def reluActivation(x):
    return np.maximum(x, 0)

def tanhActivation(x):
    return np.tanh(x)

def sigmoidActivation(x):
    return 1 / (1 + np.exp(-x))

class NeuralNetworkLayer:
    def __init__(self, input, weight, bias, activationFn, in_dim, out_dim):
        self.input = input
        self.weight = weight
        self.bias = bias
        self.activationFn = activationFn
        self.in_dim = in_dim
        self.out_dim = out_dim

    def execute(self):
        w = np.array(self.weight).reshape(self.out_dim, self.in_dim, order='F')
        return self.activationFn(np.array(self.bias) + np.matmul(self.input, w.T))
    

def testWithVectorInput():
    np.random.seed(42)  # For reproducibility

    start = time.time()
    input = np.random.randn(50000)
    weights1 = np.random.randn(25000 * 50000)
    bias1 = np.random.randn(25000)
    layer1 = NeuralNetworkLayer(input, weights1, bias1, reluActivation, 50000, 25000)
    t1 = time.time()
    out1 = layer1.execute()
    t2 = time.time()
    print(f"Layer 1 execution time: {t2-t1:.2f} seconds")

    weights2 = np.random.randn(10000 * 25000)
    bias2 = np.random.randn(10000)
    layer2 = NeuralNetworkLayer(out1, weights2, bias2, reluActivation, 25000, 10000)
    t3 = time.time()
    out2 = layer2.execute()
    t4 = time.time()
    print(f"Layer 2 execution time: {t4-t3:.2f} seconds")

    weights3 = np.random.randn(10 * 10000)
    bias3 = np.random.randn(10)
    layer3 = NeuralNetworkLayer(out2, weights3, bias3, sigmoidActivation, 10000, 10)
    t5 = time.time()
    out3 = layer3.execute()
    t6 = time.time()
    print(f"Layer 3 execution time: {t6-t5:.2f} seconds")

    print("Total time:", f"{t6-start:.2f} seconds")
    print(out3)

def tsetWithMatrixInput(): #batching
    np.random.seed(42)  # For reproducibility
    start = time.time()
    input = np.random.randn(5* 50000) ### this in only line changing for batching
    weights1 = np.random.randn(25000 * 50000)
    bias1 = np.random.randn(25000)
    layer1 = NeuralNetworkLayer(input, weights1, bias1, reluActivation, 50000, 25000)
    t1 = time.time()
    out1 = layer1.execute()
    t2 = time.time()
    print(f"Layer 1 execution time: {t2-t1:.2f} seconds")

    weights2 = np.random.randn(10000 * 25000)
    bias2 = np.random.randn(10000)
    layer2 = NeuralNetworkLayer(out1, weights2, bias2, reluActivation, 25000, 10000)
    t3 = time.time()
    out2 = layer2.execute()
    t4 = time.time()
    print(f"Layer 2 execution time: {t4-t3:.2f} seconds")

    weights3 = np.random.randn(10 * 10000)
    bias3 = np.random.randn(10)
    layer3 = NeuralNetworkLayer(out2, weights3, bias3, sigmoidActivation, 10000, 10)
    t5 = time.time()
    out3 = layer3.execute()
    t6 = time.time()
    print(f"Layer 3 execution time: {t6-t5:.2f} seconds")

    print("Total time:", f"{t6-start:.2f} seconds")
    print(out3)

#print("************* Without batching ************")
#testWithVectorInput()  

print("************* With batching ************")
tsetWithMatrixInput()  