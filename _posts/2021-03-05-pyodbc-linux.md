---
title: Setting up pyodbc for Impala connection, works on both Linux and Window
description: Easiest way to connect with Impala in Windows
comments: true
hide: false
toc: false
layout: post
author: noklam
authorURL: https://github.com/noklam
authorTitle: A data scientist in Hong Kong
authorImageURL: https://avatars0.githubusercontent.com/u/18221871?s=400&u=0ca734683fc7e41a3565c5591218008af5a77e9b&v=4
categories: [pyodbc, impala]
---

# Introduction
Long story short, connect with Impala is a big headache in Windows. `pyhive`, `impyla` are both buggy. At the end, I stick with `pyodbc` as it works on both Linux and Windows, and seems to have better performance. There are not many steps, but it would be tricky if you try to Google as there are not much guide that just work out of the box

# Setup
First, you need to download the ODBC driver from [Cloudera](https://www.cloudera.com/downloads/connectors/impala/odbc/2-6-11.html).

Then you need to instsall the driver properly.
```
dpkg -i docker/clouderaimpalaodbc_2.6.10.1010-2_amd64.deb
```

Add this file to the directory /etc/odbcinst.ini, if you already have add, append this to the file.
```
# /etc/odbcinst.ini
[ODBC Drivers]
Cloudera Impala ODBC Driver 32-bit=Installed
Cloudera Impala ODBC Driver 64-bit=Installed
[Cloudera Impala ODBC Driver 32-bit]
Description=Cloudera Impala ODBC Driver (32-bit)
Driver=/opt/cloudera/impalaodbc/lib/32/libclouderaimpalaodbc32.so
[Cloudera Impala ODBC Driver 64-bit]
Description=Cloudera Impala ODBC Driver (64-bit)
Driver=/opt/cloudera/impalaodbc/lib/64/libclouderaimpalaodbc64.so
```
Then install some additional package.

```bash
apt-get update && apt-get -y install gnupg apt-transport-https
apt-get update && apt-get -y install libssl1.0.0 unixodbc unixodbc-dev \
&& ACCEPT_EULA=Y apt-get -y install msodbcsql17
apt-get install unixodbc-dev -y

```
Last, `pip install pyodbc`  and have fun.

To read a database table, you can simply do this.
```python
import pyodbc
import pandas as pd

conn = pyodbc.connect(f"""
Driver=Cloudera ODBC Driver for Impala 64-bit; 
PWD=password;
UID=username;
Database=database
""")
```

There are multiple way to connect, but I found using a connection string is the most straight forward solution that does not require any additional enviornment variable setup.


