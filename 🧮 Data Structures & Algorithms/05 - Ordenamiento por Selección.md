
# 05. Ordenamiento por Selección y Eficiencia Cuadrática


**Versión original en inglés:** [05 - Selection Sort.md](05%20-%20Selection%20Sort.md)

**Curso:** Estructuras de Datos y Algoritmos
**Tema:** Bucles Anidados, Ordenamiento en el Mismo Espacio de Memoria, Intercambio de Elementos y Eficiencia Cuadrática
**Etiquetas:** `#dsa` `#sorting` `#selection-sort` `#complexity`



## 1. Cómo funciona el Ordenamiento por Selección

El **Ordenamiento por Selección** es un algoritmo de ordenamiento por comparación que se realiza en el mismo espacio de memoria. Divide la lista de entrada en dos partes:
1. Una **sublista ordenada** que se construye de izquierda a derecha al principio de la lista.
2. Una **sublista sin ordenar** que ocupa el resto de la lista.

En cada iteración (o pasada), el algoritmo encuentra el elemento más pequeño de la sublista sin ordenar y lo intercambia con el elemento sin ordenar más a la izquierda.



---


## 2. Implementación en Python

La implementación se apoya en **bucles anidados**:
- **Bucle externo (`j`):** Controla la marca que separa la sección ordenada de la sin ordenar.
- **Bucle interno (`i`):** Recorre la sección sin ordenar para encontrar el índice del elemento mínimo.


Python

```python
def intercambiar(lista_entrada, indice_1, indice_2):
    temp = lista_entrada[indice_1]
    lista_entrada[indice_1] = lista_entrada[indice_2]
    lista_entrada[indice_2] = temp
    return lista_entrada

def ordenamiento_seleccion(mi_lista):
    # El bucle externo mueve el límite de la sublista sin ordenar
    for j in range(len(mi_lista)):
        indice_minimo = j

        # El bucle interno encuentra el elemento más pequeño de la parte sin ordenar
        for i in range(j + 1, len(mi_lista)):
            if mi_lista[i] < mi_lista[indice_minimo]:
                indice_minimo = i

        # Intercambia el mínimo encontrado con el primer elemento sin ordenar
        mi_lista = intercambiar(mi_lista, j, indice_minimo)

    return mi_lista

# Puntos de vida de los jefes en el orden en que el bestiario los escanea
vida_jefes = [480, 120, 950, 300]  # Caballero de Brasa, Espectro de Escarcha, Golem de Piedra, Segador del Vacio

print(f"PV ordenados: {ordenamiento_seleccion(vida_jefes)}")            # Salida: PV ordenados: [120, 300, 480, 950]
print(f"Misma lista, ordenada en el sitio: {vida_jefes}")               # Salida: Misma lista, ordenada en el sitio: [120, 300, 480, 950]
```


### Observando crecer la Sección Ordenada

Imprimir la lista después de cada pasada hace visibles las dos secciones: las primeras `j + 1` posiciones son definitivas y todo lo que está después sigue en juego.

Python

```python
def ordenamiento_seleccion_traza(mi_lista):
    for j in range(len(mi_lista)):
        indice_minimo = j

        for i in range(j + 1, len(mi_lista)):
            if mi_lista[i] < mi_lista[indice_minimo]:
                indice_minimo = i

        mi_lista = intercambiar(mi_lista, j, indice_minimo)
        print(f"Pasada {j + 1}: {mi_lista}")

    return mi_lista

ordenamiento_seleccion_traza([480, 120, 950, 300])
```

```text
Pasada 1: [120, 480, 950, 300]
Pasada 2: [120, 300, 950, 480]
Pasada 3: [120, 300, 480, 950]
Pasada 4: [120, 300, 480, 950]
```

- **Pasada 1** fija el `120` e intercambia su lugar con el primer elemento actual.
    
- **Pasada 2** fija el `300`, intercambiándolo con el `480` en lugar de desplazar todos los elementos una posición hacia la derecha.
    
- **Pasada 3** fija el `480` y deja el `950` en la única posición que queda.
    
- **Pasada 4** tiene el bucle interno vacío, así que la pasada final no cambia nada.


## 3. Análisis de Eficiencia Cuadrática ($O(N^2)$)

### Recuento de Comparaciones

Para una lista de tamaño $n$:

- **Pasada 1:** Realiza $n - 1$ comparaciones.
    
- **Pasada 2:** Realiza $n - 2$ comparaciones.
    
- **Pasada 3:** Realiza $n - 3$ comparaciones.
    


Total de comparaciones:

$$(n - 1) + (n - 2) + \dots + 1 = \frac{n(n - 1)}{2}$$

Una ejecución instrumentada confirma la fórmula y muestra que el total está fijado de antemano, sin importar los datos:

Python

```python
def ordenamiento_seleccion_comparaciones(mi_lista):
    comparaciones = 0

    for j in range(len(mi_lista)):
        indice_minimo = j

        for i in range(j + 1, len(mi_lista)):
            comparaciones += 1
            if mi_lista[i] < mi_lista[indice_minimo]:
                indice_minimo = i

        mi_lista = intercambiar(mi_lista, j, indice_minimo)

    return comparaciones

for tamano in (4, 8, 16, 1000):
    print(tamano, ordenamiento_seleccion_comparaciones(list(range(tamano))))
```

```text
4 6
8 28
16 120
1000 499500
```

Un bestiario de 1000 jefes cuesta **499,500 comparaciones** — medio millón de operaciones para dejar en secuencia el orden de escaneo, y el mismo total se aplica incluso si la lista llega ya ordenada. El número de comparaciones depende únicamente de $n$, nunca de los datos de entrada.

