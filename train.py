from keras.datasets import mnist
from keras import models, layers, utils
import matplotlib.pyplot as plt
from keras.models import load_model

(train_X, train_y), (test_X, test_y) = mnist.load_data()

train_X = train_X / 255
test_X = test_X / 255

train_X = utils.normalize(train_X, axis=1)
test_X = utils.normalize(test_X, axis=1)

model = models.Sequential([
    layers.Flatten(input_shape=(28,28)),
    layers.Dense(512, activation='relu'),
    layers.Dense(256, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_X, train_y, epochs=10)
model.evaluate(test_X,test_y)

model.save("my_network.h5")