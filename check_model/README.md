## check a model result

## How to use 

### 1. Download test.py
Put `test.py` into your project folder.


### 2. Create a test folder
Create `test` folder under `dataset` folder.   

### 3. Edit test.py
You need to edit `test.py` a little bit. 
classes   
https://github.com/koji/icTrainer/blob/master/check_model/test.py#L9   
If you train "dog", "cat", "bird"
your class must be like the following.
```python
classes = ['dog', 'cat', 'bird']
```
Put your model name     
https://github.com/koji/icTrainer/blob/master/check_model/test.py#L33


### 4. Run test.py

```
$ python test.py
```
