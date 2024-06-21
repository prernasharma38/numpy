import numpy as np

arr = np.array([3,5,6,7,8])
arr1 = np.array([[1,2,3],[2,3,4]])
arr2 = np.array(34)
arr3 = np.array([[[1,2,3],[2,3,4],[5,6,7]]])
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(np.__version__)

arr = np.array([2,3,4], ndmin=3)

print(arr)
# print(arr.ndim)

arr = np.array([5,6,7])
print(arr[1] + arr[2])

arr = np.array([[2,4],[4,5]])
print(arr[1,1])

arr = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print(arr[0,1,0])

arr = np.array([2,4,5,6,7,8])
print(arr[0:5:2])

