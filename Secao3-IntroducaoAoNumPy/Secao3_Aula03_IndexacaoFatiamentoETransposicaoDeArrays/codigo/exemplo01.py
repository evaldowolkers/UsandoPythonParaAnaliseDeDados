import numpy as np

array = np.array([0,1,2,3,4,5,6,7,8,9])

print("Elemento 8: " + str(array[8]))
print("Fatia 4 a 7: " + str(array[4:7]))
array[4:7] = 66
print(array)