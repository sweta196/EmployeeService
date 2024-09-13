from datetime import timedelta
import os
from flask import Flask
from flask_jwt_extended import JWTManager
from app.config import env_config
from app.config.env_config import Config
from app.factory.db_factory import db
from app.factory.marshmallow_factory import ma
# from app.consumer.kafka_consumer import consume_messages
import threading


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)

    # Setup the Flask-JWT-Extended extension
    app.config['JWT_SECRET_KEY'] = 'secret_key'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(hours=1)
    # Change this to a random secret key
    jwt = JWTManager(app)

    with app.app_context():
        db.create_all()

    # def start_consumer():
    #     consume_messages()
    #
    # consumer_thread = threading.Thread(target=start_consumer, daemon=True)
    # consumer_thread.start()

    # env = os.getenv('FLASK_ENV', 'stage')
    # print(f"EmployeeService app running on {env}")
    # app.config.from_object(env_config.config[env])

    return app
