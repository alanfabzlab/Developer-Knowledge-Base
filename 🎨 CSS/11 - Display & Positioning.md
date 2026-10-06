# 11. Display & Positioning

**Spanish version:** [11 - Display y Posicionamiento.md](11%20-%20Display%20y%20Posicionamiento.md)

**Course:** CSS
**Topic:** `display: block` vs `inline` vs `inline-block`, Normal Flow, `position: static`, `relative`, `absolute`, `fixed`, `sticky`, `z-index` & the Academy Capstone
**Tags:** `#css` `#web-development` `#layout` `#positioning` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-F7DF1E?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Lessons-54_--_60-7C5CFF?style=for-the-badge" alt="Lessons 54 to 60">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Two boxes on a page can sit, slide, pin or overlap — this chapter is the control room.
**Display** decides how a box behaves among its siblings; **position** decides where the
box sits — in the normal flow, nudged, pinned to an ancestor, glued to the viewport or
stuck mid-scroll. The capstone assembles all five `position` values plus `z-index` into
an academy page. Reference: [[00c - CSS Cheatsheet II]].

> [!NOTE]
> **The whole chapter in one sentence**
> `static` flows, `relative` nudges, `absolute` anchors, `fixed` pins to the viewport,
> `sticky` flows then pins — and `z-index` decides who wins when two boxes collide.

---

## 54. Display: Block, Inline & Inline-Block

Every HTML element carries a default `display` value. The three stars:

| Display | Flow behavior | Width behavior | Examples |
| :--- | :--- | :--- | :--- |
| `block` | Own line, stacks vertically | Fills parent width by default, accepts `width`/`height` | `<div>`, `<h1>`, `<p>`, `<section>` |
| `inline` | Sits on the same line as siblings | Hugs content; no `width`/`height` effect | `<span>`, `<a>`, `<em>`, `<b>` |
| `inline-block` | Same line as siblings | Accepts `width`/`height` and margins | Icons, nav pills, buttons |

```css
/* Block-ish links that still share a line and obey sizing */
a {
  display: inline-block;
  width: 120px;
  padding: 8px;
  border: 1px solid #333;
}
```

> [!TIP]
> The Guild Archive nav from [[10 - Spacing & Box Sizing]] did exactly this: three
> `inline-block` links that take padding, width and margins while standing in a row.

---

## 55. Normal Flow & `position: static`

Inside every HTML document the browser lays elements out in a predictable cascade called
**normal flow**: block-level siblings stack top to bottom, inline content fills line by
line, left to right.

`position: static` is the default — the box takes its natural place, in flow, and
ignores the offset properties `top`, `right`, `bottom` and `left`:

```css
div {
  position: static; /* default; offsets have no effect */
}
```

> [!NOTE]
> Never write `position: static` in real stylesheets — it is already the default. It
> appears in tutorials as the *baseline*: every other value starts from here and
> overrides the normal flow in its own way.

---

## 56. `position: relative`

`relative` keeps the box **in normal flow** — its original space is preserved — but lets
the offset properties nudge it from where it would have been:

```css
#div-1 {
  position: relative;
  left: 50px;  /* shifted right by 50px from its normal spot */
  top: 10px;   /* shifted down by 10px */
}
```

Think of it as: *render me in my usual slot, then push me around* — the empty slot still
belongs to the box, so neighbors do not move to fill it.

> [!IMPORTANT]
> `relative` is also the trick companion of `absolute`: a positioned ancestor. Elements
> with `position: relative` (and no offsets) are the most common way to give an `absolute`
> child an anchor, as lesson 57 shows.

---

## 57. `position: absolute`

`absolute` **removes the box from normal flow** — the space it occupied collapses and
siblings move in — then pins it to the nearest **positioned ancestor**: the closest
ancestor whose `position` is anything but `static`. With no such ancestor, it anchors to
the initial containing block (the viewport at document start).

