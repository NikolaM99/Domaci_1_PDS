# Domaci_1_PDS
Fajlovi za domaci 1 - Docker and Kubernetes


Quick startup guide:

- Build a docker image from Dockerfile using the command: docker build -t serverimg:tag1 .    //being positioned in a directory containing a Dockerfile
- Run a container with serverimg image using a command: docker run -p 80:8081 --name serverapi -d serverimg:tag1   // detached mode, map the containers 8081 port to our local port 80
- Access localhost through a browser and API should work!

- Build a docker image from Dockerfile using the command: docker build -t clientimg:tag1 .   //being positioned in a directory containing a Dockerfile
- Run a container with clientimg image using a command: docker run -p 80:8081 --name clientrequest -d clientimg:tag1   // detached mode, map the containers 8081 port to our local port 80
- Access "localhost/users" through a browser and user data should be displayed in JSON format!
