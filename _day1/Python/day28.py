from matplotlib import pyplot as plt

"""Drawing a subgraph"""

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

plt.subplot(2, 1, 1)  # rows, columns, index
plt.plot(x, y, 'r--')  # third parameter = color and line style

plt.subplot(2, 1, 2)
plt.plot(y, x, 'g+-')
plt.show()


import pylab
pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'r--')
pylab.subplot(1 , 2 , 2)
pylab.plot(y , x , 'g+-')
pylab.subplot(1 , 2 , 1)
pylab.plot(y , x , 'g+-')
pylab.show()