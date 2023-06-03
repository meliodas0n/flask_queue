import os
basedir = os.path.abspath(os.path.dirname(__file__))

HOST = "127.0.0.1"
PORT = 5123

class Config:
  DEBUG = False
  DEVELOPMENT = False
  THREADED = True
  SECRET_KEY = "queuework"
  SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
  
class ProductionConfig(Config):
  DEBUG = False

class DevelopmentConfig(Config):
  DEBUG = True
  DEVELOPMENT = True