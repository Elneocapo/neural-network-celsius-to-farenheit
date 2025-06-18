# Conversor Celsius a Fahrenheit con Red Neuronal

Este proyecto implementa una red neuronal sencilla usando TensorFlow para convertir temperaturas de grados Celsius a Fahrenheit.

---

## Descripción

El modelo aprende la relación entre Celsius y Fahrenheit a partir de un conjunto pequeño de datos de entrenamiento.  
Al ejecutar el script:

- Si existe un modelo guardado, se carga para evitar reentrenamiento.  
- Si no existe, entrena el modelo y lo guarda para uso futuro.  
- Muestra la curva de aprendizaje si acaba de entrenar.  
- Solicita al usuario un valor en Celsius para predecir la temperatura equivalente en Fahrenheit usando la red neuronal.

---

## Requisitos

- Python 3.7+  
- TensorFlow  
- NumPy  
- Matplotlib  

Puedes instalarlos con:

```bash
pip install tensorflow numpy matplotlib
