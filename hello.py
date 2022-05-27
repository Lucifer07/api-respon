from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import random
import nltk
from flask import abort, Flask, jsonify, redirect, request, url_for
import json
nltk.download('punkt')
nltk.download('omw-1.4')
nltk.download('wordnet')
f = open('data.txt', 'r', errors='ignore')
raw = f.read()
raw = raw.lower()
sentence_list = nltk.sent_tokenize(raw)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! Deploy nich...</p>"

@app.route("/works")
def it_works():
    return "IT Works! nyehehe"