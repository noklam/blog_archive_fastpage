# Kubernetes

## Free Resource

{% embed url="https://www.udemy.com/course/just-enough-kubernetes/learn/lecture/11858548\#overview" %}

## Points to Learn

* Pods
* Manual Scale up
* AutoSacle
* Zero-downtime deploy

### A Sample Architecture Application

* Java \(Spring\)
* go \(catalog\)
* Frontend \(nodejs\)
* database \(mysql & mongo\)

![](../.gitbook/assets/image%20%2813%29.png)



## Why Kubernetes

Alternative:

* Dockers in a machine 

You don't connect to a container and upgrade, you deploy a new container instead.

## Pod

* Unit of deployment in Kubernetes
* Replication of pods to achieve High Availablity \(HA\) - replication controller
* Replication \(scaling\)
* Availability\(If a pod die, the controller should replace it\)

### Service

* Act like a load balancer to distribute traffic
* Has an IP and DNS
* The Application connects to each other through a common endpoint \(a service\), which has lots of pods connected to it under the hood.
* 
![](../.gitbook/assets/image%20%2815%29.png)



