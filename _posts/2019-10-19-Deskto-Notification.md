---
title: plyer - Desktop Notification in Python
author: noklam
authorURL: https://github.com/noklam
authorTitle: A data scientist in Hong Kong
authorImageURL: https://avatars0.githubusercontent.com/u/18221871?s=400&u=0ca734683fc7e41a3565c5591218008af5a77e9b&v=4
categories: python
---

```python
from plyer import notification
import random

class DesktopNotification:
    @staticmethod
    def notify(title='Hey~', message='Done!', timeout=10):
        ls = ['👍','✔','✌','👌','👍','😎']
        notification.notify(
            title = title ,
            message = random.choice(ls) * 3 + ' ' + message,
            timeout = timeout # seconds
        )


if __name__ == '__main__':
    DesktopNotification.notify()

```
You could add this simple code block to notify you when the program is done! A desktop notification will be prompt on the bottom right corner in Window.

<!--truncate-->

