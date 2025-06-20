import numpy as np
#array[start:end]
#array[start:end:stepsize]
#array[:end]
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])
print(arr[2:4])

#slice 2d array
array = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array[0,1:4])

#copy method
arr1 = np.array([1,2,3,4,5])
x = arr.copy()
arr1[0] = 42
print(arr)
print(x)

#array shape
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2.shape)

#reshape
arr3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr3.reshape(4,3)
print(newarr)

#1d to 3d
arr3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr3.reshape(2,3,2)
print(newarr)