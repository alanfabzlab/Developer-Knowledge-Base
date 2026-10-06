# 12. Flexbox

**Spanish version:** [12 - Flexbox ES.md](12%20-%20Flexbox%20ES.md)

**Course:** CSS
**Topic:** The Flex Container, Main vs Cross Axis, `flex-direction`, `flex-wrap`, `justify-content`, `gap`, `align-items`, `align-self`, `flex-basis`/`flex-grow`/`flex-shrink` & the Champion Card Collection Capstone
**Tags:** `#css` `#web-development` `#layout` `#flexbox` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-ADVANCED-F7DF1E?style=for-the-badge" alt="Advanced">
  <img src="https://img.shields.io/badge/Lessons-61_--_66-7C5CFF?style=for-the-badge" alt="Lessons 61 to 66">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

The last chapter of the module — and the layout tool modern CSS is built on. Flexbox turns
any element into a container that **distributes its children along an axis**: spacing them,
centering them, wrapping them and letting them grow and shrink in proportion. From nav
bars to card grids to the final Champion Card Collection, one container rules them all.
Reference: [[00c - CSS Cheatsheet II]].

> [!NOTE]
> **The whole chapter in one sentence**
> `display: flex` on the parent, then `justify-content`/`align-items` distribute items
> along the main/cross axes, and `flex` on the children decides who grows.

---

## 61. The Flex Container

```css
.container {
  display: flex;
}
```

Adding `display: flex` to a parent makes it a **flex container**; its direct children
become **flex items**. One declaration rewrites the layout rules from chapter
[[11 - Display & Positioning]]: items stop stacking as plain blocks and line up on a
shared row, ready to be ordered, spaced, wrapped and resized.

```css
.parent {
  display: flex;
  background: #1572B6;
  gap: 10px;
}

.child {
  background: #2DD4BF;
  padding: 16px;
  border-radius: 5px;
}
```

With no other rules, the three children sit side by side, automatically sharing the
cross-available height.

> [!TIP]
> Everything inside a flex container is a flex item — but only *direct* children. Nested
> elements keep their own behavior until their own parent becomes a flex container.
> That is how flex composes: containers inside containers.

---

## 62. Axes, Direction & Wrapping

Flexbox thinks in **axes**, not rows and columns. Two properties steer them:

### flex-direction: which axis is "main"

| Value | Main axis runs | Items end up |
| :--- | :--- | :--- |
| `row` *(default)* | left → right | side by side |
| `row-reverse` | right → left | side by side, reversed |
| `column` | top → bottom | stacked |
| `column-reverse` | bottom → top | stacked, reversed |

The **main axis** is the direction of flow; the **cross axis** is perpendicular to it.

### flex-wrap: one line or several

```css
.container {
  flex-direction: row;
  flex-wrap: wrap; /* items drop to a new line when they overflow */
}
```

| Value | Behavior |
| :--- | :--- |
| `nowrap` *(default)* | All items squeeze onto one line |
| `wrap` | Items overflow onto new lines along the cross axis |
| `wrap-reverse` | Same, but new lines grow in the opposite cross direction |

> [!NOTE]
> Change `flex-direction` and the axes swap: in `column`, "horizontal centering" becomes
> vertical, and `wrap` drops items into new *columns* instead of rows. Every flexbox
> property from here on is axis-relative, not page-relative.

---

## 63. justify-content: Distributing the Main Axis

`justify-content` distributes items **along the main axis**, handling the leftover space
when items do not fill the container:

```css
.container {
  display: flex;
  justify-content: space-between;
}
```

| Value | Effect |
| :--- | :--- |
| `flex-start` *(default)* | Packed at the start |
| `center` | Packed in the middle |
| `flex-end` | Packed at the end |
| `space-between` | Even gaps; first and last item touch the edges |
| `space-around` | Even space around each item (edges get half gaps) |
| `space-evenly` | Fully even spacing everywhere |

### Nav Bar Pattern

```css
nav {
  display: flex;
  justify-content: space-between; /* logo left, actions right */
  align-items: center;
  padding: 16px 32px;
  background: #1b1b2f;
  color: white;
}
```

One declaration and the brand sits at one end, the buttons at the other — no
`position` tricks, no calculated margins.

