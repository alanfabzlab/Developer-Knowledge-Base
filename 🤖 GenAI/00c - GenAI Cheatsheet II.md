
# 00c. GenAI Cheatsheet II

**Spanish version:** [00c - Chuleta de GenAI II.md](00c%20-%20Chuleta%20de%20GenAI%20II.md)

**Course:** GenAI
**Topic:** Prompt Patterns, Vector Representations, Similarity Math & the AI Risk Checklist
**Tags:** `#genai` `#ai` `#llm` `#cheatsheet` `#prompting` `#safety`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

The second half of the module in one page: how to build a prompt, how to compare vectors, and what to check before anything an AI produced reaches a player. Companion to [[00b - GenAI Cheatsheet]].

---

## 🎭 Prompt Building Blocks

| Block | Ask yourself | Example |
| :--- | :--- | :--- |
| 🎭 **Role** | Who is the AI? | You are a senior game developer. |
| 👥 **Audience** | Who is it for? | … for a programmer who knows basic Python. |
| 🧱 **Format** | What structure? | Use one analogy and one code example. |
| 📏 **Length** | How long? | Max 100 words. |
| 🎨 **Tone** | What voice? | In casual Japanese, avoid jargon. |
| 📚 **Examples** | What does good look like? | Two `CONCEPT / ANALOGY / CODE` samples. |
| 🧠 **Reasoning** | What to think about first? | First think step by step about… |

### Shot Types

| Type | Examples given |
| :--- | :--- |
| **Zero-shot** | 0 |
| **One-shot** | 1 |
| **Few-shot** | A few |
| **Many-shot** | Lots |

### Reusable Prompt Template

```text
You are {role}.

Here are examples of how I want answers formatted:
{example_1}
{example_2}

For the new request, first think step by step about:
- {question_1}
- {question_2}

Then answer in the same format as the examples.
Max {n} words.

{request}
```

> [!NOTE]
> In Python, fill it with `template.replace('{request}', request)` — **not** `str.format()`. A prompt full of code examples is full of braces, and `format()` reads every one of them as a field.

> [!TIP]
> Prompt engineering is iteration: run, read critically, change one thing, run again.

---

## 📐 Vector Representations

| Method | What it captures | Weakness |
| :--- | :--- | :--- |
| **One-hot** | The identity of one word | Every distinct pair is equally far apart |
| **Bag of words** | Word counts in a document | Tied to exact words; ignores order, case and meaning |
| **Embeddings** | Meaning (dense, learned vectors) | Needs a trained model |

---

## 📏 Similarity Math

| Concept | Formula / idea |
| :--- | :--- |
| **Hamming distance** | The number of positions where two vectors differ |
| **Dot product** | $A \cdot B = \sum a_i \times b_i$ |
| **Magnitude** | $\|A\| = \sqrt{\sum a_i^2}$ |
| **Cosine similarity** | $(A \cdot B) / (\|A\| \times \|B\|)$ → `1` = same direction, `0` = nothing in common |

**Worked example.** `[2, 1, 0]` vs `[1, 1, 1]` → dot `= 3`, $\|A\| \approx 2.236$, $\|B\| \approx 1.732$ → cosine `≈ 0.775`.

### Semantic Search Pipeline

```text
query -> vector -> compare with document vectors (cosine) -> sort -> top results
```

The pipeline never changes. Only the way you build the vectors does.

---

## ⚠️ Where AI Goes Wrong

| Risk | What happens | Defense |
| :--- | :--- | :--- |
| 👻 **Hallucination** | Confident, plausible, wrong | Double-check facts and sources |
| 🕰️ **Cutoff** | No knowledge after the training date | Use search or RAG; check dates |
| 💉 **Prompt injection** | Untrusted text overrides instructions | Treat user content as data; limit permissions |
| ⚖️ **Bias** | Reflects skews in the training data | Look for patterns; ask for balanced output |
| 🐛 **Buggy code** | Plausible but incorrect | Read every line, test edge cases |

### Edge Cases to Test in AI Code

| Edge case | Example |
| :--- | :--- |
| **Empty input** | `[]`, `""`, `None` |
| **Extreme values** | A single element, a very large input |
| **Formatting** | Uppercase, spaces, punctuation, accents |
| **Boundaries** | Off-by-one errors |
| **Silent failures** | Where an error should be raised |
| **Wrong type** | A number where a string was expected |

### When to Use AI

| ✅ Good fit | ❌ Bad fit |
| :--- | :--- |
| Explaining, drafting, brainstorming, summarizing | Anything that must be exactly right and cannot be checked |
| Output you can verify quickly | Recent events, precise facts, exact math |
| Remixing well-known material | High-stakes legal or medical advice |

**Workflow:** Generate → Run → Read → Fix. The output is a draft, not the final answer.

---

## 🛡️ Pre-Ship Checklist

- [ ] Facts, names, numbers and citations verified?
- [ ] Topic after the model's cutoff?
- [ ] Untrusted text inside my prompt?
- [ ] Edge cases tested (empty, huge, weird, wrong type)?
- [ ] Stereotypes or skewed assumptions checked?
- [ ] A human responsible for this output?

---
