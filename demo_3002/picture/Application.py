import sys
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QFileDialog, QApplication, QMainWindow, QMessageBox

from realui import Ui_Dialog

import winExeList, fileWrite, inputMonitor
import win32gui,win32con

def search_real_name_window(window_title):
    def enum_callback(hwnd, windows):
        title = win32gui.GetWindowText(hwnd)
        windows.append(title)
        return True
    
def minimize_window(window_title):
    window_title = search_real_name_window(window_title)
    if not window_title:
        #print(f"No window found (1) with title '{window_title}'")
        return
    
    hwnd = win32gui.FindWindowEx(None, None,None, window_title)
    if hwnd != 0:
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

class Application(QMainWindow):
    key_changing = 0
    tasks = ""
    recording_event = []
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.listWidget()
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)

        self.ui.pushButton_12.clicked.connect(self.to_icon_choice)
        self.ui.pushButton_8.clicked.connect(self.to_icon_choice)
        self.ui.sb_main_2.clicked.connect(self.to_icon_choice)
        self.ui.sb_main.clicked.connect(self.to_icon_choice)
        self.ui.pushButton_6.clicked.connect(self.to_icon_choice)
        self.ui.pushButton_23.clicked.connect(self.to_icon_choice)
        self.ui.pushButton_5.clicked.connect(self.to_icon_choice)
        self.ui.pushButton_7.clicked.connect(self.to_icon_choice)


        self.ui.Key1.clicked.connect(self.to_subject1)
        self.ui.Key2.clicked.connect(self.to_subject2)
        self.ui.Key3.clicked.connect(self.to_subject3)
        self.ui.Key21.clicked.connect(self.to_subject1)
        self.ui.Key22.clicked.connect(self.to_subject2)
        self.ui.Key23.clicked.connect(self.to_subject3)
        # self.ui.back.clicked.connect(self.to_home)
        self.ui.sb_key.clicked.connect(self.to_home)
        self.ui.pushButton_2.clicked.connect(self.to_home)
        self.ui.pushButton_22.clicked.connect(self.to_home)
        self.ui.pushButton_7.clicked.connect(self.to_home)
        self.ui.sb_key_2.clicked.connect(self.to_home)
        self.ui.pushButton_12.clicked.connect(self.to_home)
        self.ui.pushButton_9.clicked.connect(self.to_home)
        


    def listWidget(self):
        temp = winExeList.get_installed_apps()
        for app in temp:
            self.ui.listWidget.addItem(app[0])
    
    def seclect_media(self):
        path, ext = QFileDialog.getOpenFileName(self, "Open Media", ".", "Media Files (*.mp3 *.mp4 *.wav *jpg *png *jpeg)")
        if path:
            self.media_In.setText(path)
        
    def subject(self):
        self.ui.sb_next.clicked.connect(self.subject_class)
        
        
    def to_subject1(self):
        key_changing = 1
        self.ui.sb_main.setStyleSheet(self.ui.Key21.styleSheet())
        self.ui.sb_key.setText("Key 1")
        self.ui.stackedWidget.setCurrentWidget(self.ui.subject)
        self.subject()

    def to_subject2(self):
        key_changing = 2
        self.ui.sb_main.setStyleSheet(self.ui.Key22.styleSheet())
        self.ui.sb_key.setText("Key 2")
        self.ui.stackedWidget.setCurrentWidget(self.ui.subject)
        self.subject()

    def to_subject3(self):
        key_changing = 3
        self.ui.sb_main.setStyleSheet(self.ui.Key23.styleSheet())
        self.ui.sb_key.setText("Key 3")
        self.ui.stackedWidget.setCurrentWidget(self.ui.subject)
        self.subject()

    def subject_class(self):
        
        if self.ui.listWidget.currentItem().text() == "Telegram":
            # self.ui.listWidget_2.clear()
            # self.ui.listWidget_3.clear()
            self.to_telegram()
        elif self.ui.listWidget.currentItem().text() == "Excel":
            # self.ui.listWidget_2.clear()
            # self.ui.listWidget_3.clear()
            self.to_exc()
        elif self.ui.listWidget.currentItem().text() == "Outlook":
            # self.ui.listWidget_2.clear()
            # self.ui.listWidget_3.clear()
            # self.to_Exe()
            self.tasks = self.tasks + "open,C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE,\n"
            fw = fileWrite.fileWrite()
            fw.setFilename('demo_3002\\'+(str)((self.key_changing)+1)+'.txt')
            print(self.tasks)
            fw.print(self.tasks)
            fw.del_fw()
            self.to_home()

        elif self.ui.listWidget_2.currentItem() and self.ui.listWidget_2.currentItem().text() == "Action recording":
            # self.ui.listWidget.clear()
            # self.ui.listWidget_3.clear()
            self.to_Recording()
        elif self.ui.listWidget_2.currentItem() and self.ui.listWidget_2.currentItem().text() == "Notification":
            print("correct")
            # self.ui.listWidget.clear()
            # self.ui.listWidget_3.clear()
            self.to_Notification()
        elif self.ui.listWidget_2.currentItem() and self.ui.listWidget_2.currentItem().text() == "Voice Chat":
            # self.ui.listWidget.clear()
            # self.ui.listWidget_3.clear()
            self.to_Voice()
        elif self.ui.listWidget_2.currentItem() and self.ui.listWidget_2.currentItem().text() == "Change wallpaper":
            # self.ui.listWidget.clear()
            # self.ui.listWidget_3.clear()
            self.tasks = self.tasks + "wallp,"
            self.to_media()
        elif self.ui.listWidget_2.currentItem() and self.ui.listWidget_2.currentItem().text() == "Mp3 player":
            # self.ui.listWidget.clear()
            # self.ui.listWidget_3.clear()
            self.tasks = self.tasks + "mp3,"
            self.to_media()
        elif self.ui.listWidget_2.currentItem() and self.ui.listWidget_2.currentItem().text() == "Window control":
            # self.ui.listWidget.clear()
            # self.ui.listWidget_3.clear()
            self.to_WinCon()
        elif self.ui.listWidget.currentItem().text() == "Chrome":
                # self.ui.listWidget_2.clear()
            # self.ui.listWidget_3.clear()
            self.to_url()
        elif self.ui.listWidget.currentItem().text() == "Zoom":
            # self.ui.listWidget_2.clear()
            # self.ui.listWidget_3.clear()
            self.to_url()
        else:
            QMessageBox.warning(self, "Sorry", "It's not available now")
            # self.ui.listWidget.clear()
            # self.ui.listWidget_2.clear()
            # self.ui.listWidget_3.clear()
            self.ui.stackedWidget.setCurrentWidget(self.ui.Home)

    # def to_Exe(self):
    #     pass
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.Exe)
    #     self.ui.exe_finish.clicked.connect(self.finish_exe)

    # def finish_exe(self):
    #     self.tasks = self.tasks + self.ui.exe_in.text()+"\n"
    #     print(self.tasks)
    #     self.to_home()

    def to_Recording(self):
        print("correct")
        self.ui.stackedWidget.setCurrentWidget(self.ui.Recording)
        self.ui.pushButton_10.clicked.connect(self.start_recording)
        
    def start_recording(self):
        minimize_window("Workie Clickie")
        IM = inputMonitor.InputListener()
        self.recording_event = IM.start_Input_listener()
        self.finish_recording()

    def finish_recording(self):
        self.tasks = self.tasks + "recording,"
        for event in self.recording_event:
            self.tasks = self.tasks + event + ","
        self.to_home()

    def to_Notification(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Notification)
        
        self.ui.notification_finish.clicked.connect(self.finish_notification)

    def finish_notification(self):
        self.tasks = self.tasks + "notif,"
        print(self.tasks)
        self.to_home()

    def to_Voice(self):
        self.tasks = self.tasks + "share,"

        self.ui.stackedWidget.setCurrentWidget(self.ui.Voice)
        self.ui.voice_finish.clicked.connect(self.finish_voice)
        
    def finish_voice(self):
        self.tasks = self.tasks + "voice,"
        print(self.tasks)
        self.to_home()

    def to_WinCon(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.WinCon)
        self.ui.wincon_finish.clicked.connect(self.finish_wincon)

    def finish_wincon(self):
        self.tasks = self.tasks + "wincon,"
        print(self.tasks)
        self.to_home()

    def to_media(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.media)
        self.ui.media_finish.clicked.connect(self.finish_media)

    def finish_media(self):
        self.tasks = self.tasks + self.ui.media_in.text()+"\n"
        print(self.tasks)
        self.to_home()


    def to_telegram(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.telegram)
        self.tasks = self.tasks + "chat,"
        self.ui.telegram_finish.clicked.connect(self.finish_telegram)

    def finish_telegram(self):
        self.tasks = self.tasks + self.ui.telegram_in.text()+"\n"
        fw = fileWrite.fileWrite()
        fw.setFilename('demo_3002\\'+(str)((self.key_changing)+1)+'.txt')
        print(self.tasks)
        fw.print(self.tasks)
        fw.del_fw()
        self.to_home()
        

    def to_url(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.url)
        self.tasks = self.tasks + "openW,"
        self.ui.url_finish.clicked.connect(self.finish_url)

    def finish_url(self):
        self.tasks = self.tasks + self.ui.url_in.text()+"\n"
        fw = fileWrite.fileWrite()
        fw.setFilename('demo_3002\\'+(str)((self.key_changing)+1)+'.txt')
        print(self.tasks)
        fw.print(self.tasks)
        fw.del_fw()
        self.to_home()

    def to_icon_choice(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.changeIcon)
        self.ui.icon_choice_finish.clicked.connect(self.finish_icon_choice)

    def to_home(self):
        # print((str)(self.key_changing) +": "+self.tasks)
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = Application()
    application.show()
    sys.exit(app.exec())