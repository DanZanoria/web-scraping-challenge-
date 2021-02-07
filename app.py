import pandas as pd

from sqlalchemy import create_engine
from flask import Flask, render_template, redirect

#################################################
# Flask Setup
#################################################
mdamon = Flask(__name__)

#################################################
# Flask Routes
#################################################

@mdamon.route('/')
def home():
    return render_template("index.html")











if __name__ == "__main__":
    mdamon.run(debug = True)