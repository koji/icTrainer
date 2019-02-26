import os, sys
import numpy as np
from keras.applications.vgg16 import VGG16
from keras.models import Sequential, Model
from keras.layers import Input, Activation, Dropout, Flatten, Dense
from keras.preprocessing import image
from keras import optimizers

classes = ['dog', 'cat'] # put your classes
nb_classes = len(classes)
img_width, img_height = 320, 180

result_dir = 'result'

test_data_dir = 'dataset/test'

def model_load():
    # VGG16 not needed FC layer --> include_top=False
    input_tensor = Input(shape=(img_width, img_height, 3))
    vgg16 = VGG16(include_top=False, weights='imagenet', input_tensor=input_tensor)

    # build FC layer
    top_model = Sequential()
    top_model.add(Flatten(input_shape=vgg16.output_shape[1:]))
    top_model.add(Dense(256, activation='relu'))
    top_model.add(Dropout(0.5))
    top_model.add(Dense(nb_classes, activation='softmax'))

    # combine VGG16 and new FC 
    model = Model(input=vgg16.input, output=top_model(vgg16.output))

    # load model
    model.load_weights(os.path.join(result_dir, 'your_model_name'))

    model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.SGD(lr=1e-3, momentum=0.9),
              metrics=['accuracy'])

    return model


if __name__ == '__main__':

    # load model
    model = model_load()

    # get images for testing
    test_imagelist = os.listdir(test_data_dir)

    for test_image in test_imagelist:
        filename = os.path.join(test_data_dir, test_image)
        img = image.load_img(filename, target_size=(img_width, img_height))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        
        x = x / 255
        pred = model.predict(x)[0]

        # display the result
        top = 3
        top_indices = pred.argsort()[-top:][::-1]
        result = [(classes[i], pred[i]) for i in top_indices]
        print('file name is', test_image)
        print(result)
        print('=======================================')