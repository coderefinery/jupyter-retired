import math
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn
%matplotlib inline

def step():
    return 1. if random.random() > .5 else -1.

def walk(n):
    x = np.zeros(n)
    dx = 1. / n
    for i in range(n - 1):
        x_new = x[i] + dx * step()
        if x_new > 5e-3:
            x[i + 1] = 0.
        else:
            x[i + 1] = x_new
    return x

n = 100000
x = walk(n)