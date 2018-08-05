import numpy as np

arr = np.array([1,2,3,4,5])
print(arr.dtype)
arr_float = arr.astype(np.float32)
print(arr_float.dtype)
print(arr_float)
print(arr)