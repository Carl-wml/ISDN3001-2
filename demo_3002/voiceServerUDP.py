import socket
import pyaudio
import threading

class voiceServerUDP:

    def __init__(self, port) -> None:
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

        # create a PyAudio object
        self.audio = pyaudio.PyAudio()

        # define the audio format
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024

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
            data_in, self.client_address = self.udp_socket.recvfrom(4096)
            
            # decode and play the audio data
            stream.write(data_in)
        print("Thread stopped.")

    def thread_out(self,stop_event,stream):
        while not stop_event.is_set():
            if self.client_address is not None:
                # do something
                # print('out')
                # receive audio data
                data_out = stream.read(self.CHUNK)
                # send audio data to the server
                self.udp_socket.sendto(data_out, self.client_address)
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
# vs = voiceServerUDP(5000);
# vs.in_start()
# vs.out_start()
# vs.out_pause()
# vs.in_pause()