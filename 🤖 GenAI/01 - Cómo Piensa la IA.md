
# 01. Cómo Piensa la IA

**Versión original en inglés:** [01 - How AI Thinks.md](01%20-%20How%20AI%20Thinks.md)

**Curso:** GenAI
**Tema:** IA Generativa, Modelos de Lenguaje, Tokens, N-Gramas y Predicción del Siguiente Token
**Tags:** `#genai` `#ai` `#llm` `#basics` `#game-dev`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Todos los modelos de IA que has usado alguna vez son máquinas que completan frases. Suena a un retroceso hasta que caes en lo que implica: en cuanto puedas construir una tú mismo, en noventa líneas de Python, el misterio desaparece y empieza la ingeniería. Este capítulo construye esa máquina — y lo primero que escribe es texto de ambiente de *Emberfall*.

---

## 1. El truco de magia

> [!NOTE]
> **Información clave**
> La **IA Generativa** (GenAI) es inteligencia artificial que crea contenido nuevo —texto, código, imágenes, vídeo, audio— aprendiendo patrones a partir de enormes cantidades de datos.

Las herramientas de los ejercicios de este módulo son todas productos de GenAI:

| Herramienta | Casa | Qué es |
| :--- | :--- | :--- |
| **ChatGPT** | OpenAI | Una interfaz de chat sobre un modelo de lenguaje grande |
| **Claude** | Anthropic | Una interfaz de chat sobre un modelo de lenguaje grande |
| **Gemini** | Google | Una interfaz de chat sobre un modelo de lenguaje grande |

Responden preguntas, redactan textos y mantienen conversaciones. Parece magia, pero detrás de todas hay una idea sorprendentemente pequeña: **predecir qué viene después**.

### El juego de predecir

Intenta completar cada línea como lo haría un jugador:

| Prompt | Palabra más probable |
| :--- | :--- |
| El jugador desenvainó la legendaria | espada |
| La vida está al 12%, bebe la | poción |
| El jefe aparece en la | arena |

Acertaste casi todas porque has visto esos patrones miles de veces —en juegos, en libros, en las partidas de otros. Un modelo de lenguaje hace exactamente lo mismo, salvo que aprendió de una porción grande de internet en lugar de una infancia.

> [!NOTE]
> **La trampa**
> Las predicciones pueden sorprender. La IA no entiende el significado como tú, y se equivoca en cosas que a cualquier lector humano le parecen obvias.

---

## 2. Tokens

### No todos los modelos son modelos de lenguaje

| Familia de modelos | Entrada | Salida |
| :--- | :--- | :--- |
| **Modelos de lenguaje** (GPT, Claude, Gemini) | texto | texto |
| **Modelos de imagen** (DALL·E, Stable Diffusion) | texto, imágenes | imágenes |
| **Modelos de código** (Codex, Copilot) | texto, código | código |
| **Modelos de audio** (Whisper) | audio | texto |

Un **Modelo de Lenguaje Grande** (LLM) procesa y genera **texto**, y lo hace prediciendo el siguiente **token**.

### Cómo lee la IA

Los humanos leemos palabras. La IA no. Parte el texto en trozos más pequeños, y esos trozos son la unidad de todo:

> [!NOTE]
> **Token**
> Un token es uno de los trozos pequeños de texto que un modelo de IA lee y genera.

```text
"I am learning Generative AI"  ->  ["I", " am", " learning", " Gener", "ative", " AI"]
```

Esa frase se convirtió en seis tokens. El corte exacto depende del modelo — el tuyo lo partirá de otra forma.

### Un tokenizador sencillo

Las **expresiones regulares** (regex) describen la *forma* del texto que queremos extraer. Python las trae en el módulo `re`:

```python
import re

def tokenize(text):
    return re.findall(r'\w+|[^\w\s]', text)

print(tokenize("The goblin screams before it dies."))
```

**Salida:**

```text
['The', 'goblin', 'screams', 'before', 'it', 'dies', '.']
```

Desglosando el patrón `\w+|[^\w\s]`:

| Pieza | Qué encuentra | Ejemplo |
| :--- | :--- | :--- |
| `\w+` | Uno o más caracteres de palabra (una palabra) | `goblin` |
| `\|` | O — vale cualquiera de los dos lados | — |
| `[^\w\s]` | Un solo carácter que no sea de palabra ni de espacio | `.` |

```python
print(tokenize("Hello, world!"))
```

**Salida:**

```text
['Hello', ',', 'world', '!']
```

Fíjate en que la puntuación pasó a ser su propio token. No es un fallo del tokenizador; es una decisión, y sus consecuencias aparecen más adelante en este capítulo.

> [!TIP]
> No necesitas memorizar regex para seguir el hilo. Lo importante es entender qué hace el tokenizador.

### Tokenización del mundo real

Cada modelo parte el texto de forma distinta — no existe un enfoque único. Modelos como GPT y Claude usan **tokenización por subpalabras**: las palabras largas, raras o desconocidas se parten en trozos más pequeños reutilizables.

