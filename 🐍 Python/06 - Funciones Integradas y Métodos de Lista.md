# 06 - Funciones Integradas y Métodos de Lista

**Versión original en inglés:** [06 - Built-in Functions & List Methods.md](./06%20-%20Built-in%20Functions%20&%20List%20Methods.md)

**Curso:** Python
**Tema:** Funciones integradas, métodos de lista, listas anidadas y matrices, diccionarios, conjuntos
**Etiquetas:** `#python` `#list-methods` `#built-in-functions` `#data-structures` `#iteration`

## 06. Proyecto de Registro de Boss Rush (`boss_rush_log.py`)

Combina los conceptos de creación e iteración de listas para producir un registro de boss rush.


### 📝 Ejercicio de Registro de Boss Rush (`boss_rush_log.py`)

```python
# boss_rush_log.py

cosas_derrotar = [
  'Derrota al Guardián del Tiempo solo con una pistola.',
  'Limpia la Fortaleza Hundida sin objetos de curación.',
  'Supera toda la incursión con cuatro jugadores.',
  'Termina la campaña en dificultad Pesadilla.',
  'Completa las Minas del Bosque de Cenizas en menos de 10 minutos.',
  'Recoge todas las llaves doradas del reino.',
  'Sobrevive a 100 olas del modo infinito.',
  'Construye un juego que funcione y publícalo.',
  'Haz pruebas de juego con desconocidos y toma notas.',
  'Nunca abandones por rage quit. Nunca más.'
]

for cosa in cosas_derrotar:
  print(cosa)
```



## 07. Listas Anidadas y Matrices

Una **lista anidada** es una lista que contiene otras listas como elementos.

```python
# Lista anidada mixta
mi_lista = ['a', 'b', 'c', [1, 2, 3]]

# Accediendo a elementos dentro de una lista anidada
print(mi_lista[3][1]) # Salida: 2
```



### 🔹 Matrices (Listas 2D)

Cuando todos los elementos de una lista son listas anidadas de la misma longitud, se forma una **matriz** o **lista 2D** (organizada en filas y columnas).


```python
matriz = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]
```


#### Ejemplo de Mapa de Batalla


```python
mapa_batalla = [
  ['M', 'M', 'M'],
  ['M', 'B', 'M'],
  ['S', 'B', 'T']
]

# Leyenda: M = montaña, B = aparición de jefe, S = tienda, T = tesoro

# Accediendo a la fila 2, columna 1
fila = 2
columna = 1
print(mapa_batalla[fila][columna]) # Salida: B
```


---


## Bonus: Diccionarios y Conjuntos en Python

Python ofrece estructuras más allá de las listas ordenadas estándar que permiten búsquedas más rápidas, organización optimizada y recuperación directa de valores.

---


## 1. Diccionarios

Un **diccionario** conecta una `key` única con un `value`. Son colecciones ordenadas que almacenan datos como pares `key: value`.

```python
grupo = {
    'Aria': 'Explorador',
    'Kai': 'Paladin',
    'Nyx': 'Mago'
}
```


### Accediendo a los Valores

Los elementos se recuperan usando indexación por clave `[key]` en lugar de índices numéricos basados en cero:


```python
print(grupo['Nyx']) 
# Salida: Mago
```

**Nota:** Reglas de las Claves

- Cada **key** debe ser única.

- Las **keys** se asignan directamente a valores (cualquier tipo de dato).

- Las **keys** son inmutables y no se pueden modificar después de crearse.


### Métodos del Diccionario

|Método|Descripción|Salida de Ejemplo|
|---|---|---|
|`.keys()`|Devuelve todas las claves del diccionario|`dict_keys(['Aria', 'Kai', 'Nyx'])`|
|`.values()`|Devuelve todos los valores|`dict_values(['Ranger', 'Paladin', 'Mage'], ...)`|
|`.items()`|Devuelve una lista de tuplas `(key, value)`|`dict_items([('Aria', 'Ranger'), ...])`|


```python
print(grupo.keys())
print(grupo.values())
print(grupo.items())
```


## 2. Conjuntos

Un **conjunto** es una colección no ordenada de **elementos únicos** sin duplicados.


```python
favoritos_botin = {'Espada', 'Escudo', 'Poción', 'Yelmo', 'Botas'}
favoritos_hechizos = {'Bastón', 'Varita', 'Poción', 'Pergamino', 'Runa'}
```

**Advertencia:** Crear Conjuntos Vacíos Declarar `{}` crea un **diccionario** vacío, no un conjunto. Para inicializar un conjunto vacío, usa `set()`:


```python
conjunto_vacio = set()
```


### Métodos del Conjunto

- **`.union()`**: Combina los elementos de ambos conjuntos.
    
- **`.intersection()`**: Encuentra los elementos presentes en ambos conjuntos.
    
- **`.difference()`**: Encuentra los elementos únicos del conjunto que llama.
    

Python

```python
# Unión
print(favoritos_botin.union(favoritos_hechizos))

# Intersección
print(favoritos_botin.intersection(favoritos_hechizos))
# Salida: {'Poción'}

# Diferencia
print(favoritos_botin.difference(favoritos_hechizos))
# Salida: {'Espada', 'Escudo', 'Yelmo', 'Botas'}
```

## Resumen: Visión General de Estructuras de Datos

|Estructura de Datos|Características|Caso de Uso Común|
|---|---|---|
|**Lista**|Ordenada, accesible por índice, permite duplicados|Bolsas de botín, registros de combate|
|**Diccionario**|Pares clave-valor, búsquedas de claves rápidas|Archivos de guardado, configuraciones de habilidades|
|**Conjunto**|Elementos no ordenados y únicos, comprobaciones de pertenencia rápidas|Filtrar buffs duplicados, comparar configuraciones|
