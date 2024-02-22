from threading import Thread

from flask import Flask
import requests

app = Flask("")


@app.route("/")
def home():
    return "I'm alive"


@app.route("/iot", methods=["GET"])
def arduino():
    return "iot_alive"


def run():
    app.run(host="0.0.0.0", port=5000)


def keep_alive():
    t = Thread(target=run)
    t.start()


if __name__ == "__main__":
    keep_alive()