```text
"unscrolling"  ->  ["un", "scroll", "ing"]
```

Por eso un LLM puede manejar palabras que nunca ha visto enteras: ha visto las piezas.

---

## 3. Patrones

### N-gramas

Ahora que tenemos tokens, se ve cómo el modelo encuentra patrones. Un **n-grama** es una secuencia de *n* tokens consecutivos. Con la frase *the cat sat on the mat*:

| Nombre | n | Ejemplo |
| :--- | :--- | :--- |
| **Unigrama** | 1 | `the`, `cat`, `sat`, … |
| **Bigrama** | 2 | `the cat`, `cat sat`, `sat on`, … |
| **Trigrama** | 3 | `the cat sat`, `cat sat on`, … |

Los bigramas son los útiles: dicen qué token *tiende a seguir* a otro. Si `ember warden` va seguido de `patrols` mil veces, esa es una señal fuerte, y la próxima vez que el modelo vea `ember warden` podrá hacer una conjetura fundamentada.

### Construyendo un generador de bigramas

Para cada índice `i`, el bigrama es `tokens[i]` y `tokens[i + 1]`:

```python
def get_bigrams(tokens):
    result = []
    for i in range(len(tokens) - 1):
        pair = tokens[i] + ' ' + tokens[i + 1]
        result.append(pair)
    return result

print(get_bigrams(['the', 'cat', 'sat', 'on', 'the', 'mat']))
```

**Salida:**

```text
['the cat', 'cat sat', 'sat on', 'on the', 'the mat']
```

> [!NOTE]
> El bucle se detiene en `len(tokens) - 1` porque el último token no tiene con qué emparejarse.

---

## 4. Contar

### Predecir es contar

Si `slime splits` va seguido de `into` tres veces en un texto, ¿qué debería predecir el modelo? Casi seguro `into`. Predecir suele consistir en contar de alguna forma.

Podemos construir un **diccionario de frecuencias**: una estructura de datos que recuerda, para cada n-grama, qué tokens lo siguieron y cuántas veces.

```python
def count_next_tokens(tokens):
    counts = {}
    for i in range(len(tokens) - 2):
        bigram = tokens[i] + ' ' + tokens[i + 1]
        next_token = tokens[i + 2]

        if bigram not in counts:
            counts[bigram] = {}

        counts[bigram][next_token] = counts[bigram].get(next_token, 0) + 1
    return counts

tokens = tokenize("the cat sat on the mat and the cat sat on the sofa")
counts = count_next_tokens(tokens)
print(counts['sat on'])
print(counts['on the'])
```

**Salida:**

```text
{'the': 2}
{'mat': 1, 'sofa': 1}
```

Esto es un **diccionario anidado**: el diccionario exterior asocia cada bigrama con un diccionario interior, que asocia cada posible token siguiente con su conteo.

> [!NOTE]
> **Tres detalles que conviene memorizar**
> El bucle se detiene en `len(tokens) - 2` porque necesitamos tres posiciones: `tokens[i]`, `tokens[i + 1]` y `tokens[i + 2]`.
> Antes de incrementar un conteo, asegúrate de que exista la clave del bigrama, o te va a saltar un `KeyError`.
> `.get(next_token, 0)` devuelve `0` cuando la clave no existe, así que podemos sumar `1` sin riesgo.

> [!WARNING]
> **Trampa**
> Buscar un bigrama que nunca apareció (`counts.get('purple dragon')`) devuelve `None` — no un diccionario vacío. Un modelo que nunca vio ese contexto no tiene nada que decir sobre él, y un `None` que llega a tu bucle `for` lo revienta.

---

## 5. El predictor

### Construyendo el predictor

Hora de unirlo todo. Nuestro predictor va a:

1. Recibir una frase como entrada.
2. Coger sus dos últimos tokens (el contexto).
3. Buscar ese contexto en el diccionario de frecuencias.
4. Devolver el token siguiente más común.

```python
def predict_next(phrase, counts):
    tokens = tokenize(phrase.lower())
    context = tokens[-2] + ' ' + tokens[-1]

    if context not in counts:
        return None

    best_token = None
    best_count = 0
    for token, count in counts[context].items():
        if count > best_count:
            best_token = token
            best_count = count

    return best_token

print(predict_next("the cat", counts))
print(predict_next("purple dragon", counts))
```

**Salida:**

```text
sat
None
```

> [!NOTE]
> Solo usamos los dos últimos tokens porque el diccionario está indexado por bigramas (contexto de 2 tokens).
> El bucle lleva `best_token` y `best_count` mientras busca la puntuación más alta.
> Si el contexto no está en `counts`, devolvemos `None`. Nunca inventamos una predicción que no hemos visto — y ese es el hábito más importante de todo el capítulo.

### Extra: autocompletado

