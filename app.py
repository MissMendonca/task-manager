import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Homepage</h1>"

if __name__ == "__main__":
    app.run(host = os.getenv("IP", "0.0.0.0"),
        port= int(os.getenv("PORT", "5000")),
        debug= True)