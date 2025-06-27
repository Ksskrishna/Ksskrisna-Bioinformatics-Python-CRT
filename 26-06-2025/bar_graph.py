import matplotlib as mp
import numpy as np
import matplotlib.pyplot as plt
x = np.array(['A','B','C','D','E'])
y = np.array([10,20,30,40,50])
#for normal bar graph (verticle bar graph)
#plt.bar(x,y)
#for horizontal bar graph
plt.barh(x,y,color='blue')
plt.show()
