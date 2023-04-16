import json
import socket

data = {'datetime':'2023-04-14 03:14:40','temp': 30, 'humi': 56, 'node_id': 'fc:69:47:c:2d:65', 'device': 'Mobile'}
data_str = json.dumps(data)

HOST = '172.26.43.17'  # loopback address
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(data_str.encode())
