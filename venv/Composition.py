import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PERFOMANCE import Ui_MainWindow
from random import choice


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Perfomance Alpha')
        #self.setStyleSheet("background-color: blue;")

        self.mouse_coords = [[]]
        self.amount = 0

        self.pencil_clear.clicked.connect(self.clearCoords)

        self.pencil_choose_check = False
        self.pencil_choose.clicked.connect(self.runPencil)

        self.set_size_pencil.clicked.connect(self.setSizePencil)
        self.pencil_size = 1

        self.set_color_pencil.clicked.connect(self.setColorPencil)
        self.pencil_color = QColor(0, 0, 0)
        pen = QPen(QColor(self.pencil_color), self.pencil_size)
        self.all_colors_pencil = [[pen]]

        self.rainbow.clicked.connect(self.runRainbow)
        self.rainbow_choose_check = False

        self.line_choose_check = False
        self.line_choose.clicked.connect(self.runLine)

        self.mouse_coords_line = [[]]
        self.amountline = 0
        self.mouse_pos_line = None
        self.mouse_stcoords_line = None

        self.set_color_line.clicked.connect(self.setColorLine)
        self.all_colors_line = [[]]
        self.line_color = QColor(0, 0, 0)

        self.set_size_line.clicked.connect(self.setSizeLine)
        self.line_size = 1

        self.line_clear.clicked.connect(self.clearLineCoords)

        self.ell_choose_check = False
        self.ell_choose.clicked.connect(self.runEllipse)

        self.mouse_pos_ell = None
        self.mouse_stcoords_ell = None
        self.amountell = 0
        self.mouse_coords_ell = [[]]

        self.set_color_ell.clicked.connect(self.setColorEllipse)
        self.all_colors_ell = [[]]
        self.ell_color = QColor(0, 0, 0)

        self.set_size_ell.clicked.connect(self.setSizeEllipse)
        self.ell_size = 1

        self.set_nocolor_ell.clicked.connect(self.setNoColorEllipse)
        self.ell_nocolor = False

        self.ell_clear.clicked.connect(self.clearEllipseCoords)

        self.rect_choose_check = False
        self.rect_choose.clicked.connect(self.runRectangle)

        self.mouse_pos_rect = None
        self.mouse_stcoords_rect = None
        self.amountrect = 0
        self.mouse_coords_rect = [[]]

        self.set_color_rect.clicked.connect(self.setColorRectangle)
        self.all_colors_rect = [[]]
        self.rect_color = QColor(0, 0, 0)

        self.set_size_rect.clicked.connect(self.setSizeRectangle)
        self.rect_size = 1

        self.set_nocolor_rect.clicked.connect(self.setNoColorRectangle)
        self.rect_nocolor = False

        self.rect_clear.clicked.connect(self.clearRectangleCoords)

    def clearCoords(self):
        self.mouse_coords = [[]]
        pen = QPen(QColor(self.pencil_color), self.pencil_size)
        self.all_colors_pencil = [[pen]]
        self.amount = 0
        self.update()

    def mouseMoveEvent(self, event):
        if self.pencil_choose_check:
            self.mouse_coords[self.amount].append((event.x(), event.y()))
            self.update()
            if self.rainbow_choose_check:
                r = choice(range(256))
                g = choice(range(256))
                b = choice(range(256))
                color = QPen(QColor(r, g, b), self.pencil_size)
                self.all_colors_pencil[self.amount].append(color)
            else:
                pen = QPen(QColor(self.pencil_color), self.pencil_size)
                self.all_colors_pencil[self.amount].append(pen)

        if self.line_choose_check:
            self.mouse_pos_line = event.pos()
            self.update()

        if self.ell_choose_check:
            self.mouse_pos_ell = event.pos()
            self.update()

        if self.rect_choose_check:
            self.mouse_pos_rect = event.pos()
            self.update()

    def mousePressEvent(self, event):
        if self.line_choose_check:
            self.mouse_stcoords_line = event.pos()

        if self.ell_choose_check:
            self.mouse_stcoords_ell = event.pos()

        if self.rect_choose_check:
            self.mouse_stcoords_rect = event.pos()

    def mouseReleaseEvent(self, event):
        if self.pencil_choose_check:
            self.mouse_coords.append([])
            self.all_colors_pencil.append([])
            self.amount += 1

        if self.line_choose_check:
            x = self.mouse_pos_line.x()
            y = self.mouse_pos_line.y()
            x_start = self.mouse_stcoords_line.x()
            y_start = self.mouse_stcoords_line.y()
            pen = QPen(QColor(self.line_color), self.line_size)
            self.all_colors_line[self.amountline].append(pen)
            self.mouse_coords_line[self.amountline].append((x_start, y_start, x, y))

            self.mouse_coords_line.append([])
            self.all_colors_line.append([])
            self.amountline += 1
            self.update()

        if self.ell_choose_check:
            x = self.mouse_pos_ell.x()
            y = self.mouse_pos_ell.y()
            x_start = self.mouse_stcoords_ell.x()
            y_start = self.mouse_stcoords_ell.y()
            if self.ell_nocolor:
                pen = ('No', self.ell_size)
            else:
                pen = (QColor(self.ell_color), self.ell_size)
            self.all_colors_ell[self.amountell].append(pen)
            self.mouse_coords_ell[self.amountell].append((x_start, y_start, x, y))

            self.mouse_coords_ell.append([])
            self.all_colors_ell.append([])
            self.amountell += 1
            self.update()

        if self.rect_choose_check:
            x = self.mouse_pos_rect.x()
            y = self.mouse_pos_rect.y()
            x_start = self.mouse_stcoords_rect.x()
            y_start = self.mouse_stcoords_rect.y()
            if self.rect_nocolor:
                pen = ('No', self.rect_size)
            else:
                pen = (QColor(self.rect_color), self.rect_size)
            self.all_colors_rect[self.amountrect].append(pen)
            self.mouse_coords_rect[self.amountrect].append((x_start, y_start, x, y))

            self.mouse_coords_rect.append([])
            self.all_colors_rect.append([])
            self.amountrect += 1
            self.update()
            print(1)

    def paintEvent(self, event):
        picture = QPainter()
        picture.begin(self)
        self.drawFigure(picture)
        picture.end()

    def drawFigure(self, picture):
        if self.pencil_choose_check:
            for j in range(len(self.mouse_coords)):
                for i in range(len(self.mouse_coords[j])):
                    picture.setPen(self.all_colors_pencil[j][i])
                    elem = self.mouse_coords[j][i]
                    if i != 0:
                        elemlast = self.mouse_coords[j][i - 1]
                        picture.drawLine(elemlast[0], elemlast[1], elem[0], elem[1])
                    else:
                        picture.drawLine(elem[0], elem[1], elem[0], elem[1])

        if self.line_choose_check:
            x = self.mouse_pos_line.x()
            y = self.mouse_pos_line.y()
            x_start = self.mouse_stcoords_line.x()
            y_start = self.mouse_stcoords_line.y()

            picture.setPen(QPen(Qt.black, 1, Qt.DashLine))
            picture.drawLine(x, y, x_start, y_start)
            for j in range(len(self.mouse_coords_line)):
                for i in range(len(self.mouse_coords_line[j])):
                    picture.setPen(self.all_colors_line[j][i])
                    elem = self.mouse_coords_line[j][i]
                    picture.drawLine(elem[0], elem[1], elem[2], elem[3])

        if self.ell_choose_check:
            x = self.mouse_pos_ell.x()
            y = self.mouse_pos_ell.y()
            x_start = self.mouse_stcoords_ell.x()
            y_start = self.mouse_stcoords_ell.y()

            picture.setPen(QPen(Qt.black, 1, Qt.DashLine))
            picture.drawEllipse(x_start, y_start, x, y)
            for j in range(len(self.mouse_coords_ell)):
                for i in range(len(self.mouse_coords_ell[j])):
                    pen = QPen(Qt.black, self.all_colors_ell[j][i][1])
                    picture.setPen(pen)
                    if self.all_colors_ell[j][i][0] == 'No':
                        picture.setBrush(Qt.NoBrush)
                    else:
                        picture.setBrush(QBrush(self.all_colors_ell[j][i][0]))
                    elem = self.mouse_coords_ell[j][i]
                    picture.drawEllipse(elem[0], elem[1], elem[2], elem[3])

        if self.rect_choose_check:
            x = self.mouse_pos_rect.x()
            y = self.mouse_pos_rect.y()
            x_start = self.mouse_stcoords_rect.x()
            y_start = self.mouse_stcoords_rect.y()

            picture.setPen(QPen(Qt.black, 1, Qt.DashLine))
            picture.drawRect(x_start, y_start, x, y)
            for j in range(len(self.mouse_coords_rect)):
                for i in range(len(self.mouse_coords_rect[j])):
                    pen = QPen(Qt.black, self.all_colors_rect[j][i][1])
                    picture.setPen(pen)
                    if self.all_colors_rect[j][i][0] == 'No':
                        picture.setBrush(Qt.NoBrush)
                    else:
                        picture.setBrush(QBrush(self.all_colors_rect[j][i][0]))
                    elem = self.mouse_coords_rect[j][i]
                    picture.drawRect(elem[0], elem[1], elem[2], elem[3])

    def runPencil(self):
        self.pencil_choose_check = True
        self.rainbow_choose_check = False
        self.line_choose_check = False
        self.figure_choose_check = False
        self.rect_choose_check = False

    def runRainbow(self):
        self.rainbow_choose_check = True

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

            self.pencil_color = color.name()

    def runLine(self):
        self.line_choose_check = True
        self.pencil_choose_check = False
        self.rainbow_choose_check = False
        self.figure_choose_check = False
        self.rect_choose_check = False

    def setColorLine(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.set_color_line.setStyleSheet(
                "background-color: {}".format(color.name())
            )

            self.line_color = color.name()

    def setSizeLine(self):
        size, okBtnPressed = QInputDialog.getInt(
            self, "Толщина линии", "Выберите толщину:", 1, 1, 20, 1
        )
        if okBtnPressed:
            self.line_size = size
            self.set_size_line.setText('Толщина: ' + str(size))

    def clearLineCoords(self):
        self.mouse_coords_line = [[]]
        pen = QPen(QColor(self.line_color), self.pencil_size)
        self.all_colors_line = [[pen]]
        self.amountline = 0
        self.update()

    def runEllipse(self):
        self.ell_choose_check = True
        self.line_choose_check = False
        self.pencil_choose_check = False
        self.rainbow_choose_check = False
        self.rect_choose_check = False

    def setColorEllipse(self):
        self.ell_nocolor = False
        color = QColorDialog.getColor()
        if color.isValid():
            self.set_color_ell.setStyleSheet(
                "background-color: {}".format(color.name())
            )

            self.ell_color = color.name()

    def setSizeEllipse(self):
        size, okBtnPressed = QInputDialog.getInt(
            self, "Толщина эллипса", "Выберите толщину:", 1, 1, 20, 1
        )
        if okBtnPressed:
            self.ell_size = size
            self.set_size_ell.setText('Толщина: ' + str(size))

    def setNoColorEllipse(self):
        self.ell_nocolor = True

    def clearEllipseCoords(self):
        self.mouse_coords_ell = [[]]
        if self.ell_nocolor:
            pen = ('No', self.ell_size)
        else:
            pen = (QColor(self.ell_color), self.ell_size)
        self.all_colors_ell = [[pen]]
        self.amountell = 0
        self.update()

    def runRectangle(self):
        self.rect_choose_check = True
        self.ell_choose_check = False
        self.line_choose_check = False
        self.pencil_choose_check = False
        self.rainbow_choose_check = False

    def setColorRectangle(self):
        self.rect_nocolor = False
        color = QColorDialog.getColor()
        if color.isValid():
            self.set_color_rect.setStyleSheet(
                "background-color: {}".format(color.name())
            )

            self.rect_color = color.name()

    def setSizeRectangle(self):
        size, okBtnPressed = QInputDialog.getInt(
            self, "Толщина прямоугольника", "Выберите толщину:", 1, 1, 20, 1
        )
        if okBtnPressed:
            self.rect_size = size
            self.set_size_rect.setText('Толщина: ' + str(size))

    def setNoColorRectangle(self):
        self.rect_nocolor = True

    def clearRectangleCoords(self):
        self.mouse_coords_rect = [[]]
        if self.rect_nocolor:
            pen = ('No', self.rect_size)
        else:
            pen = (QColor(self.rect_color), self.rect_size)
        self.all_colors_rect = [[pen]]
        self.amountrect = 0
        self.update()


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())
