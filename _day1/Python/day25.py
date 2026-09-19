import time
import sys
import numpy as np

b = range(1000)
print(sys.getsizeof(5) * len(b))
c = np.arange(1000)
print(c.size * c.itemsize)
size = 1000
l1 = range(size)
l2 = range(size)
a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()
result = [(x , y) for x , y in zip(l1 , l2)]
print(result)
print("Python list took" , (time.time() - start) * 1000)
start = time.time()
result = a1 + a2
print(result)
print("NumPy array took" , (time.time() - start) * 1000)