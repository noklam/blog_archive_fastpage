# Launching Kubernetes in Google Cloud Platform \(GCP\)

## Kubernetes Engine

Container Images

*  * gouravshah/frontend

### Expose a deployment

* Workload &gt; Set the load balancer port to 80 \(for easy access\), Target port as 8079 \(found the exposed port from Dockerfile\)
* The load balancer IP is for external access, it points to multiple pods \(HA\)



Examples of deployed app yaml file.

```yaml
---
apiVersion: "apps/v1"
kind: "Deployment"
metadata:
  name: "frontend"
  namespace: "default"
  labels:
    app: "frontend"
spec:
  replicas: 3
  selector:
    matchLabels:
      app: "frontend"
  template:
    metadata:
      labels:
        app: "frontend"
    spec:
      containers:
      - name: "frontend-1"
        image: "gouravshah/frontend:latest"
---
apiVersion: "autoscaling/v2beta1"
kind: "HorizontalPodAutoscaler"
metadata:
  name: "frontend-hpa-kkuu"
  namespace: "default"
  labels:
    app: "frontend"
spec:
  scaleTargetRef:
    kind: "Deployment"
    name: "frontend"
    apiVersion: "apps/v1"
  minReplicas: 1
  maxReplicas: 5
  metrics:
  - type: "Resource"
    resource:
      name: "cpu"
      targetAverageUtilization: 80


```



