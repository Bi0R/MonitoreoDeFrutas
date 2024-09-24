import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QHBoxLayout
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import Qt

class VentanaSolucion(QWidget):
    etiquetas = {
        "freshapples": "Manzana fresca",
        "freshbanana": "Banana fresca",
        "freshoranges": "Naranja fresca",
        "rottenapples": "Manzana podrida",
        "rottenbanana": "Banana podrida",
        "rottenoranges": "Naranja podrida"
    }

    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowTitle('Monitoreo Inteligente de la Maduración de Frutas y Vegetales')
        self.setGeometry(100, 100, 500, 500)

        # Crear el layout principal
        layout = QVBoxLayout()

        # Etiqueta grande en la parte superior
        etiqueta_titulo = QLabel('Monitoreo Inteligente de la Maduración de Frutas y Vegetales', self)
        etiqueta_titulo.setAlignment(Qt.AlignCenter)
        etiqueta_titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(etiqueta_titulo)

        # Subtítulo "Seleccione una imagen" con el botón "Examinar"
        sub_layout = QHBoxLayout()
        etiqueta_subtitulo = QLabel('Seleccione una imagen:', self)
        etiqueta_subtitulo.setStyleSheet("font-size: 14px;")
        sub_layout.addWidget(etiqueta_subtitulo)

        # Botón para seleccionar la imagen
        boton_examinar = QPushButton('Examinar', self)
        boton_examinar.clicked.connect(self.open_image)
        sub_layout.addWidget(boton_examinar)
        layout.addLayout(sub_layout)

        # Etiqueta para mostrar la imagen
        self.etiqueta_imagen = QLabel(self)
        self.etiqueta_imagen.setFixedSize(250, 250)
        self.etiqueta_imagen.setStyleSheet("border: 1px solid black;")
        layout.addWidget(self.etiqueta_imagen)

        # Etiqueta para el resultado de la clasificacion
        self.etiqueta_clase = QLabel(self)
        self.etiqueta_clase.setAlignment(Qt.AlignCenter)
        self.etiqueta_clase.setStyleSheet("color: blue; font-size: 16px;")
        layout.addWidget(self.etiqueta_clase)

        # Configurar el layout en la ventana
        self.setLayout(layout)

    def open_image(self):
        # Abrir un diálogo para seleccionar la imagen
        image_path, _ = QFileDialog.getOpenFileName(self, 'Seleccionar imagen', '', 'Imágenes (*.png *.xpm *.jpg *.jpeg)')
        
        if image_path:
            # Cargar y mostrar la imagen en el QLabel
            pixmap = QPixmap(image_path)
            scaled_pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio)
            self.etiqueta_imagen.setPixmap(scaled_pixmap)

            # Mostrar el nombre del archivo debajo de la imagen
            file_name = image_path.split('/')[-1]
            self.etiqueta_clase.setText(file_name)

# Iniciar la aplicación
app = QApplication(sys.argv)
window = VentanaSolucion()
window.show()
sys.exit(app.exec_())
