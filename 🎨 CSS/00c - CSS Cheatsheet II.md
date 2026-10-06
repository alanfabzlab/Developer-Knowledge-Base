# 00c. CSS Cheatsheet II

**Spanish version:** [00c - Chuleta de CSS II.md](00c%20-%20Chuleta%20de%20CSS%20II.md)

**Course:** CSS
**Topic:** Quick reference for backgrounds, the box model, spacing & sizing, display, positioning, `z-index` and flexbox used across the module
**Tags:** `#css` `#web-development` `#cheatsheet` `#reference` `#layout` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-F7DF1E?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Covers-Chapters_07_--_12-7C5CFF?style=for-the-badge" alt="Chapters 07 to 12">
  <img src="https://img.shields.io/badge/Type-Cheatsheet-00C2A8?style=for-the-badge" alt="Cheatsheet">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

One page for the second half of the module. Every rule here was introduced in
[[07 - Fonts & Text]], [[08 - Backgrounds & Shorthands]], [[09 - Box Model & Borders]],
[[10 - Spacing & Box Sizing]], [[11 - Display & Positioning]] or [[12 - Flexbox]] —
nothing on this sheet is new. Syntax, selectors, colors, units, typography and
pseudo-classes/elements live in [[00b - CSS Cheatsheet]].

> [!TIP]
> Layout is where CSS actually earns its keep — and where the traps hide. When a page
> refuses to sit where you expect, walk the sections here in order: box, spacing,
> display, position, flex. One of them is lying.

**The running theme of this module: Emberfall**, a roguelike dungeon crawler. Halfway
through the module the layouts graduate from screens to pages: the feed card, the Guild
Archive, the Academy timetable, the champion card collection. The properties are the
properties a real studio ships — only the words change.

---

## 🗺️ The Box Model

Every element is a box with four concentric layers:

| Layer | From inside out | Controls | Property |
| :--- | :--- | :--- | :--- |
| Content | the actual content | size of the room | `width`, `height` |
| Padding | space *inside* the border | furniture off the walls | `padding` |
| Border | the frame | wall thickness, style, color | `border` |
| Margin | space *outside* the border | distance to neighbors | `margin` |

### box-sizing: who owns the declared size

```css
/* Default: padding and border ADD to width/height */
* {
  box-sizing: border-box; /* the modern reset — declared size stays */
}
```

| Value | Declared `width: 150px` + `padding: 20px` renders as |
| :--- | :--- |
| `content-box` | 150 + 40 = **194px** (border adds more) |
| `border-box` | **150px** — padding is absorbed inside |

> [!WARNING]
> The classic breakage: `width: 50%` on two side-by-side columns, then padding → both
> overflow the row. The universal `border-box` reset prevents it — put it in every file.

---

## 🌄 Backgrounds *(chapter 08)*

| Property | Function | Example |
| :--- | :--- | :--- |
| `background-color` | Base color | `background-color: #1b1b2f;` |
| `background-image` | Image layer | `background-image: url("bg.png");` |
| `background-repeat` | Tiling | `no-repeat`, `repeat-x`, `repeat-y` |
| `background-position` | Placement | `center`, `top right`, `10px 20px` |
| `background-size` | Scaling | `cover` (crop to fill), `contain`, `100%` |

```css
.banner {
  background-image: url("https://placehold.co/1200x200/1b1b2f/ff6b35");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  height: 200px;
}
```

> [!NOTE]
> `cover` scales the image to cover the whole element (cropping the overflow); `contain`
> fits the whole image inside (leaving empty bands). Choose by whether the element or the
> image is the boss.

---

## 📐 Shorthands: The Clock, in One Line

`border`, `margin` and `padding` share the same 1–4 value grammar. **Top → Right →
Bottom → Left**, clockwise from 12:

```css
padding: 10px;              /* all four sides */
padding: 10px 20px;         /* vertical | horizontal */
padding: 10px 20px 30px;    /* top | horizontal | bottom */
padding: 10px 20px 30px 40px; /* top | right | bottom | left */
border: 2px solid #333;     /* width | style | color — style is REQUIRED */
```

