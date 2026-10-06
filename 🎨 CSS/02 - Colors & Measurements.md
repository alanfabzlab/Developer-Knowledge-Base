# 02. Colors & Measurements

**Spanish version:** [02 - Colores y Medidas.md](02%20-%20Colores%20y%20Medidas.md)

**Course:** CSS
**Topic:** The `color` Property, Named Colors, `rgb()`, Hexadecimal, Width & Height, Absolute Units and Relative Units
**Tags:** `#css` `#web-development` `#colors` `#units` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Lessons-06_--_11-7C5CFF?style=for-the-badge" alt="Lessons 06 to 11">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Two alphabets of styling, taught together because both answer the same question: *how big
and what color?* First the palette — named colors, `rgb()` and hex — then the ruler:
pixels, percentages, `em` and `rem`. By the end you will paint a damage-type chart in three
different color notations and size the same sprite two ways. Quick reference:
[[00b - CSS Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> Color and size are the two properties you will type more than any others, so it pays to
> know three ways to write a color and two families of units — one family that never moves,
> one that adapts.

---

## 06. The Palette

One of the hallmarks of building a web page is styling it with colors. In CSS, colors
highlight text, fill backgrounds, draw borders and paint gradients.

To color **text**, use the `color` property:

```css
p {
  color: red;
}
```

### Color Names

Browsers support **140 standard color names** — `red`, `tomato`, `skyblue`, `lightgreen`,
`rebeccapurple` and 136 friends. They are the fastest way to write a color and the
least precise way to match one: no named color is "our brand orange".

```css
h1 {
  color: tomato;
}

footer {
  background-color: lightgreen;
}
```

> [!NOTE]
> Text color is `color`; background color is `background-color`. Same word, two different
> properties — mixing them up is the CSS equivalent of painting the frame instead of the wall.

---

## 07. RGB Mixer

`rgb()` represents the intensity of **R**ed, **G**reen and **B**lue. Each parameter takes an
integer from `0` (no intensity) to `255` (maximum intensity).

```css
/* Red */
color: rgb(255, 0, 0);

/* Green */
color: rgb(0, 255, 0);

/* Blue */
color: rgb(0, 0, 255);

/* Emberfall orange: red and green, no blue */
color: rgb(255, 107, 53);
```

Every color on a screen is one of these triplets. `rgb()` is what you reach for when a
designer hands you "R: 255, G: 107, B: 53" — and what you reach for *later* when you want
transparency, in its cousin `rgba()`, where a fourth value from `0` to `1` sets the alpha.

---

## 08. Hex Runes

Colors can also be written as **hexadecimal** values: a `#` followed by **6 characters** —
the digits `0`–`9` and the letters `a`–`f` (or `A`–`F`). The three pairs are red, green
and blue in that order, each pair running `00` to `ff` (= 0 to 255).

```css
color: #ff0000; /* Red   — same as rgb(255, 0, 0) */
color: #008000; /* Green — same as rgb(0, 128, 0) */
color: #0000ff; /* Blue  — same as rgb(0, 0, 255) */
color: #ff6b35; /* Emberfall orange */
```

- `#ff0000` → red pair `ff`, green pair `00`, blue pair `00`.
- `#000` is valid too: a **3-digit** shorthand where each character is doubled (`#f00` = `#ff0000`).

> [!TIP]
> Mixed case works (`#FF6B35` and `#ff6b35` are the same color), but pick one convention
> and keep it — the entire vault uses lowercase.

### Quest: Damage Chart

Three damage types, three notations. Create `index.html` and `styles.css`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Damage Types</title>
</head>
<body>
  <h1>Top Three Damage Types</h1>
  <h2 id="first-type">Fire</h2>
  <h2 id="second-type">Poison</h2>
  <h2 id="third-type">Frost</h2>
</body>
</html>
```

```css
/* Named color */
#first-type {
  color: red;
}

/* rgb() color */
#second-type {
  color: rgb(0, 128, 0);
}

