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
from rq import Queue
from rq.job import Job
from worker import conn

app = Flask(__name__)
app.config.from_object(config.APP_SETTINGS)
result_file = 'result.json'

q = Queue(connection = conn)

def count_and_save_words(url):
  errors = []
  try:
    r = requests.get(url)
  except:
    errors.append("Unable to get URL")
    return {"error" : errors}
  
  raw = BeautifulSoup(r.text).get_text()
  nltk.data.path.append('./nltk_data/')
  tokens = nltk.word_tokenize(raw)
  text = nltk.Text(tokens)
  nonPunct = re.compile('.*[A-Za-z].*')
  raw_words = [w for w in text if nonPunct.match(w)]
  # raw_word_count = Counter(raw_words)
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

@app.route("/results/<job_key>", methods = ['GET'])
def get_results(job_key):
  job = Job.fetch(job_key, connection = conn)
  if job.is_finished:
    return str(job.result), 200
  else:
    return "Nay!", 202

@app.route("/", methods = ['GET', 'POST'])
def home():
  results = {}
  if request.method == "POST":
    url = request.form['url']
    if not url[:8].startswith(('https://', 'http://')):
      url = 'http://' + url
    job = q.enqueue_call(
      func = count_and_save_words, args = (url, ), result_ttl = 5000
    )
    print(job.get_id())
  return render_template("home.html", results = results)

if __name__ == "__main__":
  app.run(host = config.HOST, port = config.PORT, debug = True, threaded = True)
