from hashlib import sha1
from base64 import b64encode

key = "dGhlIHNhbXBsZSBub25jZQ=="
GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"

response_key = b64encode(sha1((key + GUID).encode()).digest())

print(response_key)