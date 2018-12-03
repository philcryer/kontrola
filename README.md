# kontrola

A script to sweep a subnet looking for IPs with SSL certs, then querying those certs in order to determine when expiration times are approaching.

## docker

docker build .
docker run -p 80:80 -t -d nginx:latest

 1090  docker run -p 80:80 -v ${pwd}/html:/html -t -d nginx:latest
 1094  docker run -p 80:80 -v /html:${pwd}/html -t -d nginx:latest

 docker run --name docker-nginx -p 80:80 -d -v ~/docker-nginx/html:/usr/share/nginx/html nginx
