# import necessary libraries
from flask_pymongo import PyMongo
import reddit_scrape
from flask import Flask, render_template, jsonify, request, redirect


app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://jdouangs:spunky33@ds125453.mlab.com:25453/redditanalysis'
mongo = PyMongo(app)
#conn = MongoClient("ds125453.mlab.com", 25453)
#db = conn["redditanalysis"]
#client = pymongo.MongoClient(conn)
#db.authenticate('jdouangs', 'spunky33')
#db = client.redditanalysis

@app.route("/")
def home():
    reddit_data = mongo.db.redditdata.find()
    print(reddit_data)
    return render_template("index.html", reddit_data = reddit_data)

@app.route("/scrape/<choice>", methods=['GET', 'POST'])
def scrape(choice):
    mongo.db.redditdata.drop()
    scraped_data = reddit_scrape.scrape(choice)
    master = scraped_data[0]
    mongo.db.redditdata.insert_many(master)
    return redirect("/", code=302)

if __name__ == '__main__':
    app.run(debug=True)