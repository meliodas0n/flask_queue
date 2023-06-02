#!/usr/bin/python3

from flask import Flask, request, render_template
import os
import config

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")
def home():
  secret_key = app.config.get("SECRET_KEY")
  return render_template("home.html", secret = secret_key) 

if __name__ == "__main__":
  app.run(host = config.HOST, port = config.PORT, debug = True, threaded = True)
