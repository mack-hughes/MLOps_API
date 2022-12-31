from flask import Flask
from textblob import TextBlob

app = Flask("__name__")

@app.route('/')
def home():
    return "My first API"

@app.route("/felling/<phrase>")
def felling(phrase):
    text_blob = TextBlob(phrase)
    return f"the phase polarization is: {text_blob.sentiment.polarity}"

app.run(debug=True)
