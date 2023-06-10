import sys, random
# from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QFile, QObject, QUrl, Slot,Qt
from PySide6.QtGui import QIcon, QPalette, QBrush, QPixmap, QFont
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout,QGridLayout,QMessageBox,QMenu,QHBoxLayout,QStackedWidget


    #width = 1536, height = 846
RGBset = ["47,54,74","149,145,166","200,154,58"]
class Window(QWidget):
    def __init__(self):
        super().__init__()
        #width = 1536, height = 846
        self.setWindowTitle("ISDN 3002 Demo")
        self.setGeometry(1536/2-300,846/2-150,600,300)
        self.setWindowIcon(QIcon('demo_3002/picture/productImage.png'))
        # self.setStyleSheet(f"background-color: rgb({RGBset[0]});")
        # self.setWindowOpacity(0.85)#transparent
        # self.setWindowFlag(Qt.WindowStaysOnTopHint)#always on top
        self.pxiLabel = QLabel(self)
        self.pxi = QPixmap("demo_3002/picture/productImage.png")
        self.pxiLabel.setPixmap(self.pxi)

        # Create the buttons for the main window
        # self.buttonlist = []
        # for i in range(1,9):
        #     self.buttonlist.append(QPushButton(f"Button {i}"))
        #     self.buttonlist[i-1].clicked.connect(self.buttonClicked)
        #     self.buttonlist[i-1].setStyleSheet(f"color: rgb({RGBset[2]}); font-size: 24px;")
        
        
        self.button1 = QPushButton("Button 1")
        self.button2 = QPushButton("Button 2")
        self.button3 = QPushButton("Button 3")
        self.button4 = QPushButton("Button 4")
        self.button5 = QPushButton("Button 5")
        self.button6 = QPushButton("Button 6")
        self.button7 = QPushButton("Button 7")
        self.button8 = QPushButton("Button 8")
        self.button7.hide()
        self.button8.hide()

        # Connect the buttons to the buttonClicked method
        self.button1.clicked.connect(self.buttonClicked)
        self.button2.clicked.connect(self.buttonClicked)
        self.button3.clicked.connect(self.buttonClicked)
        self.button4.clicked.connect(self.buttonClicked)
        self.button5.clicked.connect(self.buttonClicked)
        self.button6.clicked.connect(self.buttonClicked)
        self.button7.clicked.connect(self.buttonClicked)
        self.button8.clicked.connect(self.buttonClicked)
        
        # Create the layout for the main window
        self.layout =  QGridLayout()
        self.layout.addWidget(self.button1, 0, 0)
        self.layout.addWidget(self.button2, 0, 1)
        self.layout.addWidget(self.button3, 0, 2)
        self.layout.addWidget(self.button4, 1, 0)
        self.layout.addWidget(self.button5, 1, 1)
        self.layout.addWidget(self.button6, 1, 2)
        self.layout.addWidget(self.button7, 2, 0)
        self.layout.addWidget(self.button8, 2, 1)
        # for i in range(1,9):
        #     self.layout.addWidget(self.buttonlist[i-1], (i-1)//3, (i-1)%3)
        self.layout.addWidget(self.pxiLabel)
        self.pxiLabel.move(0, 0)
         
        # Create the widgets for the feature selection window
        self.application_button = QPushButton("Application")
        self.tools_button = QPushButton("Tools")
        self.other_button = QPushButton("Other")
        self.application_menu = QMenu()
        # app_list = get_installed_apps()
        # for i in range(len()):
            # self.application_menu.addAction(f"Application Feature {i}")
        self.application_menu.addAction("Application Feature 1")
        self.application_menu.addAction("Application Feature 2")
        self.application_menu.addAction("Application Feature 3")
        self.tools_menu = QMenu()
        self.tools_menu.addAction("Tool 1")
        self.tools_menu.addAction("Tool 2")
        self.tools_menu.addAction("Tool 3")
        self.other_menu = QMenu()
        self.other_menu.addAction("Other Feature 1")
        self.other_menu.addAction("Other Feature 2")
        self.other_menu.addAction("Other Feature 3")
        self.application_button.setMenu(self.application_menu)
        self.tools_button.setMenu(self.tools_menu)
        self.other_button.setMenu(self.other_menu)
         
        # Connect the buttons to the featureSelected method
        self.application_button.clicked.connect(self.featureSelected)
        self.tools_button.clicked.connect(self.featureSelected)
        self.other_button.clicked.connect(self.featureSelected)
         
        # Create the layout for the feature selection window
        self.feature_layout = QHBoxLayout()
        self.feature_layout.addWidget(self.application_button)
        self.feature_layout.addWidget(self.tools_button)
        self.feature_layout.addWidget(self.other_button)
         
        # Create the widget stack and add the main window and feature selection window
        self.stack =  QStackedWidget()
        self.stack.addWidget(QWidget())
        self.stack.addWidget(QWidget())
        self.stack.widget(0).setLayout(self.layout)
        self.stack.widget(1).setLayout(self.feature_layout)
         
        # Set the widget stack as the main layout for the window
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)
         
        # Initialize the buttonSelected and featureSelected variables
        self.buttonSelected = None
        self.featureSelected = None

    def buttonClicked(self):
        # Set the buttonSelected variable to the button that was clicked
        self.buttonSelected = self.sender()
         
        # Show the hidden buttons
        self.button7.show()
        self.button8.show()
         
        # Switch to the feature selection window
        self.stack.setCurrentIndex(1)

    def featureSelected(self):
        # Set the featureSelected variable to the menu item that was selected
        self.featureSelected = self.sender().menu().actionTriggered(self.sender().menuAction())
         
        # Switch back to the main window
        self.stack.setCurrentIndex(0)
         
        # Hide the hidden buttons
        self.button7.hide()
        self.button8.hide()

    def startPage(self):
        self.label = QLabel(self)
        # label.setGeometry(50,50,100,50)
        self.label.setStyleSheet(f"color: rgb({RGBset[2]}); font-size: 24px;")
        self.label.setFont(QFont("Times New Roman", 20, QFont.Bold))

        self.pxiLabel = QLabel(self)
        self.pxi = QPixmap("demo_3002/picture/productImage.png")
        self.pxiLabel.setPixmap(self.pxi)

        self.button = QPushButton("Click me!")
        # self.text = QLabel("Hello World", alignment=Qt.AlignCenter)
        self.button.setStyleSheet(f"color: rgb({RGBset[2]}); font-size: 24px;")

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.pxiLabel)
        # self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.startPage)

    def functionPage(self):
        self.label.setText("This is the function page")
        self.pxiLabel.setPixmap(self.pxi)
        self.show()

    def endPage(self):
        self.label.setText("This is the end page")
        self.pxiLabel.setPixmap(self.pxi)
        self.show()

    @Slot()
    def magic(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('demo_3002/picture/productImage.png'))
    window = Window()
    # window.resize(800,600)
    window.show()

    print("Hello World")
    sys.exit(app.exec())

import winreg

def get_installed_apps():
    # Open the registry key for installed applications
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                         r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
    # Get the number of subkeys (installed applications)
    num_apps = winreg.QueryInfoKey(key)[0]
    # Iterate over the subkeys and retrieve the display name, publisher, and installation path for each installed application
    apps = []
    for i in range(num_apps):
        app_key = winreg.EnumKey(key, i)
        app_subkey = winreg.OpenKey(key, app_key)
        try:
            display_name, _ = winreg.QueryValueEx(app_subkey, "DisplayName")
            publisher, _ = winreg.QueryValueEx(app_subkey, "Publisher")
            install_location, _ = winreg.QueryValueEx(app_subkey, "InstallLocation")
            apps.append((display_name, publisher, install_location))
        except OSError:
            pass
        app_subkey.Close()
    key.Close()
    return apps


