<p align="center">
  <img width="auto" height="auto" src="https://github.com/koji/icTrainer/blob/master/top.png" style="border: none;
outline: none;">
</p>

[![PyPI version](https://badge.fury.io/py/pypi.svg)](https://pypi.org/project/ictrainer/)
### icTrainer is a python module which allows users to train image classifier easily

Basically, this module is for `python3`
## Install

```
$ pip install ictrainer
```
Also you can install manually.  
```
clone repo
$ git https://github.com/koji/icTrainer.git
$ cd icTrainer/ictrainer
$ python setup.py install
```

## How to Use
In this gude, we will create a dog/cat image classifier.
### 1.Collect Images
https://icrawler.readthedocs.io/en/latest/   

```
$ ictrainer --mode collect --keyword dog -n 250
$ ictrainer --mode collect --keyword cat -n 250
```
You'll have dogs & cats images under `dataset` folder.


### 2. Resize images
In this step, we will change all images size for training. The current input size must be `320 x 180`(required).
This step may be mess up images you collected, so you need to check all images manually. In the furture, there will be a function that save your time.  

```
$ ictrainer --mode resize --target dog
$ ictrainer --mode resize --target cat
```

For people want to use resize mode for other thing, you can use reize images with the following command.  
The folder structure should be the same the above.  
```
$ ictrainer --mode resize --target cat --image_width 480 --image_height 320
```

### 3.Create folders for classes
This step, we'll need to create folders and distribute images to `train` & `validation` folder.

#### 3-1. create folders
Create a couple of folders under dataset.   
This step will be automated in the future.  
```
 dataset
    ├── train
    │   ├── cat
    │   └── dog
    └── val
        ├── cat
        └── dog
```

#### 3-2. distribute images
Move images we got via `image collect mode`. In this case, probably we have 250 images for each other.
We will put 225 images for train and 25 images for validation so that `train/dog` has 225 images and `validation/dog` has 25 images. The cats should be the same.

### 4.Train Images
There are some options we need to put. The most important one is `--classes` which will be labels. In this case, we have dog & cat, so we need to put them as classes.
`--batch`: batch size default 16        
`--epoch`: epoch default 30       
`--mname`: output model name      
`--lr`: learning rate default 1e-3       
`momentum`: mementum default 0.9     

We will use default settings.

```
$ ictrainer --mode train --classes "cat" "dog" --mname "dogAndcat_"
```

## code
This code will be pushed soon. (cleaning up now)

## pre-train model
#### `smart device`   
https://github.com/koji/icTrainer/blob/master/model/smartdevice_epoch30.h5      
```
classes = ['echo', 'echoplus', 'echoshow', 'googlehome', 'googlehomemini', 'nest']   
```

