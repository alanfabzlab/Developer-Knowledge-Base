# 00b. HTML Cheatsheet

**Spanish version:** [00b - Chuleta de HTML.md](00b%20-%20Chuleta%20de%20HTML.md)

**Course:** HTML
**Topic:** Quick reference for the HTML elements, tags, semantic layout and link types used across the module
**Tags:** `#html` `#web-development` `#cheatsheet` `#reference` `#semantic-html` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Covers-Chapters_01_--_04-7C5CFF?style=for-the-badge" alt="Chapters 01 to 04">
  <img src="https://img.shields.io/badge/Type-Cheatsheet-00C2A8?style=for-the-badge" alt="Cheatsheet">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=E34F26&height=70&section=header" width="100%" alt="Emberfall wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #E34F26, #2DD4BF, #E34F26, transparent); margin: 24px 0;" />

One page for the whole module. Every element here was introduced in [[01 - HTML Basics]],
[[02 - Structure & Attributes]] or [[04 - Semantic HTML]] — nothing on this sheet is new.
Attributes, `class` vs `id`, CSS basics and form inputs live in [[00c - HTML Cheatsheet II]].

> [!TIP]
> Print it, or keep it in a split pane next to your editor. A page written without checking
> the tag name on this sheet is how `<div>` soup happens: nesting containers because nothing
> on the sheet looked right.

**The running theme of this module: Emberfall**, a roguelike dungeon crawler. Every exercise
builds part of its web companion: the bestiary, the patch notes, the item catalog, the account
form, the devlog. The markup is the same markup a real studio ships — only the words change.

---

## 🔬 Anatomy of an Element

```html
<p class="intro">The Emberfall dungeon opens at dawn.</p>
```

| Part | Example | What the browser does |
| :--- | :--- | :--- |
| Opening tag | `<p` | Announces an element and its type |
| Attribute | `class="intro"` | Extra setting, as `name="value"` |
| Closing bracket | `>` | Ends the opening tag |
| Content | `The Emberfall dungeon opens at dawn.` | What is rendered inside the element |
| Closing tag | `</p>` | Where the element ends — note the `/` |

> [!NOTE]
> Attributes go **inside** the opening tag, before the `>`, and always with their value in
> double quotes: `<p class="intro">`, never `<p class=intro>`.

### Void (Self-Closing) Elements

Some elements have no content and therefore no closing tag. Write them as `<br>`, not `<br></br>`:

| Element | Note |
| :--- | :--- |
| `<br>` | Line break |
| `<img>` | Image, sprite, screenshot |
| `<input>` | Form control |
| `<hr>` | Horizontal rule — the separator between patch notes |
| `<meta>` | Metadata in `<head>` |

The `/>` in `<br />` is legal XHTML leftover, harmless in HTML5. `<br>` is the modern form.

---

## 🧱 Page Skeleton

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Emberfall — Bestiary</title>
    <style>
      /* CSS goes here */
    </style>
  </head>
  <body>
    <!-- Visible content goes here -->
  </body>
