#!/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 5**x


x = np.linspace(-5, 5, res=1000)
y = f(x)

plt.plot(x, y)
plt.grid()
plt.axhline(y=0, color='r')
plt.axvline(x=0, color='r')
plt.show()
