# MonitoreoDeFrutas
Proyecto final para la materia Seminario de Investigación.

El presente proyecto tiene como propósito ayudar a clasificar frutas que se encuentran en buen estado y frutas en estado de descomposición.

El código se divide en dos partes:

1. El código con el que entrenamos el modelo.
2. El código en el que se usa el modelo para aplicarlo a casos específicos.

Nota: el dataset usado para entrenar el modelo fue tomado de [kaggle](https://www.kaggle.com/datasets/sriramr/fruits-fresh-and-rotten-for-classification)

## Estructura del proyecto

Como se mencionó antes el proyecto se divide en dos partes el modelo y la solución.

### Modelo

Dentro de la estructura del proyecto se encuentra la carpeta **modelo** aquí se encuentra el código necesarrio para entrenar el modelo y aunque se incluye la carpeta **data** en realidad no se incluye el dataset pues debido a la cantidad de fotografías el repositorio se volvería demasido pesado (se debe descargar por separado si se quiere ejecutar en local).

### Solucion

Al mismo nivel que la carpeta **modelo** encontramos la carpeta **solucion** aqui es donde encontramos el código de la aplicación que usa el modelo que entrenamos en la otra sección de código, no es necesario entrenar el modelo cada vez que se quiere ejecutar la aplicación.

## Como ejecutar el código

Para ejecutar este código de manera local, podemos únicamente ejecutar la aplicación que hace uso del modelo previamente entrenado, o podemos realizar el paso donde se hace el entrenamiento de manera local. A contonuación se exponen los pasos a seguir para ejecutar los distintos pasos.

### Pre-requisitos

Es importante tener un ambiente adecuado para ejecutar los componentes, en especial es importante que las versiones sean las correctas, a continuación se presentan los componentes y versiones con las que el modelo fue probado:

|python| |
|-|-|
|tensorflow| |
|matplotlib| |
|pandas| |
|numpy| |

### Ejecutar el modelo (Paso opcional)

### Ejecutar la aplicación
