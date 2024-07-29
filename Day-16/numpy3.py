import numpy as np

#where function
arr = np.array([1,2,3,4,5,6,7,8])
print(arr)
indices = np.where(arr > 3)
print(indices)

print("----------------------------------------------")

#transpose the array
arr = np.array([[1,2,3],[4,5,6]])
transpose_arr = np.transpose(arr)
print(transpose_arr)

print("----------------------------------------------")

#mean 
arr = np.array([1,2,3,4,5,6,7,8])
print(np.mean(arr))

print("----------------------------------------------")

#searchsorted 
sort_arr = np.array([1,4,7,9])
index = np.searchsorted(sort_arr,5)
print("new element inserted at:",index)

print("----------------------------------------------")

#Extracting the new_arr from existing one
arr = np.array([1,2,3,5,4,8,9])
new_arr = np.extract(arr >3,arr)
print("Array greater than 3 is",new_arr)

print("-----------------------------------------------")

#spliting into equal sized sub-array
arr = np.array([1,2,3,4,5,6])
sub_arrs = np.split(arr,3)

for sub_arr in sub_arrs:
    print(sub_arr)
