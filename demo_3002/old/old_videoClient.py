import cv2
import zmq
import mss
import numpy as np
import threading
import socket

class ScreenSharingServer:

    def __init__(self, serveraddress, port):
        self.port = port
        self.myHostName = socket.gethostname()
        self.IPAddr = socket.gethostbyname(self.myHostName)
        self.client_address = None

        print("Client Name is:"+ self.myHostName)
        print("Client IP Address is:"+self.IPAddr) 
        print()
        print("Server Name is:"+ serveraddress)
        self.server_address = (serveraddress, port)

        # create a UDP socket
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        self.context = zmq.Context()
        self.socket_in = self.context.socket(zmq.SUB)
        self.socket_in.bind(f"tcp://*:{self.port}")
        self.socket_in.setsockopt_string(zmq.SUBSCRIBE, np.unicode_(''))
        self.socket_out = self.context.socket(zmq.PUB)
        self.stop_event = threading.Event()
        self.thread_in = threading.Thread(target=self.receive_frames, args=(self.stop_event,))
        self.thread_out = threading.Thread(target=self.send_frames, args=(self.stop_event,))

    def receive_frames(self, stop_event):
        cv2.namedWindow("Screen Sharing (Server)", cv2.WINDOW_NORMAL)
        while not stop_event.is_set():
            # Receive the frame over the input socket
            frame = self.socket_in.recv()
            # Convert the frame to a NumPy array
            img = np.frombuffer(frame, dtype=np.uint8)
            # Decode the image
            img = cv2.imdecode(img, cv2.IMREAD_COLOR)
            # Display the image in a window
            cv2.imshow("Screen Sharing (Server)", img)
            if cv2.waitKey(1) == ord("q"):
                break
        cv2.destroyAllWindows()

    def send_frames(self, stop_event):
        with mss.mss() as sct:
            while not stop_event.is_set():
                # Capture the screen
                sct_img = sct.grab(sct.monitors[1])
                img = np.array(sct_img)

                # Send the frame over the output socket
                self.socket_out.send(img.tobytes())
    
    def start(self):
        self.thread_in.start()
        self.thread_out.start()

    def pause(self):
        self.stop_event.set()

    def resume(self):
        self.stop_event.clear()

    def stop(self):
        self.stop_event.set()
        self.thread_in.join()
        self.thread_out.join()

class ScreenSharingClient:

    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port_in = port
        self.port_out = port + 1
        self.context = zmq.Context()
        self.socket_in = self.context.socket(zmq.SUB)
        self.socket_in.connect(f"tcp://{self.ip_address}:{self.port_in}")
        self.socket_in.setsockopt_string(zmq.SUBSCRIBE, np.unicode_(''))
        self.socket_out = self.context.socket(zmq.PUB)
        self.socket_out.bind(f"tcp://*:{self.port_out}")
        self.stop_event = threading.Event()
        self.thread_in = threading.Thread(target=self.receive_frames, args=(self.stop_event,))
        self.thread_out = threading.Thread(target=self.send_frames, args=(self.stop_event,))

    def receive_frames(self, stop_event):
        cv2.namedWindow("Screen Sharing (Client)", cv2.WINDOW_NORMAL)
        while not stop_event.is_set():
            # Receive the frame over the input socket
            frame = self.socket_in.recv()
            # Convert the frame to a NumPy array
            img = np.frombuffer(frame, dtype=np.uint8)
            # Decode the image
            img = cv2.imdecode(img, cv2.IMREAD_COLOR)
            # Display the image in a window
            cv2.imshow("Screen Sharing (Client)", img)
            if cv2.waitKey(1) == ord("q"):
                break
        cv2.destroyAllWindows()

    def send_frames(self, stop_event):
        cap = cv2.VideoCapture(0)
        while not stop_event.is_set():
            # Capture a frame from the webcam
            ret, frame = cap.read()
            if not ret:
                break
            # Send the frame over the output socket
            self.socket_out.send(frame.tobytes())
    
    def start(self):
        self.thread_in.start()
        self.thread_out.start()

    def pause(self):
        self.stop_event.set()

    def resume(self):
        self.stop_event.clear()

    def stop(self):
        self.stop_event.set()
        self.thread_in.join()
        self.thread_out.join()

if __name__ == '__main__':
    # server = ScreenSharingServer(5000)
    client = ScreenSharingClient("localhost", 5000)
    # server.start()
    client.start()