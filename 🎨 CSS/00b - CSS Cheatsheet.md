# 00b. CSS Cheatsheet

**Spanish version:** [00b - Chuleta de CSS.md](00b%20-%20Chuleta%20de%20CSS.md)

**Course:** CSS
**Topic:** Quick reference for CSS syntax, selectors, colors, measurements, typography and pseudo-classes/elements used across the module
**Tags:** `#css` `#web-development` `#cheatsheet` `#reference` `#styling` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Covers-Chapters_01_--_06-7C5CFF?style=for-the-badge" alt="Chapters 01 to 06">
  <img src="https://img.shields.io/badge/Type-Cheatsheet-00C2A8?style=for-the-badge" alt="Cheatsheet">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

One page for the first half of the module. Every rule here was introduced in
[[01 - CSS Basics]], [[02 - Colors & Measurements]], [[03 - Selectors Pt. 1]],
[[04 - Selectors Pt. 2]], [[05 - Pseudo-elements]] or [[06 - Pseudo-classes]] — nothing
on this sheet is new. The box model, spacing, positioning and flexbox live in
[[00c - CSS Cheatsheet II]].

> [!TIP]
> Print it, or keep it in a split pane next to your editor. The fastest way to write bad
> CSS is guessing a property name from memory — this sheet exists so you never have to.

**The running theme of this module: Emberfall**, a roguelike dungeon crawler. Every
exercise styles part of its web companion: the hero title screen, the world map, the
festival flyer, the academy timetable, the champion cards. The syntax is the syntax a
real studio ships — only the words change.

---

## 🔬 Anatomy of a Declaration

```css
p {
  color: #FF6B35;   /* property: value; */
  font-size: 18px;
}
```

| Part | Example | Role |
| :--- | :--- | :--- |
| Selector | `p` | Which element(s) the rule applies to |
| Property | `color` | What is being styled |
| Value | `#FF6B35` | The new setting |
| Declaration | `color: #FF6B35;` | Property plus value, always ending in `;` |
| Rule / block | the whole `{ ... }` | Selector plus its declarations |

> [!NOTE]
> The last declaration in a block may skip its `;`, but never rely on that habit — one
> missing semicolon glues the next line to the previous value and the whole rule breaks.

---

## 🔗 Adding CSS to a Page

| Method | Where it lives | Best for | Notes |
| :--- | :--- | :--- | :--- |
| **External** | `<link rel="stylesheet" href="styles.css">` in `<head>` | Real projects | **Always prefer this** — one file styles the whole site |
| **Internal** | `<style> ... </style>` in `<head>` | Small single-page demos | Styles only that file |
| **Inline** | `style="color: blue"` on the element | Quick hacks | Highest specificity; fights every other rule |

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
</head>
<body>
  <h1 style="color: blue">Inline wins every fight — avoid it.</h1>
</body>
</html>
```

---

## 🎯 Selectors

### The Basics

| Selector | Matches | Example |
| :--- | :--- | :--- |
| `element` | Every element of that tag | `p { }` |
| `.class` | Every element with that `class` attribute | `.hero-title { }` |
| `#id` | The single element with that `id` attribute | `#top-banner { }` |
| `*` | Every element | `* { margin: 0; }` |

> [!WARNING]
> `id` must be unique — one per page, used once. `class` is reusable and the closest
> thing CSS has to a friendly default. Reach for `#id` only for anchors and
> one-of-a-kind elements.

### Combinators

| Combinator | Space | `>` | `+` | `~` |
| :--- | :--- | :--- | :--- | :--- |
| Name | Descendant | Child | Adjacent sibling | General sibling |
| Matches | any descendant | **direct** child only | next sibling only | all later siblings |

```css
nav a { }          /* links anywhere inside nav */
nav > a { }        /* links that are direct children of nav */
h2 + p { }         /* the paragraph right after an h2 */
h2 ~ p { }         /* every paragraph after an h2 in the same parent */
```

### Attribute Selectors *(chapter 04)*

| Selector | Matches |
| :--- | :--- |
| `[disabled]` | Elements with the attribute (any value) |
| `[type="text"]` | Exact value match |
| `[href^="https"]` | Value starts with `https` |
| `[src$=".png"]` | Value ends with `.png` |
| `[class*="post"]` | Value contains `post` anywhere |

