
# 03. Embeddings & Semantic Search

**Spanish version:** [03 - Embeddings y Búsqueda Semántica.md](03%20-%20Embeddings%20y%20B%C3%AAsqueda%20Sem%C3%A1ntica.md)

**Course:** GenAI
**Topic:** Vectors, One-Hot Encoding, Bag of Words, Cosine Similarity & Semantic Search
**Tags:** `#genai` `#ai` `#embeddings` `#vectors` `#game-dev`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

The predictor from [[01 - How AI Thinks]] was good at exactly one thing: it guessed `the` because that pattern showed up most often. It had no idea what any of those words *meant*. This chapter closes that gap — first with numbers, then with angles — and ends with a search engine over the *Emberfall* bestiary.

---

## 13. From Patterns to Meaning

> [!NOTE]
> Key information
> The limits of counting are easy to state: *"The cat sat on the mat"* and *"A kitty lay on the rug"* mean nearly the same thing, but they are completely different strings of tokens — and that is exactly the problem.

### The Limits of Counting

The predictor from chapter 01 compared words only by how they were spelled. Since `fast` and `quick` do not share a single letter, it had no way to see them as related. To it, `fast` and `quick` were as unrelated as `fast` and `Tuesday`.

A real LLM gets past this by turning each word into a set of numbers, picked so that words with similar meanings get similar numbers. `fast` and `quick` end up with nearly the same numbers, so the model can tell they are related even though they look nothing alike. Those sets of numbers are called **vectors**.

### Words as Vectors

In programming, a **vector** is simply an ordered list of numbers, like `[82, 84, 77]`.

- If two words mean similar things, their vectors end up **close together**.
- If they mean unrelated things, their vectors end up **far apart**.

Once words are vectors, we can do real math on them:

- Find the most similar word to `happy` (closest vector).
- Search a paragraph by meaning, not by exact word match.
- Group documents by topic.

### What Is an Embedding?

In AI, an **embedding** is a vector that represents the meaning of a piece of text. That text might be a single word, a sentence, a paragraph or an entire document. Think of an embedding as a set of coordinates on a giant map of meaning: texts about similar topics end up in nearby locations, and unrelated texts end up far apart.

| Text | Simplified embedding |
| :--- | :--- |
| I love Minecraft. | `[0.23, -0.81, 0.45, …]` |
| I like Valorant. | `[0.25, -0.79, 0.47, …]` |
| I lost $100 on Kalshi. | `[-0.62, 0.14, 0.88, …]` |

The first two embeddings are very similar, because both are about enjoying a video game. The third looks completely different because it is about losing money on a bet. Nobody explicitly told the model that the first two sentences are related — it discovered those relationships by learning from millions or billions of examples of language.

Real embeddings typically contain **hundreds** of numbers rather than three. Those numbers are not chosen by hand; they are learned automatically during training. Modern models also embed whole sentences, paragraphs or documents, not just single words.

### Probe an LLM's Understanding of Meaning

Ask an LLM the following questions, one at a time:

- Are the words `dragon` and `wyvern` similar in meaning?
- Are the words `dragon` and `toaster` similar in meaning?
- Most similar to `unicorn`: startup, skittles, or… corn? Just answer.
- Are `the player cast a fireball` and `the player hurled a fireball` about the same event?

Notice how the model seems to understand the relationship between two words instead of just looking up pre-trained strings.

---

## 14. Words as Numbers

### One-Hot Encoding

Language is made of words, but computers think in numbers. **One-hot encoding** represents each word as a vector containing a single `1` and `0s` everywhere else.

1. Choose an order for the vocabulary and number the words `0, 1, 2, 3, …`
2. To encode a word, create a vector of zeros the same length as the vocabulary.
3. Put a `1` at the position corresponding to that word.

```python
vocab = ['slime', 'warden', 'potion', 'sword', 'Tuesday']

def one_hot(word, vocab):
    vector = [0] * len(vocab)
    vector[vocab.index(word)] = 1
    return vector

print(one_hot('slime', vocab))
print(one_hot('Tuesday', vocab))
```

**Output:**

```text
[1, 0, 0, 0, 0]
[0, 0, 0, 0, 1]
```

> [!NOTE]
> The order of the words in the vocabulary is arbitrary, but once chosen it must stay fixed. A real vocabulary can have 50,000+ words, giving 50,000-number vectors with a single `1`.

