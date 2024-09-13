from sqlalchemy import create_engine

from app.config.env_config import Config


def connect_db():
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    return engine
