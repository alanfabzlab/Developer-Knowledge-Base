# 01. CSS Basics

**Spanish version:** [01 - Fundamentos de CSS.md](01%20-%20Fundamentos%20de%20CSS.md)

**Course:** CSS
**Topic:** What CSS is, Rule Anatomy, Plugging In the Stylesheet, Developer Comments & Your First Styled Screen
**Tags:** `#css` `#web-development` `#basics` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Lessons-01_--_05-7C5CFF?style=for-the-badge" alt="Lessons 01 to 05">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

The first chapter of the language that paints the web. HTML gave Emberfall its skeleton;
this module gives it skin — colors, fonts, layouts, animations. By the end of this chapter
you will have taken a raw, unstyled title screen and turned it into a finished hero banner.
Selector reference for everything ahead: [[00b - CSS Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> CSS does not *hold* content and does not *run* logic. It **describes appearance**: this
> heading is red, this panel has 20px of breathing room, these cards sit in a row. The
> markup stays where HTML left it — CSS decides how it *looks*.

---

## 01. Insert Coin

> [!NOTE]
> **Key information**
> **CSS** (**C**ascading **S**tyle **S**heets) was proposed by **Håkon Wium Lie** in 1994 and
> became a W3C recommendation in 1996. Today it styles every website in the world.

CSS is a **styling language**: it paints a page with colors, fonts, layouts and animations
while HTML keeps describing what each piece of content *is*.

### The Three Core Web Technologies

| Technology | Role | In a game site |
| :--- | :--- | :--- |
| **HTML** | Creates the **structure** | The skeleton: which HUD panels exist |
| **CSS** | Styles the **appearance** | The skin: colors, fonts, layout |
| **JavaScript** | Makes it **interactive** | The engine: health bars that update |

This module focuses on CSS. The files we create use the **`.css`** file extension.

### Quest: Before and After

Open any page you like, right-click the main heading and choose **Inspect**. In the
*Styles* panel you will see rules like `color: tomato;` — that is CSS, live. Delete one of
those rules and the page changes in front of you. Refresh to bring it back.

You just watched CSS do its only job: change how something looks without touching what it says.

---

## 02. Rule Anatomy

In CSS we write **rules** to define how HTML elements are styled on a page.

### Structure of a CSS Rule

```css
selector {
  property: value;
}
```

| Part | Example | What it does |
| :--- | :--- | :--- |
| **Selector** | `h1` | Identifies the HTML element(s) to style (`div`, `p`, `h1`…) |
| **Declaration block** | `{ … }` | The curly brackets holding one or more declarations |
| **Property** | `color` | *What* aspect of the element changes |
| **Value** | `tomato` | *How* that aspect changes |
| **Declaration** | `color: tomato;` | One `property: value;` pair — always ends with `;` |

```css
h1 {
  color: tomato;
  font-size: 32px;
}
```

Two declarations live inside one block: the `<h1>` on the page turns tomato red *and* grows
to 32 pixels tall. Every declaration needs its semicolon — the last one included, because
the next rule you add will not wait for you to remember it.

> [!WARNING]
> **The mistake everyone makes once**
> A missing `;` or a stray `:` swallows the rest of the block silently. The browser does
> not throw an error — it just drops the declarations after the typo and renders the page
> half-styled. If a rule "does nothing", check the punctuation of the rule *above* it first.

---

## 03. Plugging In

A `.css` file does nothing on its own: the HTML page has to be told where it lives. The
connection lives in the `<head>` with a `<link>` element:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Emberfall — Title Screen</title>
</head>
<body>
  <h1>Emberfall</h1>
</body>
</html>
```

- `href="styles.css"` — the path to the stylesheet, next to the `.html` file.
- `rel="stylesheet"` — tells the browser *what kind* of resource it is.

> [!NOTE]
> Two files, one connection: `index.html` holds the words, `styles.css` holds the paint.
> Keep them side by side in the same folder and the relative path stays a single filename.

### Quest: First Rule

Create `styles.css` next to your page and paint the title screen:

```css
body {
  background-color: #1b1b2f;
  color: #f5f5f5;
  font-family: Arial, sans-serif;
  text-align: center;
}

h1 {
  color: #ff6b35;
  letter-spacing: 4px;
}
```

Reload the page. Dark dungeon background, ember-orange title — your first stylesheet is live.

---

## 04. Developer Comments

CSS comments are ignored by the browser; they exist for whoever reads the file next —
usually you, six months from now.

```css
/* Comments in CSS sit between forward slashes and asterisks. */

h1 {
  /* This declaration is commented out: it does nothing right now. */
  color: tomato;
}
```

Anything between `/*` and `*/` is invisible to the browser, so a comment can document a
rule or temporarily disable one while you experiment.

> [!TIP]
> Commenting a declaration out instead of deleting it is the cheapest debugger there is:
> if the bug disappears, the comment just told you which line was guilty.

---

## 05. Title Screen

### Checkpoint: Chapter Recap

- **CSS** paints; HTML holds content, JavaScript runs logic.
- A rule is `selector { property: value; }` and every declaration ends in `;`.
- `<link href="styles.css" rel="stylesheet">` connects the two files.
- `/* … */` writes a comment the browser ignores.

### Project: Boss Title Screen

Build `index.html` + `styles.css` for the title screen of your own game: a hero heading, a
boss image and a tagline footer — all styled from the external file.

### HTML (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Emberfall — Warden Title Screen</title>
</head>
<body>
  <main>
    <section id="hero-copy">
      <h1>Emberfall</h1>
      <p>The Warden of the Ninth Floor awaits.</p>
    </section>
    <section id="hero-img">
      <figure>
        <img src="https://placehold.co/250" alt="A tall armored warden holding a lantern." width="250" />
      </figure>
    </section>
    <footer>
      <p>A dungeon crawler in the Emberfall tradition</p>
    </footer>
  </main>
</body>
</html>
```

### CSS (`styles.css`)

```css
body {
  font-family: "Chalkduster", fantasy;
  width: 100%;
  height: 100vh;
  position: absolute;
  text-align: center;
}

main {
  background-color: #1b1b2f;
  color: #f5f5f5;
  width: 70%;
  margin: auto;
  margin-top: 50px;
  position: relative;
  border-radius: 5px;
}

#hero-copy {
  padding: 5px;
}

#hero-img > figure > img {
  width: 70%;
  border-radius: 10px;
}

footer {
  background-color: #2dc653;
  color: #10240e;
  height: 100px;
}

footer > p {
  padding: 37px;
}
```

> [!TIP]
> **Game dev version**
> This is the shape of every splash screen ever shipped: a centered container, a hero
> image with rounded corners, a footer strapline. Chapter [[02 - Colors & Measurements]]
> hands you the palette — named colors, `rgb()` and hex — to replace my defaults with yours.

---

## XP Earned: Key Takeaways

- 🎨 **CSS** = Cascading Style Sheets: colors, fonts, layout, animation.
- 🧩 A rule is **selector + declaration block**; each declaration is `property: value;`.
- ⛓️ `<link href="styles.css" rel="stylesheet">` wires the page to its paint.
- 🔚 Every declaration ends with `;` — a missing one silently kills the rest of the block.
- 💬 `/* comment */` is invisible to the browser and useful to humans.

---

## Loot Table: Real-World Use Cases

- 🎮 Title screens, HUD skins and store pages for games
- 📰 Themed blogs, landing pages and portfolios
- 🎨 Brand refreshes: same HTML, new stylesheet, new identity
- 🧪 Prototypes: restyle a page without touching a single line of markup

---

## 🎮 Side Quests: Practice Exercises

1. Write a rule that turns every `<p>` on a page a different color.
2. Comment out that rule and confirm the text returns to black.
3. Add a second stylesheet link and prove the later file wins.
4. Rebuild the title screen above with your game's palette.
5. **Boss fight:** style a `patch_notes.html` page — dark background, orange `<h2>`
   headings, a green footer — using only an external `.css` file.

---

## 🔗 See Also

- [[00b - CSS Cheatsheet]] — selectors and syntax on one page
- [[02 - Colors & Measurements]] — next chapter: palettes and units
- [[03 - Selectors Pt. 1]] — aiming the rules you now know how to write
- [[01 - HTML Basics]] — the markup this module styles

---
