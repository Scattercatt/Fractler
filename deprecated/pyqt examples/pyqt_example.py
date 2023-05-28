import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPainter, QColor, QImage
import ctypes
import random

user32 = ctypes.windll.user32
SCREEN_WIDTH = user32.GetSystemMetrics(0)
SCREEN_HEIGHT = user32.GetSystemMetrics(1)

class MyWindow(QMainWindow):
    def __init__(self): 
        super(MyWindow, self).__init__()
        WINDOW_SIZE_X = 800
        WINDOW_SIZE_Y = 600

        self.setWindowTitle('My Window')

        POSX = round(SCREEN_WIDTH / 2 - WINDOW_SIZE_X / 2)
        POSY = round(SCREEN_HEIGHT / 2 - WINDOW_SIZE_Y / 2)
        self.setGeometry(POSX, POSY, WINDOW_SIZE_X, WINDOW_SIZE_Y)

        btn = QPushButton("Exit", self)

        btn.clicked.connect(QApplication.quit)

        btn.resize(100, 100) # Can resize and move widgets freely!!
        btn.move(100, 100)


        btn = QPushButton("Hello", self)

        btn.clicked.connect(self.print_hello)

        btn.resize(100, 100) 
        btn.move(200, 100)


    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.setPen(QColor(255, 0, 0))


        color = random.randrange(0, 256)
        painter.drawPoint(10, 10)
        # painter.fillRect(30, 50, 90, 80, QColor(0, color, 0))

        image = QImage(255, 255, QImage.Format.Format_RGB32)

        for ix in range(255):
            for iy in range(255):
                my_color = QColor(ix, color, iy)
                image.setPixel(ix, iy, my_color.rgb())
        
        painter.drawImage(0, 0, image)

        painter.end()



        
    
    def print_hello(self):
        self.update()



        

def run():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()