
# ME02 : Quinto punto primer parcial.

## Propósito

Verificar a través de una simulación que efectivamente la media teórica estimada para el algoritmo de QuickSort en el libro "Probabilitys Models for Computer science" de Sheldom Ross en la sección "2.2 The quicksort and Find Algorithms" se aproxima realmente a la practica.

## Integrantes

|       Integrante      |                 Correo                       |
|-----------------------|-----------------------------------------------|
| Dave Sebastian Valencia Salazar      |    <dsvalencias@unal.edu.co>    |
| Yesid Alberto Ochoa Luque      |    <yaochoal@unal.edu.co>     |

## Entregables

### 1. Código fuente del simulador construido:
### [1.1 Código fuente online](https://colab.research.google.com/drive/1-onef1pg1dCJ-EcmNn9h3BNJ6pqV_Ynm)


### 2. Manual técnico:

### Requerimientos: 
Python 3.x

### Herramientas utilizadas en el desarrollo: 

#### Colab Google:
Google Colab es un servicio en la nube que permite hacer uso de las GPUs y TPUs de google con con librerías como: **Scikit-learn**, **PyTorch**, **TensorFlow**, **Keras** y **OpenCV**. Todo ello con bajo Python 2.x y 3.x muy utilizado para practicar y desarrollar aplicaciones (pilotos) de **machine learning** y **deep learning**, sin tener que invertir en recursos hardware o del Cloud permitiendo también compartir, importar y exportar códigos que tengamos creados por medio de Drive en Google.
### Correr el código
- Pre-requisito: Haber iniciado sección con una cuenta de Google.
- Para correr el código primero debemos dar clic en el siguiente enlace.
### [ Código fuente en Colab](https://colab.research.google.com/drive/1-onef1pg1dCJ-EcmNn9h3BNJ6pqV_Ynm)
- Luego dar clic en la opción de arriba izquierda **Abrir en modo ensayo**.

![m1](/img/m1.jpg )

- Una vez ahí dar clic en el botón de **Play** de arriba izquierda.

![m2](/img/m2.jpg )

- Confirmar ejecución.

![m3](/img/m3.jpg )


- Ingrese los **n** datos a ordenar.

![m4](/img/m4.jpg )

- Ingrese el numero de muestras por **n** datos.

![m5](/img/m5.jpg )

- Espere a que termine de ejecutar y visualice la gráfica con los datos.

![m6](/img/m6.jpg )


## 3. Análisis de resultados.
Las implementaciones de QuickSort varían dependiendo de como se escoja el pivote debido a que la mayoría de optimizaciones que se aplican al algoritmo se centran en la elección del pivote por lo cual la complejidad pueden variar de **O(n²)**. a **O(n·log n)**.

Haciendo un análisis a la gráfica podemos observar que el numero de comparaciones mostradas reales son menores que las teóricas, aunque esto puede darse debido a que al momento de ejecutar esta gráfica teórica toma un escenario poco probable donde el numero de comparaciones es mas alto que el promedio.

![m6](/img/m6.jpg )

Si repetimos la prueba con 20 muestras por numero de datos **n** a organizar vemos como los datos tienden a tener un comportamiento similar a el de la gráfica teórica pero por debajo de esta.

![m7](/img/m7.jpg )

Donde se puede concluir que el valor teórico es mas alto que el valor real debido a que toma el mayor numero de comparaciones posibles al promedio que generalmente se genera.