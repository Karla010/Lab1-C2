import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator

class VentanaPersonas(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        self.setWindowTitle("Ejercicio-5")
        self.setGeometry(200, 200, 350, 500)

        # Layout vertical
        layout = QVBoxLayout()

        # Lista donde se almacenarán las entradas de datos
        self.datos_personales = []

        # Campos de datos personales
        campos = [
            "Nombre", "Apellido", "Edad", "Dirección", "Ciudad", 
            "País", "Teléfono", "Correo", "Ocupación", "Fecha de Nacimiento"
        ]

        # Crear los campos de entrada
        for campo in campos:
            layout.addWidget(QLabel(campo))  # Etiqueta del campo
            entrada = QLineEdit(self)
            entrada.setPlaceholderText(campo)

            # Validaciones para campos específicos
            if campo == "Edad":
                entrada.setValidator(QIntValidator())
                entrada.setMaxLength(3)
            elif campo == "Teléfono":
                entrada.setValidator(QIntValidator())
                entrada.setMaxLength(8)

            layout.addWidget(entrada)
            self.datos_personales.append(entrada)  # Almacenar el campo de entrada

        # Botón para mostrar los datos ingresados
        boton_mostrar = QPushButton("Mostrar Datos", self)
        boton_mostrar.clicked.connect(self.mostrar_datos)
        layout.addWidget(boton_mostrar)

        self.setLayout(layout)

    def mostrar_datos(self):
        # Crear un cuadro de diálogo para mostrar los datos ingresados
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Datos ingresados")

        # Concatenar los datos en un solo string
        datos = ""
        for campo in self.datos_personales:
            datos += f"{campo.placeholderText()}: {campo.text()}\n"

        # Mostrar el mensaje
        mensaje.setText(datos)
        mensaje.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPersonas()
    ventana.show()
    sys.exit(app.exec_())
