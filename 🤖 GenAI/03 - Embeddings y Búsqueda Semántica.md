
# 03. Embeddings y Búsqueda Semántica

**Versión original en inglés:** [03 - Embeddings & Semantic Search.md](03%20-%20Embeddings%20&%20Semantic%20Search.md)

**Curso:** GenAI
**Tema:** Vectores, codificación one-hot, bolsa de palabras, similitud coseno y búsqueda semántica
**Tags:** `#genai` `#ai` `#embeddings` `#vectors` `#game-dev`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

El predictor de [[01 - Cómo Piensa la IA]] se le daba bien exactamente una cosa: adivinar `the` porque ese patrón era el más frecuente. No tenía ni idea de lo que *significaban* esas palabras. Este capítulo cierra esa brecha —primero con números, luego con ángulos— y termina con un motor de búsqueda sobre el bestiario de *Emberfall*.

---

## 13. De los patrones al significado

> [!NOTE]
> Información clave
> El límite de contar se enuncia fácil: *"The cat sat on the mat"* y *"A kitty lay on the rug"* significan casi lo mismo, pero son cadenas de tokens completamente distintas — y ese es justamente el problema.

### Los límites de contar

El predictor del capítulo 01 comparaba palabras solo por cómo estaban escritas. Como `fast` y `quick` no comparten ni una sola letra, no tenía forma de verlas como relacionadas. Para él, `fast` y `quick` eran tan ajenas entre sí como `fast` y `Tuesday`.

Un LLM real supera eso convirtiendo cada palabra en un conjunto de números, elegidos de modo que las palabras con significado parecido tengan números parecidos. `fast` y `quick` acaban con números casi idénticos, así que el modelo puede detectar que están relacionadas aunque no se parezcan en nada. Esos conjuntos de números se llaman **vectores**.

### Palabras como vectores

En programación, un **vector** es simplemente una lista ordenada de números, como `[82, 84, 77]`.

- Si dos palabras significan cosas parecidas, sus vectores acaban **juntos**.
- Si significan cosas sin relación, sus vectores acaban **lejos**.

Una vez que las palabras son vectores, podemos hacer matemáticas de verdad con ellas:

- Encontrar la palabra más parecida a `happy` (el vector más cercano).
- Buscar un párrafo por significado, no por coincidencia exacta.
- Agrupar documentos por tema.

### ¿Qué es un embedding?

En IA, un **embedding** es un vector que representa el significado de un fragmento de texto. Ese texto puede ser una palabra, una frase, un párrafo o un documento entero. Piensa en un embedding como un conjunto de coordenadas en un mapa gigante del significado: los textos sobre temas parecidos acaban en lugares cercanos, y los que no tienen relación, lejos.

| Texto | Embedding simplificado |
| :--- | :--- |
| Me encanta Minecraft. | `[0.23, -0.81, 0.45, …]` |
| Me gusta Valorant. | `[0.25, -0.79, 0.47, …]` |
| Perdí 100 $ en Kalshi. | `[-0.62, 0.14, 0.88, …]` |

Los dos primeros embeddings son muy parecidos, porque ambos hablan de disfrutar de un videojuego. El tercero se ve completamente distinto porque habla de perder dinero en una apuesta. Nadie le dijo explícitamente al modelo que las dos primeras frases están relacionadas — lo descubrió aprendiendo de millones o miles de millones de ejemplos de lenguaje.

Los embeddings reales suelen contener **cientos** de números en lugar de tres. Esos números no se eligen a mano: se aprenden automáticamente durante el entrenamiento. Los modelos modernos además embeddean frases, párrafos o documentos enteros, no solo palabras sueltas.

### Sondea la comprensión del significado de un LLM

Hazle a un LLM estas preguntas, de una en una:

- ¿Son parecidas en significado las palabras `dragón` y `wyvern`?
- ¿Son parecidas en significado las palabras `dragón` y `tostadora`?
- Lo más parecido a `unicornio`: startup, skittles o… ¿maíz? Solo responde.
- ¿`el jugador lanzó una bola de fuego` y `el jugador lanzó una esfera de fuego` describen el mismo evento?

Fíjate en que el modelo parece entender la relación entre dos palabras en lugar de limitarse a recuperar cadenas preentrenadas.

---

## 14. Palabras como números

### Codificación one-hot

El lenguaje está hecho de palabras, pero las computadoras piensan en números. La **codificación one-hot** representa cada palabra como un vector con un único `1` y `0` en todas las demás posiciones.

