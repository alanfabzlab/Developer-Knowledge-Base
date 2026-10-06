# 06. Pseudo-classes

**Spanish version:** [06 - Pseudoclases.md](06%20-%20Pseudoclases.md)

**Course:** CSS
**Topic:** Element States, Link Pseudo-classes (`:hover`, `:visited`), Input Pseudo-classes (`:checked`) and Child Pseudo-classes (`:first-child`, `:last-child`, `:nth-child`)
**Tags:** `#css` `#web-development` `#pseudo-classes` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-F7DF1E?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Lessons-26_--_30-7C5CFF?style=for-the-badge" alt="Lessons 26 to 30">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Pseudo-elements styled the *parts* of an element; **pseudo-classes** style its *states*.
A button resting, a button hovered, a link already visited, the fifth item of a quest
log: same element, different moment, different style. The sibling chapter on parts is
[[05 - Pseudo-elements]]. Reference: [[00b - CSS Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> A pseudo-class selects an element *in a specific state* — `a:hover`, `li:first-child`,
> `input:checked` — written as `selector:name` with **single colons**, and unlike
> pseudo-elements, pseudo-classes never create content.

---

## 26. Every Element Has Moods

Some HTML elements change state depending on how the user interacts with the page:

- Hovering over a link or a button.
- A link turning a different color *after* it is clicked and visited.
- A child element's position among its siblings — first, last, or somewhere in between.

```css
selector:pseudo-class {
  /* styles go here */
}
```

A regular selector, a colon `:`, then the pseudo-class name. The state changes and the
style follows — the CSS equivalent of a button lighting up when you look at it.

> [!TIP]
> The game design translation: pseudo-classes are *input feedback*. Every time a player
> hovers or clicks and the UI reacts, at least one pseudo-class is doing the work. They
> are how interfaces communicate "this is alive".

---

## 27. Links: Living Memory

Some of the most common pseudo-classes are linked to the `<a>` element, because a link has
rich states.

### `:hover`

Styles apply only while the cursor is over the element:

```css
a:hover {
  background-color: yellow;
  color: red;
}
```

> [!NOTE]
> The same `:hover` works on `<button>` and any other interactive element — hover is a
> state, not a link-only feature.

### `:visited`

Styles apply after the link has been clicked and visited. Browsers limit what `:visited`
may change (color and a few decorative properties) so a page cannot spy on your travel
history:

```css
a:visited {
  color: purple;
}
```

> [!WARNING]
> **Order matters.** `:visited` quietly overrides earlier styles. The classic link state
> order is *LoVe/HAte* — `:link`, `:visited`, `:hover`, `:active` — so write hover and
> active rules **after** the visited rule, or the later state never shows.

---

## 28. Inputs: Awake and Selected

The `<input>` element also responds to `:hover`:

```css
input:hover {
  background-color: green;
}
```

And for checkboxes and radio buttons there is `:checked` — the state of "this box is
ticked", perfect for option toggles:

```css
input:checked {
  outline: 2px solid blue;
}
```

> [!NOTE]
> To be precise you can scope it: `input[type="checkbox"]:checked` or
> `input[type="radio"]:checked`. Same state, explicit target.

### Quest: Settings Screen

Build a settings toggle: a checkbox that visibly changes when the player enables an option.

```html
<label>
  <input type="checkbox" />
  Night mode
</label>
```

```css
input:checked {
  outline: 2px solid #ff6b35;
  box-shadow: 0 0 4px #ff6b35;
}
```

Tick the box and the outline ignites. Untick and it goes quiet — no JavaScript involved.

---

## 29. The Party Line

Pseudo-classes also target specific **child elements** from a parent. Meet the party:

```html
<ul>
  <li>Mara, the Bladeweaver</li>
  <li>Thorne, the Tinker</li>
  <li>Piper, the Scout</li>
  <li>Grum, the Bulwark</li>
  <li>Halcyon, the Sage</li>
  <li>Bash, the Forgehand</li>
  <li>Snee, the Alchemist</li>
</ul>
```

### `:first-child`

Selects the first direct child of a parent — the party leader in line position:

```css
li:first-child {
  border: 2px solid purple;
}
```

### `:last-child`

Selects the last direct child — the one holding the door:

```css
li:last-child {
  border: 2px solid purple;
}
```

### `:nth-child()`

Applies styles based on **position or pattern**, and it takes an argument inside the
parentheses:

```css
/* By position (1-based index): the fifth hero */
li:nth-child(5) {
  border: 2px solid purple;
}

/* By keyword: every odd-numbered hero */
li:nth-child(odd) {
  border: 2px solid purple;
}

/* Even works too, and arithmetic like 2n+1 */
li:nth-child(even) {
  background-color: #1b1b2f;
  color: #f5f5f5;
}
```

> [!NOTE]
> `nth-child` counts from **1**, not 0: `:first-child` and `:nth-child(1)` are the same
> element, and `odd` means positions 1, 3, 5… Zebra-striping a table or quest log is one
> line: `li:nth-child(even) { background… }`.

### Quest: Zebra Quest Log

Take any list of seven heroes and stripe it:

```css
li:nth-child(even) {
  background-color: #2b2b36;
  color: #ffffff;
}
```

Readability for a whole log from a single rule — the quest table of your game ships with
this exact line in it.

---

## 30. State Recap

### Checkpoint: Which Pseudo-class Does What

| Pseudo-class | Selects | Most common use |
| :--- | :--- | :--- |
| `:hover` | Element under the cursor | Button and link feedback |
| `:visited` | Link already clicked | "Been there" color |
| `:checked` | Ticked checkbox/radio | Option toggles, settings |
| `:first-child` | First direct child | Lead item emphasis |
| `:last-child` | Last direct child | Closing item emphasis |
| `:nth-child(n)` | Position-based child (`odd`, `even`, `2n+1`) | Striped lists, grid patterns |

> [!WARNING]
> **Pseudo-class vs pseudo-element, 30 seconds**
> `:hover` — single colon — *state of the whole element*. `::before` — double colon —
> *a part of the element*. One narrates, the other dissects; mix up the colons and the
> rule quietly stops matching.

### More Resources

- [MDN: Pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes)
- Bonus article: Pseudo-elements → [[05 - Pseudo-elements]]
- All of them in one sheet: [[00c - CSS Cheatsheet II]]

---

## XP Earned: Key Takeaways

- 🎭 A pseudo-class styles an element **in a state**: `selector:name`.
- 🖱️ `:hover` is the universal feedback; `:visited` remembers where you clicked.
- ✅ `:checked` styles ticked checkboxes and radios.
- 👥 `:first-child` / `:last-child` / `:nth-child()` pick children by position.
- 🦓 `:nth-child(even)` zebra-stripes a whole list in one line.
- ➡️ Single colon = state (pseudo-class); double colon = part (pseudo-element).

---

## Loot Table: Real-World Use Cases

- 🎮 Hover states on buttons, cards and skill icons
- ⚙️ Settings toggles and filter pills with `:checked`
- 📜 Zebra-striped quest logs, tables and inventories
- 🧭 Nav links that show where you have already been

---

## 🎮 Side Quests: Practice Exercises

1. Build three buttons with distinct `:hover` styles.
2. Force a visited-link color and confirm DevTools agrees.
3. Stripe a 10-row party log with one `:nth-child` rule.
4. Add a `:checked` highlight to a radio group of difficulty options.
5. **Boss fight:** recreate a settings screen — night mode checkbox, volume radio group —
   entirely with pseudo-classes, no JavaScript.

---

## 🔗 See Also

- [[05 - Pseudo-elements]] — the parts, styled with double colons
- [[04 - Selectors Pt. 2]] — the selectors that carry these states
- [[07 - Fonts & Text]] — what hover styles do to typography
- [[00c - CSS Cheatsheet II]] — the full state table

---