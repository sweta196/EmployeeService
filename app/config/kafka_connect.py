# from kafka import KafkaConsumer
# import threading
#
#
# def consume_messages():
#     consumer = KafkaConsumer(
#         'test',
#         bootstrap_servers='localhost:9092',
#         auto_offset_reset='latest'
#     )
#     for message in consumer:
#         print(f"Consumed message: {message.value.decode('utf-8')}")
#
#
# def start_kafka_consumer():
#     consumer_thread = threading.Thread(target=consume_messages)
#     consumer_thread.daemon = True
#     consumer_thread.start()
