---
description: 'Several ways to inspect our model, zoom in and understand your model!'
---

# Explainable AI

## Introduction

Personal collecions of model interpretation utilities.

This repository include general model interpretation methods. Most articles focus on library, but the method are actually general than that. For example, we can use partial indepedence for deep learning model too. You will find most tutorials out there are only using it on Tree.

Same applied on SHAP, many tutorials use Tree as example, but the library actually support much more general algorithm. Your feature don't even have to be a column.

1. Partial Depedence Plot 
2. SHAP
3. Tensorflow \(What-if tools\)\[[https://pair-code.github.io/what-if-tool/age.html](https://pair-code.github.io/what-if-tool/age.html)\]
4. Counterfactual \(Most simliar data point, but very different inference value\)

## Model interpretation

Model interpretation can be divided into local or global. Different method are complementary instead of replacement. For example, SHAP give you an idea what features are important for a particular prediction. But Partial Dependence plot supplement the "What-if" condition, namely, how will your prediction changes when a dependent variable changes. These are two different information which are often overlooked.

### Partial Dependence

* Local
* Global

Partial depedence can be applied in row level or dataset level. It gives you a sense that how **Change** of a feature will change the model output accordingly.

We can also "zoom in" if we want, say using a subset of data \(e.g. at country level\) or even at row level to dig into the model.

The what-if tool allows you to change the value of a feature and run inference. Partial dependence is doing the exact same thing except it run multiple prediction by changing one features to different values to obtain a continuous plot.

![What-if tools allow user to change the model input and see how prediction changes](.gitbook/assets/image%20%281%29.png)

