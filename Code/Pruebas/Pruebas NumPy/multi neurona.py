import numpy as np

entradas = np.array([2, 5, 3]) //crea array entradas
pesos = np.array([4, 1, 2]) //crea array salidas

def suma_ponderada(entradas, pesos): //hace suma ponderada

    productos = entradas * pesos

    suma = np.sum(productos)

    return suma

def calcular_z(entradas, pesos, sesgo): // devuelve z, que es la suma ponderada de las entradas y los pesos + el sesgo
    z = suma_ponderada(entradas, pesos) + sesgo
    return z

def escalon(z): // devuelve 0/1 dependiendo de z
    if(z>=0):
        return 1
    else:
        return 0

def neurona(entradas, pesos, sesgo): //crea una neurona, devolviendo el escalon de z (de la neurona)
    z = calcular_z(entradas, pesos, sesgo)
    return escalon(z)

def capa_oculta(entradas, pesos, sesgos): //crea la capa oculta, devolviendo las salidas
    salidas = []
    for i in range(4):
        salidas.append(neurona(entradas, pesos[i], sesgos[i]))
    return np.array(salidas)

def mlp (entradas, pesos_ocultos, sesgos_ocultos, pesos_salida, sesgo_salida): //devuelve una neurona
    salida_capa_oculta = capa_oculta(entradas, pesos_ocultos, sesgos_ocultos)
    return neurona(salida_capa_oculta, pesos_salida, sesgo_salida)

def error_cuad(prediccion, objetivo): //calcula el error que tuvo la neurona conforme al objetivo
    error = (prediccion - objetivo) ** 2
    return error

pesos_ocultos = np.array([ //pesos
    [1, 1],
    [1, 1],
    [1, -1],
    [-1, 1]
])

sesgos_ocultos = np.array([-0.5, -1.5, -0.5, -0.5]) //sesgos

pesos_salida = np.array([0, 0, 1, 1])
sesgo_salida = -0.5

casos = [[0, 0], [0, 1], [1, 0], [1, 1]]
objetivos = [0, 1, 1, 0]

for i in range(len(casos)): //elabora las predicciones
    prediccion = mlp(
        np.array(casos[i]),
        pesos_ocultos,
        sesgos_ocultos,
        pesos_salida,
        sesgo_salida
    )
