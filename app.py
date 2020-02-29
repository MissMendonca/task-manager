import os
from os import path
if path.exists("env.py"):
    import env
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONDO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo= PyMongo(app)

@app.route('/')
def home():
    return "<h1>Homepage</h1>"

if __name__ == "__main__":
    app.run(host = os.getenv("IP", "0.0.0.0"),
        port= int(os.getenv("PORT", "5000")),
        debug= True)