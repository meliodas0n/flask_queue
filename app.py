#!/usr/bin/python3

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import config
import requests
import os
import operator


app = Flask(__name__)
app.config.from_object(config.APP_SETTINGS)

@app.route("/", methods = ['GET', 'POST'])
def home():
  errors = []
  results = {}
  if request.method == "POST":
    try:
      url = request.form['url']
      r = requests.get(url)
      print(r.text)
    except:
      errors.append("Unable to get URL. Please make sure it's valid and try again...")
  return render_template("home.html", errors = errors, results = results)

if __name__ == "__main__":
  app.run(host = config.HOST, port = config.PORT, debug = True, threaded = True)
