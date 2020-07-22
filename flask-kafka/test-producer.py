import kafka

producer = kafka.KafkaProducer(bootstrap_servers=','.join(['localhost:9092', 'localhost:9093', 'localhost:9094']))
for i in range(1000):
    # producer.send('test-topic', b'send_message_bytes')
    producer.send('test-topic', bytearray(F'send_message_bytes - {i}'.encode()))
    print(F'test {i}')
