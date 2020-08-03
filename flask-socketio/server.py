import functools

from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, join_room, send, leave_room, emit
from kombu import Queue, Consumer, Connection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")


def authenticated_only(f):
    pass


#     @functools.wraps(f)
#     def wrapped(*args, **kwargs):
#         if not current_user.is_authenticated:
#             disconnect()
#         else:
#             return f(*args, **kwargs)
#     return wrapped

@socketio.on('connect')
def test_connect():
    emit('message', {'data': 'Connected'})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', room=room)


@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)


@socketio.on('identify')
def handle_message(message):
    print('received message: ' + message)


@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


@socketio.on('my event')
def handle_my_custom_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)


# listen rabbitmq
queue = Queue('data_feed', routing_key='data_feed.data1')
with Connection('amqp://') as conn:
    with conn.channel() as channel:
        consumer = Consumer(channel, queue)


        def callback(body, message):
            print(body)
            emit('data_feed', body)
            message.ack()


        consumer.register_callback(callback)

if __name__ == '__main__':
    socketio.run(app)
