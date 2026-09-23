from matplotlib import pyplot as plt

"""Drawing a subgraph"""

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

plt.subplot(2, 1, 1)  # rows, columns, index
plt.plot(x, y, 'r--')  # third parameter = color and line style

plt.subplot(2, 1, 2)
plt.plot(y, x, 'g+-')



import pylab
pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'r--')
pylab.subplot(1 , 2 , 2)
pylab.plot(y , x , 'g+-')
pylab.subplot(1 , 2 , 1)
pylab.plot(y , x , 'g+-')
pylab.show()


from matplotlib import pyplot as plt
fig = pylab.figure()
axis = fig.add_axes([0.1, 0.1, 0.8, 0.8])    #control left , right , width , height of canvas(from 0 to 1)
axis.plot(x , y , 'b')
axis.set_xlabel('X-Label')
axis.set_ylabel('Y-Label')
axis.set_title('Title')
plt.show()