/* Hexadecimal color */
#third-type {
  color: #0000ff;
}
```

The same three colors written three ways — and by the end of the module you will never
wonder which notation you are looking at.

---

## 09. The Ruler: Absolute Units

Most HTML elements have a default size, including a height and a width. In CSS we change
them with the `width` and `height` properties:

```css
element {
  width: 10px;
  height: 10px;
}
```

But *what* is a `px`? Units come in two families, and choosing the wrong one is how
layouts break on the next screen.

Absolute units are **fixed**: they never change size, whatever the parent or the screen does.

| Unit | Name | Use |
| :--- | :--- | :--- |
| `px` | pixels | The most common absolute unit — borders, fixed boxes |
| `pt` | points | Print (1pt = 1/72 inch) |
| `cm` / `in` | centimeters / inches | Physical media |

```css
#badge {
  width: 100px;
  height: 100px;
}
```

> [!WARNING]
> Setting **height** with absolute units is how content escapes its box. Write `height:
> 100px` under a paragraph and watch the text overflow the border when it wraps to a third
> line. Prefer letting height grow, or use relative units.

## 10. The Ruler: Relative Units

Relative units **change when something else changes** — the parent element, or the root of
the document itself.

| Unit | Relative to | Typical use |
| :--- | :--- | :--- |
| `%` | The **parent** element's size | `width: 50%` — half of whatever dad is |
| `em` | The **element's own** font size (or the parent's, when inherited) | Padding that scales with text |
| `rem` | The **root `<html>`** font size (16px by default) | Spacing that scales with the whole page |

```css
/* Half of the parent, always */
#relative {
  width: 50%;
}

/* 1.2 times this element's font size */
p {
  font-size: 1.2em;
}

/* 2 times the root font size = 32px by default */
h1 {
  font-size: 2rem;
}
```

> [!NOTE]
> `em` stacks: a `1.2em` text inside a `1.2em` container renders at 1.44× the root size.
> `rem` never stacks — it always measures from `<html>`. When you want "twice the page
> default", you want `rem`.

## 11. Quest: Sprite Sizing

The same asset, two philosophies. Create `index.html` + `styles.css`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Measurements</title>
</head>
<body>
  <h2>Absolute Units</h2>
  <img id="absolute" src="https://placehold.co/96" alt="Fire sprite" />

  <h2>Relative Units</h2>
  <img id="relative" src="https://placehold.co/96" alt="Fire sprite" />
</body>
</html>
```

```css
#absolute {
  width: 100px;
}

#relative {
  width: 50%;
}
```

Resize the window: the first sprite never moves a pixel, the second one breathes with its
container. That single difference is most of responsive design waiting to happen.

---

## XP Earned: Key Takeaways

- 🎨 Three ways to write a color: **named**, **`rgb(r, g, b)`**, **`#rrggbb`** — all three
  describe the same red.
- 🌈 Hex runs `00`–`ff` per channel; `#f00` is shorthand for `#ff0000`.
- 📏 `width` / `height` accept any unit; the family you pick decides what survives a resize.
- 🧱 **Absolute** units (`px`, `pt`, `cm`) never change. **Relative** units (`%`, `em`, `rem`)
  change with the parent, the font or the root.
- ⚠️ Absolute `height` is the classic way to make text overflow its own box.

---

## Loot Table: Real-World Use Cases

- 🎨 Brand palettes: one hex code per color, reused across the whole site
- 📊 Charts and badges where colors must match exactly
- 🖼️ Thumbnails and avatars sized in `px`, fluid grids sized in `%`
- 📝 Type scales built on `rem` so the entire page can be resized at once

---

## 🎮 Side Quests: Practice Exercises

1. Write the color `teal` as a name, as `rgb()` and as hex — confirm all three render alike.
2. Give a `<div>` `width: 50%` and drag the browser edge; then give it `width: 300px` and do it again.
3. Set a fixed `height` on a paragraph, add text until it overflows, then delete the `height`.
4. Express 32px as `rem` (root = 16px).
5. **Boss fight:** build `palette.html` — five elements, five colors, every notation used
   at least once, plus one element sized in `px` and one sized in `%`.

---

## 🔗 See Also

- [[01 - CSS Basics]] — rules, selectors and the stylesheet link
- [[03 - Selectors Pt. 1]] — aiming color at exactly the elements you mean
- [[07 - Fonts & Text]] — where color meets typography
- [[08 - Backgrounds & Shorthands]] — `background-color`, `background-image` and friends

---