### Grouping & Cascade

```css
h1, h2, h3 {
  font-family: Georgia, serif; /* comma = "and also" */
}
```

| Concept | Rule |
| :--- | :--- |
| Cascade | Later rules override earlier ones at equal specificity |
| Specificity | `inline` > `#id` > `.class` > `element` |
| `!important` | Overrides everything — and becomes a fight nobody wins; avoid |
| `inherit` | Sets a property to the parent's computed value |

---

## 🎨 Colors

| Notation | Example | When |
| :--- | :--- | :--- |
| Named | `color: rebeccapurple;` | Quick demos; a tiny palette |
| `rgb()` | `color: rgb(255, 107, 53);` | Channel values 0–255 |
| `rgba()` | `color: rgba(255, 107, 53, 0.5);` | Adds transparency on the 4th channel |
| Hex | `color: #FF6B35;` | The everyday choice — `#F6B` is short for `#FF66BB` |
| `hsl()` | `color: hsl(25, 100%, 60%);` | Hue 0–360, saturation/lightness as percentages |

> [!TIP]
> Pick one notation per project. Mixing `#FF6B35` and `rgb(255, 107, 53)` for the same
> orange is how a stylesheet forgets its own identity.

---

## 📏 Measurements

```css
p {
  font-size: 18px;
  line-height: 1.5em;
}
```

| Unit | Relative to | Typical use | Game-dev lens |
| :--- | :--- | :--- | :--- |
| `px` | nothing (absolute) | borders, shadows, small fixed sizes | 1 UI pixel |
| `em` | the element's own font-size | padding, margins that scale with text | inherits the font's "size" like a font family |
| `rem` | the root (`<html>`) font-size | consistent page-wide spacing | global scale — one dial for everything |
| `%` | the parent's matching property | widths, heights, radii | 100% of the parent box |
| `vw` / `vh` | 1% of the viewport width / height | full-screen heroes, overlays | the camera view |
| `ch` | width of the `0` glyph | reading-width paragraphs | one letter-cell |
| `auto` | the browser decides | centering, images, overflow | "do what the content needs" |

> [!IMPORTANT]
> `em` compounds with nesting (a `1.2em` inside a `1.2em` is `1.44em`), which is exactly
> why `rem` exists. Prefer `rem` for page-wide rhythm and reserve `em` for component-local
> scaling that should follow its own font.

---

## ✍️ Typography

### The Stack

```css
body {
  font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}
```

The browser walks the list left to right until it finds an installed font; the trailing
generic (`sans-serif`, `serif`, `monospace`) must always exist.

### Text Properties at a Glance

| Property | What it does | Examples |
| :--- | :--- | :--- |
| `font-family` | The typeface stack | `Georgia, serif` |
| `font-weight` | Thickness | `normal`, `bold`, `100`–`900` |
| `font-style` | Slant | `normal`, `italic` |
| `text-decoration` | Lines on the text | `none`, `underline`, `line-through` |
| `text-align` | Alignment in its container | `left`, `center`, `right`, `justify` |
| `text-transform` | Letter casing | `uppercase`, `lowercase`, `capitalize` |
| `letter-spacing` | Space between characters | `2px`, `0.1em` |
| `line-height` | Space between lines | `1.5`, `24px` — no unit = multiplier |
| `text-shadow` | Glow / shadow behind letters | `2px 2px 4px rgba(0,0,0,0.5)` |

```css
h1 {
  font-family: Georgia, serif;
  font-weight: 800;
  letter-spacing: 2px;
  text-transform: uppercase;
  text-shadow: 2px 2px 0 #1b1b2f; /* the Emberfall title-screen look */
}
```

> [!NOTE]
> Prefer `rem` for `font-size` so users who bump their browser font size see the whole
> game scale with them. Accessibility is a feature, not a patch.

---

## 👻 Pseudo-elements & Pseudo-classes

### Pseudo-elements *(chapter 05)*: style *parts* of an element — syntax `::`

