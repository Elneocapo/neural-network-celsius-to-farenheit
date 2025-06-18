import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
farenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)
se_acaba_de_entrenar = False

# Cargamos el modelo
if os.path.exists("modelo_conversion.keras"):
    modelo = tf.keras.models.load_model("modelo_conversion.keras")
    print("modelo cargado")
else:
    capa1 = tf.keras.layers.Dense(units=1, input_shape=[1])
    modelo = tf.keras.Sequential([capa1])
    modelo.compile(
        optimizer = tf.keras.optimizers.Adam(0.1),
        loss ='mean_squared_error'
    )
    print("entrenando")
    historial = modelo.fit(celsius, farenheit, epochs=1000, verbose=False)
    print("entrenado fr")
    modelo.save("modelo_conversion.keras")
    se_acaba_de_entrenar = True

if se_acaba_de_entrenar:
    plt.title("Curva de aprendizaje (cerrar para continuar)")
    plt.xlabel("# Epoca")
    plt.ylabel("magnitud de perdida")
    plt.plot(historial.history["loss"])
    plt.show()

print("hagamos prediccion")
valor = input("inserte grados celsius: ")

try:
    valor_float = float(valor)
    resultado = modelo.predict(np.array([valor_float]))
    print(f"{valor_float} celsius a fahrenheit segun la red neuronal es " + str(resultado[0][0]))
except:
    print(f"Error loco: no es posible predecir {valor}")