</html>
```

| Line | Why it exists |
| :--- | :--- |
| `<!DOCTYPE html>` | Declares an HTML5 document; **no** closing tag |
| `<html>` | Root element; everything else lives inside it |
| `<head>` | Info for the browser — invisible on the page |
| `<title>` | The text on the browser tab |
| `<body>` | Everything visible; exactly one per file |

---

## 🧰 Elements

### Document & Structure

| Element | Purpose |
| :--- | :--- |
| `<!DOCTYPE html>` | Declares an HTML5 document (no closing tag) |
| `<html>` | Root element of the page |
| `<head>` | Info for the browser, not visible on the page |
| `<title>` | Text shown in the browser tab |
| `<body>` | All visible content (only one per file) |
| `<div>` | Generic block container / section |
| `<span>` | Generic inline container |
| `<style>` | CSS styles for the page (in `<head>`) |
| `<link>` | Connects an external resource (CSS, icon) |

### Text

| Element | Purpose |
| :--- | :--- |
| `<h1>` to `<h6>` | Headings, largest to smallest (only one `<h1>` per file) |
| `<p>` | Paragraph |
| `<br>` | Line break (self-closing) |
| `<b>` / `<strong>` | Bold / important |
| `<i>` | Italic |
| `<u>` | Underline |
| `<s>` | Strikethrough — the ability you removed in the last patch |

### Lists, Links & Media

| Element | Purpose |
| :--- | :--- |
| `<ul>` | Unordered (bullet) list — stats, weaknesses, controls |
| `<ol>` | Ordered (numbered) list — crafting steps, patch items, phases |
| `<li>` | List item |
| `<a>` | Link (anchor) |
| `<img>` | Image (self-closing) |

### Interaction

| Element | Purpose |
| :--- | :--- |
| `<form>` | Form that collects user input |
| `<input>` | Interactive control inside a form (self-closing) |
| `<label>` | Caption linked to an input |
| `<textarea>` | Multi-line text input — a bug report, a review |
| `<select>` | Dropdown list — choose your class |

### Semantic Layout *(chapter 04)*

| Element | Purpose |
| :--- | :--- |
| `<header>` | Top of the page: logo, `<h1>`, `<nav>`; goes **inside** `<body>` |
| `<nav>` | Navigation links, usually a list inside `<header>` or `<footer>` |
| `<main>` | The main content of the page (only one per file) |
| `<section>` | A group of related content (many per page) |
| `<article>` | One standalone piece of content (a patch note, a boss entry) |
| `<figure>` | An image, diagram or code block, with its own caption |
| `<figcaption>` | The caption that describes the `<figure>` |
| `<footer>` | Bottom info: creator, copyright, extra links |

> [!TIP]
> `<b>`, `<i>`, `<u>` and `<s>` are fine for learning, and the CSS course replaces them
> with `font-weight`, `font-style` and `text-decoration`. Reach for them anyway and your
> next stylesheet will fight you.

---

## 🗺️ Semantic Layout

```html
<body>
  <header>
    <h1>Emberfall Devlog</h1>
    <nav>
      <ul>
        <li><a href="#patch-notes">Patch Notes</a></li>
        <li><a href="#bestiary">Bestiary</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <section id="patch-notes">
      <h2>Patch Notes</h2>

      <article>
        <h3>Patch 1.4 — The Deep Halls</h3>
        <p>Adds a new wing, two mini-bosses and a hotfix for the lantern bug.</p>
        <figure>
          <img src="deep-halls.png" alt="Screenshot of the Deep Halls corridor">
          <figcaption>Corridor 7 of the Deep Halls, lit by a single lantern.</figcaption>
        </figure>
      </article>
    </section>
  </main>

  <footer>
    <!-- Studio name, copyright, links -->
  </footer>
</body>
```

| Element | Role | How many per page |
| :--- | :--- | :--- |
| `<header>` | Top area: title, logo, `<nav>` | Usually one |
| `<nav>` | Navigation links | As many as needed |
| `<main>` | Main content | **One** |
| `<section>` | Group of related content | Many |
| `<article>` | Standalone piece of content | Many |
| `<figure>` / `<figcaption>` | Image or diagram with its caption | Many |
| `<footer>` | Bottom info | Usually one |

> [!NOTE]
> `<header>` (inside `<body>`, visible) is not the same as `<head>` (outside `<body>`, info
> for the browser). One is the game's HUD; the other is the file's ID card.

> [!WARNING]
> One `<main>` per page, but many `<section>` and `<article>` elements. Start every
> `<section>` and `<article>` with a heading — an unnamed section is a section nobody can
> jump to.

---

## 💬 Comments

```html
<!-- Single-line comment -->
<!--
  Multi-line
  comment
