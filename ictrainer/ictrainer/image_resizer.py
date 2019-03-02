import os
import glob
from PIL import Image

# ImageResizer
# resize target folder's images
#

class ImageResizer():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_size(self, filename):
        st = os.stat(filename)
        return st.st_size

    def resize_image(self, target):
        # get all image files
        files = []
        jpgs = glob.glob(target + '/*.jpg') # jpg
        jepegs = glob.glob(target + '/*.jpeg') # jpeg
        pngs = glob.glob(target + '/*.png') # png
        files.extend(jpgs)
        files.extend(jepegs)
        files.extend(pngs)
        # print(files)

        # resize
        for f in files:
            # print(f)
            file_size = self.get_size(f)
            if file_size > 0:
                img = Image.open(f)
                img_resize = img.resize((self.width, self.height))
                ftitle, fext = os.path.splitext(f)
                # img_resize.save(ftitle + '_resized' + fext)
                img_resize.save(ftitle + fext)


