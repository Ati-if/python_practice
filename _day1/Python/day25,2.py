from matplotlib import style
style.use ('ggplot')

x = [2 , 4 , 6]
y = [12 , 14 , 16]

x2 = [3 , 3 , 5]
y2 = [7 , 14 , 18]
import matplotlib.pyplot as plt
plt.bar (x , y , label = 'Bars 1' , color = 'g')
plt.bar (x2 , y2 , label = 'Bars 2' , color = 'w')
plt.xlabel ('Bar Number')
plt.ylabel ('Bar Height')
plt.title ('Bar Chart')
plt.legend()
plt.show()








import numpy as np
s = np.array([2 , 3 , 4])
plt.pie(s , labels = ['A' , 'B' , 'C'])
plt.show()
print(s)