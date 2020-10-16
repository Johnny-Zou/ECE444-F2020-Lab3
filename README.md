Jia Yu (Johnny) Zou \
This repo is a clone of: https://github.com/miguelgrinberg/flasky

## Docker Info

#### Files:
- Dockerfile located in root
- requirements.txt located in root

#### Build command:
```bash
docker build -t <name>:<tag> .
```
Example:
```bash
docker build -t myflaskapp:latest .
```
#### Start Container:
```bash
docker run -it --name <name> --rm -p 5000:5000 <name>:<tag>
```
Example:
```bash
docker run -it --name myflaskapp --rm -p 5000:5000 myflaskapp:latest
```




## Screenshots

Docker Run command
![Screenshot Docker Run command](./Screenshots/Lab4_docker_run.PNG?raw=true "Docker Run Command")

Browser
![Screenshot Browser](./Screenshots/Lab4_browser.PNG?raw=true "Browser")

Docker image
![Screenshot Docker image](./Screenshots/Lab4_docker_logs.PNG?raw=true "Docker Image")

## Briefly summarize the differences between Docker and Virtual Machine.

Virtual machines are an abstraction of physical hardware and each VM includes a copy of a complete OS. Docker containers on the other hand are an abstraction at the application layer and multiple docker containers running share the same host OS. Docker containers are ioslated from each other at the process level while virtual machines are fully isolated. This makes Docker more lightweight but at the cost of less secure isolation.