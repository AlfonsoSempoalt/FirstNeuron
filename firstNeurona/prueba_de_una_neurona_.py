# -*- coding: utf-8 -*-
"""prueba de una neurona .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FA70kPKXMHiWdLM3_7gYWkgegw-JHfH1
"""

import tensorflow as tf
import numpy as np
from tensorflow import keras

model= tf.keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
#se define la red neural, con una capa y una neurona 
model.compile(optimizer="sgd", loss="mean_squared_error")
#se compila usando el optimizador decenso del gradiente y la perdida, las cuales ayudan a conjeturar el patrón a seguir

#Datos que se utilizan para entrar la red
xs=np.array([-1.0,0.0,1.0,2.0,3.0,4.0])
ys=np.array([-3.0,-1.0,1.0,3.0,5.0,7.0])

#entrenamiento de la red neuronal con 800 epochs 
model.fit(xs,ys, epochs=800)

print(model.predict([10.0]))