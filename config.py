import os
basedir = os.path.abspath(os.path.dirname(__file__))

HOST = "127.0.0.1"
PORT = 5123
APP_SETTINGS="config.DevelopmentConfig"

class Config:
  DEBUG = False
  DEVELOPMENT = False
  THREADED = True
  SECRET_KEY = "queuework"
  
class ProductionConfig(Config):
  DEBUG = False

class DevelopmentConfig(Config):
  DEBUG = True
  DEVELOPMENT = True