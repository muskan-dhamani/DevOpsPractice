1. Build Docker Image: docker build -t tagname
2. Run: docker run -it tagname
3. Login to DockerHub from CLI: docker login
4. Push Image to DockerHub: docker push tagname
5. Pull Docker image from DockerHub: docker pull tagname
6. View Running Containers: docker ps
7. View exited containers: docker ps -a
8. Stop container: docker stop name/id

Docker Volume:
1. docker volume ls
2. docker volume create name
3. docker volume rm name/id
4. docker volume inspect name/id

Docker Networking:
Connect one container with another container - 
1. docker run -d --name nameofcontainer image
2. docker exec -it nameofcontainer path
3. apt-get install iputils-ping -y
4. Same steps for another container
5. ping IP_Address

Networking commands: 
1. docker network create network_name
2. docker run -d --name nameofcontainer --network=network_name image
3. docker network rm network_name
