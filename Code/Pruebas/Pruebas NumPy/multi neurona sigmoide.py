import numpy as np

def suma_ponderada(entradas, pesos):  # Calcula la suma ponderada
    productos = entradas * pesos
    return np.sum(productos)

def calcular_z(entradas, pesos, sesgo):  # Suma ponderada más sesgo
    return suma_ponderada(entradas, pesos) + sesgo

def sigmoide(z): # Escalón suavizado (Esc: 0/1. Sgm: 0-1 (con decimales))
    return 1 / (1 + np.exp(-z))

def neurona(entradas, pesos, sesgo):  # Calcula la salida de una neurona
    z = calcular_z(entradas, pesos, sesgo)
    return sigmoide(z)

def capa_oculta(entradas, pesos, sesgos):  # Calcula las cuatro salidas ocultas
    salidas = []
    for i in range(4):
        salidas.append(neurona(entradas, pesos[i], sesgos[i]))
    return np.array(salidas)

def mlp(entradas, pesos_ocultos, sesgos_ocultos, pesos_salida, sesgo_salida):
    # Devuelve la predicción final de la red
    salida_capa_oculta = capa_oculta(entradas, pesos_ocultos, sesgos_ocultos)
    return neurona(salida_capa_oculta, pesos_salida, sesgo_salida)

def error_cuad(prediccion, objetivo):  # Mide el error de una predicción
    return (prediccion - objetivo) ** 2

def error_porcentaje(errores):
    # Con predicciones y objetivos de 0 o 1, cada fallo tiene error 1
    return np.sum(errores) / len(errores) * 100

# Cada fila contiene los pesos de una neurona oculta
pesos_ocultos = np.array([
    [1, 1],
    [1, 1],
    [1, -1],
    [-1, 1]
])

# Un sesgo por neurona oculta
sesgos_ocultos = np.array([-0.5, -1.5, -0.5, -0.5])

pesos_salida = np.array([0, 0, 1, 1])
sesgo_salida = -0.5

casos = [[0, 0], [0, 1], [1, 0], [1, 1]]
objetivos = [0, 1, 1, 0]

errores = []

for i in range(len(casos)):  # Calcula las predicciones y sus errores
    prediccion = mlp(
        np.array(casos[i]),
        pesos_ocultos,
        sesgos_ocultos,
        pesos_salida,
        sesgo_salida
    )

    error = error_cuad(prediccion, objetivos[i])
    errores.append(error)

    print(casos[i], "→", prediccion,
          "Objetivo:", objetivos[i], "Error:", error)

porcentaje_error = error_porcentaje(errores)
print("Porcentaje de error:", porcentaje_error, "%")

peso = 0.0                 # El peso inicial que queremos ajustar
objetivo = 1               # La salida correcta que queremos alcanzar
cambio = 0.01              # Un cambio pequeño para medir la pendiente
tasa_aprendizaje = 0.1      # Controla el tamaño del ajuste del peso

error_inicial = error_cuad(sigmoide(peso), objetivo)
error_con_cambio = error_cuad(sigmoide(peso + cambio), objetivo)

pendiente = (error_con_cambio - error_inicial) / cambio
peso_nuevo = peso - tasa_aprendizaje * pendiente

error_final = error_cuad(sigmoide(peso_nuevo), objetivo)
print("Error inicial:", error_inicial)
print("Error final:", error_final)