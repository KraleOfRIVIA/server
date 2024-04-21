import socket

import cv2

HOST = '127.0.0.1'
PORT = 5000

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soc.connect((HOST, PORT))
print("connected")
while True:
    ret, img = cap.read()
    _, img_encoded = cv2.imencode('.png', img)
    soc.send(img_encoded.tobytes())

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()