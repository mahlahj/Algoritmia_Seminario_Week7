from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PySide2.QtCore import Slot
from ui_MainWindow import Ui_MainWindow
from particula import Particula
from organizador import Organizador
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.particula = Particula()
        self.organizador = Organizador()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.abInicio.clicked.connect(self.click_agregar_inicio)
        self.ui.abFinal.clicked.connect(self.click_agregar_final)
        self.ui.abMostrar.clicked.connect(self.click_mostrar)
        self.ui.actionGuardar_.triggered.connect(self.guardar)
        self.ui.actionAbrir_.triggered.connect(self.abrir)
        self.ui.abMostrarParticulas.clicked.connect(self.mostrarParticulasTodas)
        self.ui.abBuscar.clicked.connect(self.buscarParticulaId)


    @Slot()
    def click_mostrar(self):
        self.ui.plainTextEditor.clear()
        self.ui.plainTextEditor.insertPlainText(self.organizador.mostrar())
    
    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.id.value()
        origen_x = self.ui.origenX.value()
        origen_y = self.ui.origenY.value()
        destino_x = self.ui.destinoX.value()
        destino_y = self.ui.destinoY.value()
        velocidad = self.ui.velocidad.value()
        rojo = self.ui.rojo.value()
        verde = self.ui.verde.value()
        azul = self.ui.azul.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, rojo, verde, azul)
        self.organizador.agregar_inicio(particula)

    @Slot()
    def click_agregar_final(self):
        id = self.ui.id.value()
        origen_x = self.ui.origenX.value()
        origen_y = self.ui.origenY.value()
        destino_x = self.ui.destinoX.value()
        destino_y = self.ui.destinoY.value()
        velocidad = self.ui.velocidad.value()
        rojo = self.ui.rojo.value()
        verde = self.ui.verde.value()
        azul = self.ui.azul.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, rojo, verde, azul)
        self.organizador.agregar_final(particula)

    @Slot()
    def guardar(self):
        ubicacion = QFileDialog.getSaveFileName(self, 'Guardar', '.', 'JSON (*.json)')
        with open(ubicacion[0], 'w') as archivo:
            json.dump(self.organizador.guardar(), archivo, indent=4)

    @Slot()
    def abrir(self):
        ubicacion = QFileDialog.getOpenFileName(self, 'Abrir', '.', 'JSON (*.json)')
        with open(ubicacion[0], 'r') as archivo:
            self.organizador.get(json.load(archivo))

    @Slot()
    def buscarParticulaId(self):
        id = self.ui.lineaBuscar.text()
        encontrado = False
        for item in self.organizador.organizador:
            if id == item.getId():
                self.ui.tableWidget.clear()
                self.ui.tableWidget.setRowCount(1)
                headers = ["Id", "Origen", "Destino", "Velocidad", "Color", "Distancia"]
                self.ui.tableWidget.setHorizontalHeaderLabels(headers)

                id = QTableWidgetItem(item.getId())
                origen = QTableWidgetItem(item.getOrigen())
                destino = QTableWidgetItem(item.getDestino())
                velocidad = QTableWidgetItem(item.getVelocidad())
                color = QTableWidgetItem(item.getColor())
                distancia = QTableWidgetItem(item.getDistancia())

                self.ui.tableWidget.setItem(0, 0, id)
                self.ui.tableWidget.setItem(0, 1, origen)
                self.ui.tableWidget.setItem(0, 2, destino)
                self.ui.tableWidget.setItem(0, 3, velocidad)
                self.ui.tableWidget.setItem(0, 4, color)
                self.ui.tableWidget.setItem(0, 5, distancia)

                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención",
                f'La partícula con identificador "{id}" no fue encontrada'
            )

    @Slot()
    def mostrarParticulasTodas(self):
        row = 0
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(len(self.organizador.organizador))
        headers = ["Id", "Origen", "Destino", "Velocidad", "Color", "Distancia"]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        for item in self.organizador.organizador:
            id = QTableWidgetItem(item.getId())
            origen = QTableWidgetItem(item.getOrigen())
            destino = QTableWidgetItem(item.getDestino())
            velocidad = QTableWidgetItem(item.getVelocidad())
            color = QTableWidgetItem(item.getColor())
            distancia = QTableWidgetItem(item.getDistancia())

            self.ui.tableWidget.setItem(row, 0, id)
            self.ui.tableWidget.setItem(row, 1, origen)
            self.ui.tableWidget.setItem(row, 2, destino)
            self.ui.tableWidget.setItem(row, 3, velocidad)
            self.ui.tableWidget.setItem(row, 4, color)
            self.ui.tableWidget.setItem(row, 5, distancia)

            row += 1