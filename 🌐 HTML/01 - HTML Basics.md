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
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #E34F26, #2DD4BF, #E34F26, transparent); margin: 24px 0;" />

The first chapter of the language that gives every web page its bones. By the end of it you
will have written a band page from scratch — headings, formatted text, lists, a link and an
image — and you will know how to inspect any page on the internet to find out how it was
built. Element and tag reference: [[00b - HTML Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> HTML does not *draw* anything and it does not *run* anything. It **labels** content: this
> run of characters is a heading, this one is a list item, this other one is a link. Every
> other thing you want a browser to do arrives later, with CSS and JavaScript.

---

## 01. Shooting Star

> [!NOTE]
> **Key information**
> **HTML** (**H**yper**T**ext **M**arkup **L**anguage) was created by **Tim Berners-Lee** in 1991 as the foundation of the World Wide Web. Today, every website in the world uses HTML.

HTML is a **markup language**: it marks up content on a web page and tells the browser what each piece is.

### The Three Core Web Technologies

| Technology | Role |
| :--- | :--- |
| **HTML** | Creates the **structure** of a web page |
| **CSS** | Styles the **appearance** of a page |
| **JavaScript** | Makes it **interactive** |

This course focuses on HTML. The files we create use the **`.html`** file extension.

### Code Editor

A **code editor** is a text editor that can write, edit and run code.

### Exercise: First Web Page

Type these two lines into the editor, replace the placeholder text, and press **Run**:

```html
<h2>Write the date</h2>
<p>Write your wish</p>
```

- Replace `Write the date` with today's date.
- Replace `Write your wish` with a wish.

You just created your first web page with HTML.

> [!TIP]
> The files in this module are plain `.html` files in a folder. Nothing needs to be installed
> and nothing needs to be built — see [[02 - Filesystem]] for navigating to the folder and
> opening the file in a browser.

---

## 02. Elemental

### Elements

**Elements** are the smallest building blocks of the language. An element usually consists of an **opening tag**, the **content**, and a **closing tag**. A **tag** is enclosed in angle brackets.

```html
<p>Hello World!</p>
```

- `<p>` is the opening tag.
- `Hello World!` is the content.
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

### Exercise: Elemental

Create `elemental.html` that shows the four ancient Greek elements (Fire, Water, Earth, Air) in the browser, nicely indented.

```html
<body>
  <p>Fire</p>
  <p>Water</p>
  <p>Earth</p>
  <p>Air</p>
</body>
```

---

## 03. Newspaper

### Headings

HTML has **six levels of headings**, from `<h1>` to `<h6>`. `<h1>` is the largest and `<h6>` is the smallest.

```html
<h1>Heading level 1</h1>
<h2>Heading level 2</h2>
<h3>Heading level 3</h3>
<h4>Heading level 4</h4>
<h5>Heading level 5</h5>
<h6>Heading level 6</h6>
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
  <h1>Breaking News</h1>
  <p>Florida man robs convenience store with an alligator.<br>Leaves a baby Crocs behind.</p>
</body>
```

A **self-closing tag** doesn't need a separate closing tag (there is no `</br>`). `<br>` is the first one we meet.

> [!WARNING]
> **The mistake everyone makes once**
> Pressing `enter` inside a `<p>` looks correct in the editor and produces a single line in
> the browser. Whitespace is **collapsed**: any run of spaces, tabs and newlines inside an
> element becomes one space. `<br>` is the only way to break a line from HTML.

### Exercise: Newspaper

Create `newspaper.html` with what was happening in the news on the day you were born:

- `<h1>` heading for the title.
- `<h3>` heading for the date.
- `<p>` paragraph(s) for the blurb.
- `<br>` for line breaks.

```html
<h1>The Daily News</h1>
<h3>January 1, 2000</h3>
<p>Major events were happening around the world today.<br>Replace this with real headlines from your own date.</p>
```

---

## 04. Corporate Talk

### Text Formatting

| Element | Effect |
| :--- | :--- |
| `<b>` | **bold** text |
| `<i>` | *italicize* text |
| `<u>` | <u>underline</u> text |
| `<s>` | ~~strikethrough~~ text |

```html
<b>This text is using bold formatting.</b><br>
<i>This text is using italics formatting.</i><br>
<u>This text is using underline formatting.</u><br>
<s>This text is using strikethrough formatting.</s><br>
```

> [!NOTE]
> `<b>` is just for bolding text stylistically. HTML also has `<strong>`, which conveys that the content is **important** and also styles it as bold.

All four tags together in a classroom announcement:

```html
<p>This is the reminder that the <i>final exam</i> is <b>mandatory</b>.<br>
It will be held on <u>Monday, October 14th</u> at <s>7PM</s> 8PM EST.</p>
```

> [!NOTE]
> These tags are good for learning basic styling, but are **no longer best practice**. Other ways to style text are covered with CSS.

### Exercise: Corporate Talk

Recreate the exact format of some corporate jargon in `corporate.html` using `<p>`, `<b>`, `<i>`, `<s>` and `<u>`.

```html
<p>
  <b>Cutting Down, Ramping Up:</b> We have a robust strategy for <s>low-hanging fruits</s> mission-critical objectives that move the needle <i>at all costs</i>. It's time to double down on <b>revenue growth</b> while <u>cutting costs</u>. This is a win-win initiative, a win for us and <i>our amazing shareholders!</i>
</p>

<p>
  <b>P.S.</b> After several strong sales months, we are printing <b>Employee Appreciation Tees</b>! Will go on sale Monday.
</p>
```

---

## 05. Sous-Chef

### Lists

HTML has two types of lists:

- `<ul>` → **Unordered** lists (bullet points)
- `<ol>` → **Ordered** lists (numbered)

Each item is wrapped in a `<li>` **list item** element.

```html
<ul>
  <li>🧺 Go to laundromat.</li>
  <li>🖥️ Code for 45 min.</li>
  <li>🛁 Take a bubble bath.</li>
</ul>
```

`<ul>` is great for listing things in any order. To number the list, use `<ol>`:

```html
<ol>
  <li>🧺 Go to laundromat.</li>
  <li>🖥️ Code for 45 min.</li>
  <li>🛁 Take a bubble bath.</li>
</ol>
```

### Exercise: Sous-Chef

Create `chef.html` with a recipe you've been craving: an **unordered** list for the ingredients and an **ordered** list for the cooking instructions.

```html
<h2>Ingredients</h2>
<ul>
  <li>2 slices of bread</li>
  <li>2 slices of cheese</li>
  <li>1 tbsp butter</li>
</ul>

<h2>Instructions</h2>
<ol>
  <li>Butter one side of each bread slice.</li>
  <li>Place cheese between the unbuttered sides of the bread.</li>
  <li>Cook on a skillet over medium heat until golden brown on both sides.</li>
</ol>
```

> [!TIP]
> This is the shape of almost every game data screen: a `<ul>` of stats, an `<ol>` of steps,
> a `<table>` for the rest. A quest log, a recipe, a skill list and a deck of cards are the
> same three elements in a different order.

---

## 06. Lost Pet

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
<a href="mailto:frankie@example.com">📧</a>
<a href="tel:212-555-0100">🤙</a>
<a href="sms:212-555-0123">💬</a>
```

### Images

Use the `<img>` image element:

```html
<p>Here's a cute pic:</p>
<img src="https://example.com/cute-pic.jpg">
```

- `<img>` is another **self-closing** tag.
- The `src` attribute ("source") specifies the file path of the image.
- For most images, you can find the path by right-clicking the image and choosing **Copy Image Address**.

> [!IMPORTANT]
> An `<img>` without `alt` is a bug. If the image fails to load, the visitor sees a broken
> icon and no explanation — and a screen reader announces the file path out loud.

### Exercise: Lost Pet

Your friend lost their pet. Create `pet.html` that includes:

- The pet name.
- A pet picture with `<img>`.
- A short description.
- Contact info with `<a>`.

```html
<h1>Lost Dog: Barnaby</h1>
<img src="https://placehold.co/300" alt="Lost dog Barnaby">
<p>Barnaby is a friendly brown dog who went missing last night wearing a red collar.</p>
<a href="mailto:owner@example.com">Contact Owner</a>
```

---

## 07. Favorite Band

### Chapter Recap

- HTML elements, tags and indentation.
- Heading tags: `<h1>` - `<h6>`.
- Paragraph and line breaks: `<p>`, `<br>`.
- Text formatting: `<b>`, `<i>`, `<u>`, `<s>`.
- Unordered and ordered lists: `<ul>`, `<ol>`.
- Links and images: `<a>`, `<img>`.

### Project: Favorite Band

Create `band.html` for your favorite artist using **all** the elements learned and **at least two types of text formatting**. It should include:

- The name of the artist.
- A picture of the artist or album cover.
- A short blurb about the artist.
- A link to the artist's website.
- The members in an unordered list.
- Top 5 favorite songs in an ordered list.

```html
<h1>Daft Punk</h1>
<img src="https://placehold.co/300" alt="Daft Punk">

<p>Daft Punk was an <b>iconic French electronic music duo</b> formed in Paris. They achieved <i>immense success</i> worldwide in the synthpop and house genres.</p>

<a href="https://daftpunk.com">Visit Official Website</a>

<h2>Band Members</h2>
<ul>
  <li>Thomas Bangalter</li>
  <li>Guy-Manuel de Homem-Christo</li>
</ul>

<h2>Top 5 Favorite Songs</h2>
<ol>
  <li>One More Time</li>
  <li>Digital Love</li>
  <li>Harder, Better, Faster, Stronger</li>
  <li>Around the World</li>
  <li>Get Lucky</li>
</ol>
```

> [!TIP]
> **Game dev version**
> The band page is the same page as an enemy card or a character sheet. Swap the heading for
> the creature name, the blurb for the lore, the unordered list for the ability list and the
> ordered list for the drop table. Chapter [[02 - Structure & Attributes]] takes that card
> and gives it `class` and `id` so a stylesheet can target it.

---

## Bonus Article: Developer Tools

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

### Bonus: Lil' Prank

Click into the HTML code in the Elements panel, change the content of an element and see the page change. You just "hacked" a website... well, not really: the page resets after a refresh, but it's a fun trick.

### More Resources

- Google Chrome DevTools (documentation)
- Safari Developer Tools Overview
- Firefox DevTools User Docs

> [!TIP]
> Developer Tools are the fastest way to learn HTML. Find any page you like, inspect it, and
> read the tags the author chose. Ten minutes of that teaches more than an hour of guessing.

---

## Key Takeaways

- 🧱 **Elements** = opening tag + content + closing tag.
- 📐 **Indent** with two spaces to show nesting.
- 🔠 Six heading levels, but only one `<h1>` per file.
- ↩️ `<br>` and `<img>` are **self-closing** tags.
- 🖍️ `<b>`, `<i>`, `<u>`, `<s>` format text (CSS is the modern way).
- 📋 `<ul>` for bullets, `<ol>` for numbers, `<li>` for each item.
- 🔗 `<a href>` links, `<img src>` images.
- 🔍 Developer Tools let you inspect any page.

---

## Common Use Cases

- 📰 Articles, blogs and news pages
- 📋 Recipes, to-do lists and menus
- 🧑‍🎤 Profile and fan pages
- 🔗 Link pages and simple portfolios
- 🎮 Enemy cards, item catalogs and quest logs — the same markup, different words

---

## 🎮 Practice Exercises

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

---