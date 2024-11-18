import numpy as np

arr = np.array(3)
arr1 = np.array([1,2,3,4])
arr2 = np.array([[1,2,3,4],[5,6,7,8]])
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(arr)
print(arr.ndim,"dimentional")
print(arr1)
print(arr1.ndim,"dimentional")
print(arr2)
print(arr2.ndim,"dimentional")
print(arr3)
print(arr3.ndim,"dimentional")
