import numpy as np
total = 0
array = np.array([20000,21000,25000,24000])
for i in array:
    total = total + i
sum = total/len(array)
print(sum)
