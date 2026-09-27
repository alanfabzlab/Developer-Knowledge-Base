
<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 🔀 Control de Flujo y Manejo de Errores en Python

![Status Badge](https://img.shields.io/badge/Topic-Control%20Flow-orange?style=for-the-badge)

**Versión original en inglés:** [02 - Control Flow.md](./02%20-%20Control%20Flow.md)

**Curso:** Python
**Tema:** Errores comunes, sentencias condicionales, operadores relacionales y lógicos
**Etiquetas:** `#python` `#control-flow` `#logic` `#fundamentals`


---

## 01. Errores Comunes en Python

Los errores son una parte natural de la programación. Reconocer los tipos de error ayuda a depurar el código más rápido.

### 📌 Principales Tipos de Error

- **`SyntaxError`**: Ocurre cuando el código viola las reglas de sintaxis de Python (palabras clave mal escritas, comillas faltantes o estructura inválida).
- **`NameError`**: Ocurre al referenciar una variable o función que todavía no ha sido definida.
- **`TypeError`**: Ocurre al aplicar una operación a un tipo de dato incompatible (por ejemplo, combinar cadenas y enteros sin convertirlos).

---

### 🔍 Ejemplos de Errores y Soluciones

#### ❌ Ejemplo de SyntaxError

```python
# Error: Falta la comilla de cierre y la sintaxis adecuada
print(Welcome to the Kingdom!

# SyntaxError: invalid syntax
```

#### ❌ Ejemplo de NameError

```python
# Error: Referencia a una variable indefinida
print(hp_goblin)

# NameError: name 'hp_goblin' is not defined

# Solución: Define la variable antes de referenciarla
hp_goblin = 40
print(hp_goblin)  # Salida: 40
```

#### ❌ Ejemplo de TypeError

```python
# Error: Intento de concatenar una cadena con un entero directamente
estado = 'Nivel del Jugador: '
print(estado + 5)

# TypeError: can only concatenate str (not "int") to str

# Solución: Convierte el entero usando str()
estado = 'Nivel del Jugador: '
print(estado + str(5))  # Salida: Nivel del Jugador: 5
```

🐛 Reto de Depuración: Cazador de Errores (`bug_catcher.py`)

```python
# Versión corregida del script de rastreo de botín
pociones_salud = 5
pociones_mana = 8
runas_bomba = 12

print('Bolsa de Botín: ' + str(pociones_salud) + ' Pociones de Salud')
print('Bolsa de Botín: ' + str(pociones_mana) + ' Pociones de Mana')
print('Bolsa de Botín: ' + str(runas_bomba) + ' Runas de Bomba')

total_objetos = pociones_salud + pociones_mana + runas_bomba
print('Objetos totales: ' + str(total_objetos) + ' ¡objetos recogidos!')
```

## 02. Control de Flujo y Toma de Decisiones

Por defecto, Python ejecuta el código secuencialmente línea por línea. El **Control de Flujo** permite que los programas ejecuten diferentes bloques de código según condiciones específicas.

**Nota:** Concepto Piensa en el control de flujo como un cruce de caminos: si una condición se evalúa como `True`, el programa toma un camino; si es `False`, toma otro.


### 🎲 Simulación de Tirada de Daño (`damage_roll.py`)

Usa el módulo `random` para ejecutar bloques de código condicionales según un número generado:

```python
# damage_roll.py
import random

# Genera un entero aleatorio entre 1 y 6 (una tirada de d6)
num = random.randint(1, 6)

if num > 3:
  print('¡Golpe Crítico! ⚔️')
else:
  print('Golpe Normal 🛡️')
```


## 03. Sentencias Condicionales: `if` y `else`

### 🔹 Sentencia `if`

Evalúa una condición. Si la condición es `True`, se ejecuta el bloque indentado que hay debajo.

```python
experiencia = 75

if experiencia >= 60:
  print('¡Subida de Nivel Disponible! ✅')
```


### 🔹 Cláusula `else`

Proporciona un bloque de ejecución alternativo cuando la condición `if` se evalúa como `False`.

```python
experiencia = 45

if experiencia >= 60:
  print('¡Subida de Nivel Disponible! ✅')
else:
  print('Aún no tienes suficiente XP ❌')
```


### 🏆 Verificador de Umbral de Rango (`ranks.py`)

Comprueba si la puntuación de una partida alcanza el umbral mínimo para desbloquear la cola clasificada (55):

```python
# ranks.py

# Puntuación de la partida (Rango 0-100)
puntuacion = 78

if puntuacion >= 55:
  print('¡Cola clasificada desbloqueada!')
else:
  print('Sigue farmando la campaña.')
```


---

## 04. Operadores Relacionales y Sentencias `elif`

Los operadores relacionales comparan dos valores y devuelven un resultado booleano (`True` o `False`):

- `==` Igual a
- `!=` Distinto de
- `>` Mayor que
- `<` Menor que
- `>=` Mayor o igual que
- `<=` Menor o igual que


### 🔹 La Sentencia `elif`
Cuando compruebes más de dos condiciones, añade bloques `elif` (else if) entre `if` y `else`.

```python
rareza = 4.8

if rareza >= 4.5:
  print('Arma Mítica 🌟')
elif rareza >= 3.5:
  print('Arma Legendaria 👍')
elif rareza >= 2.5:
  print('Arma Rara 😐')
else:
  print('Basura Común 👎')
```


### 🧪 Análisis de Pureza de Pociones (`potion_purity.py`)

Comprueba los niveles de pureza de los elixires para determinar qué tan sobrepoderoso es un brebaje:

```python
# potion_purity.py

pureza = float(input('Introduce el nivel de pureza (0-100): '))

if pureza > 70:
  print('Sobredimensionado')
elif pureza < 30:
  print('Lodo')
else:
  print('Equilibrado')
```


## 05. Generando Valores Aleatorios (`loot_box.py`)

El módulo integrado `random` de Python proporciona funciones como `randint(a, b)` para producir enteros aleatorios dentro de un rango $[a, b]$ inclusive.

```python
import random

# Genera un resultado entre 1 y 9
opcion = random.randint(1, 9)

pregunta = input('Haz una pregunta de decisión: ')

if opcion == 1:
  respuesta = 'Cayó una hoja legendaria. Seguro.'
elif opcion == 2:
  respuesta = 'Es un crítico. Definitivamente.'
elif opcion == 3:
  respuesta = 'Sin ninguna duda, hace crítico.'
elif opcion == 4:
  respuesta = 'Reinicio pendiente, inténtalo de nuevo.'
elif opcion == 5:
  respuesta = 'Pregunta de nuevo después de las notas del parche.'
elif opcion == 6:
  respuesta = 'Mejor no te lo cuento ahora.'
elif opcion == 7:
  respuesta = 'Mis notas del parche dicen que no.'
elif opcion == 8:
  respuesta = 'La prueba de DPS no sale bien.'
else:
  respuesta = 'Muy dudoso, desconectado.'

print('Pregunta: ' + pregunta)
print('Oráculo de la Caja de Botín: ' + respuesta)
```



## 06. Operadores Lógicos

Los operadores lógicos evalúan y combinan múltiples expresiones booleanas:

- `and`: Devuelve `True` solo si **ambas** condiciones se evalúan como `True`.
    
- `or`: Devuelve `True` si **al menos una** condición se evalúa como `True`.
    
- `not`: Invierte el estado booleano (`True` se convierte en `False`).
    

|**A**|**B**|**A y B**|**A o B**|
|---|---|---|---|
|`False`|`False`|`False`|`False`|
|`False`|`True`|`False`|`True`|
|`True`|`False`|`False`|`True`|
|`True`|`True`|`True`|`True`|


```python
# Ejemplos Prácticos
resistencia = 8
puntería = 6

if resistencia > 5 and puntería > 5:
  print('¡Ventana perfecta de headshot!')

tiene_pocion = True
tiene_eter = False

if tiene_pocion or tiene_eter:
  print('Bufs obtenidos ☕')

en_pausa = False

if not en_pausa:
  print('¡Listo para farmear al jefe!')
```



### 🎢 Verificador de Acceso a Boss Rush (`boss_rush.py`)

Evalúa el requisito de nivel (Nivel $40$) y los tokens de entrada ($15\text{ tokens}$):

```python
# boss_rush.py

nivel = int(input('Introduce tu nivel: '))
tokens = int(input('Introduce tus tokens disponibles: '))

if nivel >= 40 and tokens >= 15:
  print('¡Boss Rush desbloqueado!')
elif tokens >= 15 and nivel < 40:
  print('No tienes nivel suficiente para entrar.')
elif nivel >= 40 and tokens < 15:
  print("No tienes suficientes tokens.")
else:
  print('Requisitos no cumplidos para entrar.')
```


## 7. Proyecto Final: Cuestionario de Estilos de Juego (`playstyle_quiz.py`)

```python
# playstyle_quiz.py

vanguardia = 0
explorador = 0
arcanista = 0
sombra = 0

print('Q1) ¿Prefieres el frente o la retaguardia?')
print('  1) Frontal')
print('  2) Retaguardia')
respuesta_1 = int(input('Respuesta (1-2): '))

if respuesta_1 == 1:
  vanguardia += 1
  arcanista += 1
elif respuesta_1 == 2:
  explorador += 1
  sombra += 1
else:
  print('Entrada no válida.')

print('\nQ2) En un grupo, quiero que me recuerden como:')
print('  1) El Protector')
print('  2) El Duelista')
print('  3) El Erudito')
print('  4) El Cazador')
respuesta_2 = int(input('Respuesta (1-4): '))

if respuesta_2 == 1:
  vanguardia += 2
elif respuesta_2 == 2:
  sombra += 2
elif respuesta_2 == 3:
  arcanista += 2
elif respuesta_2 == 4:
  explorador += 2
else:
  print('Entrada no válida.')

print('\nQ3) ¿Qué banda sonora te mantiene concentrado mientras farmeas?')
print('  1) Banda Sonora Orquestal')
print('  2) Heavy Metal')
print('  3) Lo-Fi Beats')
print('  4) Drum & Bass')
respuesta_3 = int(input('Respuesta (1-4): '))

if respuesta_3 == 1:
  arcanista += 4
elif respuesta_3 == 2:
  vanguardia += 4
elif respuesta_3 == 3:
  explorador += 4
elif respuesta_3 == 4:
  sombra += 4
else:
  print('Entrada no válida.')

print('\n--- Puntuaciones Finales ---')
print('Vanguardia:', vanguardia)
print('Explorador:', explorador)
print('Arcanista:', arcanista)
print('Sombra:', sombra)
```
