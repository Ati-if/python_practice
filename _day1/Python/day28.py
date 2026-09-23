# Example 1: vertical subplots
from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

plt.subplot(2, 1, 1)
plt.plot(x, y, 'r--')

plt.subplot(2, 1, 2)
plt.plot(y, x, 'g+-')

plt.show()

# Example 2: horizontal subplots
import pylab

pylab.subplot(1, 2, 1)
pylab.plot(x, y, 'r--')

pylab.subplot(1, 2, 2)
pylab.plot(y, x, 'g+-')

pylab.show()

# Example 3: custom axes
from matplotlib import pyplot as plt

fig = plt.figure()
axis = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axis.plot(x, y, 'b')
axis.set_xlabel('X-Label')
axis.set_ylabel('Y-Label')
axis.set_title('Title')

plt.show()





fig, axes = plt.subplots(nrows=3, ncols=4)  # subplots are 3 rows and 4 columns
for ax in axes.flat:
    ax.plot(x, y, 'b')

plt.tight_layout()
plt.show()