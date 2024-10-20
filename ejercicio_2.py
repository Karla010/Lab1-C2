import sys
from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt

class VentanaContrasena(QWidget):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()

    def configurar_ventana(self):
        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle("Ejercicio-2")

        # Campos para ingresar la contraseña
        etiqueta_contrasena = QLabel("Ingrese la contraseña:", self)
        self.campo_contrasena = QLineEdit(self)
        self.campo_contrasena.setEchoMode(QLineEdit.Password)

        # Checkbox para mostrar u ocultar la contraseña
        self.checkbox_mostrar = QCheckBox("Mostrar contraseña", self)
        self.checkbox_mostrar.stateChanged.connect(self.mostrar_contrasena)

        # Diseño vertical
        layout = QVBoxLayout()
        layout.addWidget(etiqueta_contrasena)
        layout.addWidget(self.campo_contrasena)
        layout.addWidget(self.checkbox_mostrar)

        self.setLayout(layout)
        self.show()

    def mostrar_contrasena(self, estado):
        # Cambia el modo de visualización según el estado del checkbox
        if estado == Qt.Checked:
            self.campo_contrasena.setEchoMode(QLineEdit.Normal)
        else:
            self.campo_contrasena.setEchoMode(QLineEdit.Password)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaContrasena()
    sys.exit(app.exec())
