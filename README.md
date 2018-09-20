# bruce-server
Bruce's guts.

![model](https://github.com/bruce-project/bruce-server/raw/master/sql/model.png)

## Running the Server

    $ docker-compose up
    
## Components

- Postgres (Data Storage)
- RabbitMQ (Task Queue, Celery)
- HTTP REST API: Falcon Web Framework
