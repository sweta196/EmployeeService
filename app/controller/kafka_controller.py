# from flask import Blueprint, request, jsonify
# from app.producer.kafka_producer import create_producer, produce_messages
#
# kafka_bp = Blueprint('kafka', __name__)
#
#
# @kafka_bp.route('/produce', methods=['POST'])
# def produce_datasets():
#     data = request.json
#     if not isinstance(data, dict) or not data.get('username') or not data.get('email') or not data.get('phone_number'):
#         return jsonify({"error": "Invalid input. Please send a dataset with 'username', 'email', and 'phone_number'."}),\
#                400
#
#     producer = create_producer()
#     produce_messages(producer, data)
#
#     return jsonify({"message": "50 datasets produced to Kafka based on the provided dataset!"})
