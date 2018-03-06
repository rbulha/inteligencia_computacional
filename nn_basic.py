#!/usr/bin/python3.5
import numpy as np

def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

def NN(ms, ws, b):
    z = b
    for m,w in ms,ws:
        z += m*w
    return sigmoid(z)

def random_weights(n):
    return [np.random.randn() for t in range(n)]

def random_bias():
    return np.random.randn()
