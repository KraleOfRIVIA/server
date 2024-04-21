import socket
import json
import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("yolov8l.pt")
HOST = '127.0.0.1'
PORT = 5000

HOST2 = '127.0.0.1'
PORT2 = 5001

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soc.bind((HOST, PORT))
soc.listen()
client_socket, client_address = soc.accept()
soc2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soc2.connect((HOST2, PORT2))
print("connected")
while True:
    data = client_socket.recv(500000)
    img = cv2.imdecode(np.frombuffer(data, dtype=np.uint8), cv2.IMREAD_COLOR)
    if img is not None:
        results = model.predict(source=img,
                                show=False, verbose=False)
        _, img_encoded = cv2.imencode('.png', results[0].orig_img)
        d = {
            "boxes": results[0].boxes.data.cpu().numpy().tolist(),
            "orig_img": list(img_encoded.tobytes())
        }
        soc2.send(json.dumps(d).encode())
