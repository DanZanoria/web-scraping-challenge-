import pandas as pd
from flask_pymongo import PyMongo
from sqlalchemy import create_engine
from flask import Flask, render_template, redirect
from scrape_mars import Marsmon

#################################################
# Flask Setup
#################################################
mdamon = Flask(__name__)

#################################################
# Flask Routes
#################################################

@mdamon.route('/')
def home():
    Marsmon = mongo.db.Marsmon.find_one()
    return render_template("index.html")

@app.route("/scrape")
def scrape():
    Marsmon = mongo.db.Marsmon
    FMars = scrape_mars.scrap()
    Marsmon.update({}, Marsmon, upsert= True)
    return render_template("scrape.html")
if __name__ == "__main__":
    mdamon.run(debug = True)