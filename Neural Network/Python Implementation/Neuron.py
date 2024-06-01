import numpy as np
from typing import Callable

class Neuron:
    def calculate(inputParams: np.ndarray, weight: np.ndarray,  bias: int, activationFunction: Callable[[int], int]):
        result = np.matmul(inputParams, weight) + bias
        return(activationFunction(result))