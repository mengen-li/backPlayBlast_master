# -*- coding: utf-8 -*-
import sys
from PyQt4.QtGui import (QPushButton, QWidget, QLineEdit, QApplication,QDrag)
from PyQt4.QtCore import Qt,QMimeData


class Button(QPushButton):
    def __init__(self, title, parent):
        super(Button, self).__init__(title,parent)

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.LeftButton:
            return

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        # drag.setHotSpot(e.pos() - self.rect().topLeft())

        drag.exec_(Qt.MoveAction)                          # dropAcion

    def mousePressEvent(self, e):
        QPushButton.mousePressEvent(self, e)

        if e.button() == Qt.RightButton:
            print("press")


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.button = Button("Button", self)
        self.button.move(100, 65)

        self.setWindowTitle("Click or Move")
        self.setGeometry(300, 300, 280, 150)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
