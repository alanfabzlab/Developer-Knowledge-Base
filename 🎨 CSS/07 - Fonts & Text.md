# 07. Fonts & Text

**Spanish version:** [07 - Fuentes y Texto.md](07%20-%20Fuentes%20y%20Texto.md)

**Course:** CSS
**Topic:** The Five Generic Font Families, `font-family` & Fallbacks, `font-size`, `font-weight`, `text-align` and `text-decoration`
**Tags:** `#css` `#web-development` `#fonts` `#typography` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-F7DF1E?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Lessons-31_--_35-7C5CFF?style=for-the-badge" alt="Lessons 31 to 35">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Fonts carry most of a page's tone, and alignment carries most of its rhythm. This chapter
covers the five generic font families, how to choose a face *and* a fallback, the `font-size`
and `font-weight` axes, and the text properties that position and decorate words. By the
end you will have given a game's tagline a real typographic system. Reference:
[[00b - CSS Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> Typography is two controls — *which face* (`font-family` + weight/size) and *how the
> text sits* (`text-align` / `text-decoration`) — and the font stack you write decides how
> the page looks on a machine that does not own your font.

---

## 31. The Five Families

CSS supports **five generic font families** across major web browsers ("web-safe"),
and every device has at least one face for each:

| Font Family | Characteristics | Examples |
| :--- | :--- | :--- |
| **Serif** | Small decorative strokes at the ends of letters; readable for printed material | Georgia, Times New Roman, Baskerville |
| **Sans-serif** | No end strokes; modern, clean look for digital media | Arial, Helvetica Neue, Open Sans |
| **Monospace** | Every character occupies the same width; built for programming | Consolas, Courier New, Lucida Console |
| **Cursive** | Hand-written appearance; personal, creative touch | Brush Script MT, Lobster, Dancing Script |
| **Fantasy** | Highly stylized or decorative letterforms; maximal personality | Impact, Chiller, Jokerman |

The decision shortcut: **serif** for long-form reading, **sans-serif** for interfaces and
HUDs, **monospace** for code and numbers, **cursive/fantasy** for titles that must feel
hand-painted.

---

## 32. Choosing a Face and a Fallback

To set font families, use the `font-family` property, with any number of names in a comma
separated list — the browser tries each one in order until one exists:

```css
p {
  font-family: Arial, sans-serif;
}
```

> [!IMPORTANT]
> Always end the stack with a **generic family** (`sans-serif`, `serif`, `monospace`…).
> The generic is the safety net: if the visitor's machine lacks every specific font, it
> still picks a face in the right *mood* instead of falling back to something random.

```css
h1 {
  font-family: "Brush Script MT", "Lobster", cursive;
}
```

Quoted names contain spaces; unquoted generic names never need quotes.

---

## 33. Sizing the Text

`font-size` sets text size using absolute units (`px`, `pt`) or relative units (`%`, `em`, `rem`):

```css
/* Absolute: the size is fixed */
p {
  font-size: 12px;
}

/* Relative: scales with its context */
p {
  font-size: 1.2em;
}
```

> [!WARNING]
> **Accessibility note**
> Favor relative units for paragraph text: browsers can rem-scale `%`/`em`/`rem` with the
> user's font preference, while `px` refuses. And keep body copy smaller than headings —
> heading size is how readers build the page's mental outline.

---

## 34. Weighing the Text

`font-weight` defines thickness using keywords or numeric values from `100` to `900`:

| Range | Feel |
| :--- | :--- |
| Below 400 | Thin / light |
| 400 – 700 | Normal range for body text (400 = regular, 700 = bold) |
| Above 700 | Heavy — headlines, damage numbers |

```css
p {
  font-weight: 800;
}
```

> [!NOTE]
> 400 and 700 are the weights most font files actually contain; the values between are
> synthesized by the browser when the face lacks them. Ask for `800` and get "bold, plus".

### Quest: Five Families

Put the family knowledge in one page. Create `index.html` and `styles.css`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Five Families</title>
</head>
<body>
  <p>Hello world! Learning CSS fonts and styles.</p>
</body>
</html>
```

```css
p {
  font-family: Arial, sans-serif;
  font-size: 18px;
  font-weight: 600;
}
```

One paragraph, three decisions: a clean interface face, a readable size, medium-bold
weight. That baseline is what every HUD in the vault will start from.

---

## 35. Placing the Text

### `text-align`

Controls the **horizontal alignment** of inline content inside a block:

```css
#left-align {
  text-align: left; /* Default */
}

#center-align {
  text-align: center;
}

#right-align {
  text-align: right;
}
```

There is also `justify` (both margins aligned, newspaper style) — great for long lore
paragraphs, dangerous for short captions, where it stretches word gaps into rivers.

### `text-decoration`

Adds visual decorations — underlines, overlines, line-throughs — to text:

```css
p {
  text-decoration: underline;
}
```

The shorthand takes up to four values (line, style, color, thickness) — the full toolbox
is in [[08 - Backgrounds & Shorthands]].

### Quest: Spellcheck

Style a deliberately misspelled line the way a text editor flags errors. Create `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Spellcheck</title>
</head>
<body>
  <h4>The <span>marskman</span> will <span>recieve</span> the relic at the guild hall.</h4>
</body>
</html>
```

And `styles.css`:

```css
h4 {
  text-align: center;
}

span {
  text-decoration: underline wavy red 2px;
}
```

Centered line, wavy red underlines exactly where the typos live. That single declaration —
`underline wavy red 2px` — is the same recipe real editors use, and it needs no extra HTML
besides the `<span>`s that point at the mistakes.

> [!TIP]
> **Game dev version**
> A dialog box with `text-align: center` and cardboard-box flavor text set in a
> different-family font is 80% of the "cinematic" look in RPGs. Alignment tells the
> player where to look; the font family tells them how to feel.

---

## XP Earned: Key Takeaways

- 🖋️ Five generic families exist everywhere: **serif, sans-serif, monospace, cursive, fantasy**.
- 🧱 `font-family` is a **stack**: specific names first, generic family last.
- 📏 `font-size`: absolute (`px`) fixed, relative (`em`/`rem`) accessible.
- ⚖️ `font-weight`: 100–900; 400 normal, 700 bold.
- 🧭 `text-align` places lines; `text-decoration` decorates them.
- 🎯 One line — `underline wavy red 2px` — is a full spellcheck highlight.

---

## Loot Table: Real-World Use Cases

- 🎮 HUD baseline: sans-serif stack, `18px`, `600` weight
- 📜 Lore pages: serif for long-form, `justify` for both margins
- 💻 Code excerpts: monospace with the same width on every glyph
- 🏷️ Title screens: cursive/fantasy for the splash text that must feel painted

---

## 🎮 Side Quests: Practice Exercises

1. Write a three-face font stack ending in a generic family; test it with the first font missing.
2. Set the same text at `12px`, `1em` and `1rem` — measure the difference.
3. Center a heading, right-align a caption, justify a paragraph.
4. Rebuild the spellcheck page with `dashed` instead of `wavy`.
5. **Boss fight:** build `hud.html` — a quest title in fantasy, body in sans-serif `600`,
   flavor text centered, and a misspelled hero name flagged wavy red.

---

## 🔗 See Also

- [[08 - Backgrounds & Shorthands]] — the full `text-decoration` and `font` shorthands
- [[02 - Colors & Measurements]] — the units `font-size` consumes
- [[05 - Pseudo-elements]] — drop caps for your lore paragraphs
- [[00b - CSS Cheatsheet]] — fonts and text on one page

---