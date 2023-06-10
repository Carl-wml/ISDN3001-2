import serial
import serial.tools.list_ports as port_list
import threading
import time
import voiceClientUDP
import voiceServerUDP
import videoServerTCP
import videoClientTCP
import exeHandler
import inputPlayerWithStop
import telegramBot
import notificationHandler
import fileRead
import os
import webbrowser

# C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE

def new_desktop():
    import pyautogui as pa
    pa.hotkey('win','ctrl','d')

def del_desktop():
    import pyautogui as pa
    pa.hotkey('win','ctrl','f4')

def min_Win():
    import pyautogui as pa
    pa.hotkey('win','d')

def change_wallpaper(path):
    import ctypes
    ctypes.windll.user32.SystemParametersInfoW(20,2,path,3)

def play_mp3(path):
    import vlc
    vlc.MediaPlayer(path).play()

class ESP32Listener:
    def __init__(self, port, baudrate=115200):
        self.count = 0
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        self.count1 = 0
        self.count2 = 0
        self.count3 = 0
        self.file_Read = fileRead.fileRead()

    def find_port(self):
        ports = list(port_list.comports())
        for p in ports:
            if self.port in str(p):
                return p.device
        return None

    def listen(self):
        port = self.find_port()
        if port is None:
            print('No Serial port not found')
            return False
        try:
            self.ser = serial.Serial(port, self.baudrate)
            print("Serial port opened on", port)
            # Set up flag variables
            flag1 = False
            flag2 = False
            flag3 = False
            start_time1 = time.time()-1
            start_time2 = time.time()-1
            start_time3 = time.time()-1

            while True:
                # Read from serial monitor
                line = self.ser.readline().decode('utf-8').rstrip()

                # Check if 0.5 seconds have elapsed since flag was set
                if flag1 and time.time() - start_time1 < 1:
                    continue
                if flag2 and time.time() - start_time2 < 1:
                    continue
                if flag3 and time.time() - start_time3 < 1:
                    continue

                # Process data
                if line == "0":
                    flag1 = True
                    self.count1 += 1
                    start_time1 = time.time()
                    thread = threading.Thread(target=self.run1, args=())
                    thread.start()

                elif line == "1":
                    flag2 = True
                    start_time2 = time.time()
                    self.count2 += 1
                    thread = threading.Thread(target=self.run2, args=())
                    thread.start()

                elif line == "2":
                    flag3 = True
                    start_time3 = time.time()
                    self.count3 += 1
                    thread = threading.Thread(target=self.run3, args=())
                    thread.start()

                # Reset flag if 0.5 seconds have elapsed
                if flag1 and time.time() - start_time1 >= 1:
                    flag1 = False 
                if flag2 and time.time() - start_time2 >= 1:
                    flag2 = False
                if flag3 and time.time() - start_time3 >= 1:
                    flag3 = False
                    
        except Exception as e:
            print('Error:', e)
        finally:
            if self.ser is not None and self.ser.isOpen():
                self.ser.close()
                print("Serial port closed")

    excute_array = ["open","close","openW","chat","share","notif","talk","wallP","mp3","play","min","newD","delD"]

    def excute(self, tasksArray):
        sharing = False
        talking = False
        playing = False
        for i in tasksArray:
            print(i)
            if i[0] == "open":
                os.startfile(i[1])
            elif i[0] == "close":
                exeHandler.exeHandler().close_app(i[1])
            elif i[0] == "openW":
                webbrowser.open(i[1])
            elif i[0] == "chat":
                tb = telegramBot.TelegramBot(r'6248471775:AAG_NOphIUK-vo1h2fw4vlhMmt52c_IrEX8')
                tb.send_message(i[1], i[2])
                tb.polling()
            elif i[0] == "share":
                if sharing == False:
                    VCT = videoClientTCP.videoClient(i[1], 5000)
                    VCT.out_start()
                else:
                    VCT.out_pause()
                    del VCT
                sharing = not sharing
            elif i[0] == "shareS":
                    VCT.out_pause()
                    del VCT
                    sharing = False
            elif i[0] == "notif":
                notificationHandler.NotificationHandler().show_notification(i[2], i[3])
            elif i[0] == "talk":
                print("talk")
                if talking == False:
                    VCU = voiceClientUDP.voiceClientUDP(i[1], 5001)
                    VCU.out_start()
                    VCU.in_start()
                else:
                    VCU.in_pause()
                    VCU.out_pause()
                    del VCU
                talking = not talking
            elif i[0] == "wallP":
                change_wallpaper(i[1])
            elif i[0] == "mp3":
                play_mp3(i[1])
            elif i[0] == "play":
                if playing == False:
                    IPS = inputPlayerWithStop.inputPlayerWithStop()
                    IPS.load(i[1])
                    IPS.play()
                else:
                    IPS.stop()
                    del IPS
                playing = not playing
            elif i[0] == "min":
                min_Win()
            elif i[0] == "newD":
                new_desktop()
            elif i[0] == "delD":
                del_desktop()
            else:
                print("error")
                return
            
        


# threading!!!
    def run1(self):
        self.excute(self.file_Read.getTasksArray(r'demo_3002\1.txt'))


    def run2(self):
        print("run2")
        with open(r'demo_3002\\2.txt', 'r') as file:
            for i in range(self.count):
                line = file.readline()
            count += 1
            line =file.readline()
            print(line.split(','))
            self.excute([line.split(',')])
        # self.excute(self.file_Read.getTasksArray(r'demo_3002\2.txt'))
            
    def run3(self):
        print("run3")
        self.excute(self.file_Read.getTasksArray(r'demo_3002\3.txt'))

def new_desktop():
    import pyautogui as pa
    pa.hotkey('win','ctrl','d')

#to-use !!!
def start_listener(espL):
    espL.listen()

def notification_display(Title,Message,time):
    from plyer import notification
    if __name__=="__main__":
     
        notification.notify(
            title = Title,
            message=Message ,
           
            # displaying time
            timeout=time
    )
if __name__ == '__main__':
    espL = ESP32Listener('COM6')
    listener_thread = threading.Thread(target=start_listener, args=(espL,))
    listener_thread.start()

# import serial
# import serial.tools.list_ports as port_list
# ports = list(port_list.comports())
# for p in ports:
#     print (p)

# try:
#     ser = serial.Serial('COM5', 115200) # Replace '/dev/ttyUSB0' with the appropriate serial port for your system
#     print("ok")
#     while True:
#         line = ser.readline().decode('utf-8').rstrip() # Read a line of data from the serial connection and decode it as a UTF-8 string
#         if line:
#             print(line) # Print the received data

# except:
#     print('Serial port not found')
