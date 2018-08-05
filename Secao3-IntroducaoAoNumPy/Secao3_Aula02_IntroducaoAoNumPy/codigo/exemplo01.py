import numpy as np


lista = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
myArray = np.array(lista)
print(np.ndim(myArray))
lista = [[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]]
myArray = np.array(lista)
print(np.ndim(myArray))