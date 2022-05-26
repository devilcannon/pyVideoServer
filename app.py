# save this as app.py
import os
from flask import Flask, render_template

app = Flask(__name__, static_folder='static')


@app.route("/")
def hello():
    filenames = os.listdir('./static/')
    return render_template('index.html', files=filenames)
