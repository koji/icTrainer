import os
import argparse
import numpy as np
import time
from .color import Color
from .const import Const

# main
def main():
    cwd = os.getcwd()

    parser = argparse.ArgumentParser(
        prog='ictrainer',
        usage='train a image classifier for keras',
        description='tool for training an image classifier',
        add_help = True 
        )
    parser.add_argument("--mode", dest="mode", help="choose one mode of 3 modes, train mode, test mode, and collect mode ", required=True)
    parser.add_argument("--classes", dest="classes", help="put your classname", type = str, nargs='*')
    parser.add_argument("--batch", dest="batch", help="batch size", default=15)
    parser.add_argument("--epoch", dest="epoch", help="epoch a big value takes so much time to train", default=30)
    parser.add_argument("--mname", dest="mname", help="your model name", default="myModel_")
    parser.add_argument("--lr", dest="lr", help="learning rate", default=1e-3)
    parser.add_argument("--momentum", dest="momentum", help="momentum: Parameter that accelerates SGD in the relevant direction and dampens oscillations.", default=0.9)
    parser.add_argument("--rotation", dest="rotation", help="image rotation for training", default=20)
    parser.add_argument("--keyword", dest="keyword", help="type keyword")
    parser.add_argument("-n", "--number", dest="number", help="number of total images", default=100)
    parser.add_argument("-t", "--target", dest="target", help="target folder")
    parser.add_argument("-iw", "--image_width", dest="width", help="resized image width", default=320)
    parser.add_argument("-ih", "--image_height", dest="height", help="resized image height", default=180)
    args = parser.parse_args()

    # args
    user_define_classes = args.classes # classes defined by user 
    batch = args.batch # batch size
    epoch = args.epoch # epoch size
    mname = args.mname  # model name
    input_lr = args.lr
    input_momentum = args.momentum
    input_rotation = args.rotation
    mode = args.mode # mode
    keyword = args.keyword
    max_num = int(args.number)
    target = args.target
    resized_width = args.width
    resized_height = args.height
    

    print('mode: ' + mode)
    if mode == 'collect':
        # mode image collect images
        from .image_collector import ImageCollector
        print(Color.CYAN + 'start image collecting mode' + Color.END)
        ic = ImageCollector(keyword, max_num)
        ic.get_images()
        print(Color.CYAN + 'end image collecting mode' + Color.END)
        print(Color.PURPLE + 'check files size' + Color.END)
        from .image_size_check import ImageSizeChecker
        isc = ImageSizeChecker()
        # check dataset folder
        folders = os.listdir('dataset')
        for folder in folders:
            if folder != '.DS_Store':
                isc.check_size('dataset/' + folder)
        print(Color.PURPLE + 'removed 0 size file' + Color.END)

    elif mode == 'resize':
        # resize ToDo
        from .image_resizer import ImageResizer
        print(Color.GREEN + 'start image resize mode' + Color.END)
        ir = ImageResizer(resized_width, resized_height)
        ir.resize_image(cwd + '/dataset/' + target)
        print(Color.GREEN + 'end image resize mode' + Color.END)

    elif mode == 'face':
        # face detector
        from .face_detector import FaceDetector
        print(Color.YELLOW + 'start detecting faces' + Color.END)
        fd = FaceDetector(cwd + '/' + target)
        fd.crop_faces()
        print(Color.YELLOW + 'end detecting faces' + Color.END)
        print(Color.RED + 'Please check output folder!!!' + Color.END)

    
    elif mode == 'train':
        # mode train train images
        from keras import optimizers
        from .ictrainer import ICTrainer
        print(Color.BLUE + 'start training mode' + Color.END)

        # create folder for result
        if not os.path.exists(Const.RESULT_DIR):
            print(Color.YELLOW + 'You do not have result dir. I will create it for you!!!' + Color.END)
            os.mkdir(Const.RESULT_DIR)

        classes = user_define_classes
        nb_classes = len(classes)

        # icTrainer instance
        ict = ICTrainer(classes, nb_classes, batch)

        # data folder path for train & validation
        train_data_dir = cwd + '/dataset/train'
        # validation_data_dir = cwd + '/dataset/val'
        train_data_num = ict.get_number_of_files(train_data_dir)
        # validation_data_num = ict.get_number_of_files(validation_data_dir)
        
        # print('train data num ' + str(train_data_num))
        # print('val data num ' + str(validation_data_num))


        # the amount of images
        # count the number of images
        nb_train_samples = train_data_num * nb_classes
        # nb_validation_samples = validation_data_num * nb_classes

        # start timer
        start = time.time()

        # create model
        vgg_model = ict.vgg_model_maker()

        # freeze layers
        for layer in vgg_model.layers[:15]:
            layer.trainable = False

        # classes
        # optimizer lr(lerning rate) # parameter
        # lr: float >= 0. Learning rate.
        # momentum: float >= 0. Parameter that accelerates SGD 
        # in the relevant direction and dampens oscillations.
        # loss
        # metrics
        # 
        vgg_model.compile(loss='categorical_crossentropy',
            optimizer=optimizers.SGD(lr=input_lr, momentum=input_momentum),metrics=['accuracy'])

        # generator for images
        train_generator, validation_generator = ict.image_generator(input_rotation)

        # Fine-tuning
        history = vgg_model.fit_generator(
            train_generator,
            samples_per_epoch=nb_train_samples,
            nb_epoch=epoch,
            validation_steps=20,
            validation_data=validation_generator
            # nb_val_samples=nb_validation_samples
            )

        # export model
        vgg_model.save_weights(os.path.join(Const.RESULT_DIR, '{model_name}.h5'.format(model_name=mname)))

        process_time = int((time.time() - start) / 60)
        print(Color.BLUE + u'Finished training!!! This process took', process_time, u' minutes' + Color.END)

    else:
        print(Color.RED + 'you have not put mode name' + Color.END)


if __name__ == '__main__':
    main()
