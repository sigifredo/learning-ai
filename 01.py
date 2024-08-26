#!/bin/env python


# import keras as kr
import matplotlib.pyplot as plt
import numpy as np
# import tensorflow as tf
# import os

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Esto muestra solo errores fatales


# print("==> GPUs disponibles:", tf.config.list_physical_devices('GPU'))


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def step(x):
    return np.piecewise(x, [x < 0.0, x > 0.0], [0, 1])


def relu(x):
    # return np.piecewise(x, [x < 0.0, x > 0.0], [0, 1]) * x
    return np.maximum(0, x)


def mse(y, y_hat, derivate=False):
    if derivate:
        return (y_hat - y)
    else:
        return np.mean((y_hat - y)**2)


data = np.linspace(10, -10, 100)

# plt.plot(data, relu(data))
# plt.show()

real = np.array([0, 0, 1, 1])
prediction = np.array([0.9, 0.5, 0.2, 0.0])

print(mse(real, prediction))
