import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1,arr2))
print(arr)

#joining 2 2d arrays
import numpy as np
arr2d1 = np.array([[1,2,3],[4,5,6]])
arr2d2 = np.array([[10,11,12],[13,15,15]])
arr2d = np.concatenate((arr2d1,arr2d2),axis=0)
print(arr2d)