1. Elige un orden para el vocabulario y numera las palabras `0, 1, 2, 3, …`
2. Para codificar una palabra, crea un vector de ceros de la misma longitud que el vocabulario.
3. Pon un `1` en la posición que corresponde a esa palabra.

```python
vocab = ['slime', 'warden', 'potion', 'sword', 'Tuesday']

def one_hot(word, vocab):
    vector = [0] * len(vocab)
    vector[vocab.index(word)] = 1
    return vector

print(one_hot('slime', vocab))
print(one_hot('Tuesday', vocab))
```

**Salida:**

```text
[1, 0, 0, 0, 0]
[0, 0, 0, 0, 1]
```

> [!NOTE]
> El orden de las palabras en el vocabulario es arbitrario, pero una vez elegido debe mantenerse fijo. Un vocabulario real puede tener más de 50.000 palabras, lo que da vectores de 50.000 números con un solo `1`.

### ¿Por qué convertir palabras en números?

**Codificar** es tomar datos y llevarlos a una forma más fácil de calcular — las imágenes también se convierten en números de píxeles. Con números podemos comparar palabras con aritmética y usarlas como características para búsqueda, agrupamiento o redes neuronales. Nada de eso funciona sobre cadenas de texto.

### Distancia de Hamming

La **distancia de Hamming** es el número de posiciones en las que dos vectores difieren.

```python
def hamming(v1, v2):
    count = 0
    for a, b in zip(v1, v2):
        if a != b:
            count += 1
    return count

slime = one_hot('slime', vocab)
warden = one_hot('warden', vocab)
tuesday = one_hot('Tuesday', vocab)

print(hamming(slime, warden), hamming(slime, tuesday), hamming(warden, tuesday))
```

**Salida:**

```text
2 2 2
```

Una distancia pequeña significa que los vectores son casi iguales; una grande, que son casi distintos.

### Por qué no captura el significado

Cada par de vectores one-hot distintos queda exactamente a distancia **2**. `slime` frente a `warden` está tan lejos como `slime` frente a `Tuesday`. Esta codificación no tiene forma de decir que algunas palabras están más cerca en significado. Es un punto de partida; lo mejoramos en las dos secciones siguientes.

---

## 15. Bolsa de palabras

### De palabras a documentos

One-hot resuelve palabras sueltas. Para comparar una frase, un párrafo o un documento entero necesitamos un vector por documento. La forma más sencilla es la **bolsa de palabras**: imagina que vacías todas las palabras de un documento en una bolsa y la agitas. Pierdes el orden, pero conservas cuántas veces aparece cada palabra. Esos conteos son el vector del documento.

```text
Doc 1: the ember warden guards the forge corridor
Doc 2: the cinder slime guards the flooded cistern
```

Vocabulario (palabras únicas de ambos documentos): `the`, `ember`, `warden`, `guards`, `forge`, `corridor`, `cinder`, `slime`, `flooded`, `cistern`.

```python
docs = ["the ember warden guards the forge corridor",
        "the cinder slime guards the flooded cistern"]

def build_vocab(docs):
    vocab = []
    for doc in docs:
        for word in doc.split():
            if word not in vocab:
                vocab.append(word)
    return vocab

def bag_of_words(doc, vocab):
    vector = [0] * len(vocab)
    for word in doc.split():
        vector[vocab.index(word)] += 1
    return vector

vocab = build_vocab(docs)
print(vocab)
print(bag_of_words(docs[0], vocab))
print(bag_of_words(docs[1], vocab))
```

**Salida:**

```text
['the', 'ember', 'warden', 'guards', 'forge', 'corridor', 'cinder', 'slime', 'flooded', 'cistern']
[2, 1, 1, 1, 1, 1, 0, 0, 0, 0]
[2, 0, 0, 1, 0, 0, 1, 1, 1, 1]
```

Los documentos que comparten muchas palabras comparten muchas posiciones distintas de cero, así que sus vectores ya reflejan esa similitud.

### Mejor, pero todavía no inteligente

La bolsa de palabras es una mejora real frente a one-hot: dos documentos sobre slimes se alinean mejor que un documento sobre slimes y otro sobre el diario de misiones, sin trabajo extra. Pero sigue atada a las palabras **exactas**. Una entrada de bestiario sobre `hojas veloces` y una misión sobre `espadas rápidas` no comparten ninguna posición, así que el motor dice que no tienen nada que ver. Eso lo arreglan los embeddings reales; por ahora, el pipeline se queda.

---

## 16. Medir la similitud

### Poner un número a la similitud

Para ordenar documentos necesitamos una única puntuación. La **similitud coseno** mide el ángulo entre dos vectores:

