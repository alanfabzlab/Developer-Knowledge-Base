# 03. Selectors Pt. 1

**Spanish version:** [03 - Selectores Pt. 1.md](03%20-%20Selectores%20Pt.%201.md)

**Course:** CSS
**Topic:** What Selectors Are, Type Selectors, Class Selectors, ID Selectors and Targeting
**Tags:** `#css` `#web-development` `#selectors` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Lessons-12_--_16-7C5CFF?style=for-the-badge" alt="Lessons 12 to 16">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

A rule is only as good as its aim. This chapter is about the first half of every rule you
will ever write — the **selector** — and the three weapons every developer carries: type,
class and ID. You will also learn **targeting**, the technique of chaining them together
until a rule hits exactly one element on the page. Reference:
[[00b - CSS Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> Selectors answer *which elements?* — by tag name (`div`), by label (`.class`) or by
> unique name (`#id`) — and combining them makes the answer more precise.

---

## 12. Target Lock

**Selectors** determine which HTML element(s) are targeted for styling. Everything to the
left of the `{` in a rule is a selector; everything inside is the paint.

```css
/* "Every <p> on the page" */
p {
  color: dimgray;
}
```

Three selector families cover almost everything:

| Family | Written as | Selects | Think of it as |
| :--- | :--- | :--- | :--- |
| **Type** | `div` | Every element with that tag | A job title: "all engineers" |
| **Class** | `.class-name` | Any element wearing that class | A uniform: "whoever is on guard duty" |
| **ID** | `#id-name` | The one element with that id | A name tag: one person, unique |

---

## 13. Type Selector

The **type selector** (also called the *element* or *tag* selector) picks every matching
element on the page by tag name.

```css
div {
  /* Applied to all <div> elements */
}

p {
  /* Applied to all <p> elements */
}
```

No dot, no hash — the bare tag name. It is the broadest brush you have, which makes it
perfect for page-wide defaults:

```css
body {
  font-family: Arial, sans-serif;
  background-color: #1b1b2f;
}
```

> [!TIP]
> Set the boring, page-wide rules with type selectors once (`body`, `h1`, `p`), then reach
> for classes and IDs whenever something needs to *break* the default. Fewer overrides,
> fewer surprises.

---

## 14. Class Selector

A **class selector** is written with a **period** `.` and targets every element whose
`class` attribute matches — which can be any number of elements.

```html
<p class="line">Ember burns brighter.</p>
<p class="line">Ash remembers everything.</p>
<p>I am not styled.</p>
```

```css
.line {
  /* Applied to all elements with class="line" */
}
```

Classes are the workhorse of CSS: reusable, stackable (`class="line active"`) and happy to
appear on as many elements as you want.

---

## 15. ID Selector

An **ID selector** is written with a **hash** `#` and targets the single unique element
whose `id` attribute matches. HTML allows each id exactly once per file.

```html
<p id="victory">Victory!</p>
```

```css
#victory {
  /* Applied to the unique element with id="victory" */
}
```

> [!WARNING]
> **class vs id**
> A class is a *role* any element can wear; an id is a *name* only one element may have.
> Reusing an id across elements is invalid HTML and quietly breaks the uniqueness that
> `#id` selectors promise. Need to style three things the same way? That is what classes
> are for.

---

## 16. Targeting

**Targeting** raises specificity by chaining element types with classes or IDs, so a rule
only fires on elements that satisfy *all* the parts.

```css
div.line {
  /* Only <div> elements that also have class="line" */
}

div#victory {
  /* Only the <div> that has id="victory" */
}
```

| Selector | Matches | Specificity |
| :--- | :--- | :--- |
| `p` | Every paragraph | Low |
| `.line` | Every element with `class="line"` | Medium |
| `#victory` | The element with `id="victory"` | High |
| `p.line` | Paragraphs that are *also* `.line` | Higher |
| `p#line` | The one paragraph that is `#victory` | Highest |

Think of it as a security checkpoint: the more badges you demand, the fewer people get
through — and the rule applies to nobody else.

### Quest: Rhymes of the Realm

Practice with all three families at once. Create `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Selectors</title>
</head>
<body>
  <div>
    <p class="line" id="rifts">Rifts are red.</p>
    <p class="line" id="runes">Runes are blue.</p>
    <p class="line" id="potions">Potions are sweet.</p>
    <p class="line">And so are you!</p>
  </div>
</body>
</html>
```

And `styles.css`:

```css
/* Type Selector */
div {
  border: 1px solid;
  text-align: center;
}

/* Class Selector */
.line {
  width: 50%;
  margin: auto;
  padding: 10px 0;
  text-decoration: underline;
}

/* ID Selectors */
#rifts {
  background-color: red;
}

#runes {
  background-color: violet;
}

#potions {
  background-color: beige;
}
```

Read the CSS top to bottom: the `div` rule frames *all* four lines, the `.line` class
centers and underlines *all* of them, and the three IDs each paint exactly one. Same
element, three different selectors stacking on top of it — which is precisely how real
stylesheets are built.

> [!NOTE]
> When two rules target the same element, the more specific one wins: `#rifts` would beat
> `.line` on background color every time. Specificity is the next chapter's hidden theme
> and the reason `04 - Selectors Pt. 2` teaches you to spread rules *across* elements with
> grouping instead of piling them onto one.

---

## XP Earned: Key Takeaways

- 🎯 Selectors decide **which** elements a rule paints.
- 🔖 **Type** = bare tag name, the broadest brush.
- 🏷️ **Class** = leading `.`, reusable on any number of elements.
- 🏷️ **ID** = leading `#`, unique per file — one element only.
- 🎯 **Targeting** = chaining them (`div.line`, `p#line`) for precision.
- 🥇 More specific selector wins when two rules collide.

---

## Loot Table: Real-World Use Cases

- 🧾 Page-wide typography set once on `body` and heading tags
- 🏷️ Reusable button, card and badge styles with classes
- 🎯 One-off hero sections and modals addressed by id
- 🎮 Party frames, quest rows and inventory slots — one class per row type, one id per screen

---

## 🎮 Side Quests: Practice Exercises

1. Style every `<h2>` on a page with a type selector, then override one with a class.
2. Give three elements `class="card"` and one `id="featured"`; style both.
3. Write a selector that hits only `<p>` elements inside `class="line"`.
4. Find the specificity winner: `.line` vs `#rifts` vs `p.line` — write them out.
5. **Boss fight:** build `roster.html` — a `<div>` containing six `<p class="hero">`
   lines, each with a unique `id`, styled by all three selector families.

---

## 🔗 See Also

- [[00b - CSS Cheatsheet]] — the selector table version of this chapter
- [[02 - Colors & Measurements]] — previous chapter: palettes and units
- [[04 - Selectors Pt. 2]] — grouping, child combinators and the capstone flyer
- [[06 - Pseudo-classes]] — selecting by *state* instead of by name

---
