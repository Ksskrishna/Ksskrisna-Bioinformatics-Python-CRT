'''
write a py prog to create a 1 dimensioanl arr with 15 elem and reshape in to 2d arr with 3 rows and 5 coloumns
5 rows are 3 colomns
''' 
'''
reshape the same array into a 3d array with 5 rows with 1 element in each coloumn
'''
import numpy as np
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
new_Array = array.reshape(3,5)
print(new_Array)
print(new_Array.ndim)
new_Array1 = array.reshape(5,3,1)
print(new_Array1)
print(new_Array1.ndim)