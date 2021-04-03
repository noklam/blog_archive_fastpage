---
title: Meta-Analysis of SQL Query, Graph - Part 0 [Help needed, I am looking for open dataset of actual user SQL query log]
description: Notes
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

Recently, I have started to thinking more about Data Catalog, Data Discovery. As a data scientist, we spent significant time to build data pipeline. We spend a large chunk of the time to understand the context of the data, and how to use it correctly. Most data catalog provides information about the `Schema` and `Column` or `Table` description. However, we deal with dirty data in reality, a table may not be perfectly design, business process could change but the table schema could not catch up. So you end up have to apply a lot of addition condition to filter out data, i.e. you may want to look at column A before  2019-Jan, but look at column B after 2019-Jan. The ultimate version of the query contains a lot of intergration efforts and it is a mental model of how certain persion views about the data. These information are usually communicate verbally and very hard to be re-used.

I have been thinking a lot how can we communicate these information, or so called domain knowledge more efficiently. I am thinking whether *Analyzing user actual query log* could add more insight about the data.

For example, I may answer these questions if I could analyze SQL query logs
* How often is this table queried (and by who?)
* How is this table related to other tables? How are they usually joined together?
* What is the most common filtering condition added when people are querying this table?

So far, I only have rough ideas and need helps to get Open Dataset of user sql query logs. If you know such dataset exist, please email me @ mediumnok@gmail.com

Thanks!



<!--truncate-->