- Vectores que apuntan en la misma dirección → puntuación alta (cerca de `1`).
- Vectores sin nada en común → puntuación de `0`.

### La fórmula

$$\text{coseno}(A, B) = \frac{A \cdot B}{\|A\| \times \|B\|}$$

| Pieza | Qué hace |
| :--- | :--- |
| **Producto escalar** $A \cdot B$ | Multiplica cada par de posiciones coincidentes y los suma. El solapamiento aumenta la suma; sin solapamiento da `0`. |
| **Magnitud** $\|A\|$ | La longitud del vector: eleva cada valor al cuadrado, los suma y saca la raíz. |
| **La división** | Dividir por las magnitudes cancela la longitud, así que solo comparamos la *dirección*. |

Dos vectores que apuntan hacia el mismo lado puntuaban alto aunque uno sea mucho más largo — y por eso una línea de tres palabras puede puntuar bien frente a un párrafo.

### Ejemplo trabajado

| Doc | Texto | Vector |
| :--- | :--- | :--- |
| A | `slime slime warden` | `[2, 1, 0]` |
| B | `slime warden wraith` | `[1, 1, 1]` |

- Producto escalar: $2\times1 + 1\times1 + 0\times1 = 3$
- Magnitudes: $\|A\| = \sqrt{5} \approx 2.236$, $\|B\| = \sqrt{3} \approx 1.732$
- Resultado: $3 / (2.236 \times 1.732) \approx 0.775$

Comparten `slime` y `warden` en distinta proporción, así que la puntuación es alta pero no `1`.

```python
import math

def dot_product(v1, v2):
    total = 0
    for a, b in zip(v1, v2):
        total += a * b
    return total

def magnitude(v):
    total = 0
    for x in v:
        total += x * x
    return math.sqrt(total)

def cosine_similarity(v1, v2):
    return dot_product(v1, v2) / (magnitude(v1) * magnitude(v2))

print(dot_product([2, 1, 0], [1, 1, 1]))
print(round(magnitude([2, 1, 0]), 3), round(magnitude([1, 1, 1]), 3))
print(cosine_similarity([2, 1, 0], [1, 1, 1]))
```

**Salida:**

```text
3
2.236 1.732
0.7745966692414834
```

Con un tercer documento sobre una criatura sin relación, el patrón es `slime` frente a `warden` claramente por encima de `0`, y el documento ajeno puntuando exactamente `0`.

> [!WARNING]
> **Trampa**
> La similitud coseno divide por dos magnitudes. Un vector de ceros tiene magnitud `0`, así que `coseno([0,0,0], cualquier_cosa)` lanza `ZeroDivisionError` — y un documento vacío produce un vector de ceros. Protege el caso vacío antes de que llegue a producción.

---

## 17. Búsqueda semántica

### El pipeline completo

Ya tenemos todas las piezas: vectores de bolsa de palabras y similitud coseno. Ahora las combinamos en un motor de búsqueda que funciona.

1. Convierte la consulta en un vector de bolsa de palabras.
2. Convierte cada documento en un vector con el mismo vocabulario.
3. Calcula la similitud coseno entre la consulta y cada documento.
4. Ordena los documentos por puntuación, de mayor a menor.

```python
def search(query, documents):
    vocab = build_vocab(documents + [query])
    query_vector = bag_of_words(query, vocab)

    results = []
    for doc in documents:
        doc_vector = bag_of_words(doc, vocab)
        score = cosine_similarity(query_vector, doc_vector)
        results.append((score, doc))

    results.sort(reverse=True)
    return results

documents = [
    "the ember warden guards the forge corridor",
    "the cinder slime guards the flooded cistern",
    "as ash wraiths drift through the walls",
]

for score, doc in search("slime cistern", documents):
    print(round(score, 3), '|', doc)
```

**Salida:**

```text
0.471 | the cinder slime guards the flooded cistern
0.0 | the ember warden guards the forge corridor
0.0 | as ash wraiths drift through the walls
```

### Búsqueda semántica

La **búsqueda semántica** devuelve resultados según lo que *significan* las palabras y frases, y no solo por coincidencias exactas. Sabe que coches y automóviles significan lo mismo.

Nuestro motor todavía no es semántico de verdad: solo puede encontrar documentos que compartan palabras exactas con la consulta.

```python
print([round(s, 3) for s, _ in search("automobile", documents)])
```

**Salida:**

```text
[0.0, 0.0, 0.0]
```

