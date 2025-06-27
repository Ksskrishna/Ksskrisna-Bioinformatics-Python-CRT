import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
x = np.array([0,1,2,3,4])
y = np.array([10,20,30,40,50])
colors = np.array([5,4,8,6,5]) #color values
#cmap --> color map
plt.scatter(x, y, c=colors, cmap='viridis')
plt.grid(axis='y',color='grey',linestyle='--')
plt.show()