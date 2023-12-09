```
running django app with kubernetes or DockerCompose in develope,deployment,kubernetes status
```

***

# DockerCompose
```
first Fill the .env file

base:
    install docker and dockercompose in your machin
    (if your life countries Sanctioned countries go to docker.ir and set config)

develop:
    STATUS variable in .env file set develope
    WEB_DOMAIN variable in .env file set localhost
    run docker-compose-develope.yml 
    go to the project directory and create virtual environment
    active your environment and install all package in requirements.txr 
    and in your command line run django project

test:
    STATUS variable in .env file set deployment
    WEB_DOMAIN variable in .env file set localhost
    run docker-compose-deployment.yml
    in your browser search localhost

deployment:
    STATUS variable in .env file set deployment
    WEB_DOMAIN variable in .env file set your domain name
    run docker-compose-deployment.yml 
```

***

# kubernetes
```
first STATUS variable in .env file set kubernetes
build image (docker build -t web:4.0 .)

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