import os
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, Model
from keras.layers import Input, Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from .color import Color
from .const import Const

cwd = os.getcwd()
train_data_dir = cwd + Const.TRAIN
validation_data_dir = cwd + Const.VAL

class ICTrainer():

    def __init__(self, classes, nb_classes,batch_size):
        self.classes = classes
        self.nb_classes = nb_classes
        self.batch_size = batch_size


    def vgg_model_maker(self):
        """
        In this case, use VGG16 except Fully Connected layer.
        Need to make FC for this model and put together them
        """

        # Load VGG16 not need fc include_top = False
        input_tensor = Input(shape=(Const.IMG_WIDTH, Const.IMG_HEIGHT, 3))
        vgg16 = VGG16(include_top=False, weights='imagenet', input_tensor=input_tensor)

        # create FC layer
        top_model = Sequential()
        top_model.add(Flatten(input_shape=vgg16.output_shape[1:]))
        top_model.add(Dense(256, activation='relu'))
        top_model.add(Dropout(0.5)) # ToDo
        top_model.add(Dense(self.nb_classes, activation='softmax'))

        # VGG16 + FC ---> new model
        model = Model(input=vgg16.input, output=top_model(vgg16.output))
        return model
    

    def image_generator(self, rotation):
        """
        load images and create dataset for training and validation
        """ 

        # training data
        train_datagen = ImageDataGenerator(
            rescale=1.0 / 255,
            zoom_range=0.2,
            rotation_range = rotation,
            horizontal_flip=True,
            vertical_flip=True)

        # validation data
        validation_datagen = ImageDataGenerator(rescale=1.0 / 255)

        train_generator = train_datagen.flow_from_directory(
            train_data_dir,
            target_size=(Const.IMG_WIDTH, Const.IMG_HEIGHT),
            color_mode='rgb',
            classes=self.classes,
            class_mode='categorical',
            batch_size=self.batch_size,
            shuffle=True)

        validation_generator = validation_datagen.flow_from_directory(
            validation_data_dir,
            target_size=(Const.IMG_WIDTH, Const.IMG_HEIGHT),
            color_mode='rgb',
            classes=self.classes,
            class_mode='categorical',
            batch_size=self.batch_size,
            shuffle=True)

        return (train_generator, validation_generator)
    
    def get_number_of_files(self, target_dir):
        dir_list = os.listdir(target_dir)
        sorted_list = sorted(dir_list)
        # print(sorted_list)
        # For Mac Users
        if sorted_list[0] == '.DS_Store':
            target = sorted_list[1]
        else:
            # print('here')
            target = sorted_list[0]
        # print('target :' + target)
        files_list = os.listdir(target_dir + '/' + target)
        # print(files_list)
        
        return len(files_list)