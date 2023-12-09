# 1- docker build -t image_name:tag .

# 2- minikube start 

# 3- minikube image load your_image_name

***

# 4-
```# step_1- kubectl apply -f configmap.yml```

```# step_2- kubectl apply -f database/redis.yml```

```# step_3- kubectl apply -f database/postgres.yml```

```# step_4- kubectl apply -f database/pgadmin.yml```

```# step_5- kubectl apply -f application/deployment.yml```

***

# other commands:
```
kubectl port-forwrad <your image name> <local-port>:<container-port>
kubectl delete -f config-file.yml
kubectl exec -it pod-name bash

kubectl get pod
kubectl describe pod-name
kubectl get pod -o yaml > file-name.yml

kubectl get configmap
kubectl delete configmap config-name
kubectl get configmap -o yaml > file-name.yml

kubectl get service
kubectl delete service service-name
kubectl get service -o yaml > file-name.yml


kubectl get secret
kubectl delete secret secret-name
kubectl get secret -o yaml > secret-name.yml

```