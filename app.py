#!/usr/bin/python3

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import config
import requests
import os
import operator
import re
from collections import Counter
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import json

app = Flask(__name__)
app.config.from_object(config.APP_SETTINGS)
result_file = 'result.json'

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
    if r:
      raw = BeautifulSoup(r.text, 'html.parser').get_text()
      nltk.data.path.append('./nltk_data/')
      tokens = nltk.word_tokenize(raw)
      text = nltk.Text(tokens)
      nonPunct = re.compile('.*[A-Za-z].*')
      raw_words = [w for w in text if nonPunct.match(w)]
      raw_word_count = Counter(raw_words)
      no_stop_words = [w for w in raw_words if w.lower() not in stopwords.words('english')]
      no_stop_words_count = Counter(no_stop_words)
      results = sorted(
        no_stop_words_count.items(),
        key = operator.itemgetter(1),
        reverse = True
      )[ : 10]
    with open(result_file, 'w') as f:
      json.dump(results, f, indent = 2)
      f.close()      
  return render_template("home.html", errors = errors, results = results)

if __name__ == "__main__":
  app.run(host = config.HOST, port = config.PORT, debug = True, threaded = True)