```css
/* The card becomes the containing block */
.card {
  position: relative;
}

/* The badge sticks to the card's top-right corner */
.badge {
  position: absolute;
  top: 10px;
  right: 10px;
}
```

The classic pattern: `position: relative` on the parent, `position: absolute` on the
child, `top`/`right` coordinates that answer *"10px from the parent's top edge, 10px from
its right edge"*.

> [!WARNING]
> An `absolute` box with **no positioned ancestor** anchors to the page itself — and other
> content does not reserve its space. Always check: if an absolute element "flies" to the
> corner of the document, the nearest positioned ancestor is missing.

---

## 58. `position: fixed`

`fixed` pins the box **relative to the viewport**: it stays glued to the same screen
position while the rest of the page scrolls beneath it. Like `absolute`, it leaves normal
flow.

```css
/* Stays visible in the corner no matter how far you scroll */
#back-to-top {
  position: fixed;
  right: 20px;
  bottom: 20px;
}
```

Classic uses: back-to-top buttons, chat widgets, navbars that never leave the screen.

> [!TIP]
> Distinguish `fixed` from `absolute`: `fixed` answers to the **viewport**, `absolute` to
> its **positioned ancestor**. Scroll the page and the `fixed` element stays put; the
> `absolute` one scrolls away with its container.

---

## 59. `position: sticky` & `z-index`

### Sticky: flow first, pin later

`sticky` lives in normal flow until it crosses a scroll threshold, then behaves like
`fixed` — **within the bounds of its parent**. It is relative to its normal position
until `top`/`bottom` is reached; past that, it pins until the parent scrolls out of view.

```css
.sticky-header {
  position: sticky;
  top: 0; /* pins to the top of the viewport once scrolled to */
}
```

### z-index: the stacking order

Positioned boxes can overlap; `z-index` sets which one wins. Higher values stack on top:

```css
.box-a { position: absolute; z-index: 1; }
.box-b { position: absolute; z-index: 10; } /* renders above box-a */
```

| z-index value | Meaning |
| :--- | :--- |
| `auto` | Default; stacking decided by document order |
| `0`..`n` | Explicit layer; larger number paints above smaller ones |
| Negative | Paints below the normal content of the page |

> [!IMPORTANT]
> `z-index` only works on **positioned** elements — `static` boxes ignore it, since they
> can never be stacked out of flow. If a `z-index` stubbornly does nothing, check that
> the element (or a flex/grid item) is actually positioned.

---

## 60. The Academy Layout

### Checkpoint: Chapter Recap

- `block` stacks and fills; `inline` hugs one line; `inline-block` hugs but sizes.
- `static` = normal flow; `relative` nudges but keeps its slot.
- `absolute` leaves flow and anchors to the nearest positioned ancestor.
- `fixed` pins to the viewport; `sticky` flows until its threshold, then pins inside its parent.
- `z-index` orders overlapping positioned elements.

### Project: Emberfall Academy

A scrolling academy page that uses every positioning tool: a notification bell anchored
to the header, a sticky section heading, a fixed "back to top" link, and overlapping
lesson cards that stack with `z-index`.

#### HTML (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Emberfall Academy</title>
</head>
<body>
  <div id="top-banner">
    <h1>Welcome to the Emberfall Academy!</h1>
    <div id="notification-bell">
      🔔
      <span id="notif-count">3</span>
    </div>
  </div>

  <main id="curriculum">
    <section class="lesson">
      <h2 class="lesson-header">Lore & Linguistics</h2>
      <p>Rune morphology, dialects of the Ashlands, and the forbidden syllabary of
      the Cinder Court.</p>
    </section>
    <section class="lesson">
      <h2 class="lesson-header">Combat Tactics</h2>
      <p>Formation drills, aggro management in the Deep Halls, and field-first-aid
      for party wipes.</p>
    </section>
    <section class="lesson">
      <h2 class="lesson-header">Enchanting Practicum</h2>
      <p>Rune circles, mana budgets, and when not to put fire runes on a torch.</p>
    </section>
  </main>

  <div class="overlap-banner">
    <div class="card card-back">Syllabus</div>
    <div class="card card-front">Timetable</div>
  </div>

  <footer>
    <a id="back-to-top" href="#top-banner">↑ Back to Top</a>
  </footer>
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

