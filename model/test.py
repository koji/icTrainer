import os
import sys
import numpy as np
from keras.applications.vgg16 import VGG16
from keras.models import Sequential, Model
from keras.layers import Input, Activation, Dropout, Flatten, Dense
from keras.preprocessing import image
from keras import optimizers
import tensorflowjs as tfjs


result_dir = 'test'
classes = ['echo', 'echoplus', 'echoshow',
           'googlehome', 'googlehomemini', 'nest']
nb_classes = len(classes)
img_width, img_height = 320, 180

def model_load(model_path):
    # VGG16 not needed FC layer --> include_top=False
    input_tensor = Input(shape=(img_width, img_height, 3))
    vgg16 = VGG16(include_top=False, weights='imagenet',
                  input_tensor=input_tensor)

    # build FC layer
    top_model = Sequential()
    top_model.add(Flatten(input_shape=vgg16.output_shape[1:]))
    top_model.add(Dense(256, activation='relu'))
    top_model.add(Dropout(0.5))
    top_model.add(Dense(nb_classes, activation='softmax'))

    # combine VGG16 and new FC
    model = Model(input=vgg16.input, output=top_model(vgg16.output))

    # load model
    model.load_weights(model_path)

    model.compile(loss='categorical_crossentropy',
                  optimizer=optimizers.SGD(lr=1e-3, momentum=0.9),
                  metrics=['accuracy'])

    return model


my_model = model_load('smartdevice_epoch30.h5')
tfjs.converters.save_keras_model(my_model, result_dir)
