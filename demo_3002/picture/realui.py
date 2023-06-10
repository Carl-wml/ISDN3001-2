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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDialog, QFrame,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QStackedWidget, QToolButton,
    QWidget)
import image_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(750, 607)
        icon = QIcon()
        icon.addFile(u":/wholeBody/3002 final model render 200.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 10, 679, 589))
        self.url = QWidget()
        self.url.setObjectName(u"url")
        self.listWidget_4 = QListWidget(self.url)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.Dense6Pattern)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        __qlistwidgetitem = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem.setFont(font);
        __qlistwidgetitem.setBackground(brush);
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.Dense6Pattern)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem1.setFont(font);
        __qlistwidgetitem1.setBackground(brush1);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem2.setFont(font);
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem3.setFont(font);
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem4.setFont(font);
        self.listWidget_4.setObjectName(u"listWidget_4")
        self.listWidget_4.setGeometry(QRect(150, 180, 151, 251))
        self.listWidget_4.setAutoFillBackground(True)
        self.listWidget_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidget_4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.listWidget_4.setSpacing(6)
        self.label_5 = QLabel(self.url)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(570, 460, 49, 16))
        self.pushButton_2 = QPushButton(self.url)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(43, 280, 61, 41))
        font1 = QFont()
        font1.setFamilies([u"Dubai Medium"])
        font1.setPointSize(11)
        self.pushButton_2.setFont(font1)
        self.url_finish = QPushButton(self.url)
        self.url_finish.setObjectName(u"url_finish")
        self.url_finish.setGeometry(QRect(490, 360, 75, 24))
        self.pushButton_5 = QPushButton(self.url)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(40, 200, 71, 71))
        self.pushButton_5.setStyleSheet(u"image: url(:/otherImage/1.jpg)")
        self.url_in = QLineEdit(self.url)
        self.url_in.setObjectName(u"url_in")
        self.url_in.setGeometry(QRect(350, 310, 201, 21))
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.url_in.sizePolicy().hasHeightForWidth())
        self.url_in.setSizePolicy(sizePolicy)
        self.url_in.setAutoFillBackground(True)
        self.label_2 = QLabel(self.url)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(400, 265, 111, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_2.setFont(font2)
        self.label_12 = QLabel(self.url)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(200, 130, 51, 41))
        font3 = QFont()
        font3.setPointSize(20)
        self.label_12.setFont(font3)
        self.stackedWidget.addWidget(self.url)
        self.url_in.raise_()
        self.pushButton_2.raise_()
        self.listWidget_4.raise_()
        self.label_5.raise_()
        self.url_finish.raise_()
        self.pushButton_5.raise_()
        self.label_2.raise_()
        self.label_12.raise_()
        self.changeIcon = QWidget()
        self.changeIcon.setObjectName(u"changeIcon")
        self.pushButton_12 = QPushButton(self.changeIcon)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(43, 280, 61, 41))
        self.pushButton_12.setFont(font1)
        self.pushButton_11 = QPushButton(self.changeIcon)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(40, 200, 71, 71))
        self.pushButton_11.setStyleSheet(u"image: url(:/otherImage/1.jpg)")
        self.frame = QFrame(self.changeIcon)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(170, 60, 441, 451))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_13 = QPushButton(self.frame)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(40, 50, 71, 71))
        self.pushButton_13.setStyleSheet(u"image: url(:/otherImage/1.jpg)")
        self.pushButton_14 = QPushButton(self.frame)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(180, 50, 71, 71))
        self.pushButton_14.setStyleSheet(u"image: url(:/otherImage/2.jpg)")
        self.pushButton_15 = QPushButton(self.frame)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(320, 50, 71, 71))
        self.pushButton_15.setStyleSheet(u"image: url(:/otherImage/3.jpg)")
        self.pushButton_16 = QPushButton(self.frame)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(40, 180, 71, 71))
        self.pushButton_16.setStyleSheet(u"image: url(:/otherImage/WhatsApp Image 2023-05-29 at 18.17.40.jpg)")
        self.pushButton_17 = QPushButton(self.frame)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(180, 180, 71, 71))
        self.pushButton_17.setStyleSheet(u"image: url(:/otherImage/WhatsApp Image 2023-05-29 at 18.17.41.jpg);")
        self.pushButton_18 = QPushButton(self.frame)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(320, 180, 71, 71))
        self.pushButton_18.setStyleSheet(u"image: url(:/otherImage/WhatsApp Image 2023-05-29 at 18..jpg)")
        self.pushButton_19 = QPushButton(self.frame)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(40, 330, 71, 71))
        self.pushButton_19.setStyleSheet(u"image: url(:/otherImage/play.png)")
        self.pushButton_20 = QPushButton(self.frame)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(180, 330, 71, 71))
        self.pushButton_20.setStyleSheet(u"image: url(:/otherImage/WhatsApp Image 2023-05-29 at 18.1.jpg)")
        self.pushButton_21 = QPushButton(self.frame)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(330, 320, 71, 71))
        self.pushButton_21.setStyleSheet(u"image: url(:/otherImage/WhatsApp Image 2023-05-29 at .jpg)")
        self.stackedWidget.addWidget(self.changeIcon)
        self.Recording = QWidget()
        self.Recording.setObjectName(u"Recording")
        self.label_17 = QLabel(self.Recording)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(185, 130, 81, 41))
        self.label_17.setFont(font3)
        self.listWidget_8 = QListWidget(self.Recording)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.Dense6Pattern)
        __qlistwidgetitem5 = QListWidgetItem(self.listWidget_8)
        __qlistwidgetitem5.setFont(font);
        __qlistwidgetitem5.setBackground(brush2);
        __qlistwidgetitem6 = QListWidgetItem(self.listWidget_8)
        __qlistwidgetitem6.setFont(font);
        __qlistwidgetitem7 = QListWidgetItem(self.listWidget_8)
        __qlistwidgetitem7.setFont(font);
        __qlistwidgetitem8 = QListWidgetItem(self.listWidget_8)
        __qlistwidgetitem8.setFont(font);
        __qlistwidgetitem9 = QListWidgetItem(self.listWidget_8)
        __qlistwidgetitem9.setFont(font);
        __qlistwidgetitem10 = QListWidgetItem(self.listWidget_8)
        __qlistwidgetitem10.setFont(font);
        self.listWidget_8.setObjectName(u"listWidget_8")
        self.listWidget_8.setGeometry(QRect(150, 180, 151, 251))
        self.listWidget_8.setAutoFillBackground(False)
        self.listWidget_8.setSpacing(6)
        self.label_7 = QLabel(self.Recording)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(570, 470, 49, 16))
        self.pushButton_8 = QPushButton(self.Recording)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(40, 200, 71, 71))
        self.pushButton_8.setStyleSheet(u"image: url(:/otherImage/1.jpg)")
        self.pushButton_9 = QPushButton(self.Recording)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(43, 280, 61, 41))
        self.pushButton_9.setFont(font1)
        self.pushButton_10 = QPushButton(self.Recording)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(460, 300, 121, 91))
        self.pushButton_10.setStyleSheet(u"image:url(:/otherImage/play.png)")
        self.label_18 = QLabel(self.Recording)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(330, 230, 221, 61))
        font4 = QFont()
        font4.setPointSize(14)
        self.label_18.setFont(font4)
        self.label_19 = QLabel(self.Recording)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(340, 390, 311, 61))
        self.label_19.setFont(font4)
        self.label_20 = QLabel(self.Recording)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(330, 430, 241, 61))
        self.label_20.setFont(font)
        self.label_24 = QLabel(self.Recording)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(340, 480, 201, 61))
        self.label_24.setFont(font)
        self.stackedWidget.addWidget(self.Recording)
        self.Notification = QWidget()
        self.Notification.setObjectName(u"Notification")
        self.sb_key_2 = QPushButton(self.Notification)
        self.sb_key_2.setObjectName(u"sb_key_2")
        self.sb_key_2.setGeometry(QRect(70, 250, 61, 41))
        self.sb_key_2.setFont(font1)
        self.label_25 = QLabel(self.Notification)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(597, 440, 49, 16))
        self.listWidget_12 = QListWidget(self.Notification)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.Dense6Pattern)
        __qlistwidgetitem11 = QListWidgetItem(self.listWidget_12)
        __qlistwidgetitem11.setFont(font);
        __qlistwidgetitem11.setBackground(brush3);
        QListWidgetItem(self.listWidget_12)
        __qlistwidgetitem12 = QListWidgetItem(self.listWidget_12)
        __qlistwidgetitem12.setFont(font);
        __qlistwidgetitem13 = QListWidgetItem(self.listWidget_12)
        __qlistwidgetitem13.setFont(font);
        __qlistwidgetitem14 = QListWidgetItem(self.listWidget_12)
        __qlistwidgetitem14.setFont(font);
        __qlistwidgetitem15 = QListWidgetItem(self.listWidget_12)
        __qlistwidgetitem15.setFont(font);
        __qlistwidgetitem16 = QListWidgetItem(self.listWidget_12)
        __qlistwidgetitem16.setFont(font);
        self.listWidget_12.setObjectName(u"listWidget_12")
        self.listWidget_12.setGeometry(QRect(170, 140, 151, 251))
        self.listWidget_12.setAutoFillBackground(False)
        self.listWidget_12.setSpacing(6)
        self.label_27 = QLabel(self.Notification)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(200, 100, 81, 41))
        self.label_27.setFont(font3)
        self.notification_finish = QPushButton(self.Notification)
        self.notification_finish.setObjectName(u"notification_finish")
        self.notification_finish.setGeometry(QRect(467, 438, 101, 51))
        self.notification_finish.setFont(font2)
        self.sb_main_2 = QPushButton(self.Notification)
        self.sb_main_2.setObjectName(u"sb_main_2")
        self.sb_main_2.setGeometry(QRect(67, 170, 71, 71))
        self.sb_main_2.setStyleSheet(u"image: url(:/otherImage/1.jpg)")
        self.lineEdit = QLineEdit(self.Notification)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(450, 320, 221, 21))
        self.lineEdit_3 = QLineEdit(self.Notification)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(450, 230, 151, 31))
        self.lineEdit_3.setFont(font4)
        self.label_26 = QLabel(self.Notification)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(400, 230, 41, 31))
        font5 = QFont()
        font5.setPointSize(16)
        self.label_26.setFont(font5)
        self.label_28 = QLabel(self.Notification)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(400, 320, 51, 20))
        self.stackedWidget.addWidget(self.Notification)
        self.telegram = QWidget()
        self.telegram.setObjectName(u"telegram")
        self.listWidget_7 = QListWidget(self.telegram)
        __qlistwidgetitem17 = QListWidgetItem(self.listWidget_7)
        __qlistwidgetitem17.setFont(font);
        __qlistwidgetitem18 = QListWidgetItem(self.listWidget_7)
        __qlistwidgetitem18.setFont(font);
        __qlistwidgetitem19 = QListWidgetItem(self.listWidget_7)
        __qlistwidgetitem19.setFont(font);
        self.listWidget_7.setObjectName(u"listWidget_7")
        self.listWidget_7.setGeometry(QRect(450, 180, 151, 251))
        self.listWidget_7.setAutoFillBackground(False)
        self.listWidget_7.setSpacing(6)
        self.pushButton_7 = QPushButton(self.telegram)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(43, 280, 61, 41))
        self.pushButton_7.setFont(font1)
        self.label_15 = QLabel(self.telegram)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(200, 130, 51, 41))
        self.label_15.setFont(font3)
        self.label_13 = QLabel(self.telegram)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(485, 130, 81, 41))
        self.label_13.setFont(font3)
        self.listWidget_5 = QListWidget(self.telegram)
        __qlistwidgetitem20 = QListWidgetItem(self.listWidget_5)
        __qlistwidgetitem20.setFont(font);
        __qlistwidgetitem21 = QListWidgetItem(self.listWidget_5)
        __qlistwidgetitem21.setFont(font);
        __qlistwidgetitem22 = QListWidgetItem(self.listWidget_5)
        __qlistwidgetitem22.setFont(font);
        self.listWidget_5.setObjectName(u"listWidget_5")
        self.listWidget_5.setGeometry(QRect(300, 180, 151, 251))
        self.listWidget_5.setAutoFillBackground(False)
        self.listWidget_5.setSpacing(6)
        self.pushButton_6 = QPushButton(self.telegram)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(40, 200, 71, 71))
        self.pushButton_6.setStyleSheet(u"image: url(:/otherImage/1.jpg)")
        self.label_6 = QLabel(self.telegram)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(570, 470, 49, 16))
        self.label_14 = QLabel(self.telegram)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(315, 130, 111, 41))
        self.label_14.setFont(font3)
        self.listWidget_6 = QListWidget(self.telegram)
        brush4 = QBrush(QColor(104, 104, 104, 255))
        brush4.setStyle(Qt.Dense6Pattern)
        __qlistwidgetitem23 = QListWidgetItem(self.listWidget_6)
        __qlistwidgetitem23.setFont(font);
        __qlistwidgetitem23.setBackground(brush4);
        QListWidgetItem(self.listWidget_6)
        __qlistwidgetitem24 = QListWidgetItem(self.listWidget_6)
        __qlistwidgetitem24.setFont(font);
        __qlistwidgetitem25 = QListWidgetItem(self.listWidget_6)
        __qlistwidgetitem25.setFont(font);
        __qlistwidgetitem26 = QListWidgetItem(self.listWidget_6)
        __qlistwidgetitem26.setFont(font);
        __qlistwidgetitem27 = QListWidgetItem(self.listWidget_6)
        __qlistwidgetitem27.setFont(font);
        self.listWidget_6.setObjectName(u"listWidget_6")
        self.listWidget_6.setGeometry(QRect(150, 180, 151, 251))
        self.listWidget_6.setAutoFillBackground(False)
        self.listWidget_6.setSpacing(6)
        self.pushButton = QPushButton(self.telegram)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(520, 450, 75, 24))
        self.stackedWidget.addWidget(self.telegram)
        self.telegram_text = QWidget()
        self.telegram_text.setObjectName(u"telegram_text")
        self.listWidget_10 = QListWidget(self.telegram_text)
        __qlistwidgetitem28 = QListWidgetItem(self.listWidget_10)
        __qlistwidgetitem28.setFont(font);
        __qlistwidgetitem29 = QListWidgetItem(self.listWidget_10)
        __qlistwidgetitem29.setFont(font);
        __qlistwidgetitem30 = QListWidgetItem(self.listWidget_10)
        __qlistwidgetitem30.setFont(font);
        self.listWidget_10.setObjectName(u"listWidget_10")
        self.listWidget_10.setGeometry(QRect(455, 130, 151, 131))
        self.listWidget_10.setAutoFillBackground(False)
        self.listWidget_10.setSpacing(6)
        self.pushButton_23 = QPushButton(self.telegram_text)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(40, 200, 71, 71))
        self.pushButton_23.setStyleSheet(u"image: url(:/otherImage/1.jpg)")
        self.pushButton_22 = QPushButton(self.telegram_text)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(43, 280, 61, 41))
        self.pushButton_22.setFont(font1)
        self.label_22 = QLabel(self.telegram_text)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(320, 80, 111, 41))
        self.label_22.setFont(font3)
        self.listWidget_9 = QListWidget(self.telegram_text)
        __qlistwidgetitem31 = QListWidgetItem(self.listWidget_9)
        __qlistwidgetitem31.setFont(font);
        __qlistwidgetitem32 = QListWidgetItem(self.listWidget_9)
        __qlistwidgetitem32.setFont(font);
        __qlistwidgetitem33 = QListWidgetItem(self.listWidget_9)
        __qlistwidgetitem33.setFont(font);
        self.listWidget_9.setObjectName(u"listWidget_9")
        self.listWidget_9.setGeometry(QRect(305, 130, 151, 131))
        self.listWidget_9.setAutoFillBackground(False)
        self.listWidget_9.setSpacing(6)
        self.listWidget_11 = QListWidget(self.telegram_text)
        brush5 = QBrush(QColor(104, 104, 104, 255))
        brush5.setStyle(Qt.Dense6Pattern)
        __qlistwidgetitem34 = QListWidgetItem(self.listWidget_11)
        __qlistwidgetitem34.setFont(font);
        __qlistwidgetitem34.setBackground(brush5);
        QListWidgetItem(self.listWidget_11)
        __qlistwidgetitem35 = QListWidgetItem(self.listWidget_11)
        __qlistwidgetitem35.setFont(font);
        __qlistwidgetitem36 = QListWidgetItem(self.listWidget_11)
        __qlistwidgetitem36.setFont(font);
        __qlistwidgetitem37 = QListWidgetItem(self.listWidget_11)
        __qlistwidgetitem37.setFont(font);
        __qlistwidgetitem38 = QListWidgetItem(self.listWidget_11)
        __qlistwidgetitem38.setFont(font);
        self.listWidget_11.setObjectName(u"listWidget_11")
        self.listWidget_11.setGeometry(QRect(155, 130, 151, 131))
        self.listWidget_11.setAutoFillBackground(False)
        self.listWidget_11.setSpacing(6)
        self.label_8 = QLabel(self.telegram_text)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(570, 470, 49, 16))
        self.label_16 = QLabel(self.telegram_text)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(205, 80, 51, 41))
        self.label_16.setFont(font3)
        self.label_21 = QLabel(self.telegram_text)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(490, 80, 81, 41))
        self.label_21.setFont(font3)
        self.label = QLabel(self.telegram_text)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 330, 31, 21))
        self.lineEdit_2 = QLineEdit(self.telegram_text)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(230, 330, 211, 21))
        self.label_23 = QLabel(self.telegram_text)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(190, 380, 51, 21))
        self.media_In = QLineEdit(self.telegram_text)
        self.media_In.setObjectName(u"media_In")
        self.media_In.setGeometry(QRect(240, 380, 171, 21))
        self.toolButton = QToolButton(self.telegram_text)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(420, 380, 21, 22))
        self.pushButton_24 = QPushButton(self.telegram_text)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(360, 420, 75, 24))
        self.stackedWidget.addWidget(self.telegram_text)
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.label_3 = QLabel(self.Home)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-30, 40, 721, 541))
        self.label_3.setStyleSheet(u"image: url(:/wholeBody/3002 final model render 200.jpg)")
        self.Key2 = QPushButton(self.Home)
        self.Key2.setObjectName(u"Key2")
        self.Key2.setGeometry(QRect(270, 170, 121, 81))
        font6 = QFont()
        font6.setFamilies([u"Dubai Medium"])
        font6.setPointSize(22)
        self.Key2.setFont(font6)
        self.Key1 = QPushButton(self.Home)
        self.Key1.setObjectName(u"Key1")
        self.Key1.setGeometry(QRect(130, 170, 121, 81))
        self.Key1.setFont(font6)
        self.Key3 = QPushButton(self.Home)
        self.Key3.setObjectName(u"Key3")
        self.Key3.setGeometry(QRect(420, 170, 121, 81))
        self.Key3.setFont(font6)
        self.Key21 = QPushButton(self.Home)
        self.Key21.setObjectName(u"Key21")
        self.Key21.setGeometry(QRect(150, 50, 81, 101))
        font7 = QFont()
        font7.setFamilies([u"Dubai Medium"])
        font7.setPointSize(36)
        self.Key21.setFont(font7)
        self.Key21.setStyleSheet(u"image: url(:/otherImage/WhatsApp Image 2023-05-29 at 18..jpg)")
        self.Key22 = QPushButton(self.Home)
        self.Key22.setObjectName(u"Key22")
        self.Key22.setGeometry(QRect(290, 50, 81, 101))
        self.Key22.setFont(font7)
        self.Key22.setStyleSheet(u"image: url(:/otherImage/WhatsApp Image 2023-05-29 at 18.17.41.jpg)")
        self.Key23 = QPushButton(self.Home)
        self.Key23.setObjectName(u"Key23")
        self.Key23.setGeometry(QRect(430, 50, 81, 101))
        self.Key23.setFont(font7)
        self.Key23.setStyleSheet(u"image: url(:/otherImage/WhatsApp Image 2023-05-29 at 18.17.40.jpg)")
        self.stackedWidget.addWidget(self.Home)
        self.subject = QWidget()
        self.subject.setObjectName(u"subject")
        self.listWidget = QListWidget(self.subject)
        __qlistwidgetitem39 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem39.setFont(font);
        __qlistwidgetitem40 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem40.setFont(font);
        __qlistwidgetitem41 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem41.setFont(font);
        __qlistwidgetitem42 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem42.setFont(font);
        __qlistwidgetitem43 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem43.setFont(font);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(150, 180, 151, 251))
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setSpacing(6)
        self.listWidget_2 = QListWidget(self.subject)
        __qlistwidgetitem44 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem44.setFont(font);
        __qlistwidgetitem45 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem45.setFont(font);
        __qlistwidgetitem46 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem46.setFont(font);
        __qlistwidgetitem47 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem47.setFont(font);
        __qlistwidgetitem48 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem48.setFont(font);
        __qlistwidgetitem49 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem49.setFont(font);
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(300, 180, 151, 251))
        self.listWidget_2.setAutoFillBackground(False)
        self.listWidget_2.setSpacing(6)
        self.listWidget_3 = QListWidget(self.subject)
        __qlistwidgetitem50 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem50.setFont(font);
        __qlistwidgetitem51 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem51.setFont(font);
        __qlistwidgetitem52 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem52.setFont(font);
        __qlistwidgetitem53 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem53.setFont(font);
        __qlistwidgetitem54 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem54.setFont(font);
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setGeometry(QRect(450, 180, 151, 251))
        self.listWidget_3.setAutoFillBackground(False)
        self.listWidget_3.setSpacing(6)
        self.sb_key = QPushButton(self.subject)
        self.sb_key.setObjectName(u"sb_key")
        self.sb_key.setGeometry(QRect(43, 280, 61, 41))
        self.sb_key.setFont(font1)
        self.label_4 = QLabel(self.subject)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(570, 470, 49, 16))
        self.sb_main = QPushButton(self.subject)
        self.sb_main.setObjectName(u"sb_main")
        self.sb_main.setGeometry(QRect(40, 200, 71, 71))
        self.sb_main.setStyleSheet(u"image: url(:/otherImage/1.jpg)")
        self.label_9 = QLabel(self.subject)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(200, 130, 51, 41))
        self.label_9.setFont(font3)
        self.label_10 = QLabel(self.subject)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(330, 130, 81, 41))
        self.label_10.setFont(font3)
        self.label_11 = QLabel(self.subject)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(485, 130, 81, 41))
        self.label_11.setFont(font3)
        self.sb_next = QPushButton(self.subject)
        self.sb_next.setObjectName(u"sb_next")
        self.sb_next.setGeometry(QRect(440, 468, 101, 51))
        self.sb_next.setFont(font2)
        self.stackedWidget.addWidget(self.subject)

        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Workie Clickie", None))

        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_4.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"Chrome", None));
        ___qlistwidgetitem1 = self.listWidget_4.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog", u"Zoom", None));
        ___qlistwidgetitem2 = self.listWidget_4.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog", u"Microsoft Todo List", None));
        ___qlistwidgetitem3 = self.listWidget_4.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Dialog", u"Microsoft Calender", None));
        ___qlistwidgetitem4 = self.listWidget_4.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Dialog", u"Telegram", None));
        self.listWidget_4.setSortingEnabled(__sortingEnabled)

        self.label_5.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Key 1", None))
        self.url_finish.setText(QCoreApplication.translate("Dialog", u"finished", None))
        self.pushButton_5.setText("")
