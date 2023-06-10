import socket
import threading
import cv2
import numpy as np
import mss

class videoServer:

    def __init__(self, port, encoding_format=cv2.IMWRITE_JPEG_QUALITY, quality=50, frame_size=(640, 480)) -> None:
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

        # create a UDP socket
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # bind the socket to a specific IP address and port number
        self.udp_socket.bind(self.server_address)

        self.stop_event_in = threading.Event()
        self.thread_in = threading.Thread(target=self.thread_in, args=(self.stop_event_in,))

        self.stop_event_out = threading.Event()
        self.thread_out = threading.Thread(target=self.thread_out, args=(self.stop_event_out,))

    # def split_img(self, img):
    #     # Split the image into its color channels
    #     b, g, r = cv2.split(img)

    #     # Split each color channel into 10 equal parts
    #     num_parts = 10
    #     b_parts = np.array_split(b, num_parts)
    #     g_parts = np.array_split(g, num_parts)
    #     r_parts = np.array_split(r, num_parts)

    #     # Combine the 1st part of each color channel into a new image
    #     new_img = []
    #     for i in range(num_parts):
    #         new_img.append(cv2.merge([b_parts[i], g_parts[i], r_parts[i]]))
    #     return new_img


    # def combine_img(self, img_parts):
    #     # Get the number of parts and dimensions of each part
    #     num_parts = 10
    #     rows, cols, channels = img_parts[0].shape

    #     # Create empty arrays for each color channel
    #     b = np.zeros((rows * num_parts, cols, channels), dtype=np.uint8)
    #     g = np.zeros((rows * num_parts, cols, channels), dtype=np.uint8)
    #     r = np.zeros((rows * num_parts, cols, channels), dtype=np.uint8)

    #     # Fill in each color channel with the corresponding part
    #     for i in range(num_parts):
    #         b[i*rows:(i+1)*rows, :, :] = img_parts[i][:, :, 0:1]
    #         g[i*rows:(i+1)*rows, :, :] = img_parts[i][:, :, 1:2]
    #         r[i*rows:(i+1)*rows, :, :] = img_parts[i][:, :, 2:3]

    #     # Merge the color channels back into a single image
    #     combined_img = cv2.merge([b, g, r])
    #     return combined_img

    def thread_in(self,stop_event):
        while not stop_event.is_set():
            try:
                # print('in')
                frame, self.client_address = self.udp_socket.recvfrom(186220800)
                # frames = []
                # for _ in range(self.num_packets):
                #     frame, server_address = self.udp_socket.recvfrom(186220800)
                #     frames.append(frame)
                # frame = b''.join(frames)

                # # decode and play the audio data
                img = np.frombuffer(frame, dtype=np.uint8)
                # Decode the image
                img = cv2.imdecode(img, cv2.IMREAD_COLOR)
                # Display the image in a window
                img = cv2.resize(img, (1980, 1080))
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
        with mss.mss() as sct:
            # imageCounter = 0
            sizeY = 1080
            sizeX = 1920
            nRows = 5
            mCols = 3
            while not stop_event.is_set():
                if self.client_address is not None:
                    # do something
                    # print('out')
                    # imageCounter += 1
                    sct_img = sct.grab(sct.monitors[1])
                    img = np.array(sct_img)

                    img = cv2.resize(img, (1920, 1080))
                    # img = cv2.resize(img, self.frame_size)
                    # send audio data to the server
                    for i in range(0,5):
                        for j in range(0, 3):
                            roi = img[int(i*sizeY/nRows):(int((i+1)*sizeY/nRows)), int(j*sizeX/mCols):(int((j+1)*sizeX/mCols))]
                            # cv2.imshow('rois'+str(i)+str(j), roi)
                            # cv2.imwrite('patches/patch_'+str(i)+str(j)+".jpg", roi)
                            _, jpeg_img = cv2.imencode(".jpg", roi, [self.encoding_format, self.quality])
                            # if imageCounter % 18 == 0:
                            self.udp_socket.sendto(jpeg_img.tobytes(), self.client_address)
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
vs = videoServer(5000)
# vs.in_start()
# vs.SetclientAddress('10.89.178.153')
vs.out_start()
# vs.out_pause()
# vs.in_pause()