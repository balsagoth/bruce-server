FROM kennethreitz/pipenv

COPY . /app

# Install curl.
RUN apt update
RUN apt install curl -y

# Install pack.
RUN curl -LO https://github.com/buildpack/pack/releases/download/v0.0.2/pack-linux
RUN mv pack-linux /usr/local/bin/pack
RUN chmod +x /usr/local/bin/pack

CMD bash
