import os
import time
import numpy as np
import cv2

import socket
import threading
import requests
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "172.16.16.84"
port = 6969

sock.connect((ip, port))
image = b""

def show():
    global image
    while True:
        if (len(image) < 360165):
            continue
        img = pickle.loads(image)
        cv2.imshow("lol", img)
        cv2.waitKey(1)

threading.Thread(target=show).start()

while (True):

    data = sock.recv(400000)
    if (data):
        if (len(image) >= 360165):
            print(len(image))
            #img = pickle.loads(image)
            #cv2.imshow("lol", img)
            image = b""
        image = image + data

sock.close()



