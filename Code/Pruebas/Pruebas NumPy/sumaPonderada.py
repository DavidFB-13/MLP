import numpy as np

entradas = np.array([2, 5, 3])
pesos = np.array([4, 1, 2])

def suma_ponderada(entradas, pesos):

    productos = entradas * pesos

    suma = np.sum(productos)

    return suma

print(suma_ponderada(entradas, pesos))  # 19
print(suma_ponderada(np.array([1, 2]), np.array([3, 4])))  # 11