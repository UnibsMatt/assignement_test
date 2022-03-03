docker build -f docker\Dockerfile -t assign .
docker build -f docker\Dockerfile_test -t assign_test .
docker run assign_test
