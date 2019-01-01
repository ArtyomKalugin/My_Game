import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PERFOMANCE import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Perfomance Alpha')

        self.mouse_coords = []

        self.pencil_clear.clicked.connect(self.clearCoords)

        self.pencil_choose_check = False
        self.pencil_choose.clicked.connect(self.runPencil)

        self.set_size_pencil.clicked.connect(self.setSizePencil)
        self.pencil_size = 1

        self.set_color_pencil.clicked.connect(self.setColorPencil)
        self.color = QColor(0, 0, 0)

    def clearCoords(self):
        self.mouse_coords = []
        self.update()

    def mouseMoveEvent(self, event):
        if self.pencil_choose_check:
            self.mouse_coords.append((event.x(), event.y()))
            self.update()

    def paintEvent(self, event):
        picture = QPainter()
        picture.begin(self)
        self.drawFigure(picture)
        picture.end()

    def drawFigure(self, picture):
        if self.pencil_choose_check:
            picture.setPen(QPen(QColor(self.color), self.pencil_size))
            for i in range(len(self.mouse_coords)):
                elem = self.mouse_coords[i]
                if i != 0:
                    elemlast = self.mouse_coords[i - 1]
                    picture.drawLine(elemlast[0], elemlast[1], elem[0], elem[1])
                else:
                    picture.drawLine(elem[0], elem[1], elem[0], elem[1])

    def runPencil(self):
        self.pencil_choose_check = True

    def setSizePencil(self):
        size, okBtnPressed = QInputDialog.getInt(
            self, "Толщина карандаша", "Выберите толщину:", 1, 1, 20, 1
        )
        if okBtnPressed:
            self.pencil_size = size
            self.set_size_pencil.setText('Толщина: ' + str(size))

    def setColorPencil(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.set_color_pencil.setStyleSheet(
                "background-color: {}".format(color.name())
            )

            self.color = color.name()
            print(self.color)


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())
