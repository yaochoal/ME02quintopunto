
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
### [1.1 Código fuente online](https://colab.research.google.com/drive/1-onef1pg1dCJ-EcmNn9h3BNJ6pqV_Ynm):

``` ejemplo: ./punto5.py```
```
import numpy as np
import matplotlib.pyplot as plt
import time

def partition(arr, low, high):
    count = 0
    i = (low - 1)  # índice de elemento más pequeño
    pivot = arr[high]  # pivote

    for j in range(low, high):
        count += 1
        # Si el elemento actual es más pequeño que el pivote
        if arr[j] < pivot:
            # índice de incremento del elemento más pequeño
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1, count

def quickSort(arr, low, high):
    count = 0
    if low < high:
        # pi es el índice de partición, arr [p] es ahora
        # en el lugar correcto
        pi, count = partition(arr, low, high)

        # Separar elementos por separado antes
        # partición y después de la partición
        count += quickSort(arr, low, pi - 1)
        count += quickSort(arr, pi + 1, high)
    return count #devuelve las comparaciones hechas


# hacer que funcione de arreglos de tamaño 1 a n
# por ahora funciona con un tamaño n fijo
def testing(size, tries):
    comparisons = []
    results = []
    for i in range(tries):
        sample = np.random.randint(0, size, size) #genera un arreglo de tamaño size y numero maximo size
        results.append(quickSort(sample, 0, size - 1)) # acá guarda las cantidades de comparaciones en un arreglo
    comparisons.append(np.average(results)) # acá les saca promedio y las guarda en un arreglo
    return comparisons


if __name__ == '__main__': 

    n=int(input("Ingrese la cantidad de datos a ordenar: \n"))
    rounds = int(input("Ingrese la cantidad de repeticiones: \n"))
    vector = list(range(0,n))
    vector1 = list(range(0, n))
    for i in range(n):
        vector[i]=testing(i, rounds)
    
    print("Puntos reales")
    print(vector)
    plt.plot(vector1, vector, 'ro')
    x = np.arange(1, n, 0.1)
    y = 2 * x * np.log(x)
    plt.plot(x, y)
    plt.xlabel('X: N° de datos')
    plt.ylabel('Y: N° de comparaciones')
    plt.grid(True)
    plt.legend(('Valor Real', ' Valor Teorico'),
           loc='lower right')
    plt.title('Comparación de QuickSort')
    plt.show()

```


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

Haciendo un análisis a la gráfica podemos observar que el numero de comparaciones mostradas por los valores reales en comparación con las teóricas en la mayoría de casos dan por debajo de esta linea .
