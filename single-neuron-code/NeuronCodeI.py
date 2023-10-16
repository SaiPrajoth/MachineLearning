# this is single input single neuron code.

import tensorflow as tf
import numpy as np

input = np.array([[0.2, 0.3, 0.5],
                      [0.1, 0.2, 0.4],
                      [0.3, 0.4, 0.6]])

weights = np.array([[0.1, 0.2, 0.3],
                    [0.2, 0.3, 0.4],
                    [0.3, 0.4, 0.5]])

bias = np.array([0.05, 0.1, 0.15])

def activationFunction(x): #activation function
    return np.where(x >= 0, x, 0)

weighted_sums = np.dot(input, weights)+bias # the linear equation

result = activationFunction(weighted_sums)

print(results)