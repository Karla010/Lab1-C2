import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()

    def configurar_ventana(self):
        self.setGeometry(230, 230, 230, 230)
        self.setWindowTitle("Ejercicio-1")

        # Crear y configurar etiquetas
        nombre = QLabel("Karla Lisseth", self)
        apellido = QLabel("Herrera", self)
        edad = QLabel("18", self)

        # Alinear las etiquetas al centro
        nombre.setAlignment(Qt.AlignCenter)
        apellido.setAlignment(Qt.AlignCenter)
        edad.setAlignment(Qt.AlignCenter)

        # Layout vertical
        layout = QVBoxLayout()
        layout.addWidget(nombre)
        layout.addWidget(apellido)
        layout.addWidget(edad)

        self.setLayout(layout)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec_())
