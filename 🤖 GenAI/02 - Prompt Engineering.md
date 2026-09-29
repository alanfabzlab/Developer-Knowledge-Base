
# 02. Prompt Engineering

**Spanish version:** [02 - Ingeniería de Prompts.md](02%20-%20Ingenier%C3%ADa%20de%20Prompts.md)

**Course:** GenAI
**Topic:** Prompts, Specificity, Roles, Few-Shot Prompting & Chain-of-Thought
**Tags:** `#genai` `#ai` `#llm` `#prompting` `#game-dev`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

A prompt is not a search query. It is the entire input the model gets, and — as [[01 - How AI Thinks]] established — the entire output is a function of it. This chapter turns that fact into a tool: four techniques, applied in order, that take a one-line instruction and produce a reusable assistant for a game studio.

---

## 7. The Prompt Is Everything

> [!NOTE]
> Key information
> A **prompt** is the text we send to an AI model. It is the only knob we have. The model does not know what we want unless we tell it.

If an LLM is fundamentally a prediction engine, why do similar questions give wildly different answers? Because two different prompts lead to two different predictions.

| Prompt | Result |
| :--- | :--- |
| Explain Flamin' Hot Cheetos | A 600-word essay with long, generic explanations |
| Explain Flamin' Hot Cheetos to a cook from the 1500s. Max 100 words. | Short, focused, on-target |

Same model, same underlying question, completely different output.

**Goal of this chapter:** learn to write prompts that produce the results we want, building a **Game Dev Study Buddy** from a one-line instruction into a polished, reusable tool that works on any LLM.

---

## 8. Specificity

A vague prompt gets an average answer. Without instructions about output length, format or tone, the model averages across everyone who has ever asked a similar question on the internet — and the result is mush.

It is like walking into the shop next door and saying "give me a weapon." Without more detail you walk out with a rusty sword. Ask for a **rapier for a swashbuckler build, one-handed, level 30 tier**, and you walk out with the right thing.

### What Specific Prompts Add

| Element | Example | Effect |
| :--- | :--- | :--- |
| 👥 **Audience** | "for a programmer who knows basic Python" | No prior knowledge assumed |
| 🎭 **Tone** | "in the voice of a grizzled dungeon master" | More relaxed, more character |
| 🧱 **Format** | "Include one analogy and one code example" | Predictable structure |
| 📏 **Length** | "Max 100 words" | No more 600-word essays |

### Building the Study Buddy (v1)

Reusable prompts use a placeholder such as `{concept}`:

```text
Explain {concept} in plain English for someone who knows basic Python.
Use one analogy and one code example.
Max 100 words.
```

Compare the bad prompt (`Explain the State pattern`) with the specific one (`Explain the State pattern in plain English for someone who knows basic Python...`) and notice how much more useful the second answer is.

---

## 9. Set the Role

When we ask an AI a question without a role, we do not pick one — it falls back to a generic assistant voice that reaches for the average. Giving it a role changes that voice completely. A role tells the AI **who it should be** when answering.

| Prompt | What you get back |
| :--- | :--- |
| How should I prep for a game jam? | The average person, hedging |
| You are a senior game developer who has shipped three commercial titles and mentors a studio. How should I prep for a game jam? | Priorities, timeline and pitfalls of someone who runs those sprints |

The second answer uses the language, priorities and experience of a professional who has actually done it.

### Common Roles

| Role | Voice you get |
| :--- | :--- |
| 👩‍🏫 **Teacher** | Educational and step-by-step |
| 📰 **Journalist** | Factual and concise |
| 👶 **5-year-old** | Simple language and toy examples |
| 🎮 **Senior game developer** | Trade-offs, engine reality, shipped experience |

> [!NOTE]
> Roles do not give the AI new knowledge. They provide context for *how to present* information.

### Study Buddy (v2)

```text
You are a senior game developer and software architect.
You explain code to working programmers, and you never use jargon
without defining it first.

Explain {concept} in plain English for someone who knows basic Python.
Use one analogy and one code example.
Max 100 words.
```

Try other roles — "You are a grizzled dungeon master who has run a hundred campaigns" — and watch the delivery change, then restore the version above.

---

## 10. Show, Don't Tell

Telling the model to "use a certain style" is hit-or-miss. **Showing** it examples is far more reliable: after seeing them, the model reproduces the format almost exactly.

| Technique | Examples given |
| :--- | :--- |
| **Zero-shot** | 0 — just the instruction |
| **One-shot** | 1 |
| **Few-shot** | A few |
| **Many-shot** | Lots |

### Adding Examples

```text
You are a senior game developer and software architect.
You explain code to working programmers, and you never use jargon
without defining it first.

Here are two examples of how I want concepts explained:

CONCEPT: object pooling
ANALOGY: A bucket of arrows. Instead of forging a new arrow for every
shot, you fire the arrows you already have and catch them on impact.
CODE:
pool = []
def acquire():
    return pool.pop() if pool else Bullet()
def release(bullet):
    pool.append(bullet)

CONCEPT: the State pattern
ANALOGY: A health bar that only accepts one of its own states: alive,
stunned, dead. Each state knows which moves it allows.
CODE:
class State:
    def update(self, player):
        raise NotImplementedError

class Alive(State):
    def update(self, player):
        player.run()

Explain {concept}.
```

The response now matches the example format almost exactly: `CONCEPT`, `ANALOGY`, `CODE`, in that order. Few-shot is one of the most reliable ways to get consistent output from an LLM.

Try different concepts — delta time, entity component systems, frustum culling. Does the format hold?

