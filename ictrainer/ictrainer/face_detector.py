import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
from PIL import Image

OUTPUT = os.getcwd() + '/' + 'output'

class FaceDetector():
    
    def __init__(self, file_path):
        # print('face detector init')
        self.file_path = file_path
        if os.path.isdir(OUTPUT) == False:
            os.mkdir(OUTPUT)
            print("Created output folder")


    def get_files(self):
        filenames = os.listdir(self.file_path)
        return filenames


    def crop_faces(self):
        pics = self.get_files()
        # print(pics)
        for i, pic in enumerate(pics):
            images = cv2.imread(self.file_path + '/' + pic)
            cascade = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
            face_list = cascade.detectMultiScale(
            images, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
            no = 1
            for rect in face_list:
                x = rect[0]
                y = rect[1]
                width = rect[2]
                height = rect[3]
                dst = images[y: y + height, x: x + width]
                save_path = OUTPUT + '/' + 'output_' + str(i) + '_' +  str(no) + '.png'
                result = cv2.imwrite(save_path, dst)
                no += 1


