import kafka
import websocket
import time
import json

producer = kafka.KafkaProducer(bootstrap_servers=','.join(['localhost:9092', 'localhost:9093', 'localhost:9094']))


def listen_binance_stream(symbol):
    subscribe = {
        'method': 'SUBSCRIBE',
        'params': [
            F'{symbol}@trade'
        ],
        'id': 2
    }
    return json.dumps(subscribe)


try:
    import thread
except ImportError:
    import _thread as thread


def on_message(ws, message):
    # producer.send('test-topic', bytearray(F'send_message_bytes - {i}'.encode()))
    print(message)
    producer.send('test-topic', bytearray(message.encode()))


def on_error(ws, error):
    print(error)


def on_close(ws):
    print('### closed ###')


def on_open(ws):
    def run(*args):
        ws.send(listen_binance_stream('btcusdt'))
        # for i in range(3):
        #     time.sleep(1)
        #     # ws.send('Hello %d' % i)
        # time.sleep(1)
        # ws.close()
        # print('thread terminating...')

    thread.start_new_thread(run, ())


if __name__ == '__main__':
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp('wss://stream.binance.com/stream',
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
