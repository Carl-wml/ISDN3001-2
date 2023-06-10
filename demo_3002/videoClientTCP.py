import socket
import threading
import cv2
import numpy as np
import mss


class videoClient:
    # Set the maximum packet size to 65507 bytes
    # MAX_PACKET_SIZE = 65507
    num_packets = 16


    def __init__(self, serveraddress, port, encoding_format=cv2.IMWRITE_JPEG_QUALITY, quality=70, frame_size=(1360, 768)) -> None:
        # image encoding parameters
        self.encoding_format = encoding_format
        self.quality = quality
        self.frame_size = frame_size

        self.port = port
        self.myHostName = socket.gethostname()
        self.IPAddr = socket.gethostbyname(self.myHostName)
        self.client_address = None
        self.serveraddress = serveraddress

        print("Client Name is:"+ self.myHostName)
        print("Client IP Address is:"+self.IPAddr) 
        print("Server IP Address is:"+self.serveraddress)
        print("Server Port is:"+ str(self.port))

        self.server_address = (self.serveraddress, self.port)

        # # create a UDP socket
        # self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # # # bind the socket to a specific IP address and port number
        # # self.udp_socket.bind(self.server_address)

        # create a TCP socket
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.tcp_socket.connect(self.server_address)

        self.stop_event_in = threading.Event()
        self.thread_in = threading.Thread(target=self.thread_in, args=(self.stop_event_in,))

        self.stop_event_out = threading.Event()
        self.thread_out = threading.Thread(target=self.thread_out, args=(self.stop_event_out,))

        self.window_open = False  # flag to track whether the window is open or closed

    def thread_in(self, stop_event):
        while not stop_event.is_set():
            try:
                frame = self.tcp_socket.recv(65507)
                img = np.frombuffer(frame, dtype=np.uint8)
                img = cv2.imdecode(img, cv2.IMREAD_COLOR)
                cv2.imshow("Screen Sharing (From Server)", img)
                if cv2.waitKey(1) == ord("q"):
                    break
            except:
                pass

        print("Thread stopped.")

    def thread_out(self,stop_event):
        imageCounter = 0
        with mss.mss() as sct:
            while not stop_event.is_set():
                # print('out')
                imageCounter += 1
                try:    
                    sct_img = sct.grab(sct.monitors[1])
                    img = np.array(sct_img)
                    img = cv2.resize(img, self.frame_size)
                    _, jpeg_img = cv2.imencode(".jpg", img, [self.encoding_format, self.quality])
                    if imageCounter % 3 == 0:
                        self.tcp_socket.sendall(jpeg_img.tobytes())
                except:
                    pass
        print("Thread stopped.")


    def in_start(self):
        self.thread_in.start()

    def in_pause(self):
        self.stop_event_in.set()

    def out_start(self):
        self.thread_out.start()

    def out_pause(self):
        self.stop_event_out.set()

    def get_IPAddr_port(self):
        return self.IPAddr, self.port

# to use !!!!!
# vs = videoClient('192.168.0.11',5000)
# vs.in_start()
# vs.out_start()
# vs.out_pause()
# vs.in_pause()
