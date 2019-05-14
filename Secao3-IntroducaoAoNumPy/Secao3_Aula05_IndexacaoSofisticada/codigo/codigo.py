import numpy as np

arr = np.zeros((5,3))
print(arr)

for i in range(5):
    arr[i] = i

print(arr)

lista = [4,3,1,0,2]
print(arr[lista])

arr2 = np.array([4,1,3,2,0])
print(arr[arr2])

print(arr[[2, 4]])
print(arr[[-1, -2]])

arr = np.arange(15).reshape(5, 3)
print(arr)

print(arr[[0, 2, 4], [2, 1, 0]])
print(arr[[1, 2, 3]][:,[2,0,1]])