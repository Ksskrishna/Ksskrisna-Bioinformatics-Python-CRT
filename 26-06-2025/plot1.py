import matplotlib as mp
import numpy as np
import matplotlib.pyplot as plt

even = np.array([2,4,6,8,10,12,14,16,18,20])
odd = np.array([1,3,5,7,9,11,13,15,17,19])
plt.title("graph of even and odd numbers",loc='right')
plt.xlabel("Even_numbers",size=15)
plt.ylabel("Odd numbers",size=15)
plt.plot(even,odd,color='green',marker='d',linestyle='--',ms=10,mec='red',mfc='y',linewidth=5)
#to get grid lines
plt.grid(axis='x',color='grey',linestyle='--',linewidth=0.5)
plt.grid(axis='y',color='grey',linestyle='--',linewidth=0.5)

plt.show()