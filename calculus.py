#!/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


def g(x):
    return x**2


def f(x):
    return np.sin(x)


x = np.linspace(-5, 5, num=1000)

plt.plot(x, f(g(x)))
plt.grid()
plt.axhline(y=0, color='r')
plt.axvline(x=0, color='r')
plt.show()
