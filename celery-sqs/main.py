from celery import Celery
from kombu.utils.url import safequote
import os

broker_url = 'sqs://ABCDEFGHIJKLMNOPQRST:ZYXK7NiynGlTogH8Nj+P9nlE73sq3@'

aws_access_key = safequote(os.getenv('aws_access_key', 'ABCDEFGHIJKLMNOPQRST'))
aws_secret_key = safequote(os.getenv('aws_secret_key', "ZYXK7NiynG/TogH8Nj+P9nlE73sq3"))

broker_url = "sqs://{aws_access_key}:{aws_secret_key}@".format(
    aws_access_key=aws_access_key, aws_secret_key=aws_secret_key,
)

broker_transport_options = {
    'region': 'eu-west-1',
    'visibility_timeout': 3600,  # 1 hour
    'polling_interval': 0.3,
    'wait_time_seconds': 15,
    'queue_name_prefix': 'celery-',
    'predefined-queues': {
        'binance-btc': {
            'url': 'https://ap-southeast-2.queue.amazonaws.com/123456/my-q',
            'access_key_id': 'xxx',
            'secret_access_key': 'xxx',
        }
    }
}
