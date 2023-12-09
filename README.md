# Kubernetes
```
#running django app with kubernetes or DockerCompose
```

***

# kubernetes
```
in kubernetes directory have two directory for configuration
kubernetes which first directory with name application(django)
and second directory for database(postgresql) 


in application:
deployment.yml for running 3 replicas djano app
secret.yml for secrets key in django
pod.yml for run just one pod django app

in database:
statefullset.yml for configuration and running postgresql


configamp.yml for key-value common in two pod

README.md have a series of commands for help
```

in project directory the django project is located
```