| Pseudo-element | Styles | Example |
| :--- | :--- | :--- |
| `::before` | Generated content *before* the element | `quote::before { content: "»"; }` |
| `::after` | Generated content *after* the element | `a::after { content: " ↪"; }` |
| `::first-line` | The first formatted line of text | drop caps for paragraphs |
| `::first-letter` | The first letter | `text-transform: uppercase` |
| `::selection` | Text the user highlights | custom highlight colors |
| `::marker` | A list item's bullet/number | recolored bullets |

```css
p::first-letter {
  font-size: 2em;       /* drop cap */
  font-weight: bold;
}
```

> [!IMPORTANT]
> `::before` and `::after` render **nothing without `content`** — an empty `content: ""`
> still counts as a value, but skip it and the pseudo-element is a ghost.

### Pseudo-classes *(chapter 06)*: style *states* of an element — syntax `:`

| Pseudo-class | Applies when |
| :--- | :--- |
| `:hover` | The pointer is over the element |
| `:active` | The element is being pressed |
| `:focus` | The element is keyboard/click focused |
| `:visited` | A link has been visited |
| `:root` | The document root — CSS variables live here |
| `:nth-child(n)` | The element is the *n*-th child of its parent |
| `:not(selector)` | The element does **not** match the selector |

### The Order That Matters: LoVe/HAte

```css
a:link      { color: blue; }
a:visited   { color: purple; }
a:hover     { color: orange; }
a:active    { color: red; }
```

Link-state pseudo-classes share specificity, so the cascade decides — and the last one
wins. Write them in this exact order or `:hover` may silently lose to `:visited`.

---

## ⚠️ Traps Worth Memorizing

| Trap | What actually happens |
| :--- | :--- |
| Missing `;` on the first declaration | The next line glues onto the value and the rule breaks |
| Using `#id` everywhere | Specificity climbs, later rules stop working, refactors hurt |
| `p { }` and `.intro { }` on the same element | The class wins; cascade is not a popularity contest |
| `!important` to "fix" a conflict | It wins now and every future rule needs its own `!important` |
| `border: 2px blue` without a style | Nothing renders — style is mandatory |
| `::before` with no `content` | Nothing renders — content is mandatory |
| `:hover` written after `:visited` | The hover style is silently overridden; keep LoVe/HAte order |
| `font-size` in `px` everywhere | Text refuses to scale with user font settings; prefer `rem` |
| Adding padding to a `width: 50%` column | The column overflows — `box-sizing` is the fix ([[00c - CSS Cheatsheet II]]) |
| Mixing `em` and `rem` | Nested `em` compounds; pick `rem` for page-wide rhythm |

---

## 🎮 The One-Page Version

Every declaration from this sheet in one block — the Emberfall title screen:

```css
* { margin: 0; padding: 0; }

body {
  font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  font-size: 18px;
  line-height: 1.5;
  background: #1b1b2f;
}

.hero-title {
  color: #FF6B35;
  font-family: Georgia, serif;
  font-weight: 800;
  font-size: 3rem;
  letter-spacing: 4px;
  text-transform: uppercase;
  text-shadow: 3px 3px 0 #000;
}

.hero-title::first-letter {
  font-size: 1.4em; /* drop cap */
}

.btn-start {
  background: #2DD4BF;
  color: #1b1b2f;
  font-weight: 700;
  border: 2px solid #fff;
  padding: 12px 24px;
}

.btn-start:hover {
  background: #7C5CFF;
  color: #fff;
}

.btn-start:active {
  transform: translateY(2px); /* the "pressed" feel */
}

nav > a {
  color: #fff;
  text-decoration: none;
  letter-spacing: 1px;
}

a:visited { color: #c4b5fd; }
a:hover   { color: #FF6B35; }
a:active  { color: #fff; }
```

---

## 🔗 See Also

- [[00c - CSS Cheatsheet II]] — box model, spacing, display, positioning, flexbox
- [[01 - CSS Basics]] — syntax, adding CSS, the cascade
- [[02 - Colors & Measurements]] — the full color and unit tables
- [[03 - Selectors Pt. 1]] — type, class, id selectors and specificity
- [[04 - Selectors Pt. 2]] — combinators and attribute selectors
- [[05 - Pseudo-elements]] — `::before`, `::after` and friends, in depth
- [[06 - Pseudo-classes]] — states, `:nth-child()` and the LoVe/HAte order

---