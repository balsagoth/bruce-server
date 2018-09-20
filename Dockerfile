FROM kennethreitz/pipenv

COPY . /app

# Install curl.
RUN apt update
RUN apt install curl -y
RUN apt install git -y

RUN apt install docker.io -y
RUN service docker start

VOLUME /var/lib/docker

CMD bash
