import pandas as pd
print(pd.__version__)

arr = [1 , 2 , 3 , 4 , 5]
s1 = pd.Series(arr)
print(s1)





order = [1 , 2 , 3 , 4 , 5 ]
s2 = pd.Series(arr , index = order)
print(s2)





import numpy as np
n = np.random.randn(5)
index = ['a' , 'b' , 'c' , 'd' , 'e']
s3 = pd.Series(n , index = index)
print(s3)