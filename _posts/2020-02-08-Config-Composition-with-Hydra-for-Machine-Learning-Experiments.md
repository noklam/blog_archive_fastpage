---
title: Hydra - Config Composition for Machine Learning Project
author: noklam
authorURL: https://github.com/noklam
authorTitle: A data scientist in Hong Kong
authorImageURL: https://avatars0.githubusercontent.com/u/18221871?s=400&u=0ca734683fc7e41a3565c5591218008af5a77e9b&v=4
comments: true
hide: false
toc: false
layout: post
categories: [python, ML]
---

GitHub: https://github.com/noklam/notadatascientist/tree/master/demo/hydra-example


 Machine learning project involves large number of hyperparmeters. In many case you could have multiple config, e.g. differnet dataset, database connection, train/test mode. __hydra__ provide a simple Command Line Interface that is useful for composing different experiment configs. In essence, it compose different files to a large config setting. It offers you the common Object Oriented Programming with YAML file. Allow you to have clear structure of configurations.

 Assume you have a config.yaml like this, where run_mode and hyperparmeter are separate folder to hold different choice of parameters. You can set defaults for them with the following structure.

## Folder Structure
```
config.yaml
demo.py
run_mode
  - train.yaml
  - test.yaml
hyperparmeter
  - base.yaml
```
## config.yaml
```yaml
defaults:
 - run_mode: train
 - hyperparameter: base
```

The benefit of using such approach is that it makes comparsion of experiments much easier. Instead of going through the parameters list, you only focus on the argument(the difference). It helps organize machine learning results and ease a lot of pain in tracking the model performance.


```python
import hydra
from omegaconf import DictConfig
@hydra.main(config_path="config.yaml")
def my_app(cfg : DictConfig) -> None:
    print(cfg.pretty())
if __name__ == "__main__":
    my_app()
```


```python
python demo.py 
```

    gamma: 0.01
    learning_rate: 0.01
    run_mode: train
    week: 8
    
    

For example, with a simple example with 4 parameters only, you can simply run the experiment with default

# Override default parameters

You can easily overrite the learning rate with an argument, it would be very clear that learning rate is the only changing parameter with this approach


```python
python demo.py learning_rate=0.1
```

    gamma: 0.01
    learning_rate: 0.1
    run_mode: train
    week: 8
    
    

In somecase, you may only need to test a model instead of changing it.


```python
python demo.py learning_rate=0.1 run_mode=test
```

    gamma: 0.01
    learning_rate: 0.1
    run_mode: test
    week: 8
        

It also safeguard your experiment if you pass in some parameters that is not exist


```python
!python demo.py typo=0.2
```

    Traceback (most recent call last):
      File "demo.py", line 7, in <module>
        my_app()
     "C:\ProgramData\Anaconda3\lib\site-packages\omegaconf\dictconfig.py", line 41, in __setitem__
        "Accessing unknown key in a struct : {}".format(self.get_full_key(key))
    KeyError: 'Accessing unknown key in a struct : typo'
    

# --Multirun,  Combination of parameters
In case you want to gridsearch paramters, which is very common in machine learning, you can use an additional argument __multirun__ to do that easily.


```python
!python demo.py --multirun learning_rate=0.1,0.01,0.001 gamma=0.1,0.01

```

    [2020-02-08 19:28:46,095][HYDRA] Sweep output dir : multirun/2020-02-08/19-28-46
    [2020-02-08 19:28:46,102][HYDRA] Launching 6 jobs locally
    [2020-02-08 19:28:46,103][HYDRA] 	#0 : learning_rate=0.1 gamma=0.1
    gamma: 0.1
    learning_rate: 0.1
    run_mode: train
    week: 8
    
    [2020-02-08 19:28:46,192][HYDRA] 	#1 : learning_rate=0.1 gamma=0.01
    gamma: 0.01
    learning_rate: 0.1
    run_mode: train
    week: 8

    ... SKIPPED