> [!IMPORTANT]
> `justify-content` needs **free space** to distribute. In a fixed-width container full of
> fixed-width items there is nothing left to space out. When `space-between` seems to do
> nothing, check who owns the leftover width — it is usually the container's, not an
> infinite `width` on the items.

---

## 64. gap, align-items & align-self: The Cross Axis

### gap: channels between items

`gap` reserves uniform space between flex items — no margins, no first/last exceptions:

```css
.container {
  display: flex;
  gap: 24px; /* also: gap: 16px 24px for row/column values */
}
```

### align-items: cross-axis alignment for all

```css
.container {
  display: flex;
  align-items: center; /* defaults to stretch */
}
```

| Value | Cross-axis behavior |
| :--- | :--- |
| `stretch` *(default)* | Items fill the container height |
| `center` | Items hug the middle of the cross axis |
| `flex-start` / `flex-end` | Items hug start / end |

### The perfect centering recipe

```css
.container {
  display: flex;
  justify-content: center; /* main axis */
  align-items: center;     /* cross axis */
}
```

Both axes centered, in two lines — the single most-used flexbox pattern in the wild.

### align-self: one rebel item

`align-self` overrides `align-items` for a single item:

```css
.item-special {
  align-self: flex-end; /* this one hugs the bottom; the rest follow the container */
}
```

> [!TIP]
> In a `row` container, `justify-content` centers horizontally and `align-items` centers
> vertically. Flip to `column` and they trade places — the same two properties, newly
> assigned axes.

---

## 65. Letting Items Grow: flex-basis, flex-grow & flex-shrink

Three properties decide how items size along the main axis — usually written as one
shorthand:

| Property | Role | Typical value |
| :--- | :--- | :--- |
| `flex-basis` | Starting size before distribution | `auto`, `200px`, `30%` |
| `flex-grow` | How much of the *free space* an item claims | `0` (default), `1`, `2` |
| `flex-shrink` | How fast an item gives space back when the line is tight | `1` (default) |

```css
.sidebar { flex: 0 0 240px; } /* fixed: no grow, no shrink, always 240px */
.main    { flex: 1; }         /* grow 1: absorbs all leftover free space */
```

`flex: 1` is short for `flex: 1 1 0%` — start at zero, claim equal shares of every free
pixel. Two `flex: 1` siblings split the row 50/50 no matter the viewport; the classic
sidebar-plus-content layout is just this.

> [!IMPORTANT]
> `flex-grow` distributes **free space**, not exact proportions. With
> `flex: 1` and `flex: 2`, the second item gets *twice the extra space*, not twice the
> width — unless the basis is `0%`, in which case grow *does* behave like ratio.

---

## 66. Champion Card Collection

### Checkpoint: Chapter Recap

- `display: flex` on the parent turns children into flex items on a shared axis.
- `flex-direction` picks the main axis; `flex-wrap` lets items overflow to new lines.
- `justify-content` spaces the main axis; `align-items`/`align-self` handle the cross axis.
- `gap` reserves uniform space; `flex` shorthand controls basis, grow and shrink.

### Project: The Champion Card Collection

A collector's gallery of Emberfall champions: a flex nav, a centered hero row, a wrapping
grid of cards that flip on click (3D flip in pure CSS, one line of JS).

#### HTML (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Champion Card Collection</title>
</head>
<body>
  <nav>
    <span id="logo">⚔️ Emberfall Champions</span>
    <div id="nav-links">
      <a href="#">Collection</a>
      <a href="#">Duels</a>
      <a href="#" class="btn-battle">Battle</a>
    </div>
  </nav>

  <header class="hero">
    <h1>Collect. Flip. Master.</h1>
    <p>Every champion of Emberfall lives in this deck — click a card to flip it.</p>
  </header>

  <main class="collection">
    <div class="card">
      <div class="card-inner">
        <div class="card-face card-front">
          <img src="https://placehold.co/180x200/ff6b35/fff?text=Ember+Warden" alt="Ember Warden" />
          <p><b>Ember Warden</b></p>
        </div>
        <div class="card-face card-back-face">
          <p>🔥 +20 Fire DMG</p>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-inner">
        <div class="card-face card-front">
          <img src="https://placehold.co/180x200/2DD4BF/1b1b2f?text=Tide+Oracle" alt="Tide Oracle" />
          <p><b>Tide Oracle</b></p>
        </div>
        <div class="card-face card-back-face">
          <p>🌊 Heals 15 HP</p>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-inner">
        <div class="card-face card-front">
          <img src="https://placehold.co/180x200/7C5CFF/fff?text=Shadow+Trickster" alt="Shadow Trickster" />
          <p><b>Shadow Trickster</b></p>
        </div>
        <div class="card-face card-back-face">
          <p>🃏 Steals 1 card</p>
        </div>
      </div>
    </div>
  </main>

  <script src="script.js"></script>
