# 1- docker build -t image_name:tag .

# 2- minikube start 

# 3- minikube image load your_image_name

***

# 4-
```# step_1- kubectl apply -f configmap.yml```

```# step_2- kubectl apply -f database/redis.yml```

```# step_3- kubectl apply -f database/postgres.yml```

```# step_4- kubectl apply -f database/pgadmin.yml```

```# step_5- kubectl apply -f application/secret.yml```

```# step_6- kubectl apply -f application/deployment.yml```

```
kubectl port-forwrad <your image name> <local-port>:<container-port>
```