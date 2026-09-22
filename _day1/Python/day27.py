from matplotlib import pylab
print(pylab.__version__)
"""Use NumPy to generate random data"""
import numpy as np
x = np.linspace(0 , 10 , 25)
y = x * x + 2
print(x)
print(y)