/* An anchor so the absolutes land on the header, not the page */
#top-banner {
  position: relative;
  background-color: #1b1b2f;
  color: white;
  padding: 20px;
}

#notification-bell {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 1.5rem;
}

#notif-count {
  position: absolute;
  top: -5px;
  right: 5px;
  background: #ff6b35;
  border-radius: 50%;
  font-size: 0.8rem;
  padding: 2px 6px;
}

/* Sticky lesson headers pin while their section scrolls */
.lesson-header {
  position: sticky;
  top: 0;
  background: #1572B6;
  color: white;
  padding: 8px 16px;
}

main {
  padding: 20px;
}

.lesson {
  margin-bottom: 30px;
}

/* Overlapping cards: z-index decides the winner */
.overlap-banner {
  position: relative;
  height: 120px;
  margin: 20px;
}

.card {
  position: absolute;
  width: 180px;
  padding: 16px;
  background: #2DD4BF;
  text-align: center;
}

.card-back {
  left: 60px;
  top: 10px;
  z-index: 1;
}

.card-front {
  left: 40px;
  top: 40px;
  z-index: 10;
}

/* Fixed forever-visible footer link */
#back-to-top {
  position: fixed;
  right: 20px;
  bottom: 20px;
  background: #7C5CFF;
  color: white;
  padding: 10px 14px;
  text-decoration: none;
  border-radius: 5px;
}
```

Read the page as a stack of positions: the bell and its counter are `absolute` inside the
`relative` header; the counters in that corner survive any header edits; `sticky` section
heads travel with the scroll inside their section only; the two cards overlap with
`z-index` 1 vs 10; the back-to-top button is `fixed` to the viewport and never leaves.

> [!TIP]
> **Game dev version**
> This is a HUD: the bell is the quest tracker, the cards are the minimap and buff icons,
> the sticky headers are the in-world floating labels, and the back-to-top link is the
> pause-menu button pinned to the corner. Screen UI runs on `position` rules.

---

## XP Earned: Key Takeaways

- 🧱 `block` stacks, `inline` hugs, `inline-block` does both.
- 🗺️ `static` flows; `relative` shifts in place; `absolute` leaves flow and anchors.
- 📌 `fixed` pins to the viewport; `sticky` pins only inside its parent after its threshold.
- 🥇 `z-index` decides overlap order — on positioned elements only.
- 🎓 Every HUD pattern — badges, floating labels, persistent buttons — is a position value.

---

## Loot Table: Real-World Use Cases

- 🔔 Notification badges and corner buttons anchored to headers
- 📌 Floating back-to-top buttons and chat widgets
- 🧭 Sticky table headers and section titles that survive scroll
- 🃏 Overlapping cards, tooltips and toasts governed by `z-index`

---

## 🎮 Side Quests: Practice Exercises

1. Turn three `<a>` links into `inline-block` nav pills and compare with `block` and `inline`.
2. Nudge a box with `relative` offsets and confirm its original space stays reserved.
3. Place a badge `absolute` inside a `relative` card; then remove `relative` and watch it fly.
4. Make a `fixed` corner button, then a `sticky` section header, and scroll both.
5. **Boss fight:** build a raid screen — health bar pinned to the top, buff icons
   overlapping with z-index, a `sticky` boss-name label, and a `fixed` "Abandon Raid"
   button in the corner.

---

## 🔗 See Also

- [[12 - Flexbox]] — the modern way to distribute boxes along an axis
- [[10 - Spacing & Box Sizing]] — spacing rules these positions offset
- [[09 - Box Model & Borders]] — the layers every positioned box carries
- [[00c - CSS Cheatsheet II]] — display and position values on one page

---