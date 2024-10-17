import cv2,imutils, socket
import numpy as np
import time
import base64
from ultralytics import YOLO
import json
model = YOLO("yolov8l.pt")
BUFF_SIZE = 65536
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host_name = socket.gethostname()
host_ip = '192.168.31.109' #socket.gethostbyname(host_name)
print(host_ip)
port = 9999

next_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
next_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host2_name = socket.gethostname()
host2_ip = '192.168.31.116'
message = b'Hello World!'
client_socket.sendto(message, (host_ip, port))

while True:
    packet, client_address = client_socket.recvfrom(BUFF_SIZE)
    data= base64.b64decode(packet,' /')
    npdata = np.fromstring(data,dtype=np.uint8)
    frame = cv2.imdecode(npdata,1)
    cv2.imshow('frame', frame)
    results = model.predict(source=frame,
                            show=True, verbose=False)
    # _, img_encoded = cv2.imencode('.jpg', results[0].orig_img)
    # d = {
    #     "boxes": results[0].boxes.data.cpu().numpy().tolist(),
    # }
    # msg, client_addr = next_socket.recvfrom(BUFF_SIZE)
    # next_socket.sendto(json.dumps(d).encode(), client_addr)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break