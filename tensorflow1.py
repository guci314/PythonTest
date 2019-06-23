#%%
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.python.keras.engine.sequential import Sequential
from numpy import ndarray

print(tf.__version__)
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train: ndarray = tf.keras.utils.normalize(x_train, axis=1)
x_test: ndarray = tf.keras.utils.normalize(x_test, axis=1)

#%%
plt.imshow(x_train[0], cmap=plt.cm.binary)
plt.show()
#%%
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)
model.fit(x_train, y_train, epochs=3)

#%%
val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)

model.save("number_read.model")
print(type(model))
#%%
new_model: Sequential = tf.keras.models.load_model("number_read.model")
predictions: ndarray = new_model.predict(x_test)
print(predictions)
#%%
import numpy as np

predict_number = np.argmax(predictions[0])
plt.imshow(x_test[0])
plt.show()
print(predict_number)

#%%

from pandas import DataFrame

df = DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=["a", "b", "c"])

df.shape