</body>
</html>
```

#### CSS (`styles.css`)

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}

/* Nav: space-between pushes logo and links apart */
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 32px;
  background: #1b1b2f;
  color: white;
}

#nav-links {
  display: flex;
  gap: 20px;
  align-items: center;
}

.btn-battle {
  background: #ff6b35;
  color: white;
  padding: 8px 16px;
  border-radius: 5px;
}

/* Hero: both axes centered */
.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 48px;
  text-align: center;
}

/* Collection: wrapping grid with uniform channels */
.collection {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 24px;
  padding: 24px;
}

/* 3D flip card */
.card {
  width: 180px;
  height: 260px;
  perspective: 1000px; /* depth for the 3D rotation */
}

.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.6s;
}

.card.flipped .card-inner {
  transform: rotateY(180deg);
}

.card-face {
  position: absolute;
  inset: 0;
  backface-visibility: hidden; /* hide whichever face is turned away */
  border: 2px solid #333;
  border-radius: 8px;
  text-align: center;
  padding: 8px;
}

.card-front {
  background: #f5f5f5;
}

.card-back-face {
  transform: rotateY(180deg);
  background: #1b1b2f;
  color: white;
}
```

#### JS (`script.js`)

```js
// Click any card to flip it: add/remove the 'flipped' class
const cards = document.querySelectorAll('.card');

cards.forEach(card => {
  card.addEventListener('click', () => {
    card.classList.toggle('flipped');
  });
});
```

Read the page through flexbox eyes: the nav uses `space-between` + `align-items`; the hero
centers both axes; the collection is a `wrap` grid distributed with `center` and `gap`;
and the flip itself is a flex item pirouetting in 3D with `perspective` and
`preserve-3d`. Every layout question this module opened — how do boxes sit, space, stack
and overlap — now has a flexbox answer. The deck is complete.

> [!TIP]
> **Game dev version**
> Swap champions for items: filter buttons in a `space-between` toolbar, a `wrap` grid of
> loot icons, and flip cards for tooltips. Flexbox is the inventory screen of the web —
> and the boss of this module. GG.

---

## XP Earned: Key Takeaways

- 📐 `display: flex` on the parent; children become items on a shared axis.
- 🧭 `flex-direction` chooses the main axis; `wrap` handles overflow lines.
- ⚖️ `justify-content` spaces the main axis; `align-items`/`align-self` the cross axis.
- 🔗 `gap` = uniform channels; `flex: 1` = grow and share free space.
- 🃏 Card grids, nav bars, hero centering — one container to rule them all.

---

## Loot Table: Real-World Use Cases

- 🧭 Nav bars and toolbar layouts with `space-between`
- 🎯 Hero sections centered on both axes
- 🃏 Card galleries, dashboards and inventory grids with `wrap` + `gap`
- 📐 Sidebar + content shells with `flex: 1`

---

## 🎮 Side Quests: Practice Exercises

1. Build a `space-between` nav and watch `gap` replace all your margin hacks.
2. Center a box with `justify-content: center` + `align-items: center`; flip the container to `column` and explain the swap.
3. Make two `flex: 1` columns, then change one to `flex: 2` and measure the split.
4. Turn a row of five fixed cards into a responsive `wrap` gallery with `gap: 16px`.
5. **Boss fight:** build a full battle screen — fixed sidebar (`flex: 0 0 200px`),
   centered play field, `wrap` hand of champion cards with flip-on-click and a
   `space-between` HUD bar at the top.

---

## 🔗 See Also

- [[11 - Display & Positioning]] — the flow rules flex replaces
- [[10 - Spacing & Box Sizing]] — sizing and `box-sizing` that flex items inherit
- [[00c - CSS Cheatsheet II]] — every flex property on one page
- [[00b - CSS Cheatsheet]] — the complete CSS reference card

---