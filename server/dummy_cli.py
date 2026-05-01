import requests
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

SERVER = "http://127.0.0.1:5000"
user_id = "user123"

# generate key pair
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

public_key = private_key.public_key()

public_pem = public_key.public_bytes(
    Encoding.PEM, PublicFormat.SubjectPublicKeyInfo
).decode()

# register
requests.post(SERVER + "/register", json={"user_id": user_id, "public_key": public_pem})

# request challenge
r = requests.post(SERVER + "/challenge", json={"user_id": user_id})

challenge = r.json()["challenge"]

# sign challenge
signature = private_key.sign(challenge.encode(), padding.PKCS1v15(), hashes.SHA256())

# login
r = requests.post(
    SERVER + "/login", json={"user_id": user_id, "signature": signature.hex()}
)

print(r.json())
