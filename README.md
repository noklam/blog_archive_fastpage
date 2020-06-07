---
description: Machine Learning Journey
---

# README

A catalog of various machine learning topics.

* [Graph Neural Network Basics](./#graph-neural-network-basics)
  * [Understand What is the weird D-1/2LD-1/2](./#understand-what-is-the-weird-dsup-12supldsup-12sup)
  * [Supplement Chinese Reading](./#supplement-chinese-reading)
* [Time Series Forecast](./#time-series-forecast)
  * [Motivation](./#motivation)
  * [Forecasting Methods](./#forecasting-methods)
    * [Statistical Method](./#statistical-method)
    * [Machine Learning](./#machine-learning)
    * [Deep Neural Network](./#deep-neural-network)
* [Prediction Interval](./#prediction-interval)
  * [Python Time Series Forecasting Library](./#python-time-series-forecasting-library)
* [Contribution](./#contribution)
* [Under Review](./#under-review)

## Graph Neural Network Basics

### Understand What is the weird D-1/2LD-1/2

1. [spectral graph theory - Why Laplacian Matrix need normalization and how come the sqrt of Degree Matrix? - Mathematics Stack Exchange](https://math.stackexchange.com/questions/1113467/why-laplacian-matrix-need-normalization-and-how-come-the-sqrt-of-degree-matrix)
2. [spectral graph theory - Why Laplacian Matrix need normalization and how come the sqrt of Degree Matrix? - Mathematics Stack Exchange](https://math.stackexchange.com/questions/1113467/why-laplacian-matrix-need-normalization-and-how-come-the-sqrt-of-degree-matrix)
3. [What's the intuition behind a Laplacian matrix? I'm not so much interested in mathematical details or technical applications. I'm trying to grasp what a laplacian matrix actually represents, and what aspects of a graph it makes accessible. - Quora](https://www.quora.com/Whats-the-intuition-behind-a-Laplacian-matrix-Im-not-so-much-interested-in-mathematical-details-or-technical-applications-Im-trying-to-grasp-what-a-laplacian-matrix-actually-represents-and-what-aspects-of-a-graph-it-makes-accessible)

### Supplement Chinese Reading

1. [Heat Diffusion](https://www.zhihu.com/question/54504471/answer/630639025)
2. [GCN use edge to agg node information](https://www.zhihu.com/question/54504471/answer/611222866)
3. [How to do batch training with GCN](https://zhuanlan.zhihu.com/p/55191463)

## Time Series Forecast

### Motivation

While neural network have gain a lot of success in NLP and computer vision, there are relatively less changes for traditional time series forecasting. This repository aims to study the lastest practical technique for time series prediction, with either statistical method, machine learning or deep neural network. I will also try to summarize practical solution from Kaggles.

### Forecasting Methods

#### Statistical Method

#### Machine Learning

#### Deep Neural Network

[Gramian Angular Field ](https://forums.fast.ai/t/time-series-sequential-data-study-group/29686/2?u=nok): Transform time series into an image and use transfer learning with CNN

## Prediction Interval

While forecasting accuracy is important, the prediction interval is also important and it is an area that the machine learning world has less focus on.

* Traditional statistical forecast \(ARIMA, ETS etc\)
* Bayesian Neural Network
* Random Forest jackknife approximation
* MCDropout  \(Use Dropout at inference time as variation inference\)
* Quantile Regression
* VOGN \(Optimizer weight pertubation\)
* Random Forest jackknife appoximation 

### Python Time Series Forecasting Library

[Prophet \(Facebook\)](https://github.com/facebook/prophet): Tool for producing high quality forecasts for time series data that has multiple seasonality with linear or non-linear growth. It has build-in modelling for Holiday effect.

[pyts](https://johannfaouzi.github.io/pyts/) : state-of-the-art algorithms for time series transformation and classification

## Contribution

Feel free to send a PR or discuss by staring an issue.😁

## Under Review

