# from confluent_kafka import Consumer
# from app.model.employee import Employee
#
#
# def create_consumer():
#     consumer = Consumer({
#         'bootstrap.servers': 'localhost:9092',  # Kafka broker address
#         'group.id': 'flask-consumer-group',
#         'auto.offset.reset': 'earliest',
#         'value.deserializer': 'org.apache.kafka.common.serialization.StringDeserializer'  # Example value deserializer
#     })
#     return consumer
#
#
# def consume_messages():
#     consumer = create_consumer()
#     for message in consumer:
#         print(message)
#
#         dataset = message.json
#         new_e = Employee(
#             username=dataset['username'],
#             email=dataset['email'],
#             phone_number=dataset['phone_number']
#         )
#         print(new_e.username)
#
#         # try:
#         #     dataset = message.value
#         #     try:
#         #         # Create a new Employee object
#         #         new_employee = Employee(
#         #             username=dataset['username'],
#         #             email=dataset['email'],
#         #             phone_number=dataset['phone_number']
#         #         )
#         #
#         #         # Add to session and commit
#         #         db.session.add(new_employee)
#         #         db.session.commit()
#         #
#         #     except SQLAlchemyError as e:
#         #         db.session.rollback()  # Rollback the transaction in case of an error
#         #         print(f"Database error: {str(e)}")
#         # except Exception as e:
#         #     print(f"Error in Kafka consumer: {str(e)}")
#         # finally:
#         # # Close the database session when done or on an error
#         #     db.session.close()
#
