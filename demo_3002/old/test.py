import socket
import threading
import cv2
import numpy as np
import mss

while True:
    with mss.mss() as sct:
        sct_img = sct.grab(sct.monitors[1])
        img = np.array(sct_img)
        img = cv2.resize(img, (640, 360))
        _, jpeg_img = cv2.imencode(".jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 70])
        jpeg_img = jpeg_img.tobytes()
        img = np.frombuffer(jpeg_img, dtype=np.uint8)
        # img = np.frombuffer(jpeg_img, dtype=np.uint8)
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
        # img = cv2.resize(img, (640, 360))
        cv2.imshow("Screen Sharing (test)", img)
    # img = cv2.resize(img, (640, 360))
    # _, jpeg_img = cv2.imencode(".jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 70])
