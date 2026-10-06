# 01. HTML Basics

**Spanish version:** [01 - Fundamentos de HTML.md](01%20-%20Fundamentos%20de%20HTML.md)

**Course:** HTML
**Topic:** What HTML is, Elements & Tags, Headings, Line Breaks, Text Formatting, Lists, Links, Images & Developer Tools
**Tags:** `#html` `#web-development` `#basics` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Lessons-01_--_07_%2B_Bonus-7C5CFF?style=for-the-badge" alt="Lessons 01 to 07">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=7C5CFF&height=70&section=header" width="100%" alt="Violet wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #E34F26, #2DD4BF, #E34F26, transparent); margin: 24px 0;" />

The first chapter of the language that gives every web page its bones. By the end of it you
will have written a **boss showcase page** for Emberfall from scratch — headings, formatted
text, lists, a link and an image — and you will know how to inspect any page on the internet to
find out how it was built. Element and tag reference: [[00b - HTML Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> HTML does not *draw* anything and it does not *run* anything. It **labels** content: this
> run of characters is a heading, this one is a list item, this other one is a link. Every
> other thing you want a browser to do arrives later, with CSS and JavaScript.

---

## 01. Insert Coin

> [!NOTE]
> **Key information**
> **HTML** (**H**yper**T**ext **M**arkup **L**anguage) was created by **Tim Berners-Lee** in 1991 as the foundation of the World Wide Web. Today, every website in the world uses HTML.

HTML is a **markup language**: it marks up content on a web page and tells the browser what each piece is.

### The Three Core Web Technologies

| Technology | Role | In a game site |
| :--- | :--- | :--- |
| **HTML** | Creates the **structure** of a web page | The skeleton: which HUD panels exist |
| **CSS** | Styles the **appearance** of a page | The skin: colors, fonts, layout |
| **JavaScript** | Makes it **interactive** | The engine: health bars that update |

This course focuses on HTML. The files we create use the **`.html`** file extension.

### Code Editor

A **code editor** is a text editor that can write, edit and run code.

### Quest: Boot Sequence

Type these two lines into the editor, replace the placeholder text, and press **Run**:

```html
<h2>Emberfall 1.0 — launch date</h2>
<p>Write your one-line pitch</p>
```

- Replace `Emberfall 1.0 — launch date` with today's date.
- Replace `Write your one-line pitch` with the pitch of your game.

You just created your first web page with HTML.

> [!TIP]
> The files in this module are plain `.html` files in a folder. Nothing needs to be installed
> and nothing needs to be built — see [[02 - Filesystem]] for navigating to the folder and
> opening the file in a browser.

---

## 02. Core Systems

### Elements

**Elements** are the smallest building blocks of the language. An element usually consists of an **opening tag**, the **content**, and a **closing tag**. A **tag** is enclosed in angle brackets.

```html
<p>Emberfall v1.0 is out now.</p>
```

- `<p>` is the opening tag.
- `Emberfall v1.0 is out now.` is the content.
- `</p>` is the closing tag.

The `<p>` **paragraph** element tells the browser that the content inside is paragraph text.

### The `<body>` Element

```html
<body><p>👋 I'm a new web developer!</p></body>
```

The `<body>` element defines an HTML document's "body": it holds any content we want to display to the user.

> [!NOTE]
> There can only be **one** `<body>` element in a file.

### Indentation

Indenting HTML isn't required, but it's good practice because it makes code easier to read and shows the **nesting levels**. We recommend **two spaces** per indentation level.

```html
<body>
  <p>👋 I'm a new web developer!</p>
</body>
```

### Quest: The Four Systems

Create `systems.html` that lists the four systems every game needs (Input, Physics, Audio, Rendering) in the browser, nicely indented.

```html
<body>
  <p>Input</p>
  <p>Physics</p>
  <p>Audio</p>
  <p>Rendering</p>
</body>
```

---

## 03. Patch Notes

### Headings

HTML has **six levels of headings**, from `<h1>` to `<h6>`. `<h1>` is the largest and `<h6>` is the smallest.

```html
<h1>Emberfall 1.4 — The Deep Halls</h1>
<h2>New content</h2>
<h3>Corridors 5 to 9</h3>
<h4>Lantern enemies</h4>
<h5>Patch notes</h5>
<h6>Fixed a typo</h6>
```

> [!NOTE]
> Only **one** `<h1>` element should be used in a file.

Headings are not about size, they are about **outline**: `<h2>` says "this belongs to the
`<h1>` above". That is what screen readers use to navigate a page, and what a search engine
reads to decide what the page is about.

### Line Break

Pressing `enter` inside an element doesn't create a new line, because **HTML ignores multiple spaces and line breaks** within elements. Use the `<br>` break tag instead.

```html
<body>
  <h1>Patch 1.4</h1>
  <p>Added the Deep Halls wing.<br>Fixed the lantern that would not turn off.</p>
</body>
```

A **self-closing tag** doesn't need a separate closing tag (there is no `</br>`). `<br>` is the first one we meet.

> [!WARNING]
> **The mistake everyone makes once**
> Pressing `enter` inside a `<p>` looks correct in the editor and produces a single line in
> the browser. Whitespace is **collapsed**: any run of spaces, tabs and newlines inside an
> element becomes one space. `<br>` is the only way to break a line from HTML.

### Quest: Release Notes

Create `patch_notes.html` with the changelog of your game's launch:

- `<h1>` heading for the version number.
- `<h3>` heading for the date.
- `<p>` paragraph(s) for the summary.
- `<br>` for line breaks.

```html
<h1>Emberfall 1.4</h1>
<h3>March 14, 2026</h3>
<p>Adds the Deep Halls wing and two new mini-bosses.<br>Replace this with your own changes.</p>
```

---

## 04. Launch Announcement

### Text Formatting

| Element | Effect |
| :--- | :--- |
| `<b>` | **bold** text |
| `<i>` | *italicize* text |
| `<u>` | <u>underline</u> text |
| `<s>` | ~~strikethrough~~ text |

```html
<b>Emberfall is out now.</b><br>
<i>Best roguelike of the year.</i><br>
<u>Free demo available.</u><br>
<s>Launch price 90% off</s><br>
```

> [!NOTE]
> `<b>` is just for bolding text stylistically. HTML also has `<strong>`, which conveys that the content is **important** and also styles it as bold.

All four tags together in a store announcement:

```html
<p>This week's patch adds the <i>Deep Halls</i> and a <b>new boss</b>.<br>
The <u>pre-order bundle</u> now includes the artbook, at <s>50€</s> 30€.</p>
```

> [!NOTE]
> These tags are good for learning basic styling, but are **no longer best practice**. Other ways to style text are covered with CSS.

### Quest: Marketing Copy

Recreate the exact format of a store page hype text in `announcement.html` using `<p>`, `<b>`, `<i>`, `<s>` and `<u>`.

```html
<p>
  <b>Deep Halls, now live:</b> We rebuilt <s>the old corridor filler</s> into a full wing that will make you <i>grind for real</i>. New loot, new bosses, and <b>one very angry lantern</b>. Grab the <u>Deep Halls DLC</u> at a <i>launch discount</i>.
</p>

<p>
  <b>P.S.</b> After three months of beta, we are printing <b>Emberfall Artbooks</b>! Pre-orders open Monday.
</p>
```

---

## 05. Crafting Recipe

### Lists

HTML has two types of lists:

- `<ul>` → **Unordered** lists (bullet points)
- `<ol>` → **Ordered** lists (numbered)

Each item is wrapped in a `<li>` **list item** element.

```html
<ul>
  <li>🪨 Ember Shard</li>
  <li>🍄 Ash Mushroom</li>
  <li>💧 Deep Water</li>
</ul>
```

`<ul>` is great for listing things in any order. To number the crafting steps, use `<ol>`:

```html
<ol>
  <li>🪨 Ember Shard</li>
  <li>🍄 Ash Mushroom</li>
  <li>💧 Deep Water</li>
</ol>
```

### Quest: Forge Blueprint

Create `recipe.html` with an item you would craft in your own game: an **unordered** list for the ingredients and an **ordered** list for the forging steps.

```html
<h2>Ingredients</h2>
<ul>
  <li>1 Ember Shard</li>
  <li>2 Ash Mushrooms</li>
  <li>3 Deep Water</li>
</ul>

<h2>Steps</h2>
<ol>
  <li>Smelt the Ember Shard until it glows orange.</li>
  <li>Grind the Ash Mushrooms into a fine powder.</li>
  <li>Pour the Deep Water over the powder and let it react.</li>
  <li>Hammer the mixture into a blade while it is still warm.</li>
</ol>
```

> [!TIP]
> This is the shape of almost every game data screen: a `<ul>` of stats, an `<ol>` of steps,
> a `<table>` for the rest. A quest log, an ability list, a skill tree and a deck of cards are
> the same three elements in a different order.

---

## 06. Missing Boss

### Links

**Links** are integral to the idea of the internet: they are how users connect to other sites and navigate the web. The first website ever (1991) is still up and it is full of links.

Use the `<a>` **anchor** element to add a hyperlink to a piece of text:

```html
<a href="https://archive.org/web">Internet Archive</a>
```

- The text inside is what is displayed.
- `href` (hyperlink reference) is the pointer to the linked page. When the text is clicked, the browser goes to that address.

> [!NOTE]
> `href` can also point to an email address, phone number or text message using `mailto:`, `tel:` or `sms:`:

```html
<a href="mailto:patch@example.com">📧</a>
<a href="tel:212-555-0100">🤙</a>
<a href="sms:212-555-0123">💬</a>
```

### Images

Use the `<img>` image element:

```html
<p>Here's a screenshot:</p>
<img src="https://example.com/boss.png">
```

- `<img>` is another **self-closing** tag.
- The `src` attribute ("source") specifies the file path of the image.
- For most images, you can find the path by right-clicking the image and choosing **Copy Image Address**.

> [!IMPORTANT]
> An `<img>` without `alt` is a bug. If the image fails to load, the visitor sees a broken
> icon and no explanation — and a screen reader announces the file path out loud.

### Quest: Bounty Board

The Emberfall boss "Warden of the Ninth Floor" escaped the data files. Create `boss.html` that includes:

- The boss name.
- A boss picture with `<img>`.
- A short description.
- Contact info with `<a>`.

```html
<h1>Missing Boss: Warden of the Ninth Floor</h1>
<img src="https://placehold.co/300" alt="A tall armored warden holding a lantern">
<p>Last seen in the Deep Halls. Drops the Ember Key on defeat and is very angry about it.</p>
<a href="mailto:archivist@example.com">Report a sighting</a>
```

---

## 07. Boss Showcase

### Checkpoint: Chapter Recap

- HTML elements, tags and indentation.
- Heading tags: `<h1>` - `<h6>`.
- Paragraph and line breaks: `<p>`, `<br>`.
- Text formatting: `<b>`, `<i>`, `<u>`, `<s>`.
- Unordered and ordered lists: `<ul>`, `<ol>`.
- Links and images: `<a>`, `<img>`.

### Project: Boss Showcase

Create `boss.html` for the boss of your own game using **all** the elements learned and **at least two types of text formatting**. It should include:

- The name of the boss.
- A picture of the boss.
- A short blurb about its lore.
- A link to the wiki or devlog.
- The phases in an unordered list.
- Top 5 attacks in an ordered list.

```html
<h1>Warden of the Ninth Floor</h1>
<img src="https://placehold.co/300" alt="Warden of the Ninth Floor">

<p>The Warden is a <b>two-phase mini-boss</b> guarding the last door of the Deep Halls. It <i>changes behaviour at 50% health</i>, dropping the lantern to fight in the dark.</p>

<a href="https://example.com/emberfall/warden">Read the full codex entry</a>

<h2>Phases</h2>
<ul>
  <li>Phase 1 — Lantern</li>
  <li>Phase 2 — Darkness</li>
</ul>

<h2>Top 5 Attacks</h2>
<ol>
  <li>Lantern Sweep</li>
  <li>Ember Bolt</li>
  <li>Floor Cleave</li>
  <li>Blind Dash</li>
  <li>Ninth Floor Collapse</li>
</ol>
```

> [!TIP]
> **Game dev version**
> A boss page is a character sheet: swap the heading for the enemy name, the blurb for the
> lore, the unordered list for the phases and the ordered list for the move list. Every data
> screen in a game is this page with different words. Chapter [[02 - Structure & Attributes]]
> takes that card and gives it `class` and `id` so a stylesheet can target it.

---

## Bonus Loot:: Developer Tools

### Inspect

**Developer Tools** allow us to create, test and debug web development software. Current browsers provide integrated developer tools, which let us **inspect** a website and see the code of virtually every site in the world. You can now see the complete HTML code of the page you are on.

| Browser | Tool Name | How To Open | Keyboard Shortcut |
| :--- | :--- | :--- | :--- |
| **Google Chrome** | DevTools | Right-click > "Inspect" | `ctrl` + `shift` + `c` (Windows/Linux); `cmd` + `option` + `i` (macOS) |
| **Apple Safari** | Safari Develop menu | Menu > Preferences > Developer > Show JavaScript Console | `option` + `cmd` + `c` |
| **Mozilla Firefox** | Firefox Developer Tools | Tools > Web Developer > Web Developer Tools | `ctrl` + `shift` + `i` (Windows/Linux); `cmd` + `option` + `i` (macOS) |

How to open them:

- **Chrome:** right-click and choose "Inspect". Click the pointer icon in the top-left corner of the dev tools and hover over an element to inspect it.
- **Safari:** Safari > Preferences > **Advanced** tab > check "Show Develop menu in menu bar". Then Develop > Show Web Inspector.
- **Firefox:** hamburger menu (upper right) > More Tools > Web Developer Tools.

### Common Features

- Inspect and highlight specific HTML elements and view that element's information, such as box model data and styles.
- A **Console** window to write and run simple JavaScript from within the developer tools.
- A **responsive device mode** to view the rendered HTML on different screen sizes.

### Bonus: Live Edit

Click into the HTML code in the Elements panel, change the content of an element and see the page change. You just "hacked" the game's website... well, not really: the page resets after a refresh, but it's a fun trick.

### More Resources

- Google Chrome DevTools (documentation)
- Safari Developer Tools Overview
- Firefox DevTools User Docs

> [!TIP]
> Developer Tools are the fastest way to learn HTML. Find any game page you like, inspect
> it, and read the tags the author chose. Ten minutes of that teaches more than an hour of
> guessing.

---

## XP Earned: Key Takeaways

- 🧱 **Elements** = opening tag + content + closing tag.
- 📐 **Indent** with two spaces to show nesting.
- 🔠 Six heading levels, but only one `<h1>` per file.
- ↩️ `<br>` and `<img>` are **self-closing** tags.
- 🖍️ `<b>`, `<i>`, `<u>`, `<s>` format text (CSS is the modern way).
- 📋 `<ul>` for bullets, `<ol>` for numbers, `<li>` for each item.
- 🔗 `<a href>` links, `<img src>` images.
- 🔍 Developer Tools let you inspect any page.

---

## Loot Table: Real-World Use Cases

- 📰 Articles, blogs and news pages
- 📋 Recipes, to-do lists and menus
- 🧑‍🎤 Profile and fan pages
- 🔗 Link pages and simple portfolios
- 🎮 Boss pages, item catalogs and patch notes — the same markup, different words

---

## 🎮 Side Quests: Practice Exercises

1. Make a `bio.html` page with an `<h1>`, two paragraphs and a list of your hobbies.
2. Add a link that opens your favorite site and an email link with `mailto:`.
3. Use all four text formatting tags in one paragraph.
4. Open Developer Tools on any site and change a heading's text.
5. **Boss fight:** build `bestiary.html` with one `<h1>`, an `<h2>` per creature, an `<img>` with `alt`, and a `<ul>` of weaknesses plus an `<ol>` of drops for each of three creatures.

---

## 🔗 See Also

- [[00b - HTML Cheatsheet]] — every element from this chapter on one page
- [[02 - Structure & Attributes]] — next chapter: page skeleton, comments, attributes
- [[03 - Forms]] — collecting player input
- [[04 - Semantic HTML]] — giving the page a meaningful layout

---