#!/usr/bin/python3

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import config

app = Flask(__name__)
app.config.from_object(config.APP_SETTINGS)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/", methods = ['GET', 'POST'])
def home():
  return render_template("home.html")

if __name__ == "__main__":
  app.run(host = config.HOST, port = config.PORT, debug = True, threaded = True)
