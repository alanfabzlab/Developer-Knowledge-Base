# 10. Spacing & Box Sizing

**Spanish version:** [10 - Espaciado y Box Sizing.md](10%20-%20Espaciado%20y%20Box%20Sizing.md)

**Course:** CSS
**Topic:** The `padding` Property, The `margin` Property, Centering with `margin: auto`, `box-sizing: content-box` vs `border-box`, the Universal Reset & the Guild Archive Capstone
**Tags:** `#css` `#web-development` `#box-model` `#spacing` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-F7DF1E?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Lessons-47_--_53-7C5CFF?style=for-the-badge" alt="Lessons 47 to 53">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Borders were the frame; now the room itself: **padding** (air *inside*), **margin** (space
*outside*), the sacred `margin: auto` centering trick, and `box-sizing` — the property that
decides whether a 100px box stays 100px once you add padding. The chapter closes with the
Guild Archive, a full page built on nothing but the box model. Reference:
[[00c - CSS Cheatsheet II]].

> [!NOTE]
> **The whole chapter in one sentence**
> Padding pushes content in, margin pushes neighbors out, `margin: auto` centers, and
> `box-sizing: border-box` keeps your declared sizes honest when padding joins the party.

---

## 47. The Padding Box

Padding is the space between an element's content and its border — **inside** the element.

### Longhand Syntax

Each side can be set individually:

```css
padding-top: 5px;
padding-right: 10px;
padding-bottom: 15px;
padding-left: 20px;
```

### Shorthand Syntax

The `padding` property accepts up to four values in **clockwise order — Top → Right →
Bottom → Left**:

```css
/* Top: 5px, Right: 10px, Bottom: 15px, Left: 20px */
padding: 5px 10px 15px 20px;
```

Common variations:

```css
/* 40px on all four sides */
padding: 40px;

/* 50px top, right and left; nothing at the bottom */
padding: 50px 50px 0px 50px;
```

> [!TIP]
> Memorize the clock: *12 → 3 → 6 → 9*. Every ordering question — padding, margin,
> border sides — answers from that dial.

---

## 48. The Margin Box

The **margin box** is the outermost layer of the box model. It surrounds the border and
creates separation between adjacent elements.

Like padding, margins are declared with directional longhands (`margin-top`,
`margin-right`, `margin-bottom`, `margin-left`) or the `margin` shorthand in the same
clockwise sequence:

```css
/* Top: 20px, Right: 10px, Bottom: 20px, Left: 10px */
margin: 20px 10px 20px 10px;
```

```css
/* 40px on all four sides */
margin: 40px;

/* 15px top/bottom, 0px left/right */
margin: 15px 0;
```

> [!NOTE]
> Margins accept **negative values** — pull an element toward its neighbor, or overlap
> two boxes on purpose. Padding cannot go negative; that is the one real difference
> besides whose space each one takes.

---

## 49. Centering With `margin: auto`

To center a block-level element **horizontally** inside its container, pair
`margin: auto` with an explicit `width`:

```css
#container-element {
  width: 300px;
  height: 300px;
  border: 3px solid;
}

#inner-element {
  width: 100px;
  height: 100px;
  border: 1px solid;
  background-color: orange;
  margin: auto; /* Centers horizontally within the container */
}
```

The browser splits the leftover horizontal space equally between the two margins, and the
box floats to the middle.

> [!IMPORTANT]
> `margin: auto` without a `width` does nothing visible: a block element already stretches
> to fill 100% of the parent, so there is no leftover space for the auto margins to
> distribute. Width first, then center.

---

## 50. Box Sizing: `content-box` vs `border-box`

The `box-sizing` property controls how an element's total width and height are computed.

| Property value | Formula | Behavior |
| :--- | :--- | :--- |
| `content-box` *(default)* | Total width = content + padding + border | Adding padding or borders grows the element beyond its declared width |
| `border-box` | Total width = declared size; padding and border are absorbed inside it | The box keeps its declared size; content shrinks to make room |

### Comparison

