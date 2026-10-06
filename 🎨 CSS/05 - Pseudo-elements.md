# 05. Pseudo-elements

**Spanish version:** [05 - Pseudoelementos.md](05%20-%20Pseudoelementos.md)

**Course:** CSS
**Topic:** `::first-letter` & `::first-line`, `::before` & `::after`, the `content` Property, Tooltips, Link Icons & the Ground Rules
**Tags:** `#css` `#web-development` `#pseudo-elements` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-F7DF1E?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Lessons-21_--_25-7C5CFF?style=for-the-badge" alt="Lessons 21 to 25">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

So far you have styled whole elements. **Pseudo-elements** let you reach *inside* an
element — its first letter, its first line, or content that does not exist in the HTML at
all — without adding a single tag. The companion chapter on states is
[[06 - Pseudo-classes]]; between them you can style anything that happens to an element.
Reference: [[00b - CSS Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> A pseudo-element selects a *part* of an element — real parts like `::first-letter`, and
> invented parts like `::before` — written as `selector::name` with **double colons**.

---

## 21. Second Skin

Pseudo-elements create, select and style specific parts of an HTML element without extra
markup. They use **double colons** `::` followed by the pseudo-element name.

### Basic Syntax

```css
selected-element::pseudo-element {
  /* CSS styles here */
}
```

> [!NOTE]
> CSS3 wrote these with a single colon (`:first-letter`). Modern CSS writes double
> (`::first-letter`), and browsers still accept both — but double is the standard you
> should use.

---

## 22. Opening Letter, Opening Line

### `::first-letter`

Targets the very first letter of the text inside a block-level element — the classic drop
cap of every fantasy novel ever printed.

### `::first-line`

Targets the entire first line of text inside a block element. (When the window narrows and
the text wraps, the browser re-decides which words are "first line" — it is a rendering
choice, not a fixed set of words.)

```html
<p>The Emberfall dungeon opens at dawn, and the lanterns go out one by one.</p>
```

```css
p {
  width: 25%;
}

p::first-letter {
  font-size: 36px;
  font-family: 'Gill Sans', sans-serif;
  text-decoration: underline;
  text-decoration-color: black;
  color: #e01a18;
}

p::first-line {
  font-size: 1.5em;
}
```

The `<p>` in the HTML is untouched: no wrapper span, no extra class. CSS went straight to
the letter.

---

## 23. Before, After and the `content` Property

`::before` and `::after` create decorative or supplemental content rendered **before or
after** the element's actual content, using the special `content` property.

```css
selected-element::before {
  content: "Loot: ";
  /* Other styles here */
}

selected-element::after {
  content: " ✨";
  /* Other styles here */
}
```

- The pseudo-element is **empty** in the HTML — `content` is what puts text in it.
- Anything can style it: size, color, background, borders, margins.

```css
p::after {
  content: " 📄";
}
```

> [!IMPORTANT]
> `content` is mandatory. A `::before` or `::after` rule without `content` — even
> `content: ""` — renders nothing, because the box itself is what `content` creates.

---

## 24. Practical Applications

Consider this HTML:

```html
<p>
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements" target="_blank">Pseudo-elements</a>
  are keywords added to a selector that let us style a specific part of the selected element(s).
</p>
```

### Application A: Add a Tooltip

Combine a pseudo-element with the `:hover` pseudo-class to float an explanation above a
link — no JavaScript, no extra markup.

Assuming `body` has `position: relative`:

```css
body {
  position: relative;
}

a:hover::before {
  content: "Matches when the user interacts with an element with a pointing device but does not necessarily activate it. It is generally triggered when the user hovers over an element with the cursor.";
  position: absolute;
  top: 35px;
  bottom: 0;
  width: 15%;
  height: max-content;
  border: 2px solid;
  background-color: lightyellow;
  color: black;
  padding: 2px;
}
```

Hover the link and a tooltip box appears; move away and it vanishes. The pseudo-element
lives entirely in CSS.

> [!TIP]
> Tooltips are the game-dev version of a codex hover: item stats, ability ranges and
> recipe hints in every inventory screen are this exact pattern — text that exists only
> while the cursor asks for it.

### Application B: Add an Icon

Decorate the end of a hyperlink inside a paragraph with a small external-link icon:

```css
a::after {
  background-image: url("https://static-00.iconduck.com/assets.00/external-link-icon.png");
  background-size: 10px 10px;
  display: inline-block;
  width: 10px;
  height: 10px;
  content: "";
  margin-left: 2.5px;
}
```

Note the empty quotes in `content: ""` — the box is created empty, and the image is
painted into it with `background-image` and `url()`. Every wiki link on the page gets the
icon without a single `<img>` tag.

---

## 25. Ground Rules

Two rules decide whether a pseudo-element rule is valid at all.

### Rule 1: One Use Per Element

The same pseudo-element cannot be used twice on the same selected element. The second
block is silently ignored:

```css
/* INVALID */
selected-element::before {
  content: "These";
  font-size: 1.5em;
}

selected-element::before {
  content: "Will not work";
  background-color: green;
}

selected-element::first-letter {
  font-family: "Helvetica";
}

selected-element::first-letter {
  background-color: purple;
}
```

Write one `::before` rule per element and put **all** of its declarations inside — the
duplicate adds nothing and the browser drops it.

### Rule 2: The Pseudo-element Goes Last

A pseudo-element must be the final part of the selector:

```css
/* INVALID */
p::after.class {
  content: " This won't work either!";
  text-decoration: underline;
}

/* VALID — the pseudo-element is last */
p.class::after {
  content: " This will work!";
  text-decoration: underline;
}
```

You can aim first (`p.class`) and decorate after (`::after`); you cannot decorate first
and aim after.

> [!WARNING]
> A rule that breaks these rules does not error — it just stops existing. When a
> pseudo-element "does nothing", check for a second rule with the same name and check
> where the `::` sits in the selector.

### More Resources

- [MDN: Pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements)
- Bonus article: Pseudo-classes → [[06 - Pseudo-classes]]

---

## XP Earned: Key Takeaways

- 🧬 `selector::name` with **double colons** selects a *part* of an element.
- 🔠 `::first-letter` / `::first-line` style the opening of a text block.
- 📦 `::before` / `::after` invent content — `content` is what makes it appear.
- 💬 `a:hover::before` is a tooltip with zero JavaScript.
- ⚠️ One pseudo-element per element, and it must end the selector.

---

## Loot Table: Real-World Use Cases

- 📖 Drop caps on articles and lore pages
- 💬 Tooltips for item stats, ability ranges and form hints
- 🔗 External-link icons appended to every anchor
- 🏷️ Price tags, "NEW" badges and required-field asterisks — all injected by CSS

---

## 🎮 Side Quests: Practice Exercises

1. Give every `<h2>` on a page a decorative `::after` emoji.
2. Build a tooltip that appears when hovering a boss name.
3. Restyle the drop cap of a lore paragraph — size, color and font.
4. Add an asterisk after every required form label using `::after`.
5. **Boss fight:** write a broken `::before` rule, then a second one trying the same
   pseudo-element — predict which one wins, then check in DevTools.

---

## 🔗 See Also

- [[06 - Pseudo-classes]] — the sibling chapter: styling by state
- [[04 - Selectors Pt. 2]] — the selectors these pseudo-elements attach to
- [[07 - Fonts & Text]] — what to do with the letters you just selected
- [[00c - CSS Cheatsheet II]] — pseudo-classes and pseudo-elements side by side

---
