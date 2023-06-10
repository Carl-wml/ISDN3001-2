#pyside6-uic untitled.ui -o teastui.py


import sys, random
# from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QFile, QObject, QUrl, Slot,Qt
from PySide6.QtGui import QIcon, QPalette, QBrush, QPixmap, QFont
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QHBoxLayout, QVBoxLayout


    #width = 1536, height = 846
RGBset = ["47,54,74","149,145,166","200,154,58"]
class Window(QWidget):
    def __init__(self):
        super().__init__()
        #width = 1536, height = 846
        self.setWindowTitle("WalkieClickie")
        self.setGeometry(1536/2-300,846/2-150,600,300)
        self.setWindowIcon(QIcon('demo_3002/picture/productImage.png'))
        self.setStyleSheet(f"background-color: rgb({RGBset[0]});")
        self.setWindowOpacity(0.85)#transparent
        # self.setWindowFlag(Qt.WindowStaysOnTopHint)#always on top
        self.startPage()

        
    def startPage(self):
        self.label = QLabel(self)
        self.label.setStyleSheet(f"color: rgb({RGBset[2]}); font-size: 24px;")
        self.label.setFont(QFont("Times New Roman", 20, QFont.Bold))

        self.button = QPushButton("Click me!")
        self.button.setStyleSheet(f"color: rgb({RGBset[2]}); font-size: 24px;")
        self.button.move(0, 0)

        self.pxiLabel = QLabel(self)
        self.pxi = QPixmap("demo_3002/picture/productImage.png")
        self.pxiLabel.setPixmap(self.pxi)
        self.pxiLabel.move(50, 50)

        

# Create a vertical layout for the label and button
        layout = QHBoxLayout()
        # layout.addWidget(self.label)
        # layout.addWidget(self.pxiLabel)
        layout.addWidget(self.button)

# Set the layout as the layout of the main widget
        self.setLayout(layout)

        self.button.clicked.connect(self.startPage)
        # self.label = QLabel()
        # # label.setGeometry(50,50,100,50)
        # self.label.setStyleSheet(f"color: rgb({RGBset[2]}); font-size: 24px;")
        # self.label.setFont(QFont("Times New Roman", 20, QFont.Bold))

        # self.pxiLabel = QLabel(self)
        # self.pxi = QPixmap("demo_3002/picture/productImage.png")
        # #background-image: url("demo_3002/picture/productImage.png");
        # self.pxiLabel.setPixmap(self.pxi)

        # self.button = QPushButton("Click me!")
        # # self.text = QLabel("Hello World", alignment=Qt.AlignCenter)
        # self.button.setStyleSheet(f"color: rgb({RGBset[2]}); font-size: 24px;")

        # self.layout = QVBoxLayout()
        # self.layout.addWidget(self.label)
        # self.layout.addWidget(self.pxiLabel)
        # # self.layout.addWidget(self.text)
        # self.layout.addWidget(self.button)


        # self.setLayout(self.layout)

        # self.button.clicked.connect(self.startPage)

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

# #wirte a login GUI application
# class loginWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Login')
#         self.resize(400, 300)
#         self.label = QLabel('Username', self)
#         self.label.setGeometry(50, 50, 100, 50)
#         self.label1 = QLabel('Password', self)
#         self.label1.setGeometry(50, 100, 100, 50)
#         self.textbox = QtWidgets.QLineEdit(self)
#         self.textbox.setGeometry(150, 50, 200, 50)
#         self.textbox1 = QtWidgets.QLineEdit(self)
#         self.textbox1.setGeometry(150, 100, 200, 50)
#         self.button = QPushButton('Login', self)
#         self.button.setGeometry(50, 150, 100, 50)
#         self.button.clicked.connect(self.on_button_click)

#     def on_button_click(self):
#         self.label.setText('Button clicked!')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    # window.resize(800,600)
    window.show()

    sys.exit(app.exec())