| Property | What the shorthand bundles | Mandatory piece |
| :--- | :--- | :--- |
| `padding` / `margin` | all four sides, clockwise | size value(s) |
| `border` | width + style + color | **style** — no style, no render |
| `background` | color + image + position + size… | a color or image |
| `font` | style + weight + size/line-height + family | size and family |

> [!TIP]
> Read `border: 2px solid blue` aloud as "width style color" and the shorthand never
> surprises you again. The clock answers every ordering question on this sheet.

---

## 📏 Spacing & Sizing *(chapter 10)*

### The Full Padding/Margin Grammar

| Declaration | Effect |
| :--- | :--- |
| `margin: 20px` | 20px all around |
| `margin: 20px 10px` | 20px top/bottom, 10px left/right |
| `margin: 10px 20px 30px` | top, then horizontal, then bottom |
| `margin: 10px 20px 30px 40px` | top, right, bottom, left |
| `margin: 0 auto` | 0 vertical, **centered horizontally** — needs a `width` |

### The Rules That Matter

| Rule | Meaning |
| :--- | :--- |
| `margin: auto` | Centers a block horizontally **only with a declared `width`** |
| Negative margins | Pull boxes closer or overlap them; padding can never be negative |
| `width: 100%` + margin | Overflows the parent — `width` already fills it; widen with padding instead |
| `rem` vs `em` | `rem` = root scale (page-wide); `em` = local scale (compounds inside nesting) |

```css
/* The universal reset: every box starts equal */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```

---

## 🧱 Display *(chapter 11)*

| Value | Flow | Width/height | Use |
| :--- | :--- | :--- | :--- |
| `block` *(default for div, p, h1…)* | own line, stacks | honored | sections, cards |
| `inline` *(default for span, a, b…)* | same line as siblings | ignored | text runs |
| `inline-block` | same line | **honored** | nav pills, icons, buttons |
| `none` | removed from the page entirely | — | hiding |

> [!NOTE]
> `display: none` removes the element *and its space*; `visibility: hidden` keeps the
> space but shows nothing. Debug menus, quick toggles and collapsed states use both.

---

## 📌 Position *(chapter 11)*

| Value | Anchored to | Leaves normal flow? | Typical use |
| :--- | :--- | :--- | :--- |
| `static` *(default)* | — | no | the baseline |
| `relative` | its own normal spot | no | nudges; **the positioned ancestor** |
| `absolute` | nearest **positioned** ancestor | yes | badges, corners, overlays |
| `fixed` | the viewport | yes | back-to-top, chat, persistent nav |
| `sticky` | its parent, after a scroll threshold | no (until pinned) | section headers, table headers |

```css
/* absolute answers to the nearest positioned ancestor */
.card { position: relative; }

.badge {
  position: absolute;
  top: 10px;
  right: 10px;
}
```

| Offset | Meaning |
| :--- | :--- |
| `top` / `bottom` | Distance from the anchor's top / bottom edge |
| `left` / `right` | Distance from the anchor's left / right edge |
| `z-index` | Stacking order **on positioned elements only** — higher = on top |

> [!WARNING]
> An `absolute` element with **no positioned ancestor** anchors to the page and other
> content ignores it completely — if a badge "flies to the corner of the document", the
> missing `position: relative` is the bug.

---

## 📦 Flexbox *(chapter 12)*

### On the Container

```css
.container {
  display: flex;              /* one line turns children into flex items */
  flex-direction: row;        /* row | row-reverse | column | column-reverse — the main axis */
  flex-wrap: wrap;            /* nowrap | wrap | wrap-reverse */
  justify-content: center;    /* main axis: start | center | end | space-between | space-around | space-evenly */
  align-items: center;        /* cross axis: stretch | center | start | end */
  gap: 16px;                  /* uniform space between items */
}
```

