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







#Draw a picture or graph inside another graph
fig = pylab.figure()
axis1 = fig.add_axes([0.1 , 0.1 , 0.8 , 0.8])  #big axis
axis2 = fig.add_axes([0.2 , 0.5 , 0.3 , 0.4])  #small canvas
axis1.plot(x , y , 'b')
axis2.plot(y , x , 'r')
pylab.show()



fig = pylab.figure() #new graphic object
fig.add_subplot()

plt.plot(x , y , 'b')
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.title('Title')
plt.show()