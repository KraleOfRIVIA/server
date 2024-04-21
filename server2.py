import socket
import json
import cv2
import numpy as np

object_names = {
    "0": "person", "1": "bicycle", "2": "car", "3": "motorcycle", "4": "airplane",
    "5": "bus", "6": "train", "7": "truck", "8": "boat", "9": "traffic light",
    "10": "fire hydrant", "11": "stop sign", "12": "parking meter", "13": "bench",
    "14": "bird", "15": "cat", "16": "dog", "17": "horse", "18": "sheep", "19": "cow",
    "20": "elephant", "21": "bear", "22": "zebra", "23": "giraffe", "24": "backpack",
    "25": "umbrella", "26": "handbag", "27": "tie", "28": "suitcase", "29": "frisbee",
    "30": "skis", "31": "snowboard", "32": "sports ball", "33": "kite", "34": "baseball bat",
    "35": "baseball glove", "36": "skateboard", "37": "surfboard", "38": "tennis racket",
    "39": "bottle", "40": "wine glass", "41": "cup", "42": "fork", "43": "knife", "44": "spoon",
    "45": "bowl", "46": "banana", "47": "apple", "48": "sandwich", "49": "orange", "50": "broccoli",
    "51": "carrot", "52": "hot dog", "53": "pizza", "54": "donut", "55": "cake", "56": "chair",
    "57": "couch", "58": "potted plant", "59": "bed", "60": "dining table", "61": "toilet",
    "62": "tv", "63": "laptop", "64": "mouse", "65": "remote", "66": "keyboard", "67": "cell phone",
    "68": "microwave", "69": "oven", "70": "toaster", "71": "sink", "72": "refrigerator", "73": "book",
    "74": "clock", "75": "vase", "76": "scissors", "77": "teddy bear", "78": "hair drier", "79": "toothbrush"
}

HOST = '127.0.0.1'
PORT = 5001

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soc.bind((HOST, PORT))
soc.listen()
client_socket, client_address = soc.accept()
print("connected")
while True:
    data = client_socket.recv(10000000)
    try:
        data = json.loads(data.decode("utf-8"))
    except:
        continue

    img = cv2.imdecode(np.frombuffer(bytes(data["orig_img"]), dtype=np.uint8), cv2.IMREAD_COLOR)
    for box in data["boxes"]:
        x, y, w, h, confidence, object_key = box
        x, y, w, h = int(x), int(y), int(w), int(h)
        object_name = object_names.get(str(int(object_key)), "Unknown")
        cv2.rectangle(img, (x, y), (w,h), (int(object_key)*2, 255 - int(object_key)*2, int(object_key)), 2)
        cv2.putText(img, f"{object_name}: {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (int(object_key)*2, 255 - int(object_key)*2, int(object_key)), 2)
    cv2.imshow("Image with Boxes", img)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()