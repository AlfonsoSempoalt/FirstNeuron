# -*- coding: utf-8 -*-
"""housing-prices basic ver 1.1 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gUDb3I5tS-VnRggsxDxxMiiB-QWOkL0d

In this exercise you'll try to build a neural network that predicts the price of a house according to a simple formula.

So, imagine if house pricing was as easy as a house costs 50k + 50k per bedroom, so that a 1 bedroom house costs 100k, a 2 bedroom house costs 150k etc.

How would you create a neural network that learns this relationship so that it would predict a 7 bedroom house as costing close to 400k etc.

Hint: Your network might work better if you scale the house price down. You don't have to give the answer 400...it might be better to create something that predicts the number 4, and then your answer is in the 'hundreds of thousands' etc.
"""

!nvidia-smi

import tensorflow as tf
import numpy as np
from tensorflow import keras

# GRADED FUNCTION: house_model
def house_model(y_new):
    #
    xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0], dtype=float)
    ys = np.array([100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 450.0, 500.0, 550.0,600.0, 650.0,700.0], dtype=float)
    model = tf.keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
    model.compile(optimizer="sgd", loss="mean_squared_error")
    model.fit(xs,ys, epochs=3500)
    return model.predict(y_new)[0]

prediction = house_model([7.0])
print(prediction)