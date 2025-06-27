import matplotlib as mp
import numpy as np
import matplotlib.pyplot as plt
labels = ["apples","bananas","grapes","cherries","mangoes"]
y = np.array([10,20,30,40,50])
myexplode = [0.3,0,0,0,0]
plt.pie(y,labels=labels,startangle=45,explode=myexplode,shadow=True)
plt.legend(labels)
plt.show()