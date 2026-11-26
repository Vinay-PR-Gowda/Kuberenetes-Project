import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "v1")

PRODUCTS = [
    {"id": 1, "name": "Cotton Kurti", "price": 399},
    {"id": 2, "name": "Running Shoes", "price": 799},
    {"id": 3, "name": "Phone Cover", "price": 149},
]

@app.route("/")
def home():
    return jsonify(message="Welcome to Meesho App", version=VERSION, pod=socket.gethostname())

@app.route("/products")
def products():
    return jsonify(PRODUCTS)

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

@app.route("/cpu")
def cpu():
    total = 0
    for i in range(2_000_000):
        total += i * i
    return jsonify(done=True)

@app.route("/crash")
def crash():
    os._exit(1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
