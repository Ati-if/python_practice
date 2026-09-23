from matplotlib import pyplot as plt

"""Drawing a subgraph"""

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

plt.subplot(2, 1, 1)  # rows, columns, index
plt.plot(x, y, 'r--')  # third parameter = color and line style

plt.subplot(2, 1, 2)
plt.plot(y, x, 'g+-')
plt.show()