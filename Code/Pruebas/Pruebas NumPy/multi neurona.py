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

def capa_oculta(entradas, pesos, sesgos):
    salidas = []
    for i in range(4):
        salidas.append(neurona(entradas, pesos[i], sesgos[i]))
    return np.array(salidas)

def mlp (entradas, pesos_ocultos, sesgos_ocultos, pesos_salida, sesgo_salida):
    salida_capa_oculta = capa_oculta(entradas, pesos_ocultos, sesgos_ocultos)
    return neurona(salida_capa_oculta, pesos_salida, sesgo_salida)

def error_cuad(prediccion, objetivo):
    error = (prediccion - objetivo) ** 2
    return error

pesos_ocultos = np.array([
    [1, 1],
    [1, 1],
    [1, -1],
    [-1, 1]
])

sesgos_ocultos = np.array([-0.5, -1.5, -0.5, -0.5])

pesos_salida = np.array([0, 0, 1, 1])
sesgo_salida = -0.5

casos = [[0, 0], [0, 1], [1, 0], [1, 1]]
objetivos = [0, 1, 1, 0]

for i in range(len(casos)):
    prediccion = mlp(
        np.array(casos[i]),
        pesos_ocultos,
        sesgos_ocultos,
        pesos_salida,
        sesgo_salida
    )
for i in range(len(casos)):
    prediccion = mlp(
        np.array(casos[i]),
        pesos_ocultos,
        sesgos_ocultos,
        pesos_salida,
        sesgo_salida
    )
    error = error_cuad(prediccion, objetivos[i])
    print(casos[i], "→", prediccion,
          "Objetivo:", objetivos[i], "Error:", error)