# 1- docker build -t <image name>:<tag> .

# 2- minikube start 

# 3- minikube image load <your image name>

# 4
```# step 1- kubectl apply -f configmap.yml```

```# step 2- kubectl apply -f database/database.yml```

```# step 3- kubectl apply -f application/secret.yml```

```# step 4- kubectl apply -f application/deployment.yml```

```
kubectl port-forwrad <your image name> <local-port>:<container-port>
```