#!/usr/bin/python3

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import config

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/<name>")
def hello_name(name):
  return render_template("home.html", name = name)

if __name__ == "__main__":
  app.run(host = config.HOST, port = config.PORT, debug = True, threaded = True)
