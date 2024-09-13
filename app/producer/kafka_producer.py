# from confluent_kafka import Producer
#
# from app.config.kafka_topic import Config
# from app.model.employee import Employee
#
#
# def create_producer():
#     producer = Producer({
#         'bootstrap.servers': 'localhost:9092',  # Kafka broker address
#         'client.id': 'flask-app',  # Custom key serializer
#         'value.serializer': 'org.apache.kafka.common.serialization.StringSerializer'
#     })
#     return producer
#
#
# def generate_datasets(base_dataset):
#     datasets = []
#     for i in range(1, 51):
#         employee = Employee(
#             username=f"{base_dataset['username']}{i}",
#             password=f"{base_dataset['password']}{i}",
#             first_name=f"{base_dataset['first_name']}{i}",
#             last_name=f"{base_dataset['first_name']}{i}",
#             hire_date=f"{base_dataset['hire_date']}",
#             department=f"{base_dataset['department']}{i}",
#             position=f"{base_dataset['position']}{i}",
#             salary=f"{base_dataset['salary']}{i}",
#             email=f"{base_dataset['email'].split('@')[0]}{i}@{base_dataset['email'].split('@')[1]}",
#             phone_number=str(int(base_dataset['phone_number']) + i)  # Increment mobile number
#         )
#         datasets.append(employee)
#
#     print(len(datasets))
#     return datasets
#
#
# def produce_messages(producer, base_dataset):
#     datasets = generate_datasets(base_dataset)
#     for emp in datasets:
#         producer.send(Config.KAFKA_TOPIC, emp)
#     producer.flush()
