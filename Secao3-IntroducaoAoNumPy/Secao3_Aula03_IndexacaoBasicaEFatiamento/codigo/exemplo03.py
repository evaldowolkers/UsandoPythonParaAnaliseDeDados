import numpy as np

array = np.array([0,1,2,3,4,5,6,7,8,9])
print("Array original: " + str(array))
fatia = array[4:9].copy()
print("Fatia antes alteração: " + str(fatia))
fatia[3] = 17
print("Fatia depois alteração: " + str(fatia))
print("Array original: " + str(array))