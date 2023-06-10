import socket
import threading
import cv2
import numpy as np
import mss


class videoClient:
    # Set the maximum packet size to 65507 bytes
    # MAX_PACKET_SIZE = 65507
    num_packets = 16


    def __init__(self, serveraddress, port, encoding_format=cv2.IMWRITE_JPEG_QUALITY, quality=50, frame_size=(640, 480)) -> None:
        #image encoding parameters
        # self.encoding_format = encoding_format
        # self.quality = quality
        # self.frame_size = frame_size

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

        # create a UDP socket
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # # bind the socket to a specific IP address and port number
        # self.udp_socket.bind(self.server_address)

        self.stop_event_in = threading.Event()
        self.thread_in = threading.Thread(target=self.thread_in, args=(self.stop_event_in,))

        self.stop_event_out = threading.Event()
        self.thread_out = threading.Thread(target=self.thread_out, args=(self.stop_event_out,))

        self.window_open = False  # flag to track whether the window is open or closed

    def separate_send(self, data):
        # calculate the total number of packets needed
        # num_packets = (len(data) + self.MAX_PACKET_SIZE - 1) // self.MAX_PACKET_SIZE

        num_packets = 16
        MAX_PACKET_SIZE = len(data)//num_packets

        # send each packet with a header
        for i in range(num_packets):
            # calculate the packet number and offset
            packet_num = i + 1
            offset = i * MAX_PACKET_SIZE

            # add the header to the packet
            header = f"{num_packets}:{packet_num}:{len(data)}".encode()
            packet = header + data[offset:offset + MAX_PACKET_SIZE]

            # send the packet
            self.udp_socket.sendto(packet, self.server_address)

    # def separate_receive(self):
    #     # receive the packets and concatenate them
    #     received_data = b''
    #     num_packets = None
    #     for i in range(num_packets):
    #         # receive a packet
    #         packet, address = self.udp_socket.recvfrom(self.MAX_PACKET_SIZE + HEADER_SIZE)
            
    #         # extract the header information
    #         header = packet[:HEADER_SIZE].decode()
    #         total_packets, packet_num, data_len = map(int, header.split(":"))
            
    #         # append the packet data to the received data
    #         received_data += packet[HEADER_SIZE:]
            
    #         if packet_num == 1:
    #             num_packets = total_packets

    #     # the received_data now contains the original data
    #     print(received_data)
    #     return received_data

    def thread_in(self, stop_event):
        imageCounter = 0
        sizeY = 1080
        sizeX = 1920
        nRows = 5
        mCols = 3
        patch_size = int(sizeY / nRows), int(sizeX / mCols)
        full_screen_size = nRows * patch_size[0], mCols * patch_size[1]
        full_screen = np.zeros((full_screen_size[0], full_screen_size[1], 3), dtype=np.uint8)

        while not stop_event.is_set():
            try:
                frame, server_address = self.udp_socket.recvfrom(65507)
                img = np.frombuffer(frame, dtype=np.uint8)
                img = cv2.imdecode(img, cv2.IMREAD_COLOR)

                patch_row_index = int(imageCounter / mCols)
                patch_col_index = int(imageCounter % mCols)
                patch_start_y = patch_row_index * patch_size[0]
                patch_end_y = (patch_row_index + 1) * patch_size[0]
                patch_start_x = patch_col_index * patch_size[1]
                patch_end_x = (patch_col_index + 1) * patch_size[1]

                full_screen[patch_start_y:patch_end_y, patch_start_x:patch_end_x] = img

                imageCounter += 1

                if imageCounter == nRows * mCols:
                    # Display the full screen
                    cv2.imshow("Screen Sharing (From Server)", full_screen)
                    if cv2.waitKey(1) == ord("q"):
                        break
                    # Reset the counter and full screen image
                    imageCounter = 0
                    full_screen = np.zeros((full_screen_size[0], full_screen_size[1], 3), dtype=np.uint8)

            except Exception as e:
                #print("Error receiving frame: ", e)
                pass

        print("Thread stopped.")

    def thread_out(self,stop_event):
        with mss.mss() as sct:
            while not stop_event.is_set():
                sizeY = 1080
                sizeX = 1920
                nRows = 5
                mCols = 3
                # print('out')
                try:    
                    # do something
                    sct_img = sct.grab(sct.monitors[1])
                    img = np.array(sct_img)
                    img = cv2.resize(img, (1280, 400))
                    _, jpeg_img = cv2.imencode(".jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 70])
                    # print(img.tobytes().__sizeof__())
                    # send data to the server
            #        for i in range(0,5):
             #           for j in range(0, 3):
              #              roi = img[int(i*sizeY/nRows):(int((i+1)*sizeY/nRows)), int(j*sizeX/mCols):(int((j+1)*sizeX/mCols))]
                            # cv2.imshow('rois'+str(i)+str(j), roi)
                            # cv2.imwrite('patches/patch_'+str(i)+str(j)+".jpg", roi)
               #             _, jpeg_img = cv2.imencode(".jpg", roi, [self.encoding_format, self.quality])
                            # if imageCounter % 18 == 0:
                #            self.udp_socket.sendto(jpeg_img.tobytes(), self.server_address)

                    self.udp_socket.sendto(jpeg_img.tobytes(), self.server_address)
                    # self.seperate_send(jpeg_img.tobytes())
                    
                    # img = np.frombuffer(jpeg_img, dtype=np.uint8)
                    # img = cv2.imdecode(img, cv2.IMREAD_COLOR)
                    # cv2.imshow("Screen Sharing (Server)", img)
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
vs = videoClient('10.89.74.186',5000);
vs.in_start()
# vs.out_start()
# vs.out_pause()
# vs.in_pause()
