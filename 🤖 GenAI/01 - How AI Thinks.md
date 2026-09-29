
# 01. How AI Thinks

**Spanish version:** [01 - Cómo Piensa la IA.md](01%20-%20C%C3%B3mo%20Piensa%20la%20IA.md)

**Course:** GenAI
**Topic:** Generative AI, Large Language Models, Tokens, N-Grams & Next-Token Prediction
**Tags:** `#genai` `#ai` `#llm` `#basics` `#game-dev`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Every AI model you have ever used is a machine that finishes sentences. That sounds like a downgrade until you realize what it implies: once you can build one yourself, in ninety lines of Python, the mystique is gone and the engineering starts. This chapter builds that machine — and the first thing it writes is *Emberfall* flavor text.

---

## 1. The Magic Trick

**Note:** Key information
**Generative AI** (GenAI) is artificial intelligence that creates new content — text, code, images, video, audio — by learning patterns from massive amounts of data. The tools in this module's exercise list are all GenAI products:

| Tool | Maker | What it is |
| :--- | :--- | :--- |
| **ChatGPT** | OpenAI | A chat interface over a large language model |
| **Claude** | Anthropic | A chat interface over a large language model |
| **Gemini** | Google | A chat interface over a large language model |

They answer questions, draft text and hold conversations. It feels like magic, but behind every one of them is a surprisingly small idea: **predict what comes next**.

### The Prediction Game

Try to complete each line the way a player would:

| Prompt | Likely next word |
| :--- | :--- |
| The player drew the legendary | sword |
| Health is at 12%, drink the | flask |
| The boss spawns in the | arena |

You matched most of them because you have seen those patterns thousands of times — in games, in books, in other players' runs. A language model does exactly the same thing, except it learned from a large portion of the internet instead of a childhood.

> [!NOTE]
> **The catch**
> Predictions can be surprising. The AI does not understand meaning the way you do, and it makes mistakes that look obvious to any human reader.

---

## 2. Tokens

### Not All Models Are Language Models

| Model family | Input | Output |
| :--- | :--- | :--- |
| **Language models** (GPT, Claude, Gemini) | text | text |
| **Image models** (DALL·E, Stable Diffusion) | text, images | images |
| **Code models** (Codex, Copilot) | text, code | code |
| **Audio models** (Whisper) | audio | text |

A **Large Language Model** (LLM) processes and generates **text**, and it does so by predicting the next **token**.

### How AI Reads

Humans read words. AI does not. It breaks text into smaller chunks, and those chunks are the unit of everything:

> [!NOTE]
> **Token**
> A token is one of the small chunks of text that an AI model reads and generates.

```text
"I am learning Generative AI"  ->  ["I", " am", " learning", " Gener", "ative", " AI"]
```

That sentence became six tokens. The exact split depends on the model — yours will split it differently.

### A Simple Tokenizer

**Regular expressions** (regex) describe the *shape* of the text we want to extract. Python ships them in the `re` module:

```python
import re

def tokenize(text):
    return re.findall(r'\w+|[^\w\s]', text)

print(tokenize("The goblin screams before it dies."))
```

**Output:**

```text
['The', 'goblin', 'screams', 'before', 'it', 'dies', '.']
```

Breaking down the pattern `\w+|[^\w\s]`:

| Piece | Matches | Example |
| :--- | :--- | :--- |
| `\w+` | One or more word characters (a word) | `goblin` |
| `\|` | Or — either side is acceptable | — |
| `[^\w\s]` | A single character that is neither a word character nor whitespace | `.` |

```python
print(tokenize("Hello, world!"))
```

**Output:**

```text
['Hello', ',', 'world', '!']
```

Notice that punctuation became its own token. That is not a bug in the tokenizer; it is a decision, and the consequences show up later in this chapter.

> [!TIP]
> You do not need to memorize regex to follow along. Understanding what the tokenizer does is what matters.

### Real-World Tokenization

Different models split text differently — there is no one-size-fits-all approach. Models like GPT and Claude use **subword tokenization**: long, rare or unfamiliar words are broken into smaller reusable pieces.

```text
"unscrolling"  ->  ["un", "scroll", "ing"]
```

This is why an LLM can handle words it has never seen as a whole: it has seen the pieces.

---

## 3. Patterns

### N-Grams

Now that we have tokens, we can see how the model finds patterns. An **n-gram** is a sequence of *n* consecutive tokens. Using the sentence *the cat sat on the mat*:

| Name | n | Example |
| :--- | :--- | :--- |
| **Unigram** | 1 | `the`, `cat`, `sat`, … |
| **Bigram** | 2 | `the cat`, `cat sat`, `sat on`, … |
| **Trigram** | 3 | `the cat sat`, `cat sat on`, … |

Bigrams are the useful ones: they tell us which token *tends to follow* another. If `ember warden` is followed by `patrols` a thousand times, that is a strong signal, and the next time the model sees `ember warden` it can make an educated guess.

### Building a Bigram Generator

For each index `i`, the bigram is `tokens[i]` and `tokens[i + 1]`:

```python
def get_bigrams(tokens):
    result = []
    for i in range(len(tokens) - 1):
        pair = tokens[i] + ' ' + tokens[i + 1]
        result.append(pair)
    return result

print(get_bigrams(['the', 'cat', 'sat', 'on', 'the', 'mat']))
```

