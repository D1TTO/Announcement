#!/usr/bin/python
# simple text box with configurable font size
# require the price as script argument
myFontSize = 60

from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
import os
import pygame

def main():

    path = '/home/pi/ShareFile/ClockAnnounce'
    name = ''
    for filename in os.listdir(path):
       name = filename
    f = open(path+'/'+name, 'r')
    text = f.read()
    app     = QtGui.QApplication(sys.argv)
    palette = QtGui.QPalette()
    label   = QtGui.QLabel(text)
    label.setWordWrap(True)
    label.setStyleSheet("background-color:#000000;")
    label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)

    palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.white)
    label.setPalette(palette)

    label.showFullScreen()
    font = label.font()
    font.setPixelSize(myFontSize)
    label.setFont(font)

    label.setWindowTitle('PyQt QLabel Text Color')
    label.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