-->
<p>Visible text. <!-- This part is not rendered. --></p>
```

Comments document intent, and they can hide code while you experiment. They are also the
easiest place to leave a lie behind: `<!-- fix this before the demo -->` survives for years.

---

## 🔗 Link Types

```html
<a href="https://example.com">Studio website</a>
<a href="https://example.com" target="_blank">Open in a new tab</a>
<a href="mailto:support@example.com">Report a bug</a>
<a href="tel:212-555-0100">Call the studio</a>
<a href="sms:212-555-0123">Text the studio</a>
<a href="#deep-halls">Jump to a section on the same page</a>
```

| `href` value | Opens |
| :--- | :--- |
| `https://…` | Another page |
| `mailto:…` | The visitor's email client |
| `tel:…` | The dialer, on phones |
| `sms:…` | The message composer |
| `#id` | A spot inside the same page — the nav skip link |

---

## 🪄 Developer Tools Shortcuts

| Browser | Windows / Linux | macOS |
| :--- | :--- | :--- |
| Chrome | `ctrl` + `shift` + `c` | `cmd` + `option` + `i` |
| Safari | n/a | `option` + `cmd` + `c` |
| Firefox | `ctrl` + `shift` + `i` | `cmd` + `option` + `i` |

---

## ⚠️ Traps Worth Memorizing

| Trap | What actually happens |
| :--- | :--- |
| Two `<h1>` tags | Nothing breaks, but the document outline loses its single title |
| Two `<body>` tags | The browser silently merges them; the file lies about its own structure |
| Missing `alt` on an `<img>` | Screen readers announce the file name, and a broken image shows nothing useful |
| `<br></br>` | A stray closing tag appears as literal text in some cases — `<br>` has no end |
| Indenting with tabs | Works, but the vault and most teams use two spaces |
| Nesting `<p>` inside `<p>` | Invalid HTML; the browser closes the first `<p>` and your layout shifts |
| `enter` for a new line in HTML | Ignored — use `<br>`. HTML collapses repeated whitespace |
| `<header>` written inside `<head>` | Nothing renders; the browser silently drops it. `<header>` belongs in `<body>` |
| Two `<main>` elements | The second one is ignored for landmark navigation |
| `<b>` for styling | Works, and then fights the CSS course. Use CSS |

---

## 🎮 The One-Page Version

Everything from this sheet in a single file — one Emberfall bestiary entry:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Emberfall — Bestiary</title>
  </head>
  <body>
    <header>
      <h1>Emberfall Bestiary</h1>
      <nav>
        <ul>
          <li><a href="#cinder-slime">Cinder Slime</a></li>
          <li><a href="#ash-wraith">Ash Wraith</a></li>
        </ul>
      </nav>
    </header>

    <main>
      <section id="cinder-slime">
        <article>
          <h2>Cinder Slime</h2>
          <img src="cinder-slime.png" alt="A lava-glowing slime">

          <figure>
            <img src="cinder-slime-artwork.png" alt="Official artwork of the Cinder Slime">
            <figcaption>Key art for the Slime family.</figcaption>
          </figure>

          <p>Slow, fragile, splits into two smaller slimes when it dies.</p>

          <h3>Weaknesses</h3>
          <ul>
            <li>Cold damage</li>
            <li>Physical attacks</li>
          </ul>

          <h3>Drops</h3>
          <ol>
            <li>Slime gel</li>
            <li>Ember shard</li>
          </ol>

          <hr>

          <a href="https://example.com/emberfall/cinder-slime">Full entry</a>
          <a href="mailto:archivist@example.com">Report a correction</a>
        </article>
      </section>
    </main>

    <footer>
      <ul>
        <li><a href="#legal">Legal</a></li>
        <li><a href="mailto:support@example.com">Support</a></li>
      </ul>
    </footer>
  </body>
</html>
```

---

## 🔗 See Also

- [[00c - HTML Cheatsheet II]] — attributes, `class` vs `id`, CSS basics, form inputs
- [[01 - HTML Basics]] — where these elements are introduced, with quests
- [[02 - Structure & Attributes]] — page skeleton, comments, attributes and selectors
- [[03 - Forms]] — the interactive elements, in depth
- [[04 - Semantic HTML]] — `<header>`, `<nav>`, `<main>`, `<article>`, `<figure>`, `<footer>`

---