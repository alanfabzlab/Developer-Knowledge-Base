
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
def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
            
        lista[j + 1] = clave
        
    return lista

velocidades_enemigas = [55, 30, 80, 45, 20, 95]
print(insertion_sort(velocidades_enemigas))
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
def linear_search(lista, objetivo):
    intentos = 0
    for i in range(len(lista)):
        intentos += 1
        if lista[i] == objetivo:
            print(f"Encontrado {objetivo} en {intentos} intentos usando búsqueda lineal.")
            return i
    print(f"{objetivo} no encontrado después de {intentos} intentos usando búsqueda lineal.")
    return -1

# Binary Search: O(log N) worst-case
def binary_search(lista, objetivo):
    izq, der = 0, len(lista) - 1
    intentos = 0
    
    while izq <= der:
        intentos += 1
        medio = (izq + der) // 2
        
        if lista[medio] == objetivo:
            print(f"Encontrado {objetivo} en {intentos} intentos usando búsqueda binaria.")
            return medio
        elif lista[medio] < objetivo:
            izq = medio + 1
        else:
            der = medio - 1
            
    print(f"{objetivo} no encontrado después de {intentos} intentos usando búsqueda binaria.")
    return -1

# Comparison Demo
rango_min = 1
rango_max = 100000

numeros = [i for i in range(rango_min, rango_max + 1)]
numero_aleatorio = random.randint(rango_min, rango_max)

print(f"Tu tirada secreta de PV de jefe es {numero_aleatorio}")
linear_search(numeros, numero_aleatorio)
binary_search(numeros, numero_aleatorio)
```


## 4. Aplicación Práctica: Optimización de Rutas de Mazmorra

Un reto clásico de optimización en Ciencias de la Computación es la planificación de rutas (conocida históricamente como el **Problema del Agente Viajero**).

- **Elección de la Estructura de Datos:** Una **Lista** es ideal cuando la secuencia de ejecución y el orden importan.
    
- **Objetivo del Algoritmo:** Minimizar la distancia/tiempo total recorrido a lo largo de varias paradas en la mazmorra.
    


Python

```python
# Dungeon route planning using an ordered List
ruta = [
    "Fortaleza Hundida (Inicio)",
    "Catacumbas Inundadas",
    "Aguja de Cristal",
    "Forja de la Caída de Brasa",
    "Yermos Cenicientos",
    "Puerta de las Lunas Gemelas"
]

print("Ruta planificada:")
for parada in ruta:
    print(parada)
```
