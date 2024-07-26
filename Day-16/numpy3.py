import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])
print(arr)
indices = np.where(arr > 3)
print(indices)

print("----------------------------------------------")

arr = np.array([[1,2,3],[4,5,6]])
transpose_arr = np.transpose(arr)
print(transpose_arr)

print("----------------------------------------------")

arr = np.array([1,2,3,4,5,6,7,8])
print(np.mean(arr))

print("----------------------------------------------")

sort_arr = np.array([1,4,7,9])
index = np.searchsorted(sort_arr,5)
print("new element inserted at:",index)

print("----------------------------------------------")

arr = np.array([1,2,3,5,4,8,9])
new_arr = np.extract(arr >3,arr)
print("Array greater than 3 is",new_arr)
