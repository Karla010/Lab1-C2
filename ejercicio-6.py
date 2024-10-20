import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class AdministradorVuelos:
    def __init__(self):
      
        self.vuelos = {
            "ABC123": {"origen": "Ciudad A", "destino": "Ciudad B", "salida": "10:00 AM", "llegada": "12:00 PM", "estado": "A tiempo", "puerta": "A5"},
            "DEF456": {"origen": "Ciudad B", "destino": "Ciudad C", "salida": "11:00 AM", "llegada": "01:30 PM", "estado": "Retrasado", "puerta": "B2"},
            "GHI789": {"origen": "Ciudad A", "destino": "Ciudad C", "salida": "09:00 AM", "llegada": "11:00 AM", "estado": "Cancelado", "puerta": "C3"},
        }

    def obtener_info_vuelo(self, codigo_vuelo):
        # Buscar el vuelo
        if codigo_vuelo in self.vuelos:
            return self.vuelos[codigo_vuelo]
        else:
            raise ValueError("Código de vuelo no encontrado.")

class EstadoVueloAeropuerto(QWidget):
    def __init__(self):
        super().__init__()
        self.administrador = AdministradorVuelos()
        self.iniciar_interfaz()

    def iniciar_interfaz(self):
        self.setWindowTitle("Estado de Vuelos - Aeropuerto")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # 
        self.label_instruccion = QLabel("Introduce el código de vuelo:")
        layout.addWidget(self.label_instruccion)
        self.codigo_vuelo = QLineEdit(self)
        self.codigo_vuelo.setPlaceholderText("Ej: ABC123")
        layout.addWidget(self.codigo_vuelo)

        # Botón para consultar estado del vuelo
        self.btn_consultar = QPushButton("Consultar Estado", self)
        self.btn_consultar.clicked.connect(self.consultar_vuelo)
        layout.addWidget(self.btn_consultar)

        # Resultados de la consulta
        self.resultado_label = QLabel("", self)
        layout.addWidget(self.resultado_label)

        self.setLayout(layout)

    def consultar_vuelo(self):
        codigo_vuelo = self.codigo_vuelo.text().strip().upper()

        try:
            #información del vuelo
            vuelo_info = self.administrador.obtener_info_vuelo(codigo_vuelo)
            self.mostrar_info_vuelo(vuelo_info)
        except ValueError as e:
            self.resultado_label.setText(f"Error: {str(e)}")

    def mostrar_info_vuelo(self, info):
        # Mostrar la información del vuelo
        resultado = (
            f"Origen: {info['origen']}\n"
            f"Destino: {info['destino']}\n"
            f"Hora de salida: {info['salida']}\n"
            f"Hora de llegada: {info['llegada']}\n"
            f"Estado: {info['estado']}\n"
            f"Puerta de embarque: {info['puerta']}"
        )
        self.resultado_label.setText(resultado)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = EstadoVueloAeropuerto()
    ventana.show()
    sys.exit(app.exec_())
