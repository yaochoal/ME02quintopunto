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
    return count  # devuelve las comparaciones hechas


# hacer que funcione de arreglos de tamaño 1 a n
# por ahora funciona con un tamaño n fijo
def testing(size, tries):
    comparisons = []
    results = []
    for i in range(tries):
        sample = np.random.randint(0, size, size)  # genera un arreglo de tamaño size y numero maximo size
        results.append(quickSort(sample, 0, size - 1))  # acá guarda las cantidades de comparaciones en un arreglo
    comparisons.append(np.average(results))  # acá les saca promedio y las guarda en un arreglo
    return comparisons


if __name__ == '__main__':

    n = int(input("Ingrese la cantidad de datos a ordenar: \n"))
    rounds = int(input("Ingrese la cantidad de repeticiones: \n"))
    vector = list(range(0, n))
    vector1 = list(range(0, n))
    for i in range(n):
        vector[i] = testing(i, rounds)

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