
# 04. Búsqueda Binaria

**Versión original en inglés:** [04 - Binary Search.md](04%20-%20Binary%20Search.md)

**Curso:** Estructuras de Datos y Algoritmos
**Tema:** Divide y Vencerás, Búsqueda en Listas Ordenadas, Búsqueda Iterativa y Recursiva, Casos Límite
**Etiquetas:** `#dsa` `#searching` `#binary-search` `#complexity`



## 1. ¿Qué es la Búsqueda Binaria?

La **Búsqueda Binaria** es un algoritmo eficiente para encontrar un elemento en una lista **ordenada**. Funciona dividiendo a la mitad el intervalo de búsqueda repetidamente, hasta encontrar el valor objetivo o hasta que la sublista queda vacía.

> **Requisito clave:** La lista de entrada **debe estar ordenada** antes de aplicar Búsqueda Binaria.



---


## 2. ¿Cómo funciona la Búsqueda Binaria?

En lugar de revisar los elementos uno por uno (como la Búsqueda Lineal), la Búsqueda Binaria descarta la mitad de los elementos restantes en cada paso:

1. Ubica el elemento central de la lista (`medio`).
2. Si el elemento central es igual al objetivo, la búsqueda termina.
3. Si el objetivo es menor que el elemento central, descarta la mitad derecha y busca en la mitad izquierda.
4. Si el objetivo es mayor que el elemento central, descarta la mitad izquierda y busca en la mitad derecha.
5. Repite hasta encontrar el objetivo o hasta que los punteros se crucen (`izquierda > derecha`).

Esta es una estrategia de **divide y vencerás**: el problema se parte en dos mitades, solo una de ellas puede seguir conteniendo el objetivo, y el trabajo restante se reduce a la mitad en cada paso.

---

## 3. Implementación en Python

### Enfoque Iterativo

Python

```python
def busqueda_binaria(lista_entrada, objetivo):
    izquierda = 0
    derecha = len(lista_entrada) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2  # Encuentra el índice del centro

        if lista_entrada[medio] == objetivo:
            return True  # Objetivo encontrado
        elif objetivo < lista_entrada[medio]:
            derecha = medio - 1  # Busca en la mitad izquierda
        else:
            izquierda = medio + 1  # Busca en la mitad derecha

    return False  # Objetivo no encontrado
```


### Enfoque Recursivo

La misma lógica expresada llamándose a sí misma sobre la mitad que sobrevivió. Un valor por defecto no puede hacer referencia a `lista_entrada`, así que `derecha` se resuelve en la primera llamada y después se pasa explícitamente:

Python

```python
def busqueda_binaria_recursiva(lista_entrada, objetivo, izquierda=0, derecha=None):
    if derecha is None:
        derecha = len(lista_entrada) - 1

    if izquierda > derecha:  # Intervalo vacío — el objetivo no puede estar aquí
        return False

    medio = (izquierda + derecha) // 2

    if lista_entrada[medio] == objetivo:
        return True
    elif objetivo < lista_entrada[medio]:
        return busqueda_binaria_recursiva(lista_entrada, objetivo, izquierda, medio - 1)
    else:
        return busqueda_binaria_recursiva(lista_entrada, objetivo, medio + 1, derecha)
```


### Ejemplo de Ejecución

Python

```python
# El mapa de zonas ya está ordenado — ese es el requisito previo
mapa_zonas = ['Bosque de Cenizas', 'Breva del Ocaso', 'Cascadas Luminosas', 'Everest', 'Pico de Brasa', 'Puente Dorado', 'Puerta de Escarcha']

print(busqueda_binaria(mapa_zonas, 'Breva del Ocaso'))   # Salida: True
print(busqueda_binaria(mapa_zonas, 'Torre de la Luna'))  # Salida: False
```

La versión recursiva devuelve las mismas respuestas sobre la misma lista:

Python

```python
print(busqueda_binaria_recursiva(mapa_zonas, 'Breva del Ocaso'))   # Salida: True
print(busqueda_binaria_recursiva(mapa_zonas, 'Torre de la Luna'))  # Salida: False
```

