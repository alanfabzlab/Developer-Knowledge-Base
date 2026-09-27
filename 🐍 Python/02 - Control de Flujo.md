
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
# Error: Missing closing quote and proper syntax
print(Welcome to the Kingdom!

# SyntaxError: invalid syntax
```

#### ❌ Ejemplo de NameError

```python
# Error: Referencing an undefined variable
print(goblin_hp)

# NameError: name 'goblin_hp' is not defined

# Fix: Define the variable before referencing it
goblin_hp = 40
print(goblin_hp)  # Output: 40
```

#### ❌ Ejemplo de TypeError

```python
# Error: Attempting string concatenation with an integer directly
status = 'Player Level: '
print(status + 5)

# TypeError: can only concatenate str (not "int") to str

# Fix: Cast integer using str()
status = 'Player Level: '
print(status + str(5))  # Output: Player Level: 5
```

🐛 Reto de Depuración: Cazador de Errores (`bug_catcher.py`)

```python
# Fixed version of loot tracking script
health_potions = 5
mana_potions = 8
bomb_runes = 12

print('Loot Bag: ' + str(health_potions) + ' Health Potions')
print('Loot Bag: ' + str(mana_potions) + ' Mana Potions')
print('Loot Bag: ' + str(bomb_runes) + ' Bomb Runes')

total_items = health_potions + mana_potions + bomb_runes
print('Total items: ' + str(total_items) + ' items collected!')
```

## 02. Control de Flujo y Toma de Decisiones

Por defecto, Python ejecuta el código secuencialmente línea por línea. El **Control de Flujo** permite que los programas ejecuten diferentes bloques de código según condiciones específicas.

**Nota:** Concepto Piensa en el control de flujo como un cruce de caminos: si una condición se evalúa como `True`, el programa toma un camino; si es `False`, toma otro.


### 🎲 Simulación de Tirada de Daño (`damage_roll.py`)

Usa el módulo `random` para ejecutar bloques de código condicionales según un número generado:

```python
# damage_roll.py
import random

# Generate a random integer between 1 and 6 (a d6 roll)
num = random.randint(1, 6)

if num > 3:
  print('Critical Hit! ⚔️')
else:
  print('Normal Hit 🛡️')
```


## 03. Sentencias Condicionales: `if` y `else`

### 🔹 Sentencia `if`

Evalúa una condición. Si la condición es `True`, se ejecuta el bloque indentado que hay debajo.

```python
xp = 75

if xp >= 60:
  print('Level Up Available! ✅')
```


### 🔹 Cláusula `else`

Proporciona un bloque de ejecución alternativo cuando la condición `if` se evalúa como `False`.

```python
xp = 45

if xp >= 60:
  print('Level Up Available! ✅')
else:
  print('Not Enough XP Yet ❌')
```


### 🏆 Verificador de Umbral de Rango (`ranks.py`)

Comprueba si la puntuación de una partida alcanza el umbral mínimo para desbloquear la cola clasificada (55):

```python
# ranks.py

# Match score (Range 0-100)
score = 78

if score >= 55:
  print('Ranked queue unlocked!')
else:
  print('Keep grinding the campaign.')
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
rarity = 4.8

if rarity >= 4.5:
  print('Mythic Weapon 🌟')
elif rarity >= 3.5:
  print('Legendary Weapon 👍')
elif rarity >= 2.5:
  print('Rare Weapon 😐')
else:
  print('Common Junk 👎')
```


### 🧪 Análisis de Pureza de Pociones (`potion_purity.py`)

Comprueba los niveles de pureza de los elixires para determinar qué tan sobrepoderoso es un brebaje:

```python
# potion_purity.py

purity = float(input('Enter purity level (0-100): '))

if purity > 70:
  print('Overpowered')
elif purity < 30:
  print('Sludge')
else:
  print('Balanced')
```


## 05. Generando Valores Aleatorios (`loot_box.py`)

El módulo integrado `random` de Python proporciona funciones como `randint(a, b)` para producir enteros aleatorios dentro de un rango $[a, b]$ inclusive.

```python
import random

# Generate a result between 1 and 9
option = random.randint(1, 9)

prompt = input('Ask a decision question: ')

if option == 1:
  answer = 'Legendary blade dropped. Definitely.'
elif option == 2:
  answer = 'It is a crit. Decidedly so.'
elif option == 3:
  answer = 'Without a doubt, it crits.'
elif option == 4:
  answer = 'Reroll pending, try again.'
elif option == 5:
  answer = 'Ask again after the patch notes.'
elif option == 6:
  answer = 'Better not tell you now.'
elif option == 7:
  answer = 'My patch notes say no.'
elif option == 8:
  answer = 'DPS check not so good.'
else:
  answer = 'Very doubtful, disconnected.'

print('Question: ' + prompt)
print('Loot Box Oracle: ' + answer)
```



## 06. Operadores Lógicos

Los operadores lógicos evalúan y combinan múltiples expresiones booleanas:

- `and`: Devuelve `True` solo si **ambas** condiciones se evalúan como `True`.
    
- `or`: Devuelve `True` si **al menos una** condición se evalúa como `True`.
    
- `not`: Invierte el estado booleano (`True` se convierte en `False`).
    

|**A**|**B**|**A and B**|**A or B**|
|---|---|---|---|
|`False`|`False`|`False`|`False`|
|`False`|`True`|`False`|`True`|
|`True`|`False`|`False`|`True`|
|`True`|`True`|`True`|`True`|


```python
# Practical Examples
stamina = 8
aim = 6

if stamina > 5 and aim > 5:
  print('Perfect headshot window!')

has_potion = True
has_ether = False

if has_potion or has_ether:
  print('Buffs acquired ☕')

is_paused = False

if not is_paused:
  print('Ready to grind the boss!')
```



### 🎢 Verificador de Acceso a Boss Rush (`boss_rush.py`)

Evalúa el requisito de nivel (Nivel $40$) y los tokens de entrada ($15\text{ tokens}$):

```python
# boss_rush.py

level = int(input('Enter your level: '))
tokens = int(input('Enter your available tokens: '))

if level >= 40 and tokens >= 15:
  print('Boss Rush unlocked!')
elif tokens >= 15 and level < 40:
  print('You are not high enough level to enter.')
elif level >= 40 and tokens < 15:
  print("You don't have enough tokens.")
else:
  print('Requirements not met for entry.')
```


## 7. Proyecto Final: Cuestionario de Estilos de Juego (`playstyle_quiz.py`)

```python
# playstyle_quiz.py

vanguard = 0
ranger = 0
arcanist = 0
shadow = 0

print('Q1) Do you prefer the frontlines or the backline?')
print('  1) Frontlines')
print('  2) Backline')
q1_answer = int(input('Answer (1-2): '))

if q1_answer == 1:
  vanguard += 1
  arcanist += 1
elif q1_answer == 2:
  ranger += 1
  shadow += 1
else:
  print('Invalid input.')

print('\nQ2) In a party, I want to be remembered as:')
print('  1) The Protector')
print('  2) The Duelist')
print('  3) The Scholar')
print('  4) The Hunter')
q2_answer = int(input('Answer (1-4): '))

if q2_answer == 1:
  vanguard += 2
elif q2_answer == 2:
  shadow += 2
elif q2_answer == 3:
  arcanist += 2
elif q2_answer == 4:
  ranger += 2
else:
  print('Invalid input.')

print('\nQ3) Which soundtrack gets you focused while grinding?')
print('  1) Orchestral Score')
print('  2) Heavy Metal')
print('  3) Lo-Fi Beats')
print('  4) Drum & Bass')
q3_answer = int(input('Answer (1-4): '))

if q3_answer == 1:
  arcanist += 4
elif q3_answer == 2:
  vanguard += 4
elif q3_answer == 3:
  ranger += 4
elif q3_answer == 4:
  shadow += 4
else:
  print('Invalid input.')

print('\n--- Final Scores ---')
print('Vanguard:', vanguard)
print('Ranger:', ranger)
print('Arcanist:', arcanist)
print('Shadow:', shadow)
```
