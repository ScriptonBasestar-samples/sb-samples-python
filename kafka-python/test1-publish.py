from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

for _ in range(100):
    producer.send('my-topic', b'some_message_bytes')
    producer.flush()
