#Primero realizamos los imports necesarios
# Bibliotecas para manejo de datos
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Necesario para manejo de archivos
import os
# Manejo de dataset
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import preprocessing
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.preprocessing.image import ImageDataGenerator
# Inician dependencias para el modelo
from tensorflow.keras.applications import VGG16
# Optimizador
from tensorflow.keras.optimizers import Adam
#Layers de Keras
from tensorflow.keras.layers import Input, Dense, Dropout, Flatten, AveragePooling2D
#Modelo Keras
from tensorflow.keras.models import Model


#### Explorar datos
print("Iniciando ejecucion modelo")
clases = []
contador_de_clases = 0

RUTA_ENTRENAMIENTO = 'C:/Users/jbior/Documents/proyecto/MonitoreoDeFrutas/modelo/data/archive/dataset/train/'
RUTA_PRUEBAS = 'C:/Users/jbior/Documents/proyecto/MonitoreoDeFrutas/modelo/data/archive/dataset/test/'
RUTA_MODELO = 'C:/Users/jbior/Documents/proyecto/MonitoreoDeFrutas/modelo/'

ejecucion_con_grafica = False


for nombre_dir, directorios, archivos in os.walk(RUTA_ENTRENAMIENTO):
    if nombre_dir.endswith('/'):
        continue
    else:
        clases.append({nombre_dir.split('/')[-1]: 0})
    contador_archivos = 0
    for filename in archivos:
        contador_archivos += 1
    clases[contador_de_clases][nombre_dir.split('/')[-1]] = contador_archivos
    contador_de_clases += 1
    
print('{:<16} {:<16}'.format('Clase', 'Numero de Ocurrencias'))
print()
for d in clases:
    [(k, v)] = d.items()
    print('{:<15} {:<15}'.format(k, v))

## Si la ejecucion_con_grafica esta activa muestra una grafica de barras con el numero de coincidencias por categoria.

if ejecucion_con_grafica:
    ocurrencias = []
    etiquetas = []
    for d in clases:
       [(k, v)] = d.items()
       etiquetas.append(k)
       ocurrencias.append(v)

    plt.figure()
    plt.bar(range(len(ocurrencias)), ocurrencias, color = ['yellow', 'orange', 'orange', 'green', 'green', 'yellow'], alpha = .7)
    plt.xticks(range(len(ocurrencias)), etiquetas, rotation = 30)
    plt.title('Numero de ocurrencias por etiqueta')
    plt.show()

## Se generan mas imagenes a partir de la existentes

data_generada = ImageDataGenerator(
    rotation_range = 30, 
    zoom_range = .3, 
    horizontal_flip = True, 
    vertical_flip = True, 
    validation_split = .3
)

## Se perpara la data de entrenamiento
data_entrenamiento = data_generada.flow_from_directory(
    directory = RUTA_ENTRENAMIENTO,
    target_size = (256, 256),
    color_mode = 'rgb',
    class_mode = 'categorical',
    subset = 'training'
)

## Se prepara data para validacion
data_validacion = data_generada.flow_from_directory(
    directory = RUTA_ENTRENAMIENTO,
    target_size = (256, 256),
    color_mode = 'rgb',
    class_mode = 'categorical',
    subset = 'validation'
)

## Se crea la arquitectura del modelo, se usa vgg16

vgg16 = VGG16(include_top = False, weights = 'imagenet', input_shape = (224, 224, 3))
vgg16.trainable = False

X_input = Input(shape = (256, 256, 3))
X = vgg16(X_input)
X = AveragePooling2D(pool_size = (3, 3), strides = 2, padding = 'valid',name = 'AvgPool2D')(X)
X = Flatten(name = 'Flatten')(X)
X = Dense(200, activation = 'relu', name = 'Dense1')(X)
X = Dropout(.1)(X)
X = Dense(100, activation = 'relu', name = 'Dense2')(X)
X = Dropout(.1)(X)
X = Dense(6, activation = 'softmax', name = 'Dense3')(X)

modelo = Model(inputs = X_input, outputs = X, name = 'Monitoreo_de_Frutas')

print(modelo.summary())

## Se crea el optimizador

optimizador = Adam(learning_rate = 0.001)

modelo.compile(optimizer = optimizador, loss = 'categorical_crossentropy', metrics = ['accuracy'])

directorios = modelo.fit(data_entrenamiento, validation_data = data_validacion, epochs = 5, batch_size = 32)

## Se evalua el modelo

data_pruebas = image_dataset_from_directory(
    RUTA_PRUEBAS,
    label_mode = 'categorical',
    color_mode = 'rgb',
    image_size = (256, 256)
)

## Imprimiendo resultados

resultados = modelo.evaluate(data_pruebas)

print('{:<20} {:<20}'.format('Perdida en prueba', 'Precision de la prueba'))
print('{:<20} {:<20}'.format(np.round(resultados[0], 2), np.round(resultados[1], 2)))

## Guardar modelo
modelo.save(RUTA_MODELO + "modelo.keras")