
# 02. Algoritmos y Eficiencia Algorítmica

**Versión original en inglés:** [02 - Algorithms & Efficiency.md](02%20-%20Algorithms%20&%20Efficiency.md)

**Curso:** Estructuras de Datos y Algoritmos
**Tema:** Ordenamiento por Inserción, Búsqueda Lineal y Binaria, Análisis de Complejidad
**Etiquetas:** `#dsa` `#algorithms` `#sorting` `#complexity`



## 1. ¿Qué es un Algoritmo?

Un **algoritmo** es un procedimiento paso a paso que toma una entrada, la procesa mediante pasos estructurados y produce una salida esperada.

### Ejemplos de Algoritmos del Mundo Real
- **Sistemas de emparejamiento (por ejemplo, colas por habilidad):** Toman el historial de los jugadores (ratio de victorias, K/D) como entrada y producen partidas equilibradas.
- **Algoritmos de camino más corto (por ejemplo, navegación de NPC):** Toman las posiciones de inicio/fin y los datos del terreno como entrada para calcular la ruta más rápida.
- **Algoritmos de ordenamiento:** Toman una colección no ordenada de elementos y los acomodan en orden alfabético o numérico.

---

## 2. Implementación del Ordenamiento por Inserción

El ordenamiento por inserción es un algoritmo de ordenamiento simple basado en comparaciones.

Python

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
        
    return arr

enemy_speeds = [55, 30, 80, 45, 20, 95]
print(insertion_sort(enemy_speeds))
# Output: [20, 30, 45, 55, 80, 95]
```


## 3. Eficiencia Algorítmica y Escenario de Peor Caso

Al diseñar algoritmos, la **eficiencia** es tan importante como la corrección. En lugar de medir el tiempo de ejecución (que varía según el hardware), la eficiencia se evalúa calculando cuántos pasos necesita un algoritmo a medida que crece el tamaño de la entrada.


### Comparación de Estrategias de Búsqueda

1. **Búsqueda Lineal:** Revisa los elementos uno por uno de forma secuencial. En el peor caso, puede requerir hasta $N$ pasos.
    
2. **Búsqueda Binaria:** Divide a la mitad el rango de búsqueda en cada paso. En el peor caso, para 100 elementos, no necesita más de 7 intentos ($\log_2 N$).
    


Python

```python
import random

# Linear Search: O(N) worst-case
def linear_search(arr, target):
    guesses = 0
    for i in range(len(arr)):
        guesses += 1
        if arr[i] == target:
            print(f"Found {target} in {guesses} guesses using linear search.")
            return i
    print(f"{target} not found after {guesses} guesses using linear search.")
    return -1

# Binary Search: O(log N) worst-case
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    guesses = 0
    
    while left <= right:
        guesses += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            print(f"Found {target} in {guesses} guesses using binary search.")
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    print(f"{target} not found after {guesses} guesses using binary search.")
    return -1

# Comparison Demo
range_low = 1
range_high = 100000

numbers = [i for i in range(range_low, range_high + 1)]
random_num = random.randint(range_low, range_high)

print(f"Your secret boss HP roll is {random_num}")
linear_search(numbers, random_num)
binary_search(numbers, random_num)
```


## 4. Aplicación Práctica: Optimización de Rutas de Mazmorra

Un reto clásico de optimización en Ciencias de la Computación es la planificación de rutas (conocida históricamente como el **Problema del Agente Viajero**).

- **Elección de la Estructura de Datos:** Una **Lista** es ideal cuando la secuencia de ejecución y el orden importan.
    
- **Objetivo del Algoritmo:** Minimizar la distancia/tiempo total recorrido a lo largo de varias paradas en la mazmorra.
    


Python

```python
# Dungeon route planning using an ordered List
route = [
    "Sunken Keep (Start)",
    "Flooded Catacombs",
    "Crystal Spire",
    "Emberfall Forge",
    "Ashen Barrens",
    "Gate of the Twin Moons"
]

print("Planned route:")
for stop in route:
    print(stop)
```
