FROM ubuntu:latest
ENV TZ="Asia/Tokyo"
VOLUME ../:/var/test
WORKDIR /var/test
RUN apt-get update && apt-get install -y python3 python3-pip python3-dev libmysqlclient-dev && apt-get update
CMD ["pip3","install","."]