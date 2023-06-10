import mss
import socket
import numpy as np
import cv2

WINDOW_TITLE_SERVER = "Screen Sharing (Server)"
WINDOW_TITLE_CLIENT = "Screen Sharing (Client)"
ENCODING_FORMAT = cv2.IMREAD_COLOR


cv2.namedWindow(WINDOW_TITLE_SERVER, cv2.WINDOW_NORMAL)
with mss.mss() as sct:         
    while True:
        # Capture the screen
        # sct_img = sct.grab(sct.monitors[1])
        # img = np.array(sct_img)

        # Capture the screen
        sct_img = sct.grab(sct.monitors[1])
        img = np.array(sct_img)

        # Resize the image to 360x640 and reduce the frame rate to 15fps
        img = cv2.resize(img, (1080, 960))

        # Compress the image using JPEG compression
        _, jpeg_img = cv2.imencode(".jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 70])

                # Send the compressed frame over the output socket
        jpeg_img.tobytes()
        
        img = np.frombuffer(jpeg_img, dtype=np.uint8)
        # Decode the image
        img = cv2.imdecode(img, ENCODING_FORMAT)
        # Display the image in a window
        cv2.imshow(WINDOW_TITLE_CLIENT, img)
        if cv2.waitKeyEx(1) == ord("q"):
            break

        # cv2.imshow(WINDOW_TITLE_SERVER, img)
        # if cv2.waitKeyEx(1) == ord("q"):
        #     break