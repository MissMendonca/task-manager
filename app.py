import os
from os import path
if path.exists("env.py"):
    import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONDO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo= PyMongo(app)

@app.route('/')
@app.route('/tasks')
def tasks():
    return render_template("tasks.html", tasks = mongo.db.tasks.find())

if __name__ == "__main__":
    app.run(host = os.getenv("IP", "0.0.0.0"),
        port= int(os.getenv("PORT", "5000")),
        debug= True)