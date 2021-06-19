---
title: A logging.config.dictConfig() issue in python
description: logging.config.dictConfig() 
comments: true
hide: false
layout: post
toc: false
author: noklam
authorURL: https://github.com/noklam
authorTitle: A data scientist in Hong Kong
authorImageURL: https://avatars0.githubusercontent.com/u/18221871?s=400&u=0ca734683fc7e41a3565c5591218008af5a77e9b&v=4
categories: [python]
---

```python
import logging
from clearml import Task
conf_logging = {"version":1, 
                "formatters":{
                      "simple":{
                             "format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
                      }
                  }
t = Task.init(project_name="test")
logging.config.dictConfig(conf_logging)
logging.info("INFO!")
logging.debug("DEBUG!")
logging.warning("WARN!")
print("PRINT!")
```

With this code block, you will find no print() or logging is sent to ClearML logging Console. Turns out `kedro` use `logging.config.dictConfig(conf_logging)` as the default and causing this issue.

A quick fix is to add `"incremental": True` in the config dict. In the [standard documentation](https://docs.python.org/3/library/logging.config.html#:~:text=incremental%20-%20whether%20the%20configuration%20is%20to%20be%20interpreted%20as%20incremental%20to%20the%20existing%20configuration.%20This%20value%20defaults%20to%20False%2C%20which%20means%20that%20the%20specified%20configuration%20replaces%20the%20existing%20configuration%20with%20the%20same%20semantics%20as%20used%20by%20the%20existing%20fileConfig()%20API.), the default is `False`, which means the configuration will replace existing one, thus removing the `clearml` handlers, and causing the issue I had.

```python
conf_logging = {"version":1, 
                "incremental": True
                "formatters":{
                      "simple":{
                             "format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
                      }
                  }
```



<!--truncate-->