#if QT_CONFIG(accessibility)
        self.url_in.setAccessibleDescription(QCoreApplication.translate("Dialog", u"e.g. www.youtube.com", None))
#endif // QT_CONFIG(accessibility)
        self.url_in.setText("")
        self.url_in.setPlaceholderText(QCoreApplication.translate("Dialog", u"e.g. www.youtube.com", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Type Below:", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"App", None))
        self.pushButton_12.setText(QCoreApplication.translate("Dialog", u"Key 1", None))
        self.pushButton_11.setText("")
        self.pushButton_13.setText("")
        self.pushButton_14.setText("")
        self.pushButton_15.setText("")
        self.pushButton_16.setText("")
        self.pushButton_17.setText("")
        self.pushButton_18.setText("")
        self.pushButton_19.setText("")
        self.pushButton_20.setText("")
        self.pushButton_21.setText("")
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Macro", None))

        __sortingEnabled1 = self.listWidget_8.isSortingEnabled()
        self.listWidget_8.setSortingEnabled(False)
        ___qlistwidgetitem5 = self.listWidget_8.item(0)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Dialog", u"Action recording", None));
        ___qlistwidgetitem6 = self.listWidget_8.item(1)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Dialog", u"Notification", None));
        ___qlistwidgetitem7 = self.listWidget_8.item(2)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Dialog", u"Voice Chat", None));
        ___qlistwidgetitem8 = self.listWidget_8.item(3)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("Dialog", u"Change wallpaper", None));
        ___qlistwidgetitem9 = self.listWidget_8.item(4)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("Dialog", u"Mp3 player", None));
        ___qlistwidgetitem10 = self.listWidget_8.item(5)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("Dialog", u"New desktop", None));
        self.listWidget_8.setSortingEnabled(__sortingEnabled1)

        self.label_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"Key 1", None))
        self.pushButton_10.setText("")
        self.label_18.setText(QCoreApplication.translate("Dialog", u"You can press this button ", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"whenever you are ok,", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"It will start after you press", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Press \"space\" to stop", None))
        self.sb_key_2.setText(QCoreApplication.translate("Dialog", u"Key 1", None))
        self.label_25.setText("")

        __sortingEnabled2 = self.listWidget_12.isSortingEnabled()
        self.listWidget_12.setSortingEnabled(False)
        ___qlistwidgetitem11 = self.listWidget_12.item(0)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("Dialog", u"Notification", None));
        ___qlistwidgetitem12 = self.listWidget_12.item(2)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("Dialog", u"Action recording", None));
        ___qlistwidgetitem13 = self.listWidget_12.item(3)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("Dialog", u"Voice Chat", None));
        ___qlistwidgetitem14 = self.listWidget_12.item(4)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("Dialog", u"Change wallpaper", None));
        ___qlistwidgetitem15 = self.listWidget_12.item(5)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("Dialog", u"Mp3 player", None));
        ___qlistwidgetitem16 = self.listWidget_12.item(6)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("Dialog", u"Window control", None));
        self.listWidget_12.setSortingEnabled(__sortingEnabled2)

        self.label_27.setText(QCoreApplication.translate("Dialog", u"Macro", None))
        self.notification_finish.setText(QCoreApplication.translate("Dialog", u"Finish", None))
        self.sb_main_2.setText("")
        self.label_26.setText(QCoreApplication.translate("Dialog", u"Title:", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"Content:", None))

        __sortingEnabled3 = self.listWidget_7.isSortingEnabled()
        self.listWidget_7.setSortingEnabled(False)
        ___qlistwidgetitem17 = self.listWidget_7.item(0)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("Dialog", u"Text", None));
        ___qlistwidgetitem18 = self.listWidget_7.item(1)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("Dialog", u"Media", None));
        self.listWidget_7.setSortingEnabled(__sortingEnabled3)

        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Key 1", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"App", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Action", None))

        __sortingEnabled4 = self.listWidget_5.isSortingEnabled()
        self.listWidget_5.setSortingEnabled(False)
        ___qlistwidgetitem19 = self.listWidget_5.item(0)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("Dialog", u"Boss", None));
        ___qlistwidgetitem20 = self.listWidget_5.item(1)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("Dialog", u"Andrew Li", None));
        ___qlistwidgetitem21 = self.listWidget_5.item(2)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("Dialog", u"Carl", None));
        self.listWidget_5.setSortingEnabled(__sortingEnabled4)

        self.pushButton_6.setText("")
        self.label_6.setText("")
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Contacts", None))

        __sortingEnabled5 = self.listWidget_6.isSortingEnabled()
        self.listWidget_6.setSortingEnabled(False)
        ___qlistwidgetitem22 = self.listWidget_6.item(0)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("Dialog", u"Telegram", None));
        ___qlistwidgetitem23 = self.listWidget_6.item(2)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("Dialog", u"Chrome", None));
        ___qlistwidgetitem24 = self.listWidget_6.item(3)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("Dialog", u"Zoom", None));
        ___qlistwidgetitem25 = self.listWidget_6.item(4)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("Dialog", u"Microsoft Todo List", None));
        ___qlistwidgetitem26 = self.listWidget_6.item(5)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("Dialog", u"Microsoft Calender", None));
        self.listWidget_6.setSortingEnabled(__sortingEnabled5)

        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))

        __sortingEnabled6 = self.listWidget_10.isSortingEnabled()
        self.listWidget_10.setSortingEnabled(False)
        ___qlistwidgetitem27 = self.listWidget_10.item(0)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("Dialog", u"Text", None));
        ___qlistwidgetitem28 = self.listWidget_10.item(1)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("Dialog", u"Media", None));
        self.listWidget_10.setSortingEnabled(__sortingEnabled6)

        self.pushButton_23.setText("")
        self.pushButton_22.setText(QCoreApplication.translate("Dialog", u"Key 1", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"Contacts", None))

        __sortingEnabled7 = self.listWidget_9.isSortingEnabled()
        self.listWidget_9.setSortingEnabled(False)
        ___qlistwidgetitem29 = self.listWidget_9.item(0)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("Dialog", u"Boss", None));
        ___qlistwidgetitem30 = self.listWidget_9.item(1)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("Dialog", u"Andrew Li", None));
        ___qlistwidgetitem31 = self.listWidget_9.item(2)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("Dialog", u"Carl", None));
        self.listWidget_9.setSortingEnabled(__sortingEnabled7)


        __sortingEnabled8 = self.listWidget_11.isSortingEnabled()
        self.listWidget_11.setSortingEnabled(False)
        ___qlistwidgetitem32 = self.listWidget_11.item(0)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("Dialog", u"Telegram", None));
        ___qlistwidgetitem33 = self.listWidget_11.item(2)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("Dialog", u"Chrome", None));
        ___qlistwidgetitem34 = self.listWidget_11.item(3)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("Dialog", u"Zoom", None));
        ___qlistwidgetitem35 = self.listWidget_11.item(4)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("Dialog", u"Microsoft Todo List", None));
        ___qlistwidgetitem36 = self.listWidget_11.item(5)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("Dialog", u"Microsoft Calender", None));
        self.listWidget_11.setSortingEnabled(__sortingEnabled8)

        self.label_8.setText("")
        self.label_16.setText(QCoreApplication.translate("Dialog", u"App", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"Action", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Text:", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"Media:", None))
        self.toolButton.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.pushButton_24.setText(QCoreApplication.translate("Dialog", u"Finish", None))
        self.label_3.setText("")
        self.Key2.setText(QCoreApplication.translate("Dialog", u"Key 2", None))
        self.Key1.setText(QCoreApplication.translate("Dialog", u"Key 1", None))
        self.Key3.setText(QCoreApplication.translate("Dialog", u"Key 3", None))
        self.Key21.setText("")
        self.Key22.setText("")
        self.Key23.setText("")

        __sortingEnabled9 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem37 = self.listWidget.item(0)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("Dialog", u"Chrome", None));
        ___qlistwidgetitem38 = self.listWidget.item(1)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("Dialog", u"Zoom", None));
        ___qlistwidgetitem39 = self.listWidget.item(2)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("Dialog", u"Outlook", None));
        ___qlistwidgetitem40 = self.listWidget.item(3)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("Dialog", u"Excel", None));
        ___qlistwidgetitem41 = self.listWidget.item(4)
        ___qlistwidgetitem41.setText(QCoreApplication.translate("Dialog", u"Telegram", None));
        self.listWidget.setSortingEnabled(__sortingEnabled9)


        __sortingEnabled10 = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem42 = self.listWidget_2.item(0)
        ___qlistwidgetitem42.setText(QCoreApplication.translate("Dialog", u"Action recording", None));
        ___qlistwidgetitem43 = self.listWidget_2.item(1)
        ___qlistwidgetitem43.setText(QCoreApplication.translate("Dialog", u"Notification", None));
        ___qlistwidgetitem44 = self.listWidget_2.item(2)
        ___qlistwidgetitem44.setText(QCoreApplication.translate("Dialog", u"Voice Chat", None));
        ___qlistwidgetitem45 = self.listWidget_2.item(3)
        ___qlistwidgetitem45.setText(QCoreApplication.translate("Dialog", u"Change wallpaper", None));
        ___qlistwidgetitem46 = self.listWidget_2.item(4)
        ___qlistwidgetitem46.setText(QCoreApplication.translate("Dialog", u"Mp3 player", None));
        ___qlistwidgetitem47 = self.listWidget_2.item(5)
        ___qlistwidgetitem47.setText(QCoreApplication.translate("Dialog", u"Window control", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled10)


        __sortingEnabled11 = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        ___qlistwidgetitem48 = self.listWidget_3.item(0)
        ___qlistwidgetitem48.setText(QCoreApplication.translate("Dialog", u"Design Project", None));
        ___qlistwidgetitem49 = self.listWidget_3.item(1)
        ___qlistwidgetitem49.setText(QCoreApplication.translate("Dialog", u"Study Mode", None));
        ___qlistwidgetitem50 = self.listWidget_3.item(2)
        ___qlistwidgetitem50.setText(QCoreApplication.translate("Dialog", u"Meeting Mode", None));
        ___qlistwidgetitem51 = self.listWidget_3.item(3)
        ___qlistwidgetitem51.setText(QCoreApplication.translate("Dialog", u"Clear Screen", None));
        self.listWidget_3.setSortingEnabled(__sortingEnabled11)

        self.sb_key.setText(QCoreApplication.translate("Dialog", u"Key 1", None))
        self.label_4.setText("")
        self.sb_main.setText("")
        self.label_9.setText(QCoreApplication.translate("Dialog", u"App", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Macro", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Modes", None))
        self.sb_next.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