Declared `width: 150px`, `padding: 20px`, `border: 2px`:

- **`content-box`**: rendered width = 150 + (20 × 2) + (2 × 2) = **194px**.
- **`border-box`**: rendered width stays **150px**; the content area narrows to
  150 − 40 − 4 = **106px**.

```css
/* Default: padding adds to the width */
.box { width: 150px; padding: 20px; }

/* Border-box: padding is wrapped inside the 150px */
.border-box { width: 150px; padding: 20px; box-sizing: border-box; }
```

> [!WARNING]
> **Layout breakage 101**
> Two `content-box` columns that both claim `width: 50%` overflow their parent the moment
> padding is added. `border-box` is the answer used by virtually every modern framework —
> which is why the reset below makes it the default.

---

## 51. The Universal Reset

A standard practice in modern CSS is applying a **universal box model reset** at the top of
the stylesheet using the universal selector `*`:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```

Every element starts at zero spacing with honest sizing — so the spacing you write later is
the only spacing that exists. No surprise browser defaults, no 8px body margin inherited
from nowhere.

> [!NOTE]
> `*` targets every element — descendants included — so the reset runs before any rule you
> write. Keep it as the first rule of a file and every box starts from the same blank slate.

---

## 52. Quest: Feed Spacing

Take the framed feed from [[09 - Box Model & Borders]] and give it the full spacing pass.

#### CSS (`styles.css`)

```css
* {
  font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}

div {
  border: 2px solid grey;
}

#post-list {
  padding-right: 40px;
}

#post-list > li {
  list-style-type: none;
}

li > div {
  text-align: left;
}

#top-img {
  width: 10em;
  height: 10em;
  border: 12px solid green;
  border-radius: 50%;
}

#outside-wrapper {
  width: 90%;
  background-color: rgb(169, 206, 221);
  text-align: center;
}

.post-wrapper {
  text-align: left;
  background-color: #f5f5f5;
  border-radius: 5px;
  padding: 50px 50px 0px 50px; /* air inside the post card */
}

.post-img {
  width: 100%;
  border-radius: 5px;
}
```

Watch how each rule touches a different layer of the box model: `#post-list` gains padding,
`.post-wrapper` gains inner padding, and the styled list markers disappear so the cards sit
clean — spacing, not borders, turned a framed list into a feed.

> [!TIP]
> The `padding: 50px 50px 0px 50px` oddity is deliberate: the card breathes on three sides
> and lets the next divider touch the bottom edge. Clockwise shorthand, deliberate
> asymmetry — this is the whole art of spacing in one declaration.

---

## 53. Guild Archive

### Checkpoint: Chapter Recap

- Padding = air inside; margin = space outside; both follow the clockwise shorthand.
- `margin: auto` centers horizontally — with an explicit `width`.
- `box-sizing: border-box` keeps declared sizes honest; `content-box` grows with padding.
- The universal reset zeroes margins, padding and forces `border-box` everywhere.

### Project: The Guild Archive

A guild library homepage: navigation, welcome text, a catalog search and seasonal staff
picks. Pure HTML5 semantic structure + one stylesheet that is *only* box model rules.

#### HTML (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Guild Archive</title>
</head>
<body>
  <header>
    <nav>
      <h1>Welcome to the Guild Archive!</h1>
      <a class="nav-item" href="#welcome">Home</a>
      <a class="nav-item" href="#catalog-form">Search</a>
      <a class="nav-item" href="#staff-picks">Staff Picks</a>
    </nav>
  </header>
  <main>
    <section id="welcome">
      <p>Guided by our dedication to lore and learning, the Archive keeps every tome,
      map and bestiary entry of Emberfall safe under one roof.</p>
    </section>
    <section id="catalog">
      <form id="catalog-form">
        <input id="catalog-input" type="text" placeholder="Search the Catalog..." />
        <input id="form-btn" type="submit" value="Search" />
      </form>
    </section>
    <section id="staff-picks">
      <h2>Staff Picks</h2>
      <div class="staff-pick-row">
        <img class="staff-pick-img" src="https://placehold.co/160x240" alt="Tome cover: Lanterns of the Deep Halls" />
        <img class="staff-pick-img" src="https://placehold.co/160x240" alt="Tome cover: A Field Guide to Cinder Slimes" />
        <img class="staff-pick-img" src="https://placehold.co/160x240" alt="Tome cover: The Ninth Floor Codex" />
      </div>
    </section>
  </main>
