from matplotlib import pylab
print(pylab.__version__)

"""Use NumPy to generate random data"""
import numpy as np
x = np.linspace(0 , 10 , 25)
y = x * x + 2
print(x)
print(y)




print(np.array([x , y]) . reshape(25 , 2))


pylab.plot(x , y , 'g' , 'w')
pylab.show()



"""Drawing a subgraph"""
pylab.subplot(2 , 2 , 1) # The content of the brackets represent(rows , columns , indexes)
pylab.plot(x , y , 'r--')
pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'g--')
pylab.subplot(2 , 2 , 3)
pylab.plot(x , y , 'b--')
pylab.subplot(2 , 2 , 4)
pylab.plot(y , x , 'y--')
pylab.show()