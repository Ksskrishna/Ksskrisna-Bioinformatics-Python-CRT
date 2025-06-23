#splitting arrays
import numpy as np
arr = np.array([1,2,3,4,5])
new_arr = np.array_split(arr,4)
print(f"original array: {arr}")
print(f"splitted array: {new_arr}")

#for 2d array
arrr2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
new_arrr2d = np.array_split(arrr2d,4)
print(f"splitted 2d array: {new_arrr2d}")