import socket
from hashlib import sha1
from base64 import b64encode

HOST = "127.0.0.1"
PORT = 5000

GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"

def server(portNumber):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(2048)
                if (data[0:3] == b'GET'):
                    if (data.decode().find("Sec-WebSocket-Key")) != -1:
                        key = (data.decode().split()[(data.decode().split()).index("Sec-WebSocket-Key:") + 1])
                        response_key = b64encode(sha1((key + GUID).encode()).digest())
                        handshake1response = b"HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: " + response_key + b"\r\n\r\n"

                        if (conn.sendall(handshake1response) == None):
                            print(handshake1response)
                            print("Response sent successfully")
                        else:
                            print("Response failed to send")
                elif (data[0:1] == b'\x88' or data == b''):
                    conn.close()
                    break
                else:
                    print(int.from_bytes(data, byteorder='big'))
                if not data:
                    break
                
                # conn.sendall(data)

if __name__ == "__main__":
    server(PORT)