import cv2
import socket
import numpy as np
import pyautogui
import mss

class ScreenServer:
    def __init__(self, host='', port=5000, encoding_format=cv2.IMWRITE_JPEG_QUALITY, quality=50, frame_size=(640, 480)):
        self.myHostName = socket.gethostname()
        self.IPAddr = socket.gethostbyname(self.myHostName)
        self.host = self.IPAddr
        self.port = port
        self.encoding_format = encoding_format
        self.quality = quality
        self.frame_size = frame_size
        self.socket = None

    def start(self):
        # Create a socket object
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind the socket to a specific IP address and port
        self.socket.bind((self.host, self.port))

    def send_frame(self):
        # Capture a screenshot of the screen
        screen = pyautogui.screenshot()

        # Convert the screenshot to a NumPy array
        screen = np.array(screen)

        # Resize the screenshot to the desired frame size
        screen = cv2.resize(screen, self.frame_size)

        # Compress the frame using JPEG compression
        _, jpeg_frame = cv2.imencode('.jpg', screen, [self.encoding_format, self.quality])

        # Send the compressed frame to the client
        self.socket.sendto(jpeg_frame.tobytes(), ('<broadcast>', self.port))

    def stop(self):
        # Release the resources
        self.socket.close()

    def test(self):
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
                img = cv2.resize(img, (1920, 1080))

                # Compress the image using JPEG compression
                _, jpeg_img = cv2.imencode(".jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 70])

                        # Send the compressed frame over the output socket
                jpeg_img.tobytes()
                
                img = np.frombuffer(jpeg_img, dtype=np.uint8)
                # Decode the image
                img = cv2.imdecode(img, ENCODING_FORMAT)
                # Display the image in a window
                cv2.imshow(WINDOW_TITLE_CLIENT, img)
                cv2.imshow(WINDOW_TITLE_SERVER, img)
                if cv2.waitKeyEx(1) == ord("q"):
                    break


class ScreenClient:
    def __init__(self, server_ip='', port=5000, buffer_size=65536, window_title='Screen Share'):
        self.myHostName = socket.gethostname()
        self.IPAddr = socket.gethostbyname(self.myHostName)
        self.server_ip = self.IPAddr
        self.port = port
        self.buffer_size = buffer_size
        self.window_title = window_title
        self.socket = None

    def connect(self):
        # Create a socket object
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind the socket to a specific IP address and port
        self.socket.bind((self.server_ip, self.port))

        # Set the socket to non-blocking mode
        self.socket.setblocking(0)

    def receive_frame(self):
        try:
            # Receive a compressed frame from the server
            data, address = self.socket.recvfrom(self.buffer_size)
            jpeg_frame = np.frombuffer(data, dtype=np.uint8)

            # Decompress the frame using JPEG decompression
            frame = cv2.imdecode(jpeg_frame, cv2.IMREAD_COLOR)

            # Display the frame in a window
            cv2.imshow(self.window_title, frame)

            # Check for key press to exit
            if cv2.waitKey(1) == ord('q'):
                return False

        except socket.error:
            pass

        return True

    def disconnect(self):
        # Release the resources
        cv2.destroyAllWindows()
        self.socket.close()

import time

# Create a screen server object and start it
server = ScreenServer()
server.test()

# # Create a screen client object and connect to the server
# client = ScreenClient()
# client.connect()

# # Receive and display frames from the server
# while True:
#     if not client.receive_frame():
#         break
#     server.send_frame()
#     time.sleep(0.01)

# # Disconnect the client and stop the server
# client.disconnect()
# server.stop()