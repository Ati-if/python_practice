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




import pandas as pd
d = {'a' : 1 , 'b' : 2 , 'c' : 3 , 'd' : 4 , 'e' : 5}
s4 = pd.Series(d)
print(s4)





print(s1)
s1.index = ['A' , 'B' , 'C' , 'D' , 'E']
s1