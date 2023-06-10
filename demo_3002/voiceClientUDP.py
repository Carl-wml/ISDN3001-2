import socket
import pyaudio
import threading

class voiceClientUDP:
    
    def __init__(self, serveraddress, port) -> None:
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

        # create a PyAudio object
        self.audio = pyaudio.PyAudio()

        # define the audio format
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024

        # open an audio stream
        stream_in = self.audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        stream_out = self.audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, output=True, frames_per_buffer=self.CHUNK)

        self.stop_event_in = threading.Event()
        self.thread_in = threading.Thread(target=self.thread_in, args=(self.stop_event_in, stream_out,))

        self.stop_event_out = threading.Event()
        self.thread_out = threading.Thread(target=self.thread_out, args=(self.stop_event_out, stream_in,))


    def thread_in(self,stop_event,stream):
        while not stop_event.is_set():
            # do something
            # print('in')
            try:
                data_in, server_address = self.udp_socket.recvfrom(4096)
                
                # decode and play the audio data
                stream.write(data_in)
            except:
                pass
        print("Thread stopped.")

    def thread_out(self,stop_event,stream):
        while not stop_event.is_set():
            # do something
            # print('out')
            # receive audio data
            try:
                data_out = stream.read(self.CHUNK)
                # send audio data to the server
                # print(data_out.__len__())
                self.udp_socket.sendto(data_out, self.server_address)
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

# # to use !!!!!
# vc = voiceClientUDP('192.168.0.11',5000)
# vc.in_start()
# vc.out_start()
# vc.out_pause()
# vc.in_pause()