Buscar `automobile` en un documento que habla de `car` puntúa `0`, aunque signifiquen lo mismo.

> [!NOTE]
> El proceso es siempre el mismo: **vectorizar la consulta → vectorizar los documentos → calcular la similitud coseno → ordenar**. Lo único que cambia entre un juguete y un producto es cómo haces los vectores.

### Hito del proyecto: `lore_search.py`

```python
LORE = [
    "the ember warden guards the forge corridor",
    "the cinder slime guards the flooded cistern",
    "as ash wraiths drift through the walls",
    "the ash blade drops from fast wraiths on death",
]

def lore_search(query, entries=LORE, top=4):
    """Devuelve las entradas de lore más parecidas, mejor primero."""
    return [(round(score, 3), doc)
            for score, doc in search(query, entries)[:top]]

for hit in lore_search('wraith'):
    print(hit)
```

**Salida:**

```text
(0.0, 'the ember warden guards the forge corridor')
(0.0, 'the cinder slime guards the flooded cistern')
(0.0, 'the ash blade drops from fast wraiths on death')
(0.0, 'as ash wraiths drift through the walls')
```

Todas las puntuaciones son `0.0` en un bestiario lleno de wraiths. El motivo es una `s` que falta: `bag_of_words` cuenta palabras **exactas**, y `wraith` no es el mismo token que `wraiths`. Un jugador escribe `wraith`, tu base de datos dice `wraiths`, y el motor no devuelve nada.

Cambia la consulta por el plural exacto y el motor funciona:

```python
for hit in lore_search('ash blade drops', top=2):
    print(hit)
```

**Salida:**

```text
(0.577, 'the ash blade drops from fast wraiths on death')
(0.218, 'as ash wraiths drift through the walls')
```

Ese hueco —`0.577` contra `0.218`— es la razón completa por la que existen los embeddings. Una consulta que comparte palabras **exactas** con un documento se puede ordenar. Una consulta que comparte **significado**, no.

---

## 18. Resumen de embeddings

### Técnicas aprendidas

1️⃣ La **codificación one-hot** convirtió cada palabra en un vector, y la distancia de Hamming mostró por qué no bastaba: cada par de palabras distintas queda exactamente a la misma distancia.
🎒 La **bolsa de palabras** escaló la idea de una palabra suelta a documentos enteros contando cuántas veces aparece cada una.
📐 La **similitud coseno** midió el ángulo entre vectores.
🔎 La **búsqueda** combinó todo ello en un pipeline de ordenación.

### De un juguete a lo real

| | Nuestros vectores | Embeddings reales |
| :--- | :--- | :--- |
| **Tipo** | Conteos dispersos de palabras | Números densos |
| **Sabe** | Solo si dos textos comparten palabras exactas | Significado aprendido de muchísimo texto |
| **`automóvil` vs `coche`** | Puntuación `0` | Juntos en el espacio numérico |
| **Los hace** | Contar | Modelos como word2vec, sentence-transformers o la API de embeddings de OpenAI |

> [!NOTE]
> La arquitectura no cambia. Los sistemas reales solo sustituyen nuestro paso de conteo por un modelo de embeddings de verdad, y se quedan con `cosine_similarity()` y `search()` exactamente igual.

---

## Casos de Uso Comunes

- 🔎 Búsqueda semántica y recomendaciones
- 🗂️ Agrupamiento y clasificación de documentos
- 🧾 Detección de contenido duplicado o similar
- 📚 Recuperación para sistemas RAG (ver [[04 - Límites y Riesgos]])

---

## Conclusiones Clave

- 🔢 One-hot convierte palabras en vectores, pero destruye todas las relaciones: cada par queda igual de lejos.
- 🎒 La bolsa de palabras lleva la idea a los documentos, a costa del significado y del orden.
- 📐 La similitud coseno compara dirección, no longitud.
- 🔎 El pipeline de búsqueda no cambia nunca; lo que cambia es cómo construyes los vectores.
- 🤖 La misma función `search()` sostiene la búsqueda semántica real y los sistemas RAG: cambia los vectores, conserva el motor.

---

## 🎮 Ejercicios de Práctica

- Implementa `cosine_similarity()` para tres entradas de lore propias e imprime todos los pares.
- Busca `automóvil` en una colección que contenga `coche` y observa la puntuación.
- Añade un documento a `documents` y comprueba si el orden cambia como esperabas.
- **Jefe final:** haz que `bag_of_words` pase a minúsculas y quite la puntuación, y vuelve a ejecutar la consulta de `lore_search`. ¿Qué puntuaciones se mueven, y por qué?

---
