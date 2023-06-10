from win10toast import ToastNotifier

class NotificationHandler:
    def __init__(self):
        self.toast = ToastNotifier()

    def show_notification(self, title, message):
        self.toast.show_toast(
            title,
            message,
            duration = 20,
            icon_path = "icon.ico",
            threaded = True,
        )



# from PyQt6.QtGui import QIcon
# from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
# from PyQt6.QtCore import Qt


# class Notification:

#     def __init__(self):
#         self.app = QApplication([])
#         self.system_tray_icon = QSystemTrayIcon(QIcon('icon.ico'), self.app)
#         self.system_tray_icon.setVisible(True)

#     def show_notification(self, title, message):
#         notification = QMenu()
#         notification.addAction(QAction(QIcon('icon.ico'), title))
#         notification.addAction(QAction(message))
#         self.system_tray_icon.setContextMenu(notification)
#         self.system_tray_icon.activated.connect(self.notification_activated)

#     def notification_activated(self, reason):
#         if reason == QSystemTrayIcon.ActivationReason.Trigger:
#             print('Notification clicked')
#         elif reason == QSystemTrayIcon.ActivationReason.Context:
#             print('Notification closed')
#         self.app.quit()

#     def run(self):
#         self.app.exec()


# if __name__ == '__main__':
#     notification = Notification()
#     notification.show_notification('Notification Title', 'Notification Message')
#     notification.run()