La Búsqueda Binaria también funciona con datos numéricos. Estas son las mismas velocidades enemigas que el ordenamiento por inserción dejó en su sitio en la nota anterior:

Python

```python
velocidades_enemigas = [20, 30, 45, 55, 80, 95]  # Ya ordenadas con insertion_sort()

print(busqueda_binaria(velocidades_enemigas, 55))  # Salida: True
print(busqueda_binaria(velocidades_enemigas, 70))  # Salida: False
```


### Manejo de Casos Límite

Una búsqueda nunca falla en un valor de frontera siempre que la comprobación del intervalo sea `izquierda <= derecha` y los punteros se muevan con `medio + 1` / `medio - 1`:

Python

```python
# Primer y último elemento de la lista
print(busqueda_binaria(mapa_zonas, 'Bosque de Cenizas'))   # Salida: True
print(busqueda_binaria(mapa_zonas, 'Puerta de Escarcha'))  # Salida: True

# Lista de un solo elemento, con coincidencia y sin coincidencia
print(busqueda_binaria(['Puerta de Escarcha'], 'Puerta de Escarcha'))  # Salida: True
print(busqueda_binaria(['Puerta de Escarcha'], 'Everest'))             # Salida: False

# Lista vacía
print(busqueda_binaria([], 'Everest'))  # Salida: False
```


## 4. Eficiencia Algorítmica

- **Complejidad Temporal:** $O(\log N)$ — Dividir a la mitad el espacio de búsqueda en cada paso reduce drásticamente el total de operaciones frente a los $O(N)$ de una búsqueda lineal.
    
- **Complejidad Espacial:** $O(1)$ para la implementación iterativa, $O(\log N)$ para la recursiva (la pila de llamadas guarda un marco por cada división a la mitad).

Contar los pasos sobre un mapa de 1000 sectores hace medible la diferencia:

Python

```python
def busqueda_binaria_intentos(lista_entrada, objetivo):
    izquierda, derecha, intentos = 0, len(lista_entrada) - 1, 0

    while izquierda <= derecha:
        intentos += 1
        medio = (izquierda + derecha) // 2

        if lista_entrada[medio] == objetivo:
            return intentos
        elif objetivo < lista_entrada[medio]:
            derecha = medio - 1
        else:
            izquierda = medio + 1

    return intentos

def busqueda_lineal_intentos(lista_entrada, objetivo):
    for paso, elemento in enumerate(lista_entrada, 1):
        if elemento == objetivo:
            return paso
    return len(lista_entrada)

mapa_grande = [f'Sector-{indice:03d}' for indice in range(1000)]

print(busqueda_binaria_intentos(mapa_grande, 'Sector-000'))  # Salida: 9
print(busqueda_binaria_intentos(mapa_grande, 'Sector-999'))  # Salida: 10
print(busqueda_lineal_intentos(mapa_grande, 'Sector-999'))   # Salida: 1000
```

La Búsqueda Binaria nunca necesita más de 10 revisiones sobre 1000 elementos, porque $2^{10} = 1024$. La Búsqueda Lineal tuvo que recorrer el mapa entero.

- **Mejor Caso:** $O(1)$ — el objetivo cae justo en el primer índice central evaluado.
    
- **Peor Caso:** $O(\log N)$ — el objetivo no está presente y cada intervalo se divide a la mitad hasta colapsar.



### Errores Comunes

- **Buscar en una lista sin ordenar:** el algoritmo devuelve `False` de forma silenciosa para valores que sí están presentes, porque la mitad descartada ya no garantiza estar del lado equivocado.
    
- **Mover `izquierda = medio` en lugar de `medio + 1`:** el puntero nunca avanza más allá de `medio` y el bucle se repite indefinidamente.
    
- **Aplicarlo sobre una lista enlazada:** la Búsqueda Binaria necesita acceso aleatorio $O(1)$, y los nodos se alcanzan uno por uno.


> **Conclusión:** Ordenar es el precio que se paga por adelantado ($O(N \log N)$) a cambio de una búsqueda que responde en $O(\log N)$ pasos. Cuando una colección se consulta una y otra vez, pagar una sola vez el ordenamiento sale más barato que recorrerla en cada consulta.
