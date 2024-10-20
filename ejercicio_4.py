import sys
from PyQt5.QtWidgets import*
class VentanaMascotas(QWidget):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()

    def configurar_ventana(self):
        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle("Ejercicio-4")

        # Layout vertical
        layout = QVBoxLayout()

        # Lista donde se almacenarán las entradas de datos
        self.mascotas = []

        # Crear entradas para 3 mascotas
        for i in range(3):
            layout.addWidget(QLabel(f"Mascota {i+1}:"))

            nombre = QLineEdit(self)
            nombre.setPlaceholderText("Nombre")
            layout.addWidget(nombre)

            edad = QLineEdit(self)
            edad.setPlaceholderText("Edad")
            layout.addWidget(edad)

            tipo = QLineEdit(self)
            tipo.setPlaceholderText("Tipo (Ej: Perro, Gato)")
            layout.addWidget(tipo)

            # Guardar las entradas en una lista
            self.mascotas.append((nombre, edad, tipo))

        # Botón para ver los datos ingresados
        boton_mostrar = QPushButton("Mostrar Datos", self)
        boton_mostrar.clicked.connect(self.mostrar_datos)
        layout.addWidget(boton_mostrar)

        self.setLayout(layout)

    def mostrar_datos(self):
        # Crear un cuadro de diálogo para mostrar los datos ingresados
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Datos ingresados")

        # Concatenar los datos de todas las mascotas
        texto_mensaje = ""
        for i, mascota in enumerate(self.mascotas):
            nombre = mascota[0].text()
            edad = mascota[1].text()
            tipo = mascota[2].text()
            texto_mensaje += f"Mascota {i+1}:\nNombre: {nombre}\nEdad: {edad}\nTipo: {tipo}\n\n"

        # Mostrar el mensaje en el cuadro de diálogo
        mensaje.setText(texto_mensaje)
        mensaje.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaMascotas()
    ventana.show()
    sys.exit(app.exec_())
