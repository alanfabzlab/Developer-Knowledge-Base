
<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 🐍 Fundamentos de Python: Configuración, Salida y Tipos de Datos

![Python Badge](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)![Status Badge](https://img.shields.io/badge/Difficulty-Beginner-brightgreen?style=for-the-badge)

**Versión original en inglés:** [01 - Setup & Data Types.md](./01%20-%20Setup%20&%20Data%20Types.md)

**Curso:** Python
**Tema:** Configuración del entorno, salida, variables, tipos de datos y operadores aritméticos
**Etiquetas:** `#python` `#programming` `#basics` `#open-source` `#notes`


---

## 01. Configuración e Historia

**Nota:** Información Clave
**Python** fue creado por **Guido van Rossum** a comienzos de la década de 1990. Está diseñado para ser legible, de alto nivel y versátil.

### Casos de Uso Comunes
- 🎮 Desarrollo de Juegos y Scripting de Motores
- 🤖 Inteligencia Artificial (IA) y Machine Learning (ML)
- 📊 Análisis y Visualización de Datos
- 🌐 Desarrollo Web

### Herramientas Principales
- **Archivos:** El código se guarda en archivos de texto con la extensión `.py`.
- **Editor de código:** Software usado para escribir, editar y ejecutar código.

---

## 02. Salida e Impresión en Consola

En Python, usamos la función integrada `print()` para enviar texto o datos a la terminal (salida).

```python

# Basic Output
print('¡Hola Mundo!')

```

**Consejo:** Orden de Ejecución
Python ejecuta el código línea por línea, de forma secuencial de arriba abajo.

Python

```python
print('👾 ¡Hola Desarrollador!')
print('🚀 ¡Sistemas Listos!')
```

**Salida:**

```
👾 ¡Hola Desarrollador!
🚀 ¡Sistemas Listos!
```


## 03. Retos de Práctica y Patrones

### 📐 Reto del Contador de Daño (`damage_board.py`)

Para imprimir formas formateadas o líneas de texto, apila varias sentencias `print()`:

Python

```python
# damage_board.py
print('   1')
print('  2 3')
print(' 4 5 6')
print('7 8 9 10')
```

### 🎮 Reto de Letras de Bloque (`initials.py`)

Crea iniciales de letras de bloque en ASCII acompañadas de un comentario de código.


```python
# Fun fact: My favorite genre is dungeon crawler RPGs!

print(" DDD   DDD ")
print("D   D D   D")
print("D   D D   D")
print("D   D D   D")
print(" DDD   DDD ")
```

## 04. Carta a tu Yo Futuro (`letter.py`)

Usa comentarios (`#`) para la documentación junto a las sentencias de salida:


```python
# Goal: Note to my future game developer self
# Date: 2026

print("Fecha: 13 de septiembre de 2026")
print("Estado: Construyendo un dungeon crawler roguelike en Obsidian.")
print("Meta: Dominar la ingeniería de software y el desarrollo de juegos.")
print("Mensaje: ¡Publica una mazmorra todos los días!")
print("Emoji Favorito: 🎮")
```

## 05. Variables y Tipos de Datos

**Nota:** ¿Qué es una Variable?

Una **variable** actúa como un contenedor con nombre que guarda un valor de dato en memoria.

Asigna valores usando el signo igual (`=`): `variable_name = value`.


```python
# Variable declarations & reassignment
nombre_heroe = 'Aria Stormborn'
guardado = 2
progreso = 0.85
experiencia = 120
tiene_mapa = True

# Value Reassignment
experiencia = 150
experiencia = 200
print(experiencia)  # Output: 200
```

| Tipo        | Nombre            | Descripción             | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Cadena** | `str` | Texto entre comillas simples o dobles | `'Level 12'`, `"Ranger"` |
| **Entero** | `int` | Números enteros (positivos, negativos o cero) | `2026`, `-42` |
| **Decimal** | `float` | Números decimales | `0.75`, `3.14159` |
| **Booleano** | `bool` | Valores lógicos de verdad | `True`, `False` |

---

## 06. Operadores Aritméticos

Python incluye operadores aritméticos estándar para realizar cálculos matemáticos:

|**Operador**|**Nombre**|**Descripción**|**Ejemplo**|**Resultado**|
|---|---|---|---|---|
|`+`|Suma|Suma dos valores|`15 + 5`|`20`|
|`-`|Resta|Resta un valor de otro|`15 - 5`|`10`|
|`*`|Multiplicación|Multiplica dos valores|`15 * 5`|`75`|
|`/`|División|Divide el numerador por el denominador (devuelve decimal)|`15 / 5`|`3.0`|
|`%`|Módulo|Devuelve el resto de una división|`15 % 4`|`3`|
|`**`|Potencia|Eleva la base a la potencia del exponente|`3 ** 3`|`27`|


### 🧮 Ejemplos Prácticos y Retos de Fórmulas


#### 💡 Cálculo de Daño Crítico (`crit.py`)
```python
daño_base = 45
bonus_arma = 15

total = daño_base + bonus_arma
daño_critico = total * 0.25

print(daño_critico)  # Output: 15.0
```


#### ⚖️ Ratio de Peso Transportado (`encumbrance.py`)

$$bmi = \frac{mass}{height^2}$$

```python
# encumbrance.py
peso_cargado = 80     # in kilograms of carried loot
altura_heroe = 1.86    # in meters

carga = peso_cargado / (altura_heroe ** 2)
print(carga)
```


#### 📐 Trayectoria del Hechizo (`spell_range.py`)

$$c = \sqrt{a^2 + b^2}$$

```python
# spell_range.py
a = int(input('Introduce la distancia horizontal del lanzamiento a: '))
b = int(input('Introduce la distancia vertical del lanzamiento b: '))

c = (a**2 + b**2) ** 0.5
print(c)
```


## 07. Entrada del Usuario y Conversión de Tipos

Para interactuar con los usuarios, Python proporciona la función integrada `input()`.

**Advertencia:** Tipo de Entrada por Defecto `input()` **siempre** devuelve la respuesta del usuario como un `str` (cadena). Para realizar cálculos, conviértela usando `int()` o `float()`.


### ⌨️ Entrada Estándar

```python
heroe = input('Introduce el nombre de tu héroe: ')
print(heroe)
```


🔢 Conversión de Tipos (`int()`)

```python
nivel = int(input('¿Cuál es tu nivel actual? '))
print(nivel)  # Stored as integer 30, not string "30"
```


## 08. Reto de Repaso del Capítulo: Convertidor a Oro (`gold_converter.py`)

Un programa convertidor de múltiples monedas que convierte Monedas de Cobre, Monedas de Plata y Esmeraldas a Oro:

```python
# gold_converter.py

cobre = int(input('Cantidad en monedas de cobre: '))
plata = int(input('Cantidad en monedas de plata: '))
esmeraldas = int(input('Cantidad de esmeraldas: '))

# Standard exchange rate factors
oro_del_cobre = cobre * 0.0001
oro_de_la_plata = plata * 0.1
oro_de_las_esmeraldas = esmeraldas * 5

oro_total = oro_del_cobre + oro_de_la_plata + oro_de_las_esmeraldas

print(oro_total)
```