### Why Turn Words Into Numbers?

**Encoding** is taking data and turning it into a form that is easier to compute on — images become pixel numbers, too. With numbers we can compare words using arithmetic, and use them as features for search, clustering or neural networks. None of that works on raw strings.

### Hamming Distance

The **Hamming distance** is the number of positions where two vectors differ.

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

**Output:**

```text
2 2 2
```

A small distance means the vectors are mostly the same; a large one means they are mostly different.

### Why It Doesn't Capture Meaning

Every pair of distinct one-hot vectors comes out exactly **2** apart. `slime` vs `warden` is the same distance as `slime` vs `Tuesday`. There is no way for this encoding to say some words are closer in meaning. It is a starting point; we improve it in the next two sections.

---

## 15. Bag of Words

### From Words to Documents

One-hot handles single words. To compare a sentence, a paragraph or a whole document we need one vector per document. The simplest way is the **bag of words**: imagine dumping every word from a document into a bag and shaking it. You lose the order, but you keep a count of how many times each word appears. Those counts become the document's vector.

```text
Doc 1: the ember warden guards the forge corridor
Doc 2: the cinder slime guards the flooded cistern
```

Vocabulary (unique words across both documents): `the`, `ember`, `warden`, `guards`, `forge`, `corridor`, `cinder`, `slime`, `flooded`, `cistern`.

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

**Output:**

```text
['the', 'ember', 'warden', 'guards', 'forge', 'corridor', 'cinder', 'slime', 'flooded', 'cistern']
[2, 1, 1, 1, 1, 1, 0, 0, 0, 0]
[2, 0, 0, 1, 0, 0, 1, 1, 1, 1]
```

Documents that share many words share many non-zero positions, so their vectors already reflect that similarity.

### Better, But Still Not Smart

Bag of words is a real upgrade over one-hot: two documents about slimes line up better than a slime document and a quest-log document, even without extra work. But it is still tied to **exact words**. A bestiary entry about `fast blades` and a quest about `quick swords` share no positions, so the vectors say they are unrelated. We fix that in the next chapter of the real thing — for now, keep the pipeline.

---

## 16. Measuring Similarity

### Putting a Number on Similarity

To rank documents we need a single score. **Cosine similarity** measures the angle between two vectors:

- Vectors pointing in the same direction → high score (close to `1`).
- Vectors with nothing in common → score of `0`.

### The Formula

$$\text{cosine}(A, B) = \frac{A \cdot B}{\|A\| \times \|B\|}$$

| Piece | What it does |
| :--- | :--- |
| **Dot product** $A \cdot B$ | Multiply each pair of matching positions and add them up. Overlap increases the sum; no overlap gives `0`. |
| **Magnitude** $\|A\|$ | The vector's length: square each value, add them, take the square root. |
| **The division** | Dividing by the magnitudes cancels out length, so we compare only *direction*. |

Two vectors pointing the same way get a high score even if one is much longer — which is why a three-word blurb can score well against a paragraph.

### Worked Example

| Doc | Text | Vector |
| :--- | :--- | :--- |
| A | `slime slime warden` | `[2, 1, 0]` |
| B | `slime warden wraith` | `[1, 1, 1]` |

- Dot product: $2\times1 + 1\times1 + 0\times1 = 3$
- Magnitudes: $\|A\| = \sqrt{5} \approx 2.236$, $\|B\| = \sqrt{3} \approx 1.732$
- Result: $3 / (2.236 \times 1.732) \approx 0.775$

They share `slime` and `warden` in different amounts, so the score is high but not `1`.

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

**Output:**

```text
3
2.236 1.732
0.7745966692414834
```

With a third document about an unrelated creature, the pattern is `slime` vs `warden` noticeably above `0`, and the unrelated one scoring exactly `0`.

> [!WARNING]
> **Trap**
> Cosine similarity divides by two magnitudes. A zero vector has magnitude `0`, so `cosine([0,0,0], anything)` raises `ZeroDivisionError` — and an empty document produces a zero vector. Guard the empty case before it reaches production.

---

## 17. Semantic Search

### The Whole Pipeline

We have built every piece we need: bag-of-words vectors and cosine similarity. Now we combine them into a working search engine.

1. Take the query and turn it into a bag-of-words vector.
2. Turn every document into a vector with the same vocabulary.
3. Compute the cosine similarity between the query and each document.
4. Sort the documents by score, highest first.

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

