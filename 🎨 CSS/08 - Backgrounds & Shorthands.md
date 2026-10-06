# 08. Backgrounds & Shorthands

**Spanish version:** [08 - Fondos y Shorthands.md](08%20-%20Fondos%20y%20Shorthands.md)

**Course:** CSS
**Topic:** `text-decoration` in Depth, `background-color`, `background-image`, `background-size` & `background-repeat`, the `border` and `font` Shorthands & the Invitation Capstone
**Tags:** `#css` `#web-development` `#backgrounds` `#shorthand` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-F7DF1E?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Lessons-36_--_41-7C5CFF?style=for-the-badge" alt="Lessons 36 to 41">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Two halves: the **decorations** — full `text-decoration` control and background
properties — and the **shorthands** — `border` and `font` as one-line declarations that
collapse four lines of CSS into one. The chapter caps with an invitation screen: an
Emberfall launch party invite styled with exactly those tools. Reference:
[[00b - CSS Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> Shorthands are CSS's way of saying "you already know the longhand" — one declaration
> (`border: 3px dashed #f00`) that packs four, as long as you respect the order and the
> required values.

---

## 36. Decoration, In Depth

`text-decoration` controls decorative lines added to text elements, and it accepts **four
sub-values** — or the shorthand that combines them:

| Sub-value | Options |
| :--- | :--- |
| **Line** | `underline`, `overline`, `line-through` |
| **Style** | `solid`, `wavy`, `dotted`, `dashed`, `double` |
| **Color** | Named, Hex or RGB values |
| **Thickness** | Pixels, e.g. `2px` |

```css
/* Custom underline for spellcheck-style error indicators */
span {
  text-decoration: underline wavy red 2px;
}
```

Read it left to right: *line, style, color, thickness*. Any of them may be omitted — the
shorthand remembers only what you give it.

> [!NOTE]
> Partials work: `text-decoration: underline` is perfectly valid and is the plainest of
> the family. The shorthand is not "all four or nothing".

---

## 37. Backgrounds

### `background-color`

Applies a solid background color. It accepts the same three notations as `color`:

```css
div {
  background-color: red;            /* Named color */
  background-color: rgb(0, 0, 255); /* RGB function */
  background-color: #ffff00;        /* Hexadecimal */
}
```

### `background-image` & Display Rules

Images can be set as element backgrounds with the `url()` function:

```css
#inner {
  width: 400px;
  height: 400px;
  background-image: url("https://images.unsplash.com/photo-...");
  background-size: cover;
  background-repeat: no-repeat;
}
```

| Property | Values | Effect |
| :--- | :--- | :--- |
| `background-size` | `contain` / `cover` | `contain` fits the whole image inside; `cover` fills the box and crops the overflow |
| `background-repeat` | `no-repeat` / `repeat` | `no-repeat` draws the image once; `repeat` tiles it |

> [!WARNING]
> The default `repeat` is why a background image suddenly tiles across the page. For a
> single backdrop you almost always want both `cover` **and** `no-repeat`.

---

## 38. The `border` Shorthand

The `border` property is a shorthand that combines **width, style and color** in one
declaration.

### Longhand vs. Shorthand

```css
/* Longhand */
span {
  border-width: 3px;
  border-style: dashed;
  border-color: #ff0000;
}

/* Shorthand — the same rule, one line */
span {
  border: 3px dashed #ff0000;
}
```

| Piece | What it does |
| :--- | :--- |
| `border-width` | Thickness, in units like `px` |
| `border-style` | `solid`, `dashed`, `dotted`, `double`, `groove`, `ridge`… |
| `border-color` | Named, `rgb()` or Hex |

> [!IMPORTANT]
> `border` needs a **style** to render: `border: 3px red;` with no style is invisible,
> because the default style is `none`. Width and color without a style are ghosts.

---

## 39. The `font` Shorthand

The `font` property declares multiple typography settings in one line.

### Syntax Rules

- **Required values:** `font-size` and `font-family` — the shorthand refuses to exist
  without them.
- **Order rule:** optional values like `font-weight` must come **before** `font-size`.
- **Fallback font:** always end with a generic family (`sans-serif`, `cursive`…).

### Longhand vs. Shorthand

```css
/* Longhand */
span {
  font-family: Georgia, serif;
  font-weight: 800;
  font-size: 12px;
}

/* Shorthand — weight first, then size, then family */
span {
  font: 800 12px Georgia, serif;
}
```

> [!CAUTION]
> **Browser compatibility**
> Some shorthand sub-values behave inconsistently across browsers — Safari in particular
> has its own ideas about certain `text-decoration` values. Shorthands save lines; they
> do not forgive. Test the exotic ones on every platform you ship.

### Practical: Borders and Fonts Together

```css
h1 {
  border: 2px solid black;
}

p {
  font: bold 18px Arial, sans-serif;
}
```

Note `bold` is a keyword weight standing in for `700`, sitting in the *weight* slot before
`18px` — the order rule at work.

---

## 40. Nested Containers

Backgrounds and shorthands shine when elements sit inside elements. Consider a scroll
frame and its inner artwork:

### HTML

```html
<div id="outer">
  <div id="inner"></div>
</div>
```

### CSS

```css
#outer {
  width: 500px;
  height: 500px;
  background-color: lightskyblue;
}

#inner {
  width: 400px;
  height: 400px;
  background-image: url("https://images.unsplash.com/photo-...");
  background-size: cover;
  background-repeat: no-repeat;
}
```

`#inner` is 400px. Its background is painted with `cover`, so the artwork fills the whole
box and crops whatever does not fit — on a window half the size, the same code still fills
the box. The container (#outer) stays a quiet backdrop color.

> [!NOTE]
> This two-box pattern is every avatar-over-banner, icon-over-frame and vignette-over-
> screenshot in game UI. Pick the outer color, then decide how the inner image must fit.

---

## 41. Party Invitation

### Checkpoint: Chapter Recap

- `text-decoration`: line + style + color + thickness, in one declaration.
- Backgrounds: `background-color` for solid fills; `background-image` + `size` +
  `repeat` for artwork.
- `border: width style color` and `font: weight size family` collapse longhands.

### Project: You're Invited

A styled invitation for the Emberfall launch party. The HTML is pure structure — every
ounce of style comes from the two shorthands you just learned.

#### HTML (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Invitation</title>
</head>
<body>
  <div id="invite-wrapper">
    <h1>You're Invited!</h1>
    <div id="invite-text">
      <p>
        Come join us for a night of embers, laughter and good company at the most
        anticipated launch party of the year! We're thrilled to invite you to our
        exclusive soirée, where the Cinderlight Fest acts reunite and the studio shows
        the first playable build of the Deep Halls expansion.
      </p>
      <p>
        Expect live music by The Ashen Choir, signature cinder cocktails and a first look
        at the artbook. Dress code is adventuring casual — come as your favorite
        character class.
      </p>
      <p>We can't wait to see you there!</p>
    </div>
    <p id="itinerary">
      Date: <br />
      Time: <br />
      Location: <br />
      RSVP by <span>October 15, 2026</span> to let us know you'll be joining!
    </p>
    <p>Sincerely,</p>
    <span>Alan</span>
  </div>
</body>
</html>
```

#### CSS (`styles.css`)

```css
#invite-wrapper {
  width: 50%;
  padding: 25px;
  background-color: #2b2b36;
  color: #ffffff;
  border: 2px solid #ff6b35;
  border-radius: 8px;
  margin: auto;
}

h1 {
  font-family: Arial, sans-serif;
  text-align: center;
}

#invite-text {
  width: 85%;
}

#itinerary {
  text-align: center;
}
```

> [!TIP]
> **Game dev version**
> The invite wrapper is a quest-start card; `#itinerary` is the objective list. Date,
> time, location and an RSVP deadline — three lines of info, centered — is the exact
> anatomy of a raid sign-up screen. Chapter [[09 - Box Model & Borders]] explains why
> `padding`, `border` and `margin` behave the way they just did.

---

## XP Earned: Key Takeaways

- 📝 `text-decoration: underline wavy red 2px` — line, style, color, thickness.
- 🖼️ `background-color` fills; `background-image` + `size: cover` + `no-repeat` paints.
- 🧱 `border: 3px dashed #ff0000` replaces three longhand lines — but needs a **style**.
- 🔤 `font: 800 12px Georgia, serif` packs weight+size+family — size and family are
  required, and the order is fixed.
- 🧫 Nested boxes: outer color, inner artwork, `cover` decides the crop.

---

## Loot Table: Real-World Use Cases

- 🎨 Backdrops, banners and parallax backgrounds on game pages
- 🏷️ Card frames, button borders and invitation/interstitial screens
- ✉️ Announcement cards with a single `font` line per text role
- 🖼️ Avatar/banner pairs sized with `cover` and one container color

---

## 🎮 Side Quests: Practice Exercises

1. Write the same border as longhand, then shorthand — prove the output matches.
2. Set a background image with `contain`, then `cover`, and describe the crop difference.
3. Give a dialog box `font: 600 1.1rem Georgia, serif` and check the order requirement.
4. Build a second invitation variant with a `dashed` border and a different backdrop.
5. **Boss fight:** rebuild the invitation as a raid-signup card — title, three
   info lines, RSVP by date — using `border`, `font` and background shorthands only.

---

## 🔗 See Also

- [[09 - Box Model & Borders]] — why borders, padding and margins behave as they do
- [[07 - Fonts & Text]] — the longhand behind the `font` shorthand
- [[02 - Colors & Measurements]] — every color notation used here, explained
- [[10 - Spacing & Box Sizing]] — padding and margin, next

---