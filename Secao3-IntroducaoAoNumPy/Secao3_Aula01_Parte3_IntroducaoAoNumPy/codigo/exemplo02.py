import numpy as np


arr = np.array([[0, 1, 2, 3],[4, 5, 6, 7],[8, 9, 10, 11]])
itens = arr.flat
for item in itens:
    print(item)

arr = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
print(arr.flat[6])
print(arr.flat[[0,3]])
arr.flat = 8
print(arr)
arr.flat[[0,1,7]] = 3
print(arr)