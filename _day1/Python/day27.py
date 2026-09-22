from matplotlib import pylab
print(pylab.__version__)
"""Use NumPy to generate random data"""
import numpy as np
x = np.linspace(0 , 10 , 25)
y = x * x + 2
print(x)
print(y)



print(np.array([x , y]) . reshape(25 , 2))


"""It only takes only one command to draw"""
pylab.plot(x , y , 'g' , 'w') # r stands for red