# project/config.py
import os
import logging
from pickle import TRUE
from dotenv import load_dotenv
load_dotenv()
class BaseConfig:
    """Base configuration"""
    DEBUG = True
    TESTING = True
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'flask-base.log'
    LOGGING_LEVEL = logging.DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    DB_NAME=os.getenv('DB_NAME')
    DB_PASSWORD=os.getenv('DB_PASSWORD')
    DB_HOST=os.getenv('DB_HOST')
    DB_DOCKER_HOST=os.getenv('DB_DOCKER_HOST')
    BCRYPT_LOG_ROUNDS = 13
    TOKEN_EXPIRATION_DAYS = 30
    TOKEN_EXPIRATION_SECONDS = 0
    TOKEN_PASSWORD_EXPIRATION_DAYS = 1
    TOKEN_PASSWORD_EXPIRATION_SECONDS = 0
    SENTRY_DSN = 'Sentry_DNS'
    FCM_SERVER_KEY = os.environ.get('FCM_SERVER_KEY')
    CACHE_REDIS_HOST="localhost"
    CACHE_REDIS_PORT=6379
    CACHE_REDIS_URL='redis://localhost:6379'

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG =True
    TESTING=True
    ENV='development'
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{BaseConfig.DB_NAME}:{BaseConfig.DB_PASSWORD}@{BaseConfig.DB_HOST}/employees"
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_BROKER_URL')
    BCRYPT_LOG_ROUNDS = 4

class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{BaseConfig.DB_NAME}:{BaseConfig.DB_PASSWORD}@{BaseConfig.DB_HOST}/employees"
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_TEST_URL')
    CELERY_TASK_ALWAYS_EAGER = True
    BCRYPT_LOG_ROUNDS = 4
    TOKEN_EXPIRATION_DAYS = 0
    TOKEN_EXPIRATION_SECONDS = 3


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{BaseConfig.DB_NAME}:{BaseConfig.DB_PASSWORD}@{BaseConfig.DB_HOST}/employees"
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
    SENTRY_DSN = 'Sentry_DNS'
class DockerConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{BaseConfig.DB_NAME}:{BaseConfig.DB_PASSWORD}@{BaseConfig.DB_DOCKER_HOST}/employees"
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
    SENTRY_DSN = 'Sentry_DNS'

config_by_name= dict(
    dev= DevelopmentConfig,
    test= TestingConfig,
    prod= ProductionConfig,
    docker=DockerConfig
)