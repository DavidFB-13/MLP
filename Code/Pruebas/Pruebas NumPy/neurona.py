import numpy as np

entradas = np.array([2, 5, 3])
pesos = np.array([4, 1, 2])

def suma_ponderada(entradas, pesos):

    productos = entradas * pesos

    suma = np.sum(productos)

    return suma

def calcular_z(entradas, pesos, sesgo):
    z = suma_ponderada(entradas, pesos) + sesgo
    return z

def escalon(z):
    if(z>=0):
        return 1
    else:
        return 0

def neurona(entradas, pesos, sesgo):
    z = calcular_z(entradas, pesos, sesgo)
    return escalon(z)

print(neurona(entradas, pesos, -4))  # 1
print(neurona(np.array([0, 0, 0]), pesos, -4))  # 0