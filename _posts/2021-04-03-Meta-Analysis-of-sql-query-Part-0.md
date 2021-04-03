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
Recently, I have started to think more about Data Catalog, Data Discovery. As data scientists, we spent significant time building a data pipeline. We spend a large chunk of the time understanding the context of the data, and how to use it correctly. Most data catalog provides information about the Schema and Column or Table description. However, we deal with dirty data in reality, a table may not be perfectly design, the business process could change but the table schema could not catch up. So you end up having to apply a lot of additional conditions to filter out data, i.e. you may want to look at column A before 2019-Jan but look at column B after 2019-Jan. The ultimate version of the query contains a lot of integration efforts and it is a mental model of how a certain person views the data. This information is usually communicate verbally and very hard to be re-used.

I have been thinking a lot about how can we communicate this information, or so-called domain knowledge more efficiently. I am thinking whether *Analyzing user's actual query log* could add more insight into the data.

For example, I may answer these questions if I could analyze SQL query logs
How often is this table queried (and by who?)
How is this table related to other tables? How are they usually joined together?
What is the most common filtering condition added when people are querying this table?

So far, I only have rough ideas and need helps to get an Open Dataset of user SQL query logs. If you know such a dataset exists, please email me @ mediumnok@gmail.com
Thanks!


<!--truncate-->

