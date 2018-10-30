import numpy as np


vendedores = np.array(["Sócrates", "Aristóteles",
                       "Platão", "Sócrates",
                       "Sócrates", "Platão",
                       "Platão", "Platão",
                       "Aristóteles", "Sócrates",
                       "Aristóteles", "Aristóteles"])

print(vendedores)

vendas = np.array([
                    [10,19,30,3,14],
                    [13,18,18,5,16],
                    [0,4,19,16,20],
                    [17,21,1,3,4],
                    [25,6,14,9,7],
                    [18,17,21,7,6],
                    [9,10,2,3,3],
                    [7,5,12,21,9],
                    [8,3,5,4,17],
                    [1,9,4,4,16],
                    [4,8,3,4,13],
                    [6,5,5,4,27]
                   ])


print("******************")
print(vendas[vendedores != "Sócrates"])
print("******************")
print(vendas[~(vendedores == "Sócrates")])
print("******************")