docker rm `docker ps -qa`
docker volume rm $(docker volume ls -q)
