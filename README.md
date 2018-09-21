# bruce-server

Bruce's guts. *See [meta repo](https://github.com/bruce-project/meta) for more information.*

![model](https://github.com/bruce-project/bruce-server/raw/master/sql/model.png)

## Running the Server

    $ docker-compose up
    
## Components

- Postgres (Data Storage)
- Minio (OCI Image Storage)
- RabbitMQ (Task Queue, Celery)
- HTTP REST API: Falcon Web Framework
