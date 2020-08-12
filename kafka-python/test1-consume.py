import kafka

consumer = kafka.KafkaConsumer('my_favorite_topic')
for msg in consumer:
    print(msg)
