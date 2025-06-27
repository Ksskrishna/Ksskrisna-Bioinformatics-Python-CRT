import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
arr1 = np.array([10,20,30])
arr2 = np.array([22,30,44])
plt.plot(arr1,arr2,marker='d',color='orange',linestyle='--',ms=25)
plt.show()