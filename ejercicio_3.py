import sys
from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt

class VentanaLista(QWidget):
    def __init__(self):
        super().__init__()
        # Lista que se mostrará en la ventana
        self.datos_agregados = ["Cédula: 34567212", "Nombre: Karla Lisseth Herrera"]
        self.interfaz()

    def interfaz(self):
        self.setGeometry(100, 100, 300, 100)
        self.setWindowTitle("Ejercicio_3")

        # Crear etiqueta para la lista
        etiqueta_agregados = QLabel("Agregados", self)
        etiqueta_agregados.setAlignment(Qt.AlignCenter)  # Centramos la etiqueta

        # Crear lista y ocultarla inicialmente
        self.lista = QListWidget(self)
        self.lista.hide()

        # Crear botón para mostrar la lista al hacer clic
        boton_mostrar = QPushButton("Mostrar", self)
        boton_mostrar.clicked.connect(self.mostrar_lista)

        # Layout vertical
        layout = QVBoxLayout()
        layout.addWidget(etiqueta_agregados)
        layout.addWidget(self.lista)
        layout.addWidget(boton_mostrar)

        self.setLayout(layout)

    def mostrar_lista(self):
        # Mostrar la lista si está oculta
        if not self.lista.isVisible():
            self.lista.addItems(self.datos_agregados)
            self.lista.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaLista()
    ventana.show()
    sys.exit(app.exec())

          