</body>
</html>
```

#### CSS (`styles.css`)

```css
/* Universal Reset & Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  width: 100%;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  text-align: center;
}

header {
  background-image: url("https://placehold.co/1200x200/1b1b2f/ff6b35?text=Guild+Archive");
  background-size: cover;
  background-repeat: no-repeat;
  height: 200px;
}

/* Header & Navigation Rules */
h1 {
  margin-top: 10px;
  margin-bottom: 10px;
}

.nav-item {
  display: inline-block;
  width: 33%;
  border: 1px solid #333;
  border-radius: 5px;
  padding: 5px;
  margin: 10px;
}

/* Layout Structural Margins */
main {
  margin-top: 20px;
}

section {
  margin-top: 10px;
  margin-bottom: 10px;
}

/* Paragraph Content Alignment */
#welcome > p {
  text-align: center;
  margin-left: 5em;
  margin-right: 5em;
}

/* Catalog Search Form Inputs */
#catalog-input, #form-btn {
  text-align: center;
  font-size: 1.25rem;
  font-weight: 800;
  padding: 8px;
}

#catalog-input {
  border: 2px solid #000;
  width: 37.5%;
}

/* Staff Picks Section & Book Cover Images */
#staff-picks {
  text-align: center;
}

.staff-pick-img {
  border: 1px solid #000;
  border-radius: 0 7px 7px 0; /* book-spine effect: rounds the right edge only */
  width: 10em;
  height: 15em;
  margin: 10px;
}
```

Read the numbers as box model moves: `em`-based horizontal margins on the welcome text keep
it readable at any font size; `inline-block` lets the nav links take width, padding and
margins while still sitting on one line; the asymmetric `border-radius` shapes the book
covers with a spine. One stylesheet, one mental model: every rule is a layer in a box.

> [!TIP]
> **Game dev version**
> Swap "Staff Picks" for "Seasonal Drops", the tomes for loot cards, and `Search` for the
> inventory filter — the page is a shop screen. The box model does not care what the
> content is; it only agrees on the boxes.

---

## XP Earned: Key Takeaways

- 🧽 **Padding** = air inside; **margin** = space outside; both go clockwise.
- 🎯 `margin: auto` centers horizontally **with a `width`**.
- 📏 `content-box` grows with padding; `border-box` absorbs it inside the declared size.
- 🧹 The universal reset — `margin: 0; padding: 0; box-sizing: border-box` — starts
  every box equal.
- 🛠️ One stylesheet can be 100% box model rules and ship a whole page.

---

## Loot Table: Real-World Use Cases

- 📚 Archive, newsroom and storefront homepages
- 🔍 Search bars and filter rows with breathing room
- 🎨 Book/album/collection covers with spine-style radius
- 🎮 Shop screens, codex entries and seasonal drop pages

---

## 🎮 Side Quests: Practice Exercises

1. Write `padding` for 10px all sides, then for 10px/20px/30px/40px — say the clock order out loud.
2. Center a 200px box in a full-width parent with `margin: auto`; remove the width and explain the jump.
3. Compare a 150px `content-box` and 150px `border-box` panel, both with 20px padding.
4. Reset a page with the universal rule and list every layout that changes.
5. **Boss fight:** style a `guild-members.html` page — welcome section, search form and a
   three-card front row — using only box model properties, no positioning.

---

## 🔗 See Also

- [[09 - Box Model & Borders]] — the four layers these properties live in
- [[11 - Display & Positioning]] — how boxes flow on the page
- [[00c - CSS Cheatsheet II]] — spacing and sizing on one page
- [[08 - Backgrounds & Shorthands]] — the border shorthand this page stacks on

---