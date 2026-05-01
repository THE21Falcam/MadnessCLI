import os

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}
challenges = {}


@app.route("/register", methods=["POST"])
def register():
    data = request.json
    user_id = data["user_id"]
    public_key = data["public_key"]

    users[user_id] = public_key
    return jsonify({"status": "registered"})


@app.route("/challenge", methods=["POST"])
def challenge():
    data = request.json
    user_id = data["user_id"]

    if user_id not in users:
        return jsonify({"error": "user not found"}), 404

    challenge = os.urandom(32).hex()
    challenges[user_id] = challenge

    return jsonify({"challenge": challenge})


@app.route("/login", methods=["POST"])
def login():

    data = request.json
    user_id = data["user_id"]
    signature = bytes.fromhex(data["signature"])

    challenge = challenges.get(user_id)

    if not challenge:
        return jsonify({"error": "no challenge"}), 400

    public_key_pem = users[user_id].encode()
    public_key = load_pem_public_key(public_key_pem)

    try:
        public_key.verify(
            signature, challenge.encode(), padding.PKCS1v15(), hashes.SHA256()
        )
        return jsonify({"status": "login successful"})
    except:
        return jsonify({"status": "login failed"})


if __name__ == "__main__":
    app.run(port=5000)
