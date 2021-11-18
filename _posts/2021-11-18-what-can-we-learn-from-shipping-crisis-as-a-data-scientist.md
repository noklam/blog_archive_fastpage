---
title: What can we learn from Shipping Crisis as a Data Scientist?
description: The Long Beach port congestion could teach us a lot about data science in real world.
comments: true
hide: false
layout: post
toc: false
author: noklam
authorURL: https://github.com/noklam
categories: [product]
---

Even if you are not working in shipping industry, you probably heard about shipping cost is skyrocking for the last year. COVID is clearly the initial disruption, but the story does not end there. Recently, [Long Beach's port congestion is at a historcial scale](https://www.wsj.com/video/series/on-the-news/what-america-supply-chain-backlog-looks-like-up-close/388D6F02-5BCD-43AD-A3EE-B945F7373983), there are now more than 70+ ships waiting outside the port, the typical number is 1 or 2.

You may think the terminal must be busy as hell, so did I, but it is actualy far from the truth. [In fact, the port is actually paralyzed](https://twitter.com/typesfast/status/1451543776992845834?s=20). The reason surprised me a lot, it is not because of lacking of driver or empty containers, but yard space. Container are being unloaded from ships, then they are being put at the container yard before they go into depot or being stuffed again.

On a high level, it is caused by a negative feedback loop which COVID probably contributed a lot, as it caused a lot of disruption to the supply chain.

1. Port Congestion -> Containers pilled up at container yard since it is waiting to be loaded on ship
2. Container yard space is taken up by cotnainers, less space is available
3. A container need to be put on a chassis before it is loaded, but as the container yard is full, empty containers stuck on the chassis and they need to be unloaded before you put a stuffed container.
4. Less Chassis is available to load stuff, so it further slow down the process
5. The loop complete and it starts from 1 again


![Port Congestion Feedback Loop](images/2021-11-18-23-37-38.png)

This is a simplified story, you can find more details from this [twitter thread from flexport's CEO Ryan](https://twitter.com/typesfast/status/1451543776992845834?s=20). There are more constraints that making this load/unload process inefficient, so the whole process is jammed. Think about a restaurant with limited amount of trays, you need to get a tray if you want to get food. But because there are too many customers, it jammed the door .
So there are many customers holding an empty tray while many food are waiting to be served.

Ryan point out a very important lesson here, that is, `you need to choose your bottleneck, and it should really be the capital intensive assets.` Going back to our restaurant's analogy, chef and space is probably the most expensive assets, so we should try to keep the utilization high. A simple solution is to buy more trays, so that it won't be jammed. Ofcourse, you can also find a larger space, build a bigger door, but that will cost you more money too.

For shipping, the terminal's crane should be the most capital intensive, so we should try our best to keep it working 24/7 to digest the terminal queue.

This is a simple idea yet it is powerful and it strikes me hard. As a data scientist, I work on optimization problem. To maximize the output of a system, we can use linear programming. When we are solving this problem, we are asking question like this.

> Given x1 Terminals, x2 drivers, x3 containers, x4 ships, what is the maximize output of this system and **how** do you arrange them to achieve so?

However, if you are a product/business analyst, a better question may be
> What is the output of this system if I add more container yard space?

By changing the input of the system, you may achieve much better result. But as a data scientist, we often stuck in a mode that how do we optimize x metrics with these features. So we may end up spending months and try to schedule ships and driver perfectly to load 10% more container, but you can actually increase loading efficiency by 50% simply by adding more yard space. It feels like cheating as a scientific question, since this is not we asked originally, but this happened a lot in a business context. 

We are not trying to find the best algorithm to solve a problem, the algorithm is just **one way** of doing it. We may get surprising result by just tweaking the asked question a little bit.

I am curious about what is the limiting factor in our current supply chain system, and how sensitive it is to the environment. Is forecasting & optimization the right way to do it? Do we actually need a precise forecast or we can have a bit of redundancy (like in this case, having extra yard space which could be a waste but improve the system robustness)? This is questions that we need to ask ourselves constantly, as the true question is often not asked, but explored after lots of iterations. We need to, and we have to ask the right question, and that is an art more elegant than an algorithm in my opinion.

I do not know if Ryan's word are 100% true, but it reminds me an important lesson. The right solution (question) may be simple, but it may not be obvious. Have we exploited all the simple solution before we went nuts with fancy algorithms?

p.s. Apologised as I don't have time to proofread but simply try to write down the snapshot of my current mind  [2021-11-18]



# Reference
{% twitter https://twitter.com/typesfast/status/1451543776992845834?s=20 %}
https://twitter.com/typesfast/status/1451543776992845834?s=20
https://www.facebook.com/669645890/posts/10159859049175891/
unroll version: https://threadreaderapp.com/thread/1451543776992845834.html

