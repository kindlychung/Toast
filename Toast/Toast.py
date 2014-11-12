#!/usr/bin/env python3
import sys, time
from PySide import QtCore, QtGui
import base64


# Usage: Toast('Message')
class Toast(QtGui.QDialog):
    def __init__(self, title, msg, duration=2):
        QtGui.QDialog.__init__(self)
        self.duration = duration
        self.title_label = QtGui.QLabel(self.make_bold(title))
        self.title_label.setWordWrap(True)
        # self.title_label.setAlignment(QtCore.Qt.AlignLeft)
        self.msg_label = QtGui.QLabel(msg)
        self.msg_label.setWordWrap(True)
        self.icon_button = QLabelButton()
        img_b64 = "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAITgAACE4BjDEA7AAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAABJdEVYdENvcHlyaWdodABQdWJsaWMgRG9tYWluIGh0dHA6Ly9jcmVhdGl2ZWNvbW1vbnMub3JnL2xpY2Vuc2VzL3B1YmxpY2RvbWFpbi9Zw/7KAAAB2ElEQVRIibWVPW/TUBiFz7mJTBFSGgnUqmABRgpMUYi53pCK1IWxUxd2BgYk/goDAzuq+AFILEhIZUuq/ACPrYRKGSJPdHkPQx3UOK7tJOKd7Guf57nXH++lJFRVr9e70el03pLcBnAnH/4t6SzLsvdpml5U5duVdABhGDLLsj6AjSvD9wFshWHIujzrVgBcrqLb7b6U9AoASH6aTqdf62YPAK6WDiBN0wszO52dm9lpEzhQs4LhcNhzzj13zj2TtDUXJH+Z2bGZ/ZhMJulSApL03r+WtNdoluS38Xj8USWw0kcUx/F+UzgASNqL43i/7NqCwHu/A+CgKfxKHeTZagGAPsnWsvQ8028ieLIsvCq7IJD0eFV6WXZO4L3fzFvCSkVy23u/ea2A5KNV4dcx5gRm9nBdQZFRfAcP1hUUGXMC59zagiLjn2AwGNwCsPCjrFA7OWteEATBrqRG3bWqJLkgCHZn523gsrnFcdwi+YXkrGEJAMxMs+OSonNutukwF9DMWiQpSUyS5Kmku+vOvKzM7KxtZu8A3PwfAgB/2iQ/m9m9qrtIxgBuF4bPJY1qBD8b7clJkryQ9KYg/TAajb7XZRt9NVEUHUk6BHAC4ETSYRRFR02yfwEMBLRPQVtfqgAAAABJRU5ErkJggg=="
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(base64.b64decode(img_b64))
        self.icon_button.setPixmap(pixmap)
        self.icon_button.resize(20, 20)
        self.connect(self.icon_button, QtCore.SIGNAL("clicked()"), self.close_all)

        title_layout = QtGui.QVBoxLayout()
        title_layout.addWidget(self.title_label)
        title_layout.addWidget(self.msg_label)
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.icon_button)
        layout.addLayout(title_layout, 1)
        self.setGeometry(0, 0, 300, 100)
        self.setLayout(layout)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setStyleSheet("border: 1px solid red; border-radius: 5px;")
        self.toastThread = ToastThread(self.duration)
        self.toastThread.finished.connect(self.close_all)
        self.toastThread.start()

    def close_all(self):
        self.toastThread.terminate()
        self.close()

    def make_bold(self, text):
        return "<b>" + text + "</b>"



class ToastThread(QtCore.QThread):
    def __init__(self, n_seconds):
        QtCore.QThread.__init__(self)
        self.n_seconds = n_seconds
    def run(self):
        time.sleep(self.n_seconds)

class QLabelButton(QtGui.QLabel):
    def __init(self, parent):
        QLabel.__init__(self, parent)
    def mouseReleaseEvent(self, ev):
        self.emit(QtCore.SIGNAL('clicked()'))

def toast(title, msg, duration):
    app = QtGui.QApplication(sys.argv)
    toast = Toast(title, msg, duration)
    toast.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    toast("Important message", "You have won 1000 euros, what are you waiting for? Come and get it!", 10)
