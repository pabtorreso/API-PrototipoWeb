docker buildx build -t api-docker .
docker run -p 5000:5000 api-docker