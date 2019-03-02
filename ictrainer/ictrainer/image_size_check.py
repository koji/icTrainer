import os

class ImageSizeChecker():

    def __init__(self):
        print('check image file size')
    
    # check images under target folder
    # if the size is zero remove the image
    def check_size(self, targetPath):
        files = os.listdir(targetPath)

        for file in files:
            file_size = os.path.getsize(targetPath + '/' + file)
            if file_size == 0:
                # remove file
                os.remove(targetPath + '/' + file)
                print(file + ' removed')