Sigue prediciendo en un bucle y añade cada predicción a la frase, y el modelo empezará a escribir frases enteras:

```python
def autocomplete(phrase, counts, num_tokens=5):
    result = phrase
    for _ in range(num_tokens):
        next_token = predict_next(result, counts)
        if next_token is None:
            break
        result = result + ' ' + next_token
    return result

print(autocomplete("the cat", counts, 6))
```

**Salida:**

```text
the cat sat on the mat and the
```

Dale un texto más largo —un capítulo de Project Gutenberg, un montón de tus propios diarios de misiones, los documentos de diseño del juego que estás construyendo— y empezará a producir texto que suena al original.

> [!NOTE]
> Esto es, en esencia, cómo ha funcionado el autocompletado de tu teléfono durante años. El autocompletado no es un ChatGPT más pequeño: es la misma idea con un diccionario mucho más corto.

---

## 6. La gran imagen

### Tu predictor frente a un LLM real

| Tu predictor | Un LLM moderno |
| :--- | :--- |
| Usa bigramas (contexto de 2 tokens) | Mira miles de tokens de contexto |
| Elige el token siguiente más común | Pondera muchos candidatos por probabilidad |
| Entrenado con un texto pequeño | Entrenado con una porción enorme de internet |
| Guarda conteos explícitos | Guarda miles de millones de **parámetros** (números) |

Tu predictor funciona contando. Un LLM real no guarda conteos — guarda miles de millones de números que se ajustaron durante el entrenamiento para que los tokens probables puntuen más alto.

| Término | Significado |
| :--- | :--- |
| **Entrenamiento** | El proceso lento y caro en el que el modelo ajusta sus parámetros con datos. |
| **Inferencia** | El proceso rápido en el que un modelo entrenado predice el siguiente token de tu prompt. |

Los LLM modernos pasan semanas o meses entrenándose para poder darte la inferencia en milisegundos. Durante la inferencia el modelo predice un token, lo añade al texto, y lo hace una y otra vez hasta que llega a una señal de parada.

### 🎮 Hito del proyecto: `flavor_engine.py`

Las cuatro funciones de arriba son `Loreforge/loreforge/flavor_engine.py`. Aquí van funcionando sobre el bestiario de *Emberfall*:

```python
CORPUS = [
    "The Ember Warden patrols the forge corridor, unhurried and unafraid.",
    "The Cinder Slime splits into two smaller slimes when it dies.",
    "Ashen Wraiths drift through walls, and they ignore the light.",
    "The player drinks a health flask before the boss room.",
]

tokens = []
for line in CORPUS:
    tokens += tokenize(line.lower())

counts = count_next_tokens(tokens)
print(len(tokens), 'tokens,', len(counts), 'bigrams')
print(autocomplete("the ember warden", counts, 5))
```

**Salida:**

```text
47 tokens, 44 bigrams
the ember warden patrols the forge corridor ,
```

Dos cosas que conviene notar, y las dos son toda la lección:

- El modelo produjo la coma. No tiene ni idea de qué es una frase — la coma es simplemente el token más habitual que sigue a `corridor` en este corpus. Un LLM real saca la gramática de haber visto muchísimo más texto, no de una regla.
- El corpus tiene cuatro líneas, así que el modelo se repite en cuanto se sale del guion. No está escribiendo texto de ambiente: lo está **recitando**.

### Pruébalo tú mismo

- Ejecuta tu predictor con la frase `the capital of france is`.
- Pide a un LLM que complete la misma frase.
- Compara las salidas. ¿Dónde falla tu predictor y acierta el LLM? Pista: longitud del contexto y datos de entrenamiento.

---

## Casos de Uso Comunes

- 💬 Chatbots y asistentes virtuales
- ✍️ Redacción, resúmenes y traducción de texto
- 💻 Generación de código y autocompletado
- 🎨 Generación de imágenes, audio y vídeo

---

## Conclusiones Clave

- 🧩 **Tokens:** la IA ve el texto como una secuencia de trozos, no como palabras.
- 🔍 **Patrones:** los n-gramas revelan qué tokens tienden a seguir a otros.
- 🔢 **Contar:** predecir es, sobre todo, contar lo que suele venir después.
- 🔁 **Bucle:** generación = predecir → añadir → repetir hasta una señal de parada.
- 🧠 **Escala:** un LLM es la misma idea escalada a miles de millones de parámetros.

---

## 🎮 Ejercicios de Práctica

- Modifica `tokenize()` para que pase a minúsculas todos los tokens.
- Escribe `get_trigrams(tokens)` que devuelva las secuencias de 3 tokens.
- Adapta el predictor para usar contexto de trigramas en lugar de bigramas, y compara la calidad de la salida en el mismo corpus.
- Pasa a `autocomplete()` un párrafo de un libro de dominio público e inspecciona el resultado.
- **Jefe final:** haz que el tokenizador parta `fireball` en `fire` + `ball` y explica qué haría eso con los conteos que ya has construido.

---
