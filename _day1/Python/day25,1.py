import numpy as np
import pandas as pd

# Create dataframe with dictionary array
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog']}
age = {'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3]}
visits = {'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]}
priority = {'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df2 = pd.DataFrame(data, index=labels)
df3 = pd.DataFrame(age, index=labels)
df4 = pd.DataFrame(visits, index=labels)
df5 = pd.DataFrame(priority, index=labels)

print(df2)
print(df3)
print(df4)
print(df5)









