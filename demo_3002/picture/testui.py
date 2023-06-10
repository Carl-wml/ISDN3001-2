# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)
import image_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(703, 592)
        self.Key1 = QPushButton(Dialog)
        self.Key1.setObjectName(u"Key1")
        self.Key1.setGeometry(QRect(150, 150, 121, 81))
        font = QFont()
        font.setFamilies([u"Elephant"])
        font.setPointSize(18)
        self.Key1.setFont(font)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 10, 711, 581))
        self.label_3.setStyleSheet(u"image: url(:/wholeBody/WhatsApp Image 2023-05-29 at 18.48.30.jpg)")
        self.Key1_2 = QPushButton(Dialog)
        self.Key1_2.setObjectName(u"Key1_2")
        self.Key1_2.setGeometry(QRect(300, 150, 121, 81))
        self.Key1_2.setFont(font)
        self.Key1_3 = QPushButton(Dialog)
        self.Key1_3.setObjectName(u"Key1_3")
        self.Key1_3.setGeometry(QRect(450, 150, 121, 81))
        self.Key1_3.setFont(font)
        self.label_3.raise_()
        self.Key1.raise_()
        self.Key1_2.raise_()
        self.Key1_3.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Key1.setText(QCoreApplication.translate("Dialog", u"Key1", None))
        self.label_3.setText("")
        self.Key1_2.setText(QCoreApplication.translate("Dialog", u"Key2", None))
        self.Key1_3.setText(QCoreApplication.translate("Dialog", u"Key3", None))
    # retranslateUi

if __name__ == '__main__':
    import sys
    import PySide6.QtWidgets
    app = QApplication(sys.argv)

    window = PySide6.QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(window)
    # window.resize(800,600)
    window.show()

    sys.exit(app.exec())

    # pyside6-rcc demo_3002\picture\image.qrc -o demo_3002\picture\image_rc.py
    # pyside6-uic demo_3002\picture\mainui.ui -o demo_3002\picture\realui.py    