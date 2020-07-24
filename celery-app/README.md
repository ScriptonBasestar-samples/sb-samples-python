Celery Redis
============

## Run

### SetUp
Running redis cluster
```bash
docker-compose up --scale redis-sentinel=3 --scale redis-slave=2
```

Running single redis
```bash
docker run --rm -p 6379:6379 -e REDIS_PASSWORD=str0ng_passw0rd -d bitnami/redis:latest
```

Running rabbitmq
```bash
docker run --rm -p 5672:5672 -d rabbitmq:3
```

### App
Run celery app
```bash
celery -A tasks_redis worker --loglevel=info
```

### TearDown

```bash
docker rm -f $(docker ps -qa)
```

## REF

* https://hub.docker.com/r/bitnami/redis-sentinel
