# 09. Box Model & Borders

**Spanish version:** [09 - Modelo de Caja y Bordes.md](09%20-%20Modelo%20de%20Caja%20y%20Bordes.md)

**Course:** CSS
**Topic:** The Four Box Layers, Inspecting the Box, the `border` Property, Single-Side Borders, `border-radius` and the Profile Feed Frame
**Tags:** `#css` `#web-development` `#box-model` `#borders` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-F7DF1E?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Lessons-42_--_46-7C5CFF?style=for-the-badge" alt="Lessons 42 to 46">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

The most important mental model in CSS: every element on a page is a **box** with four
layers — content, padding, border, margin — and every spacing rule you write manipulates
one of them. This chapter maps the layers, shows you how to inspect any box in the
browser, and masters the `border` property in all its forms. Reference:
[[00b - CSS Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> Content inside, padding around it, border around that, margin outside — four concentric
> layers that decide where an element starts, stops and sits relative to its neighbors.

---

## 42. The Four Layers

The CSS Box Model defines how every element renders as a rectangular box. From innermost
to outermost:

| Layer | What it holds | Think of |
| :--- | :--- | :--- |
| **Content box** | The actual content: text, images, media | The room itself |
| **Padding box** | Space between content and border, still *inside* the element | Furniture pushed off the walls |
| **Border box** | The frame wrapping the padding box | The walls |
| **Margin box** | Empty space outside the border, controlling distance from neighbors | The yard between houses |

```css
div {
  padding: 20px;     /* inside space */
  border: 2px solid; /* the frame */
  margin: 10px;      /* outside space */
}
```

Each layer is optional: zero padding, no border and zero margin are all legal — and the
box still exists, because the content layer always does.

> [!TIP]
> Whenever a layout "looks wrong", ask *which layer* is lying. Too close to the edge →
> padding. Touching its neighbor → margin. Missing frame → border. The question points at
> the property every time.

---

## 43. Inspecting the Box

Browsers ship Developer Tools that inspect an element's dimensions and spatial
properties — the fastest teacher in the module.

| Browser | How to open |
| :--- | :--- |
| **Google Chrome** | Right-click an element → *Inspect* → the *Computed* tab |
| **Apple Safari** | Settings → Advanced → check *Show features for web developers*; then Develop → *Show Web Inspector* |

Inside the element panel you will find four nested rectangles — the box model diagram —
that light up the exact layer you are hovering. Click any numeric value and edit it live;
the page updates while you look.

> [!NOTE]
> The header in the HTML module (`[[01 - HTML Basics]]` Bonus Loot) opened DevTools for
> the markup. Here the same tool shows the *geometry*: hover the box diagram and watch the
> highlight move from content to padding to border to margin.

---

## 44. The border Property

The `border` shorthand combines **width, style and color** in one declaration.

### Longhand vs. Shorthand

```css
/* Longhand syntax */
h1 {
  border-width: 2px;
  border-style: solid;
  border-color: blue;
}

/* Equivalent shorthand syntax */
h1 {
  border: 2px solid blue;
}
```

| Key property | Options |
| :--- | :--- |
| `border-width` | Unit values like `px` |
| `border-style` | `solid`, `dashed`, `dotted`, `double`, `groove`, `ridge` |
| `border-color` | Named colors, `rgb()`, Hex |

### The Styles, Side By Side

| Style | looks like |
| :--- | :--- |
| `solid` | one unbroken line |
| `dashed` | short dashes |
| `dotted` | dots |
| `double` | two parallel lines |
| `groove` / `ridge` | carved-in / raised 3D effect |

> [!IMPORTANT]
> As in [[08 - Backgrounds & Shorthands]], a border with no **style** does not render —
> `border: 2px blue` is a ghost. Style first, then size and color.

---

## 45. Single-Side Borders & Rounded Corners

### Individual Borders

Each side can be styled independently with directional properties:

```css
h1 {
  border-top: 5px dashed red;
  border-right: 5px dotted purple;
  border-bottom: 5px double yellow;
  border-left: 5px solid green;
}
```

Four sides, four identities: `top`/`right`/`bottom`/`left` go clockwise from the top.

### Border Radius

`border-radius` rounds the corners; higher values make rounder edges:

```css
h1 {
  border: 2px solid blue;
  border-radius: 5px;
}
```

The extremes: `border-radius: 50%` on a square element makes a circle — the standard move
for avatars and class icons.

> [!NOTE]
> `border-radius` works without a border too: it rounds the padding box. An avatar does
> not need a frame to be round, just a radius.

---

## 46. Profile Feed Frame

### Checkpoint: Chapter Recap

- Four layers: content → padding → border → margin.
- DevTools *Computed* tab shows the box diagram and edits values live.
- `border: width style color` — style required, sides independently stylable.
- `border-radius` rounds corners; `50%` turns a square into a circle.

### Project: Feed Card Frame

A social feed card for Emberfall players, framed with the box model. The full spacing pass
(padding, margin, sizing) is chapter [[10 - Spacing & Box Sizing]] — here we lay the borders.

#### HTML (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>My Feed</title>
</head>
<body>
  <div id="outside-wrapper">
    <img id="top-img" src="https://placehold.co/160" alt="Player avatar" />

    <ul id="post-list">
      <h2>My Feed</h2>
      <li>
        <div class="post-wrapper">
          <img class="post-img" src="https://placehold.co/600x200" alt="The Guild Archive at dusk" />
          <p>Raided the archive! <b>#guildruns</b> <b>#lorehunting</b></p>
        </div>
      </li>
      <hr />
      <li>
        <div class="post-wrapper">
          <img class="post-img" src="https://placehold.co/600x100" alt="Co-op victory banner" />
          <p>Carpe diem! <b>#partywipe</b> <b>#tryagain</b></p>
        </div>
      </li>
    </ul>
  </div>
</body>
</html>
```

#### CSS (`styles.css`)

```css
* {
  font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}

div {
  border: 2px solid grey;
}

#top-img {
  width: 10em;
  height: 10em;
  border: 12px solid green;
  border-radius: 50%;
}

.post-img {
  width: 100%;
  border-radius: 5px;
}
```

The avatar becomes a green-ringed circle with one `border-radius`; every card in the feed
is framed by the generic `div` border; inner artwork gets a soft 5px radius. Borders are
in place — spacing comes next.

> [!TIP]
> **Game dev version**
> Feed cards, achievement plaques and loot announcements are all framed the same way: a
> ring, a radius, a divider. The `hr` between posts is what the box model calls "two
> listings separated by a thin margin box". [[10 - Spacing & Box Sizing]] gives them room
> to breathe.

---

## XP Earned: Key Takeaways

- 📦 Four layers: **content → padding → border → margin**, inner to outer.
- 🔍 DevTools *Computed* tab = the box model diagram, editable live.
- 🖼️ `border: width style color` — and a missing style means an invisible border.
- 🧭 `border-top/right/bottom/left` style single sides; `border-radius` rounds corners.
- ⭕ `border-radius: 50%` turns squares into circles.

---

## Loot Table: Real-World Use Cases

- 🧑‍🤝‍🧑 Avatar rings and class icons in every profile screen
- 🏷️ Card frames, dividers and highlight outlines
- 📰 Feed and timeline layouts with per-side borders
- 🎮 Achievement plaques, loot cards and friend-list frames

---

## 🎮 Side Quests: Practice Exercises

1. Draw the box model of a `<p>` with padding, border and margin — by hand, then in DevTools.
2. Give a card four differently bordered sides.
3. Round only the top corners of a banner with two-value `border-radius`.
4. Make an avatar circular with `border-radius: 50%` and a thick colored ring.
5. **Boss fight:** frame a guild-membership card — circular avatar, two posts with
   dividers, rounded inner artwork — borders first, no spacing rules yet.

---

## 🔗 See Also

- [[10 - Spacing & Box Sizing]] — padding, margin, centering and `box-sizing`
- [[08 - Backgrounds & Shorthands]] — where the `border` shorthand was born
- [[02 - Colors & Measurements]] — units and color notations for borders
- [[00c - CSS Cheatsheet II]] — the box model diagram on one page

---