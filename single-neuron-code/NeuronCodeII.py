# Basic neuron code with multiple inputs

import tensorflow as tf
import numpy as np

inputs = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[0.2,0.3,0.4,0.5,0.6]]
weights = [[0.28, -0.43, 0.58,0.66,-0.71],[0.22, -0.34, -0.46,-0.2, 0.3],[0.34, -0.52, 0.7,-0.2, 0.3 ],[0.123,-0.98,0.07,-0.88,0.31],[1,-1,0.6,-0.8,0]]
bias = [0.2, -0.3,0.22, -0.34, 0.46]

def activationFun3(x):
    return np.where(x>=0,1,-1)

weighted_sums=np.dot(inputs, weights)+bias
results= activationFun3(weighted_sums);
print(results)