> [!TIP]
> Two well-chosen examples beat ten instructions. If the output keeps drifting, add one more example before you add another sentence to the instructions.

---

## 11. Think Step by Step

### Chain-of-Thought Prompting

**Chain-of-thought (CoT)** prompting asks the model to reason through intermediate steps before producing a final answer. The phrase that started the whole technique is famously simple — *"Let's think step by step."* Many research papers exist on it, and most of the benefit comes from those few extra words.

> [!WARNING]
> **Trap**
> Reasoning out loud does not solve huge problems. You can ask a model to think step by step about building a Discord clone; that task is still out of reach. CoT is for getting better answers on tasks the model could already do on its own.

### Adding a Thinking Step

```text
You are a financial advisor helping a client make investment decisions.

QUESTION: Should I invest in stocks or bonds?
THINK: Compare risk, expected return, time horizon.
RECOMMENDATION: Stocks may grow faster but fluctuate more...

Analyze {question}.
Think step by step:
- What factors matter most?
- What could go wrong?
```

### Study Buddy (v3)

```text
For the new concept, first think step by step about:
- What everyday object is this most like?
- What is the most common mistake a programmer makes with it?
- Where does it show up in a game?

Then write the answer matching the format of the examples above.
```

> [!NOTE]
> Chain-of-thought helps most on hard concepts (decoration, generators, memory layouts). Easy ones benefit far less — so choose carefully which prompt to use.

---

## 12. Prompt Recap

| Technique | Idea |
| :--- | :--- |
| 🎯 **Specificity** | State audience, tone, format and length |
| 🎭 **Role prompting** | Tell the AI who it should be |
| 📚 **Few-shot prompting** | Show examples of the desired output |
| 🧠 **Chain-of-thought** | Reason through intermediate steps |

These same four techniques run inside most AI products you have already touched.

### 🎮 The Final Game Dev Study Buddy

```text
You are a senior game developer and software architect.
You explain code to working programmers, and you never use jargon
without defining it first.

Here are two examples of how I want concepts explained:

CONCEPT: object pooling
ANALOGY: A bucket of arrows. Instead of forging a new arrow for every
shot, you fire the arrows you already have and catch them on impact.
CODE:
pool = []
def acquire():
    return pool.pop() if pool else Bullet()
def release(bullet):
    pool.append(bullet)

CONCEPT: the State pattern
ANALOGY: A health bar that only accepts one of its own states: alive,
stunned, dead. Each state knows which moves it allows.
CODE:
class State:
    def update(self, player):
        raise NotImplementedError

class Alive(State):
    def update(self, player):
        player.run()

For the new concept, first think step by step about:
- What everyday object is this most like?
- What is the most common mistake a programmer makes with it?
- Where does it show up in a game?

Then write the answer in the same format as the examples above.
Max 120 words.

Explain {concept}.
```

> [!NOTE]
> The real skill of prompt engineering is **iteration**: run the prompt, read the output critically, find the weak spot, edit *one* thing, run again. The first draft is never the last.

### Project Milestone: `prompts.py`

A prompt is a string, so storing it as one is the whole engineering task. This is `Loreforge/loreforge/prompts.py`:

```python
STUDY_BUDDY = """You are a senior game developer and software architect.
You explain code to working programmers, and you never use jargon
without defining it first.

Here are two examples of how I want concepts explained:

CONCEPT: object pooling
ANALOGY: A bucket of arrows. Instead of forging a new arrow for every
shot, you fire the arrows you already have and catch them on impact.
CODE:
pool = []
def acquire():
    return pool.pop() if pool else Bullet()
def release(bullet):
    pool.append(bullet)

Explain {concept}."""


def build_prompt(concept):
    """Fill the placeholder in a prompt template.

    Uses replace() instead of str.format(): the template contains code
    examples, and any {braces} in them would be read as a format field.
    """
    return STUDY_BUDDY.replace('{concept}', concept)


print(build_prompt('delta time')[-40:])
```

**Output:**

```text
CODE:
pool = []
def acquire():
    return pool.pop() if pool else Bullet()
def release(bullet):
    pool.append(bullet)

Explain delta time.
```

> [!WARNING]
> **Trap**
> A prompt template full of Python code is full of curly braces. `TEMPLATE.format(concept=...)` raises `KeyError` the moment an example contains `{health}` or `{0}`. Reach for `str.replace()`, or keep the code examples outside the string and concatenate them.

---

## Common Use Cases

- 🧑‍🏫 Personalized tutors & study tools
- 📝 Consistent report and email generation
- 🧾 Structured data extraction — "extract the quest name, the reward and the level from this design doc"
- 🤝 Customer-support assistants with a defined voice

---

## Key Takeaways

- 🎯 A vague prompt gets the average; a specific prompt gets an answer you can use.
- 🎭 A role is free context — use it.
- 📚 Examples are more reliable than instructions.
- 🧠 Chain-of-thought is for hard concepts, not for every prompt.
- 🔁 The loop that matters is: run, read, change one thing, run again.

---

## 🎮 Extra Challenge

Build the same four-technique prompt for a new domain of your choice — a **Quest Writer**, a **Code Reviewer**, a **Localization Pipeline** — and answer these questions as you go:

- 🎭 Who is the AI?
- 👥 Who is the audience?
- 🧱 What format should the answer follow?
- 📏 How long should it be?
- 📚 What examples can I provide?
- 🧠 What should it think about before answering?

There is no single correct answer and no magic words. The goal is a prompt that reliably works **for you**.

---
