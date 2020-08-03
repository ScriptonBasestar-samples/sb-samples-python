from celery import Celery
from kombu.utils.url import safequote
import os

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY', 'ABCDEFGHIJKLMNOPQRST')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY', 'ZYXK7NiynG/TogH8Nj+P9nlE73sq3')
AWS_REGION = os.getenv('AWS_REGION', 'ap-northeast-2')
AWS_USER_ID= os.getenv('AWS_USER_ID', '191919191919')
SQS_NAME=os.getenv('SQS_NAME', 'test_sqs_1')

broker_url = "sqs://{AWS_ACCESS_KEY}:{AWS_SECRET_KEY}@".format(
    AWS_ACCESS_KEY=safequote(AWS_ACCESS_KEY), AWS_SECRET_KEY=safequote(AWS_SECRET_KEY),
)

broker_transport_options = {
    'region': AWS_REGION,
    'visibility_timeout': 3600,  # 1 hour
    'polling_interval': 0.3,
    'wait_time_seconds': 15,
    'queue_name_prefix': '',
    'predefined-queues': {
        'test1': {
            'url': 'https://{AWS_REGION}.queue.amazonaws.com/{AWS_USER_ID}/{SQS_NAME}'.format(
                AWS_REGION=AWS_REGION,
                AWS_USER_ID=AWS_USER_ID,
                SQS_NAME=SQS_NAME,
            ),
            'access_key_id': AWS_ACCESS_KEY,
            'secret_access_key': AWS_SECRET_KEY,
        }
    }
}


app = Celery('tasks', broker=broker_url, backend='rpc://')

@app.task
def add(x, y):
    return x + y

if __name__ == '__main__':
    argv = [
        'worker',
        '--loglevel=INFO',
    ]
    app.worker_main(argv)

    r0 = add.delay(2,5)
    r1 = add.delay(2,7)
    r2 = add.delay(7,5)
    r3 = add.delay(2,3)

    print(r0.ready())
    print(r0.ready())
    print(r0.ready())
    print(r0.ready())
