#!/usr/bin/env python3

from flask import Flask
import os
app = Flask(__name__)


@app.route("/")
def hello():
    hostname = os.getenv('HOSTNAME')
    return f"I am: {hostname}\n"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