**Output:**

```text
0.471 | the cinder slime guards the flooded cistern
0.0 | the ember warden guards the forge corridor
0.0 | as ash wraiths drift through the walls
```

### Semantic Search

**Semantic search** returns results based on what words and phrases *mean*, not just exact matches. It knows that cars and automobiles mean the same thing.

Our engine is not truly semantic yet: it can only match documents that share exact words with the query.

```python
print([round(s, 3) for s, _ in search("automobile", documents)])
```

**Output:**

```text
[0.0, 0.0, 0.0]
```

Searching for `automobile` against a document about `car` scores `0`, even though they mean the same thing.

> [!NOTE]
> The process is always the same: **vectorize the query → vectorize the documents → compute cosine similarity → sort**. The only thing that changes between a toy and a product is how you make the vectors.

### Project Milestone: `lore_search.py`

```python
LORE = [
    "the ember warden guards the forge corridor",
    "the cinder slime guards the flooded cistern",
    "as ash wraiths drift through the walls",
    "the ash blade drops from fast wraiths on death",
]

def lore_search(query, entries=LORE, top=4):
    """Return the top matching lore entries, most similar first."""
    return [(round(score, 3), doc)
            for score, doc in search(query, entries)[:top]]

for hit in lore_search('wraith'):
    print(hit)
```

**Output:**

```text
(0.0, 'the ember warden guards the forge corridor')
(0.0, 'the cinder slime guards the flooded cistern')
(0.0, 'the ash blade drops from fast wraiths on death')
(0.0, 'as ash wraiths drift through the walls')
```

Every score is `0.0` for a bestiary full of wraiths. The reason is one missing `s`: `bag_of_words` counts **exact** words, and `wraith` is not the same token as `wraiths`. A player types `wraith`, your lore database says `wraiths`, and the engine returns nothing.

Change the query to the exact plural and the engine works:

```python
for hit in lore_search('ash blade drops', top=2):
    print(hit)
```

**Output:**

```text
(0.577, 'the ash blade drops from fast wraiths on death')
(0.218, 'as ash wraiths drift through the walls')
```

That gap — `0.577` against `0.218` — is the whole reason embeddings exist. A query that shares **exact** words with a document can be ranked. A query that shares **meaning** cannot.

---

## 18. Embeddings Recap

### Techniques Learned

1️⃣ **One-hot encoding** turned each word into a vector, and Hamming distance showed why it was not enough: every pair of distinct words comes out exactly the same distance apart.
🎒 **Bag of words** scaled up from single words to whole documents by counting how many times each word appears.
📐 **Cosine similarity** measured the angle between vectors.
🔎 **Search** combined all of it into a ranking pipeline.

### From a Toy to the Real Thing

| | Our vectors | Real embeddings |
| :--- | :--- | :--- |
| **Type** | Sparse word counts | Dense numbers |
| **Knows** | Only whether two texts share exact words | Meaning learned from huge amounts of text |
| **`automobile` vs `car`** | Score `0` | Close together in number-space |
| **Made by** | Counting | Models like word2vec, sentence-transformers, or the OpenAI embeddings API |

> [!NOTE]
> The architecture itself does not change. Real systems just swap our counting step for a real embedding model, keeping `cosine_similarity()` and `search()` exactly as they are.

---

## Common Use Cases

- 🔎 Semantic search & recommendations
- 🗂️ Clustering and classifying documents
- 🧾 Finding duplicate or similar content
- 📚 Retrieval for RAG systems (see [[04 - Limits & Risks]])

---

## Key Takeaways

- 🔢 One-hot turns words into vectors but destroys all relationships: every pair is equally far apart.
- 🎒 Bag of words scales the idea to documents, at the cost of meaning and word order.
- 📐 Cosine similarity compares direction, not length.
- 🔎 The search pipeline never changes; only the way you build the vectors does.
- 🤖 The same `search()` function drives real semantic search and RAG — swap the vectors, keep the engine.

---

## 🎮 Practice Exercises

- Implement `cosine_similarity()` for three custom lore entries and print every pair.
- Search for `automobile` in a collection that contains `car` and observe the score.
- Add a document to `documents` and check whether the ranking changes the way you expect.
- **Boss fight:** make `bag_of_words` lowercase and strip punctuation, and re-run the `lore_search` query. Which scores move, and why?

---
