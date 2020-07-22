from flask import Flask
from threading import Event
import signal

from flask_kafka import FlaskKafka

app = Flask(__name__)

INTERRUPT_EVENT = Event()

bus = FlaskKafka(INTERRUPT_EVENT,
                 bootstrap_servers=','.join(['localhost:9092', 'localhost:9093', 'localhost:9094']),
                 group_id='consumer-grp-id'
                 )


def listen_kill_server():
    signal.signal(signal.SIGTERM, bus.interrupted_process)
    signal.signal(signal.SIGINT, bus.interrupted_process)
    signal.signal(signal.SIGQUIT, bus.interrupted_process)
    signal.signal(signal.SIGHUP, bus.interrupted_process)


@bus.handle('test-topic')
def test_topic_handler(msg):
    print('consumed {} from test-topic'.format(msg))


if __name__ == '__main__':
    bus.run()
    listen_kill_server()
    app.run(debug=True, port=5004)
