#to check if os is windows or linux or apple or raspberry pi
import platform

# Get the OS name
os_name = platform.system()

# Check if the OS is Windows
if os_name == 'Windows':
    print('Running on Windows')
    #file importshi

    # import voiceServerUDP
    # import voiceClientUDP
    # import textClient
    # import exeHandler
    # import webHandler
    # import notificationHandler
    import inputMonitor
    import inputPlayer
    import time 
 
    #class objects construction
    # voiceServerUDP = voiceServerUDP.voiceServerUDP()
    # voiceClientUDPtest = voiceClientUDP.voiceClientUDP()
    # textClient = textClient.textClient()
    # exeHandler = exeHandler.exeHandler()
    # webHandler = webHandler.webHandler()
    # notificationHandler = notificationHandler.notificationHandler()
    InputListen = inputMonitor.InputListener()

    cmd = input("cmd:\nMP: Moinitor and play\n")
    if cmd == "MP":
        # InputListen.start()
        # while InputListen.keyboard_listener.running:
        #     time.sleep(1)
        # InputListen.stop()

        InputList= InputListen.start_Input_listener()

        print(InputList)

        ip = inputPlayer.InputPlayer()
        ip.load(InputList) 
        ip.play(0)
        # print(InputList)
     
 
# Check if the OS is Linux
elif os_name == 'Linux':
    print('Running on Linux')
  
# Check if the OS is macOS
elif os_name == 'Darwin':
    print('Running on macOS')

# Check if the OS is Raspberry Pi
elif 'arm' in platform.machine():
    print('Running on Raspberry Pi')

# If the OS is not recognized, print a warning
else: 
    print('Unknown OS:', os_name)
    print('Sorry, this program is not compatible with your OS.\n And we are sorry for the inconvenience caused.')
