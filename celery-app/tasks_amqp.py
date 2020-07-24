from celery import Celery
from dotenv import load_dotenv
import os

load_dotenv('.env-sample_rabbitmq')
app = Celery('tasks_amqp', broker=os.getenv('BROKER_URL'), backend=os.getenv('BACKEND_URL'))


class Config:
    enable_utc = True
    timezone = 'Europe/London'


app.config_from_object(Config)


# app.conf.humanize(with_defaults=False, censored=True)
# app.conf.table(with_defaults=False, censored=True)

# app.conf.broker_url = 'redis://:str0ng_passw0rd@localhost:6379/0'


# app.conf.broker_url = 'sentinel://localhost:26379;sentinel://localhost:26380;sentinel://localhost:26381'
# app.conf.broker_transport_options = {'master_name': "cluster1"}

@app.task
def add(x, y):
    print('task add')
    return x + y


if __name__ == '__main__':
    argv = [
        'worker',
        '--loglevel=DEBUG',
    ]
    app.worker_main(argv)

    # app.worker_main()

    # app.start()
