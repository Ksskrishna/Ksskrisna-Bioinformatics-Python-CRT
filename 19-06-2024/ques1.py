'''
write a py prog to create a matrix with 4 roes and 4 coloumns using numpy library and give only multiples of 5
'''
import numpy as np
array = np.array([[[[10, 20, 30, 40], [50, 60, 70, 80]]]])
for i in range(len(array)):
    if array[i]%5==0:
        print(array[i])