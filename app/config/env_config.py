class Config:
    # General Configurations
    DB_NAME = 'PythonConnect'
    DB_USER_NAME = 'postgres'
    DB_PASSWORD = 'admin'
    DB_HOST = 'localhost'

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER_NAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/mydatabase_dev'
    PORT = 5000


class StagingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/mydatabase_test'
    PORT = 5002


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/mydatabase_prod'
    PORT = 5003


config = {
    'dev': DevelopmentConfig,
    'stage': StagingConfig,
    'prod': ProductionConfig
}