| Property | Axis | Spaces… |
| :--- | :--- | :--- |
| `justify-content` | main | the line of items |
| `align-items` | cross | all the items |
| `align-self` | cross | **one** item (overrides `align-items`) |
| `gap` | both | the channels between items |

```css
/* The perfect centering recipe — both axes, two lines */
.hero {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

### On the Items

```css
.item {
  flex: 1;           /* flex-grow: 1  — claim equal shares of free space */
  flex: 0 0 200px;   /* grow-0 shrink-0 basis-200px — fixed item */
  align-self: end;   /* override the container's cross-axis rule */
  order: -1;         /* reorder without touching the HTML */
}
```

| Item property | Role | Shorthand |
| :--- | :--- | :--- |
| `flex-grow` | share of *free space* (0 = never) | `flex: 1 1 0%` |
| `flex-shrink` | how fast to give space back (1 = default) | part of `flex` |
| `flex-basis` | starting size before distribution | `flex: 1` ≈ `1 1 0%` |

> [!IMPORTANT]
> `flex-grow` distributes **free space**, not proportions: `flex: 1` vs `flex: 2` gives
> the second item twice the *extra*, not twice the width — unless `flex-basis: 0%` turns
> grow into a real ratio.

---

## ⚠️ Traps Worth Memorizing

| Trap | What actually happens |
| :--- | :--- |
| `width: 50%` + padding (content-box) | Both columns overflow the row — `border-box` |
| `margin: auto` with no width | Nothing moves — there is no leftover space to share |
| `border: 2px blue` (no style) | No border renders; style is mandatory |
| `absolute` with no positioned ancestor | The element anchors to the page; siblings ignore it |
| `z-index` on a `static` element | Ignored — z-index works on positioned/flex items only |
| `justify-content` when items fill the row | Nothing to distribute — free space must exist first |
| `flex: 1` with `flex-wrap` | Items grow to fill the *first* line and leave gaps at the end |
| `display: none` when you meant "hidden" | The layout collapses — use `visibility: hidden` to keep the space |
| `background-size: contain` in a header | Empty bands appear — `cover` is usually the banner answer |
| Sticky header that scrolls out | A `relative` parent taller than the viewport eats the sticky pin |

---

## 🎮 The One-Page Version

Every layout rule from this sheet, in one block — the battle screen:

```css
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  display: flex;              /* the whole screen is a flex app shell */
  height: 100vh;
  font-family: 'Segoe UI', Roboto, Arial, sans-serif;
  background: #1b1b2f;
}

#hud {
  position: fixed;            /* pinned to the screen top */
  top: 0; left: 0; right: 0;
  background: #333;
  color: #fff;
  padding: 8px 16px;
  z-index: 100;
}

main {
  flex: 1;                    /* absorbs all remaining width */
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 16px;
  padding: 64px 24px 24px;    /* clear the fixed HUD */
}

#sidebar {
  flex: 0 0 200px;            /* fixed-width sidebar */
  border-right: 2px solid #555;
  padding: 16px;
}

.card {
  position: relative;
  width: 160px;
  height: 220px;
  border: 2px solid #FF6B35;
  border-radius: 8px;
  background-image: url("champion.png");
  background-size: cover;
  background-position: center;
}

.card .hp {
  position: absolute;         /* badge in the card's corner */
  bottom: 8px;
  left: 8px;
  background: #2DD4BF;
  border-radius: 4px;
  padding: 2px 8px;
}

.lesson-title {
  position: sticky;           /* pins while its section scrolls */
  top: 48px;
  background: #7C5CFF;
  color: #fff;
  padding: 8px;
}
```

---

## 🔗 See Also

- [[00b - CSS Cheatsheet]] — syntax, selectors, colors, units, typography, pseudo
- [[08 - Backgrounds & Shorthands]] — the full background and shorthand tables
- [[09 - Box Model & Borders]] — the four layers and all border styles
- [[10 - Spacing & Box Sizing]] — padding/margin grammar and `box-sizing`
- [[11 - Display & Positioning]] — display, the five position values, `z-index`
- [[12 - Flexbox]] — container and item properties, with the card capstone

---