# icTrainer
image classifier train program



## How to Use
In this gude, we will create a dog/cat image classifier.
### 1.Collect Images
https://icrawler.readthedocs.io/en/latest/   

```
$ ictrainer --mode "collect" --search "dog' -n 250
$ ictrainer --mode "collect" --search "cat' -n 250

```
You'll have dogs & cats images under `dataset` folder.


### 2. Resize images
In this step, we will change all images size for training. The current input size is 256 x 256.
This step may be mess up images you collected, so you need to check all images manually. In the furture, there will be a function that save your time.  

```
$ ictrainer --mode "resize" --target dataset/dog
$ ictrainer --mode "resize" --target dataset/cat
```

### 3.Create folders for classes
This step, we'll need to create folders and distribute images to `train` & `validation` folder.

#### 3-1. create folders
Create a couple of folders under dataset.
```
 dataset
    ├── train
    │   ├── cat
    │   └── dog
    └── validation
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
$ ictrainer --mode "train" --classes "cat" "dog" --mname "dogAndcat_"
```
