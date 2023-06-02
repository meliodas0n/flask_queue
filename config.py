import os

HOST = "127.0.0.1"
PORT = 5123

class Config:
  DEBUG = False
  DEVELOPMENT = False
  THREADED = True
  SECRET_KEY = os.getenv("SECRET_KEY", "automation")
  
class ProductionConfig(Config):
  pass

class DevelopmentConfig(Config):
  DEBUG = True
  DEVELOPMENT = True