### Clasificación Big-O

Al aproximarnos a las operaciones del peor caso a medida que crece el tamaño de la lista:

- Tanto el **Ordenamiento por Selección** como el **Ordenamiento por Burbuja** y el **Ordenamiento por Inserción** realizan aproximadamente $n \times n = n^2$ comparaciones.
    
- **Complejidad Temporal:** $O(N^2)$ (Tiempo Cuadrático).
    
- **Complejidad Espacial:** $O(1)$ (Espacio Auxiliar — se ordena en el mismo espacio de memoria).
    

> **Conclusión:** Los algoritmos cuadráticos se ralentizan de forma dramática a medida que crece el tamaño de la entrada. Para conjuntos de datos grandes, algoritmos como el **Ordenamiento por Mezcla** ($O(N \log N)$) son significativamente más rápidos. La única ventaja del Ordenamiento por Selección es que realiza como máximo $n - 1$ intercambios, lo cual importa cuando escribir en memoria es costoso — pero las comparaciones siguen dominando, así que es un algoritmo para enseñar más que para usar en producción.


---

## 4. Demo de Eficiencia y Análisis Comparativo

La fórmula anterior predice el total, así que vale la pena confirmarla — y revisar cómo se comparan entre sí los tres ordenamientos cuadráticos sobre los mismos datos.

Python

```python
# Cada variante solo cuenta comparaciones; el ordenamiento sigue reordenando la lista
def ordenamiento_seleccion_contado(mi_lista):
    comparaciones = 0
    for j in range(len(mi_lista)):
        indice_minimo = j

        for i in range(j + 1, len(mi_lista)):
            comparaciones += 1
            if mi_lista[i] < mi_lista[indice_minimo]:
                indice_minimo = i

        mi_lista = intercambiar(mi_lista, j, indice_minimo)

    return comparaciones

def ordenamiento_burbuja_contado(mi_lista):
    comparaciones = 0

    for j in range(len(mi_lista) - 1):
        for i in range(0, len(mi_lista) - 1 - j):
            comparaciones += 1
            if mi_lista[i] > mi_lista[i + 1]:
                mi_lista = intercambiar(mi_lista, i, i + 1)

    return comparaciones

def ordenamiento_insercion_contado(mi_lista):
    comparaciones = 0

    for i in range(1, len(mi_lista)):
        clave = mi_lista[i]
        k = i - 1

        while k >= 0:
            comparaciones += 1
            if mi_lista[k] <= clave:
                break
            mi_lista[k + 1] = mi_lista[k]
            k -= 1

        mi_lista[k + 1] = clave

    return comparaciones
```

Ejecutando los tres sobre la misma lista de 10 elementos, primero ya ordenada y luego al revés:

```python
ordenado = [20, 30, 45, 55, 60, 70, 80, 85, 90, 95]
orden_inverso = ordenado[::-1]

print('n = 10, ya ordenado')
print('Selección:', ordenamiento_seleccion_contado(ordenado[:]))
print('Burbuja:   ', ordenamiento_burbuja_contado(ordenado[:]))
print('Inserción:', ordenamiento_insercion_contado(ordenado[:]))

print('\nn = 10, orden inverso')
print('Selección:', ordenamiento_seleccion_contado(orden_inverso[:]))
print('Burbuja:   ', ordenamiento_burbuja_contado(orden_inverso[:]))
print('Inserción:', ordenamiento_insercion_contado(orden_inverso[:]))
```

```text
n = 10, ya ordenado
Selección: 45
Burbuja:    45
Inserción: 9

n = 10, orden inverso
Selección: 45
Burbuja:    45
Inserción: 45
```


### Conclusiones Clave del Demo

- **Fórmula Exacta de Comparaciones:** Para $n = 10$, el Ordenamiento por Selección realiza exactamente $(10 \times 9) / 2 = 45$ comparaciones, y el total es idéntico en ambas ejecuciones. Solo $n$ decide la cantidad, nunca el orden de los datos.
    
- **Ordenamiento por Burbuja frente a Inserción:** El Ordenamiento por Burbuja también reporta 45 en los dos casos, porque la versión ingenua siempre ejecuta las $n - 1$ pasadas. El Ordenamiento por Inserción baja a 9 con la lista ordenada — exactamente el caso de $n - 1$ — y sube a 45 cuando los datos vienen al revés.
    
- **La Distinción Real:** Los tres comparten el peor caso $O(N^2)$, pero solo el Ordenamiento por Inserción mejora con una entrada ya ordenada, y por eso es el que vale la pena elegir cuando es probable que haya un orden parcial.


---

## 5. Repaso del Capítulo y Patrones Algorítmicos

Este capítulo completa la comparación central de los fundamentos de búsqueda y ordenamiento:

- **Búsqueda Lineal:** Recorre cada elemento de forma secuencial y funciona sobre una lista sin ordenar ($O(N)$).
    
- **Búsqueda Binaria:** Divide a la mitad repetidamente una lista ordenada ($O(\log N)$), pagando de antemano el ordenamiento.
    
- **Ordenamiento por Selección:** Usa **bucles `for` anidados** para hacer crecer una sección ordenada y colocar en cada pasada el elemento mínimo del resto sin ordenar, con un trabajo cuadrático ($O(N^2)$).

El patrón que recorre los tres es el mismo canje: cuanta más estructura se le permita asumir al algoritmo sobre la entrada, menos trabajo tiene que hacer. La Búsqueda Lineal no asume nada y paga $O(N)$. La Búsqueda Binaria asume que la lista está ordenada y paga $O(\log N)$. El Ordenamiento por Selección no asume nada y paga $O(N^2)$.

