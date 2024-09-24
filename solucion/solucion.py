import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QHBoxLayout
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import Qt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np

class VentanaSolucion(QWidget):

    # Cargar el modelo desde el archivo .keras
    modelo = keras.models.load_model('C:/Users/jbior/Documents/proyecto/MonitoreoDeFrutas/modelo/modelo.keras')

    #Etiquetas para desplegar como resultado
    etiquetas = ["Manzana fresca", "Banana Fresca", "Naranja Fresca", "Manzana Podrida", "Banana Podrida", "Naranja Podrida"]

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
        boton_examinar.clicked.connect(self.abrir_imagen)
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


    def abrir_imagen(self):
        # Abrir un diálogo para seleccionar la imagen
        ruta_imagen, _ = QFileDialog.getOpenFileName(self, 'Seleccionar imagen', '', 'Imágenes (*.png *.xpm *.jpg *.jpeg)')
        
        if ruta_imagen:
            # Cargar y mostrar la imagen en el QLabel
            pixmap = QPixmap(ruta_imagen)
            scaled_pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio)
            self.etiqueta_imagen.setPixmap(scaled_pixmap)

            # Mostrar el el resultado de clasificar la imagen
            clase_imagen = self.clasificar_imagen(ruta_imagen)
            self.etiqueta_clase.setText(clase_imagen)
    
    def clasificar_imagen(self, ruta_imagen):
        # Cargar la imagen con el tamaño adecuado
        img = image.load_img(ruta_imagen, target_size=(256, 256))

        # Convertir la imagen a un array numpy y escalar los valores de píxeles
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Añadir un nuevo eje para el batch
        img_array /= 255.0  # Escalar la imagen entre 0 y 1

        # Realizar la predicción
        prediccion = self.modelo.predict(img_array)

        # Obtener el índice de la clase con la mayor probabilidad
        clase_predicha = np.argmax(prediccion, axis=1)[0] 

        return self.etiquetas[clase_predicha]

# Iniciar la aplicación
app = QApplication(sys.argv)
window = VentanaSolucion()
window.show()
sys.exit(app.exec_())