**Output:**

```text
['the cat', 'cat sat', 'sat on', 'on the', 'the mat']
```

> [!NOTE]
> The loop stops at `len(tokens) - 1` because the last token has no next token to pair with.

---

## 4. Counting

### Prediction Is Counting

If `slime splits` is followed by `into` three times in a text, what should the model predict? Most likely `into`. Prediction usually comes down to counting in some form.

We can build a **frequency dictionary**: a data structure that remembers, for each n-gram, which tokens followed it and how often.

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

**Output:**

```text
{'the': 2}
{'mat': 1, 'sofa': 1}
```

This is a **nested dictionary**: the outer dictionary maps each bigram to an inner dictionary, which maps each possible next token to its count.

> [!NOTE]
> **Three details worth memorizing**
> The loop stops at `len(tokens) - 2` because we need three positions: `tokens[i]`, `tokens[i + 1]` and `tokens[i + 2]`.
> Before incrementing a count, make sure the bigram key exists, otherwise you hit a `KeyError`.
> `.get(next_token, 0)` returns `0` when the key is missing, so we can safely add `1`.

> [!WARNING]
> **Trap**
> Looking up a bigram that never appeared (`counts.get('purple dragon')`) returns `None` — not an empty dictionary. A model that has never seen a context has nothing to say about it, and a `None` that reaches your `for` loop crashes it.

---

## 5. The Predictor

### Building the Predictor

Time to wire everything together. Our predictor will:

1. Take a phrase as input.
2. Grab its last two tokens (the context).
3. Look up that context in the frequency dictionary.
4. Return the most common next token.

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

**Output:**

```text
sat
None
```

> [!NOTE]
> We only use the last two tokens because the dictionary is keyed on bigrams (2-token context).
> The loop tracks `best_token` and `best_count` while it scans for the highest score.
> If the context is not in `counts`, we return `None`. We never invent a prediction we have never seen — which is the single most important habit in this chapter.

### Bonus: Autocomplete

Keep predicting in a loop and append each prediction to the phrase, and the model starts writing whole sentences:

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

**Output:**

```text
the cat sat on the mat and the
```

Feed it a longer text — a chapter from Project Gutenberg, a pile of your own quest logs, the design docs of the game you are building — and it will start producing text that sounds like the source.

> [!NOTE]
> This is, in essence, how autocomplete on your phone has worked for years. Autocomplete is not a smaller ChatGPT; it is the same idea with a much smaller dictionary.

---

## 6. The Big Picture

### Your Predictor vs. a Real LLM

| Your predictor | A modern LLM |
| :--- | :--- |
| Uses bigrams (2 tokens of context) | Looks at thousands of tokens of context |
| Picks the single most common next token | Weighs many candidates by probability |
| Trained on a small text | Trained on a huge portion of the internet |
| Stores explicit counts | Stores billions of **parameters** (numbers) |

Your predictor works by counting. A real LLM does not store counts — it stores billions of numbers that were adjusted during training so that likely next tokens score higher.

| Term | Meaning |
| :--- | :--- |
| **Training** | The slow, expensive process where the model adjusts its parameters using data. |
| **Inference** | The fast process where a trained model predicts the next token for your prompt. |

Modern LLMs spend weeks or months in training so they can run inference for you in milliseconds. During inference the model predicts a token, appends it to the text, and does it again and again until it hits a stop signal.

### 🎮 Project Milestone: `flavor_engine.py`

The four functions above are `Loreforge/loreforge/flavor_engine.py`. Here they are running on the *Emberfall* bestiary:

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

**Output:**

```text
47 tokens, 44 bigrams
the ember warden patrols the forge corridor ,
```

Two things to notice, and both of them are the whole lesson:

- The model produced the comma. It has no idea what a sentence is — the comma is simply the most common token that ever follows `corridor` in this corpus. A real LLM gets grammar from having seen vastly more text, not from a rule.
- The corpus is four lines long, so the model repeats itself the moment it leaves the script. It is not writing flavor text. It is *reciting* it.

### Try It Yourself

- Run your predictor on the phrase `the capital of france is`.
- Ask an LLM to complete the same phrase.
- Compare the outputs. Where does your predictor fail and the LLM succeed? Hint: context length and training data.

---

## Common Use Cases

- 💬 Chatbots & virtual assistants
- ✍️ Writing, summarizing & translating text
- 💻 Code generation & autocomplete
- 🎨 Image, audio & video generation

---

## Key Takeaways

- 🧩 **Tokens:** AI sees text as a sequence of chunks, not words.
- 🔍 **Patterns:** N-grams reveal which tokens tend to follow others.
- 🔢 **Counting:** predicting is mostly counting what usually comes next.
- 🔁 **Loop:** generation = predict → append → repeat until a stop signal.
- 🧠 **Scale:** an LLM is the same idea scaled up to billions of parameters.

---

## 🎮 Practice Exercises

- Modify `tokenize()` so it lowercases every token.
- Write `get_trigrams(tokens)` that returns the 3-token sequences.
- Extend the predictor to use trigram context instead of bigram context, and compare the output quality on the same corpus.
- Feed `autocomplete()` a paragraph from a public-domain book and inspect the output.
- **Boss fight:** make the tokenizer split `fireball` into `fire` + `ball` and explain what that would do to the counts you have already built.

---
