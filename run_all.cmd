docker stop assign
docker container rm assign
docker build -f docker\Dockerfile -t assign .
docker run -d --name=assign -p 5000:5000 assign
