# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 530)
        MainWindow.setMinimumSize(QSize(500, 500))
        MainWindow.setMaximumSize(QSize(800, 530))
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionAbrir_ = QAction(MainWindow)
        self.actionAbrir_.setObjectName(u"actionAbrir_")
        self.actionGuardar_ = QAction(MainWindow)
        self.actionGuardar_.setObjectName(u"actionGuardar_")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 20, 871, 511))
        font = QFont()
        font.setFamily(u"Arial")
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.tab1.setFont(font1)
        self.widget = QWidget(self.tab1)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 800, 500))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(500, 500))
        self.widget.setMaximumSize(QSize(800, 500))
        self.widget.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.labelColorVerde = QLabel(self.widget)
        self.labelColorVerde.setObjectName(u"labelColorVerde")
        self.labelColorVerde.setGeometry(QRect(200, 260, 95, 35))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.labelColorVerde.setFont(font2)
        self.labelColorVerde.setAlignment(Qt.AlignCenter)
        self.id = QSpinBox(self.widget)
        self.id.setObjectName(u"id")
        self.id.setGeometry(QRect(120, 50, 90, 30))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(12)
        self.id.setFont(font3)
        self.id.setCursor(QCursor(Qt.PointingHandCursor))
        self.id.setWrapping(False)
        self.id.setMaximum(9999)
        self.labelCOLOR = QLabel(self.widget)
        self.labelCOLOR.setObjectName(u"labelCOLOR")
        self.labelCOLOR.setGeometry(QRect(0, 300, 95, 35))
        self.labelCOLOR.setFont(font2)
        self.labelCOLOR.setAlignment(Qt.AlignCenter)
        self.labelColorRojo = QLabel(self.widget)
        self.labelColorRojo.setObjectName(u"labelColorRojo")
        self.labelColorRojo.setGeometry(QRect(100, 260, 95, 35))
        self.labelColorRojo.setFont(font2)
        self.labelColorRojo.setAlignment(Qt.AlignCenter)
        self.destinoY = QSpinBox(self.widget)
        self.destinoY.setObjectName(u"destinoY")
        self.destinoY.setGeometry(QRect(240, 210, 90, 30))
        self.destinoY.setFont(font3)
        self.destinoY.setCursor(QCursor(Qt.PointingHandCursor))
        self.destinoY.setWrapping(False)
        self.destinoY.setMaximum(500)
        self.rojo = QSpinBox(self.widget)
        self.rojo.setObjectName(u"rojo")
        self.rojo.setGeometry(QRect(100, 300, 90, 30))
        self.rojo.setFont(font3)
        self.rojo.setCursor(QCursor(Qt.PointingHandCursor))
        self.rojo.setWrapping(False)
        self.rojo.setMaximum(255)
        self.labelVELOCIDAD = QLabel(self.widget)
        self.labelVELOCIDAD.setObjectName(u"labelVELOCIDAD")
        self.labelVELOCIDAD.setGeometry(QRect(240, 10, 95, 35))
        self.labelVELOCIDAD.setFont(font2)
        self.labelVELOCIDAD.setAlignment(Qt.AlignCenter)
        self.labelORIGEN_X = QLabel(self.widget)
        self.labelORIGEN_X.setObjectName(u"labelORIGEN_X")
        self.labelORIGEN_X.setGeometry(QRect(120, 90, 95, 35))
        self.labelORIGEN_X.setFont(font2)
        self.labelORIGEN_X.setAlignment(Qt.AlignCenter)
        self.velocidad = QSpinBox(self.widget)
        self.velocidad.setObjectName(u"velocidad")
        self.velocidad.setGeometry(QRect(240, 50, 90, 30))
        self.velocidad.setFont(font3)
        self.velocidad.setCursor(QCursor(Qt.PointingHandCursor))
        self.velocidad.setWrapping(False)
        self.velocidad.setMaximum(9999)
        self.destinoX = QSpinBox(self.widget)
        self.destinoX.setObjectName(u"destinoX")
        self.destinoX.setGeometry(QRect(240, 130, 90, 30))
        self.destinoX.setFont(font3)
        self.destinoX.setCursor(QCursor(Qt.PointingHandCursor))
        self.destinoX.setWrapping(False)
        self.destinoX.setMaximum(500)
        self.labelDESTINO_X = QLabel(self.widget)
        self.labelDESTINO_X.setObjectName(u"labelDESTINO_X")
        self.labelDESTINO_X.setGeometry(QRect(240, 90, 95, 35))
        self.labelDESTINO_X.setFont(font2)
        self.labelDESTINO_X.setAlignment(Qt.AlignCenter)
        self.labelID = QLabel(self.widget)
        self.labelID.setObjectName(u"labelID")
        self.labelID.setGeometry(QRect(120, 10, 95, 35))
        self.labelID.setFont(font2)
        self.labelID.setAlignment(Qt.AlignCenter)
        self.labelColorAzul = QLabel(self.widget)
        self.labelColorAzul.setObjectName(u"labelColorAzul")
        self.labelColorAzul.setGeometry(QRect(300, 260, 95, 35))
        self.labelColorAzul.setFont(font2)
        self.labelColorAzul.setAlignment(Qt.AlignCenter)
        self.labelDESTINO_Y = QLabel(self.widget)
        self.labelDESTINO_Y.setObjectName(u"labelDESTINO_Y")
        self.labelDESTINO_Y.setGeometry(QRect(240, 170, 95, 35))
        self.labelDESTINO_Y.setFont(font2)
        self.labelDESTINO_Y.setAlignment(Qt.AlignCenter)
        self.verde = QSpinBox(self.widget)
        self.verde.setObjectName(u"verde")
        self.verde.setGeometry(QRect(200, 300, 90, 30))
        self.verde.setFont(font3)
        self.verde.setCursor(QCursor(Qt.PointingHandCursor))
        self.verde.setWrapping(False)
        self.verde.setMaximum(255)
        self.origenY = QSpinBox(self.widget)
        self.origenY.setObjectName(u"origenY")
        self.origenY.setGeometry(QRect(120, 210, 90, 30))
        self.origenY.setFont(font3)
        self.origenY.setCursor(QCursor(Qt.PointingHandCursor))
        self.origenY.setWrapping(False)
        self.origenY.setMaximum(500)
        self.azul = QSpinBox(self.widget)
        self.azul.setObjectName(u"azul")
        self.azul.setGeometry(QRect(300, 300, 90, 30))
        self.azul.setFont(font3)
        self.azul.setCursor(QCursor(Qt.PointingHandCursor))
        self.azul.setWrapping(False)
        self.azul.setMaximum(255)
        self.origenX = QSpinBox(self.widget)
        self.origenX.setObjectName(u"origenX")
        self.origenX.setGeometry(QRect(120, 130, 90, 30))
        self.origenX.setFont(font3)
        self.origenX.setCursor(QCursor(Qt.PointingHandCursor))
        self.origenX.setWrapping(False)
        self.origenX.setMaximum(500)
        self.labelORIGEN_Y = QLabel(self.widget)
        self.labelORIGEN_Y.setObjectName(u"labelORIGEN_Y")
        self.labelORIGEN_Y.setGeometry(QRect(120, 170, 95, 35))
        self.labelORIGEN_Y.setFont(font2)
        self.labelORIGEN_Y.setAlignment(Qt.AlignCenter)
        self.abInicio = QPushButton(self.widget)
        self.abInicio.setObjectName(u"abInicio")
        self.abInicio.setGeometry(QRect(30, 430, 100, 40))
        self.abInicio.setFont(font2)
        self.distancia = QDoubleSpinBox(self.widget)
        self.distancia.setObjectName(u"distancia")
        self.distancia.setEnabled(True)
        self.distancia.setGeometry(QRect(180, 390, 90, 30))
        self.distancia.setDecimals(2)
        self.labelDistancia = QLabel(self.widget)
        self.labelDistancia.setObjectName(u"labelDistancia")
        self.labelDistancia.setGeometry(QRect(180, 350, 95, 35))
        self.labelDistancia.setFont(font2)
        self.labelDistancia.setAlignment(Qt.AlignCenter)
        self.plainTextEditor = QPlainTextEdit(self.widget)
        self.plainTextEditor.setObjectName(u"plainTextEditor")
        self.plainTextEditor.setGeometry(QRect(420, 20, 371, 451))
        self.abMostrar = QPushButton(self.widget)
        self.abMostrar.setObjectName(u"abMostrar")
        self.abMostrar.setGeometry(QRect(300, 430, 100, 40))
        self.abMostrar.setFont(font2)
        self.abFinal = QPushButton(self.widget)
        self.abFinal.setObjectName(u"abFinal")
        self.abFinal.setGeometry(QRect(160, 430, 100, 40))
        self.abFinal.setFont(font2)
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.tableWidget = QTableWidget(self.tab2)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(50, 10, 681, 391))
        self.abBuscar = QPushButton(self.tab2)
        self.abBuscar.setObjectName(u"abBuscar")
        self.abBuscar.setGeometry(QRect(50, 420, 100, 40))
        self.abBuscar.setFont(font1)
        self.lineaBuscar = QLineEdit(self.tab2)
        self.lineaBuscar.setObjectName(u"lineaBuscar")
        self.lineaBuscar.setGeometry(QRect(170, 420, 200, 40))
        font4 = QFont()
        font4.setFamily(u"Arial")
        self.lineaBuscar.setFont(font4)
        self.lineaBuscar.setAlignment(Qt.AlignCenter)
        self.lineaBuscar.setDragEnabled(False)
        self.lineaBuscar.setReadOnly(False)
        self.abMostrarParticulas = QPushButton(self.tab2)
        self.abMostrarParticulas.setObjectName(u"abMostrarParticulas")
        self.abMostrarParticulas.setGeometry(QRect(440, 420, 171, 40))
        self.abMostrarParticulas.setFont(font1)
        self.tabWidget.addTab(self.tab2, "")
        self.menubar = QMenuBar(self.centralwidget)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir_)
        self.menuArchivo.addAction(self.actionGuardar_)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.actionAbrir_.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionGuardar_.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.labelColorVerde.setText(QCoreApplication.translate("MainWindow", u"VERDE:", None))
        self.labelCOLOR.setText(QCoreApplication.translate("MainWindow", u"COLOR:", None))
        self.labelColorRojo.setText(QCoreApplication.translate("MainWindow", u"ROJO:", None))
        self.labelVELOCIDAD.setText(QCoreApplication.translate("MainWindow", u"VEL.:", None))
        self.labelORIGEN_X.setText(QCoreApplication.translate("MainWindow", u"ORIGEN: X", None))
        self.labelDESTINO_X.setText(QCoreApplication.translate("MainWindow", u"DESTINO: X", None))
        self.labelID.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.labelColorAzul.setText(QCoreApplication.translate("MainWindow", u"AZUL:", None))
        self.labelDESTINO_Y.setText(QCoreApplication.translate("MainWindow", u"DESTINO: Y", None))
        self.labelORIGEN_Y.setText(QCoreApplication.translate("MainWindow", u"ORIGEN: Y", None))
        self.abInicio.setText(QCoreApplication.translate("MainWindow", u"A. INICIO", None))
        self.labelDistancia.setText(QCoreApplication.translate("MainWindow", u"DISTANCIA", None))
        self.abMostrar.setText(QCoreApplication.translate("MainWindow", u"MOSTRAR", None))
        self.abFinal.setText(QCoreApplication.translate("MainWindow", u"A. FINAL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Origen", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Destino", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Distancia", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Color", None));
        self.abBuscar.setText(QCoreApplication.translate("MainWindow", u"Busca Part\u00edculas", None))
        self.lineaBuscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduce el Identificador", None))
        self.abMostrarParticulas.setText(QCoreApplication.translate("MainWindow", u"Mostrar Part\u00edculas (Todas)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi
