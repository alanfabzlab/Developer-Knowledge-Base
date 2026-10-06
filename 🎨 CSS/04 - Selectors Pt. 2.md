# 04. Selectors Pt. 2

**Spanish version:** [04 - Selectores Pt. 2.md](04%20-%20Selectores%20Pt.%202.md)

**Course:** CSS
**Topic:** Grouping Selectors, the Child Combinator, Practice Drills & the Festival Flyer Capstone
**Tags:** `#css` `#web-development` `#selectors` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER_TO_INTERMEDIATE-6CC24A?style=for-the-badge" alt="Beginner to intermediate">
  <img src="https://img.shields.io/badge/Lessons-17_--_20-7C5CFF?style=for-the-badge" alt="Lessons 17 to 20">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Two ways to aim smarter: **grouping** writes one rule for many targets instead of copying
it three times, and the **child combinator** reaches inside a parent without dragging every
descendant along. The chapter ends with a full capstone — a festival flyer built from
semantic HTML and nothing but the selectors you now own. Reference:
[[00b - CSS Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> Grouping saves keystrokes; combinators save precision — together they keep a stylesheet
> short enough to read and sharp enough to trust.

---

## 17. Grouping

Grouping applies the same styling rules to **multiple selectors at once**, preventing code
duplication. Selectors are separated by commas.

```css
ul, ol {
  border: 1px solid;
  width: 200px;
}
```

One rule, both lists framed. Without grouping you would write the same two declarations
twice — and then remember them *again* the day you change the border color.

```css
/* Three copies of the same rule — don't */
ul { border: 1px solid; }
ol { border: 1px solid; }
li { border: 1px solid; }
```

---

## 18. Child Combinator

The **child combinator** `>` selects **direct children** inside a parent element, giving
targeted specificity without over-reach.

```css
ul > li {
  text-decoration: underline wavy 3px brown;
}
```

`ul > li` matches an `<li>` whose immediate parent is a `<ul>` — and skips the `<li>`
buried three `<div>`s deeper, which a plain descendant rule would also have caught.

| Pattern | Matches |
| :--- | :--- |
| `ul li` | Every `li` *anywhere* inside the `ul` (descendant) |
| `ul > li` | Only `li` children of the `ul` (direct child) |

> [!TIP]
> The difference matters the moment you nest lists, cards or accordions: descendant rules
> bleed through every layer, child rules stop at the first one. Reach for `>` when the
> deeper elements should keep their own style.

---

## 19. Quest: Realms & Seas

Everything so far, in one document: grouping for shared frames, separate rules for the
palette, child combinators for the decorations.

### HTML (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Realms & Seas</title>
</head>
<body>
  <h2>Realms of Emberfall 🏰</h2>
  <ul>
    <li>Cinderfen</li>
    <li>Ember Wastes</li>
    <li>Deep Halls</li>
    <li>Gloam Marsh</li>
    <li>Northreach</li>
    <li>High Kindle</li>
    <li>Blackstone Vale</li>
  </ul>

  <h2>Dungeons By Depth ⛏️</h2>
  <ol>
    <li>The Cracked Spire</li>
    <li>Flooded Archive</li>
    <li>Lantern Warrens</li>
    <li>The Sunken Kiln</li>
    <li>Ninth Floor</li>
  </ol>
</body>
</html>
```

### CSS (`styles.css`)

```css
/* 1. Grouping: one frame for both lists */
ul, ol {
  border: 1px solid;
  width: 200px;
}

/* 2. Specific palette per list */
ul {
  background-color: lightgreen;
}

ol {
  background-color: skyblue;
  color: white;
}

/* 3. Child combinators for the list items */
ul > li {
  text-decoration: underline wavy 3px brown;
}

ol > li {
  text-decoration: underline dotted 3px indigo;
}
```

Four selector techniques — type, id, grouping and `>` — in twenty lines. That is the whole
vocabulary for the capstone below.

---

## 20. Festival Flyer

### Checkpoint: Selector Recap

- **Type** selectors set page-wide defaults.
- **Class** (`.name`) styles any number of elements; **ID** (`#name`) styles one.
- **Targeting** (`div.line`) chains them for specificity.
- **Grouping** (`h1, h2`) shares one rule across selectors.
- **Child combinator** (`ul > li`) stops at direct children.

### Project: Cinderlight Fest

A one-page flyer for the Emberfall soundtrack launch — semantic HTML (`main`, `header`,
`section`, `footer`) painted only with the selectors above.

#### HTML (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Cinderlight Fest</title>
</head>
<body>
  <main>
    <header>
      <img src="https://placehold.co/600x200/1b1b2f/ff6b35?text=Cinderlight+Fest" alt="Festival banner with the Emberfall skyline" />
      <h1>Cinderlight Fest</h1>
    </header>

    <section id="night-1">
      <h2>The Ashen Choir</h2>
      <h3>Act one · Act two</h3>
      <p>
        <b>
          Opening night belongs to the choir that scored the Deep Halls. Two acts: the
          quiet lantern themes first, then the full Ninth Floor suite with live percussion
          and a choir that has never once missed a cue.
        </b>
      </p>
    </section>

    <section id="night-2">
      <h2>Lil' Spark</h2>
      <h3>Act one · Act two</h3>
      <p>
        <b>
          The chiptune closer. Act one remixes the overworld themes everyone can hum;
          act two drops the new expansion tracks for the first time anywhere, with the
          devs in the front row taking notes.
        </b>
      </p>
    </section>

    <footer>
      <p>Art installations by</p>
      <p><b>The Kiln Collective · Marrow &amp; Co · Studio Nightglass</b></p>
    </footer>
  </main>
</body>
</html>
```

#### CSS (`styles.css`)

```css
main {
  text-align: center;
  font-family: sans-serif;
}

header img {
  width: 100%;
  max-width: 600px;
}

/* Grouping: both nights share the same frame */
#night-1, #night-2 {
  margin: 20px 0;
  padding: 10px;
  border: 1px solid #1572B6;
  border-radius: 5px;
}

footer {
  margin-top: 30px;
  font-size: 0.9em;
}
```

> [!TIP]
> **Game dev version**
> This flyer is the template for every announcement page a game ships: launch date, two
> acts of news, credits in the footer. Swap `#night-1` for patch versions or tournament
> days and the markup does not change — only the ids. Next up, [[05 - Pseudo-elements]]:
> decoration that needs no extra HTML at all.

---

## XP Earned: Key Takeaways

- 📎 **Grouping** = selectors separated by commas, one shared rule.
- 🎯 **`>` child combinator** = direct children only; a plain space matches descendants.
- 🧩 Type + class + id + grouping + `>` cover the majority of real-world selectors.
- 🗞️ A capstone page needs no framework: semantic HTML and five selector types.

---

## Loot Table: Real-World Use Cases

- 📋 Shared table/list/card frames across a whole page
- 🧭 Navigation styles that reach the links but not the dropdowns nested inside
- 🎪 Event, festival and patch-note flyers
- 🏷️ One rule for every `.btn`, one override for `#submit`

---

## 🎮 Side Quests: Practice Exercises

1. Rewrite three identical rules as one grouped rule.
2. Style only the `<a>` tags that are *direct* children of a `<nav>` — then make them
   descendants instead and watch the dropdowns change.
3. Give two sections the same frame with a grouped id selector.
4. Build a `tournament.html` flyer with a grouped `#day-1, #day-2` schedule.
5. **Boss fight:** rebuild the festival flyer with your own event, using every selector
   family from chapters 03 and 04 at least once.

---

## 🔗 See Also

- [[03 - Selectors Pt. 1]] — type, class, id and targeting
- [[05 - Pseudo-elements]] — styling parts of an element without extra markup
- [[06 - Pseudo-classes]] — styling elements by state
- [[11 - Display & Positioning]] — where these selected elements end up on the page

---
