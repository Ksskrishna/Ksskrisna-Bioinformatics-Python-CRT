import numpy as np
arr = np.array([1,2,3,4,5])
x = np.where(arr==4)
print(x)

#finding the elements whose indexes are in even

arr1 = np.array([1,2,3,4,5,6,7,8])
x1 = np.where(arr1%2==0)
print(x1)

#finding the elements whose indexes are in odd
arr2 = np.array([1,2,3,4,5,6,7,8])
x2 = np.where(arr2%2!=0)
print(x2)