# 🧠 Reconocimiento de dígitos MNIST — MLP desde cero

Proyecto de reconocimiento de números escritos a mano mediante una **red neuronal de tipo perceptrón multicapa (MLP)**, desarrollada desde cero utilizando **Python y NumPy**.

El objetivo es construir un sistema de **reconocimiento óptico de caracteres (OCR)** capaz de identificar dígitos del 0 al 9 utilizando el conjunto de datos **MNIST**, comprendiendo al mismo tiempo los fundamentos matemáticos y de programación de las redes neuronales.

## 🎯 Objetivos del proyecto

- Desarrollar un perceptrón multicapa (MLP) desde cero.
- Utilizar **Python y NumPy** para implementar los cálculos de la red neuronal.
- Implementar la propagación hacia delante (*forward propagation*).
- Implementar la retropropagación del error (*backpropagation*).
- Comprender el funcionamiento de los pesos, sesgos, funciones de activación y descenso de gradiente.
- Entrenar la red neuronal utilizando el dataset MNIST.
- Crear un sistema OCR capaz de reconocer números escritos a mano.
- Evaluar la precisión y el rendimiento del modelo.

## ⚙️ Funcionamiento

La red neuronal recibirá una imagen de un número escrito a mano y deberá predecir qué dígito representa.

Cada imagen de MNIST tiene una resolución de **28 × 28 píxeles**, lo que equivale a 784 valores de entrada.

### Arquitectura prevista

```text
       Imagen MNIST (28 × 28)
                 |
                 v
      Capa de entrada (784)
                 |
                 v
          Capa oculta
                 |
                 v
          Capa oculta
                 |
                 v
      Capa de salida (10)
                 |
                 v
       Predicción (0–9)
```

Durante el entrenamiento, la red ajustará sus pesos y sesgos mediante retropropagación y descenso de gradiente para mejorar progresivamente sus predicciones.

## 🛠️ Tecnologías

- **Python:** lenguaje principal del proyecto.
- **NumPy:** operaciones matriciales y cálculos matemáticos de la red neuronal.
- **MNIST:** conjunto de datos de dígitos manuscritos.
- **Matplotlib (opcional):** visualización de imágenes, predicciones y resultados del entrenamiento.

El núcleo de la red neuronal se implementará con NumPy, sin utilizar frameworks de aprendizaje profundo como TensorFlow o PyTorch.

## 📊 Dataset MNIST

El proyecto utilizará **MNIST (Modified National Institute of Standards and Technology)**, un conjunto de datos ampliamente utilizado para introducirse en el aprendizaje automático.

Contiene:

- 60.000 imágenes de entrenamiento.
- 10.000 imágenes de prueba.
- Imágenes en escala de grises de 28 × 28 píxeles.
- Dígitos escritos a mano del 0 al 9.

## 🚀 Plan de desarrollo

- [ ] Configurar el entorno de Python.
- [ ] Cargar y preparar el dataset MNIST.
- [ ] Implementar la arquitectura del MLP con NumPy.
- [ ] Implementar la propagación hacia delante.
- [ ] Implementar el cálculo del error.
- [ ] Implementar la retropropagación.
- [ ] Implementar el descenso de gradiente.
- [ ] Entrenar la red neuronal.
- [ ] Evaluar la precisión con los datos de prueba.
- [ ] Desarrollar el sistema de reconocimiento de dígitos.
- [ ] Visualizar las predicciones y los resultados.

## 📈 Resultados esperados

Una vez completado, el proyecto permitirá:

1. Procesar imágenes de números escritos a mano.
2. Identificar dígitos del 0 al 9.
3. Calcular la precisión de las predicciones.
4. Observar cómo aprende una red neuronal durante su entrenamiento.

## 📚 Finalidad educativa

Este proyecto tiene un objetivo principalmente educativo: **comprender cómo funciona una red neuronal desde sus fundamentos**, en lugar de utilizar modelos ya implementados.

El desarrollo se realizará progresivamente, combinando el aprendizaje de conceptos matemáticos con su implementación práctica en Python.

## 📌 Estado del proyecto

🚧 **En desarrollo** — Fase inicial de planificación e implementación.
