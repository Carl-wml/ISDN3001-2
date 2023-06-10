import socket
import threading
import cv2
import numpy as np
import mss

class videoServer:

    def __init__(self, port, encoding_format=cv2.IMWRITE_JPEG_QUALITY, quality=50, frame_size=(1360, 768)) -> None:
        #image encoding parameters
        self.encoding_format = encoding_format
        self.quality = quality
        self.frame_size = frame_size

        self.port = port
        self.myHostName = socket.gethostname()
        self.IPAddr = socket.gethostbyname(self.myHostName)
        self.client_address = None

        print("Server Name is:"+ self.myHostName)
        print("Server IP Address is:"+self.IPAddr) 
        print("Server Port is:"+ str(port))
        
        self.server_address = (self.IPAddr, self.port)

        # # create a UDP socket
        # self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # # bind the socket to a specific IP address and port number
        # self.udp_socket.bind(self.server_address)

        # create a TCP socket
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind the socket to a specific IP address and port number
        self.tcp_socket.bind(self.server_address)

        # listen for incoming connections
        self.tcp_socket.listen()
        self.conn, self.client_address = self.tcp_socket.accept()


        self.stop_event_in = threading.Event()
        self.thread_in = threading.Thread(target=self.thread_in, args=(self.stop_event_in,))

        self.stop_event_out = threading.Event()
        self.thread_out = threading.Thread(target=self.thread_out, args=(self.stop_event_out,))


    def thread_in(self,stop_event):
        while not stop_event.is_set():
            try:
                frame = self.conn.recv(2100400)
                # decode and play the video data
                img = np.frombuffer(frame, dtype=np.uint8)
                # Decode the image
                img = cv2.imdecode(img, cv2.IMREAD_COLOR)
                # Display the image in a window
                # img = cv2.resize(img, (400,300))
                cv2.imshow("Screen Sharing (From Client)", img)
                if cv2.waitKey(1) == ord("q"):
                    break
            except:
                pass
        print("Thread stopped.")
        try:
            cv2.destroyAllWindows()
        except:
            pass
 
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
                        self.conn.sendall(jpeg_img.tobytes())
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
    def SetclientAddress(self, client_address):
        self.client_address = client_address


# to use !!!!!
# vs = videoServer(5000)
# vs.in_start()
# vs.SetclientAddress('10.89.178.153')
# vs.out_start()
# vs.out_pause()
# vs.in_pause()