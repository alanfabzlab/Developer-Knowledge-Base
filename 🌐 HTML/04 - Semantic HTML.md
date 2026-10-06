# 04. Semantic HTML

**Spanish version:** [04 - HTML Semántico.md](04%20-%20HTML%20Sem%C3%A1ntico.md)

**Course:** HTML
**Topic:** Semantic HTML, `header`, `footer`, `main`, `article`, `section`, `aside`, `nav`, `figure`, `time`, Accessible Links, Entity Escapes
**Tags:** `#html` `#web-development` `#semantics` `#accessibility` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Lessons-19_--_24-7C5CFF?style=for-the-badge" alt="Lessons 19 to 24">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=FF6B35&height=70&section=header" width="100%" alt="Ember wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #E34F26, #2DD4BF, #E34F26, transparent); margin: 24px 0;" />

So far every page has been a `<div>` with some text inside. It renders, and it works — but a
browser seeing `<div>` sees nothing but a box. This chapter swaps those boxes for elements
that **state what they are**: this is the game's header, this is the walkthrough, this is the
sidebar with related builds. The rendering barely changes. Everything else does.

> [!NOTE]
> **The whole chapter in one sentence**
> Semantic HTML is a promise you make to the browser, to screen readers, to search engines and
> to your future self: *this element means this thing.* The visual result is almost
> incidental — which is exactly why it is so often skipped.

---

## 19. Top HUD

### Header, Main and Footer

Every modern page has the same three-region layout, and HTML has one element for each:

- `<header>` — typically the top of the page: logo, nav, title. It can also go inside an `<article>` or `<section>`.
- `<main>` — the unique, central content of the page. **There should only ever be one per page.**
- `<footer>` — typically the bottom: copyright, links, author. It can also go inside an `<article>` or `<section>`.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Emberfall</title>
  </head>
  <body>
    <header>
      <h1>Emberfall</h1>
      <p>A roguelike about dying in interesting places.</p>
    </header>

    <main>
      <p>The run starts in the Ember Vault and ends in the Deep Halls.</p>
    </main>

    <footer>
      <p>© 2026 Emberfall Studio. No bosses were permanently harmed.</p>
    </footer>
  </body>
</html>
```

> [!IMPORTANT]
> `<header>` and `<footer>` are **not** `<head>` and `<body>`. They live inside `<body>`,
> they render on the page, and `<header>` has no special effect on the document's metadata —
> its only jobs are the banner at the top and (when nested) the header of a section or article.
>
> A `<footer>` inside an `<article>` holds the byline, date and tags of that article — not the
> site's legal boilerplate. Two different things, two different elements.

> [!TIP]
> **Game dev version**
> `<header>` / `<main>` / `<footer>` is a viewport layout. A HUD, a game view and a menu bar
> are three roles in the same scene, and giving each its own element is the difference
> between a screen you can lay out per-region and one you can only position by hand.

### Quest: Emberfall Landing Page

Create `header_footer.html`. Inside `<body>`, add:

- A `<header>` with an `<h1>` and a short paragraph about your site or project.
- A `<main>` with at least two paragraphs (or a heading plus paragraphs).
- A `<footer>` with a `<p>` containing a copyright notice.

Then confirm in the browser that the three regions appear in that order.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Emberfall</title>
  </head>
  <body>
    <header>
      <h1>Emberfall</h1>
      <p>A roguelike about dying in interesting places.</p>
    </header>

    <main>
      <h2>Release 1.4</h2>
      <p>The Ember Vault got a new boss. The Deep Halls got darker.</p>
      <p>Nothing was rebalanced except the things that were broken.</p>
    </main>

    <footer>
      <p>© 2026 Emberfall Studio. No bosses were permanently harmed.</p>
    </footer>
  </body>
</html>
```

---

## 20. Walkthrough Article

### `article`, `section` and `aside`

### `article`

Use `<article>` for a piece of **self-contained content** that would still make sense if it were pulled out of the page and read on its own. News stories, blog posts and product reviews qualify.

For an article, it's often good practice to include a heading inside the `<article>`, along with a `<footer>` containing metadata (byline, publish date, tags).

```html
<article>
  <h2>Patch 1.4: The Warden Awakens</h2>
  <p>The Warden was a rumor in the Ember Vault. As of 1.4, the rumor has a health bar.</p>
  <footer>
    <p>Posted by <strong>Dev_Wanda</strong> on <time datetime="2026-03-14">March 14, 2026</time></p>
  </footer>
</article>
```

> [!IMPORTANT]
> An `<article>` is not a "post" or a "blog entry" specifically. It is any chunk of content
> that stands on its own: a forum thread, a product card with its own review, a wiki entry, a
> comment with enough substance to be quoted alone.

### `section`

Use `<section>` to group related content that does **not** stand alone — it needs the surrounding page for context.

For a `<section>`, it's strongly encouraged to have a heading. Many developers argue that a `<section>` without a heading is really just a `<div>`.

```html
<section>
  <h2>Boss Strategies</h2>
  <p>The Warden teleports on the third phase. Bait it with the second.</p>
</section>
```

> [!TIP]
> **Game dev version**
> An `<article>` is a quest: self-contained, with its own name, its own rewards and its own
> byline. A `<section>` is a zone: it only means something as part of the map. That
> distinction — "does this still make sense on its own?" — is the fastest way to choose
> between the two, and it applies to UI panels too.

### `aside`

Use `<aside>` for content that is **tangentially related** to the content around it — a sidebar, a pull quote, a glossary, an advert.

```html
<article>
  <h2>Patch 1.4: The Warden Awakens</h2>
  <p>The Warden was a rumor in the Ember Vault. As of 1.4, the rumor has a health bar.</p>
  <aside>
    <h3>Related builds</h3>
    <ul>
      <li>Ranger Prime — trap and punish</li>
      <li>Tank Wanda — aggro sponge</li>
    </ul>
  </aside>
</article>
```

### Quest: Patch Notes

Create `patch_notes.html` with:

1. An `<article>` for the patch announcement, with an `<h2>` title and two paragraphs.
2. Inside the `<article>`, a `<footer>` with a `<p>` naming the author and a `datetime` attribute on a `<time>` element.
3. A `<section>` for "Balance Changes" with an `<h2>` and an unordered list of at least three changes.
4. An `<aside>` inside the `<article>` with an `<h3>` and a list of two related items.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Patch Notes — Emberfall</title>
  </head>
  <body>
    <main>
      <article>
        <h2>Patch 1.4: The Warden Awakens</h2>
        <p>The Warden was a rumor in the Ember Vault. As of 1.4, the rumor has a health bar.</p>
        <p>Phase three teleports. Phase four does not. Good luck.</p>

        <aside>
          <h3>Related builds</h3>
          <ul>
            <li>Ranger Prime — trap and punish</li>
            <li>Tank Wanda — aggro sponge</li>
          </ul>
        </aside>

        <footer>
          <p>Posted by <strong>Dev_Wanda</strong> on <time datetime="2026-03-14">March 14, 2026</time></p>
        </footer>
      </article>

      <section>
        <h2>Balance Changes</h2>
        <ul>
          <li>Ember Blade damage: 14 → 17</li>
          <li>Health potion cooldown: 30s → 20s</li>
          <li>Warden phase three no longer resets aggro</li>
        </ul>
      </section>
    </main>
  </body>
</html>
```

---

## 21. Site Navigation

### `nav`

Use `<nav>` for **major navigation links**: a site menu, a table of contents, pagination.

```html
<nav>
  <ul>
    <li><a href="/loadouts">Loadouts</a></li>
    <li><a href="/bosses">Bosses</a></li>
    <li><a href="/patch-notes">Patch notes</a></li>
  </ul>
</nav>
```

A `<nav>` is not every group of links. **Links within a `<footer>` don't need a `<nav>` wrapper.** It's for substantial, site-level navigation.

> [!NOTE]
> Multiple `<nav>` elements are fine and common — one for the main menu, one for a table of
> contents in an article, one for pagination. The rule of thumb is that each one is a real
> navigational region a user relies on to move around.

> [!TIP]
> A table of contents is the clearest example: it is `<nav>` containing a list of `<a>`
> elements whose `href="#anchor"` targets headings with `id`s. That pattern is exactly how
> a game's pause menu is structured too — a list of destinations.

---

## 22. Item Showcase

### `figure` & `figcaption`

Use `<figure>` to represent self-contained content: an illustration, a diagram, a photo, a code snippet. Sometimes a `<figure>` has a caption that describes the content, which can be wrapped in a `<figcaption>` element.

```html
<figure>
  <img src="https://placehold.co/300" alt="Map of the Emberfall overworld">
  <figcaption>Figure 1: The overworld. The Deep Halls are somewhere under it.</figcaption>
</figure>
```

> [!NOTE]
> An `<img>` is not a `<figure>`. The figure is the *thing plus its caption*; the image is
> just the thing. A captioned table, a code snippet with an explanation or a diagram all work
> equally well inside a `<figure>`.

### Accessible Links

The text inside a link should describe **where the link goes**. "Click here" is a dead end for anyone navigating by voice or by screen reader — they hear "click here" with no destination.

```html
<a href="/bosses/warden">The Warden boss guide</a>
```

Also avoid raw URLs as link text. And never use the URL itself as the label:

```html
<!-- Bad -->
<a href="https://emberfall.example/wiki/warden">https://emberfall.example/wiki/warden</a>

<!-- Good -->
<a href="https://emberfall.example/wiki/warden">The Warden boss guide</a>
```

> [!IMPORTANT]
> A link that opens in a new tab should say so. If it does not, the reader loses their place
> with no warning. The same goes for links that download a file, or that trigger something
> unexpected — announce it in the link text, not in a tooltip nobody sees.

### `time`

Use `<time>` when the content is a date, a time, or both. The `datetime` attribute holds the machine-readable value; the text inside is whatever reads best for a human.

```html
<p>Patch 1.4 shipped on <time datetime="2026-03-14T18:00:00Z">March 14, 2026 at 6pm UTC</time>.</p>
```

Without `datetime`, `<time>` still marks up the text as a date for styling and parsing — but the machine-readable form is what makes it useful.

### Quest: Boss Showcase Page

Create `bosses.html` with:

1. A `<nav>` at the top with at least three links to `#warden`, `#frost-witch` and `#gilded-one`.
2. A `<main>` containing one `<article>` per boss, each with an `<h2>` carrying the matching `id`.
3. Inside each `<article>`, a `<figure>` with an `<img>` (with `alt`) and a `<figcaption>`.
4. Inside the first `<article>`, a `<p>` with a `<time datetime="...">` element for the last nerf date.
5. One external link whose text describes the destination — not "click here" and not a raw URL.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Bosses — Emberfall</title>
  </head>
  <body>
    <nav>
      <ul>
        <li><a href="#warden">The Warden</a></li>
        <li><a href="#frost-witch">The Frost Witch</a></li>
        <li><a href="#gilded-one">The Gilded One</a></li>
      </ul>
    </nav>

    <main>
      <article>
        <h2 id="warden">The Warden</h2>
        <p>Third phase teleports. Bait it with the second. Last nerfed on <time datetime="2026-03-14">March 14, 2026</time>.</p>
        <figure>
          <img src="https://placehold.co/300" alt="The Warden holding a lantern">
          <figcaption>Figure 1: The Warden, mid-phase-three.</figcaption>
        </figure>
      </article>

      <article>
        <h2 id="frost-witch">The Frost Witch</h2>
        <figure>
          <img src="https://placehold.co/300" alt="The Frost Witch surrounded by ice shards">
          <figcaption>Figure 2: Freeze, don't get frozen.</figcaption>
        </figure>
      </article>

      <article>
        <h2 id="gilded-one">The Gilded One</h2>
        <figure>
          <img src="https://placehold.co/300" alt="The Gilded One wearing gold armor">
          <figcaption>Figure 3: Every piece is a debuff.</figcaption>
        </figure>
        <a href="https://emberfall.example/wiki/the-gilded-one">The full Gilded One wiki page</a>
      </article>
    </main>
  </body>
</html>
```

---

## 23. Escape Room

### Entities & Escapes

HTML has a set of special characters called **entities**, which stand in for characters that either don't exist in plain text or that HTML reads as markup.

To display a character that **HTML uses in its syntax**, add an ampersand `&` and an identifier and a semicolon. Here are a few:

| Character | Entity | Renders as |
| :--- | :--- | :--- |
| `&` | `&amp;` | `&` |
| `<` | `&lt;` | `<` |
| `>` | `&gt;` | `>` |
| `"` | `&quot;` | `"` |
| `'` | `&apos;` | `'` |

```html
<p>&lt;p&gt; is the paragraph element, not a tag.</p>
<p>Ranger &amp; Tank make a good pair.</p>
```

Where a character like `é` or `¡` doesn't need an escape (modern HTML files are UTF-8 by
default), you can use the character directly:

```html
<p>Chispa carries a llama. 🦙</p>
```

Other entities exist for characters with no keyboard key — `&copy;` (©), `&nbsp;` (a
non-breaking space), `&hellip;` (…). A full list lives in the MDN reference.

> [!WARNING]
> The classic bug: writing `Tom & Jerry` in raw HTML. The browser reads `& Jerry` as an
> entity it does not recognise and either swallows it or prints it literally. The same
> happens with any `<` you mean as text — write `&lt;` instead. If your paragraph text is
> disappearing or your page shows "Tom Jerry", look here first.

> [!IMPORTANT]
> Inside an attribute value that contains text with quotes — `alt="The "great" sword"` —
> the inner quotes end the attribute early and the rest becomes garbage attributes. Use
> `&quot;`, or switch the attribute to single quotes.

### Quest: Escape Room

Create `escape_room.html` with four paragraphs:

1. Text containing `<` and `>` used as symbols, not as tags.
2. Text containing an ampersand.
3. A paragraph whose `alt` attribute (or a `title` attribute) contains a quoted word.
4. A paragraph with one non-breaking space (`&nbsp;`) between two words, plus one ellipsis.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Escape Room</title>
  </head>
  <body>
    <p>Chests drop loot between levels 3 and 5, never below level 3.</p>
    <p>Ranger &amp; Tank make a good pair. So do Mage &amp; Healer.</p>
    <p><img src="https://placehold.co/100" alt="The &quot;great&quot; sword"></p>
    <p>Bring&nbsp;a lantern. And hope&nbsp;for the Warden to stay asleep&nbsp;...</p>
  </body>
</html>
```

---

## 24. Hall of Fame

### Checkpoint: Chapter Recap

- `<header>` and `<footer>` are the top and bottom regions of a page — **not** `<head>` and `<body>`.
- `<main>` holds the unique central content; a page should have exactly one.
- `<article>` is self-contained content. `<section>` is content that needs its page for context.
- `<aside>` is tangentially related content: sidebars, pull quotes, glossaries.
- `<nav>` wraps major navigation, not every group of links.
- `<figure>` pairs content with an optional `<figcaption>`.
- Link text must describe the destination.
- `<time datetime="...">` marks up dates and times.
- Escape `&`, `<`, `>`, `"` and `'` with entities.

### Project: Hall of Fame

Your last build task: a single page that is *semantically correct from top to bottom*, with
every region labelled by the right element.

Create `hall_of_fame.html`:

1. `<header>` with an `<h1>` and a `<nav>` (list of three links to `#first`, `#second`, `#third`).
2. `<main>` with **three** `<article>` elements, each `id`-ed, each containing:
   - an `<h2>`,
   - a `<figure>` with an `<img>` and a `<figcaption>`,
   - a `<p>` that mentions a date inside a `<time datetime>`,
   - an `<aside>` with related info.
3. A `<section>` after the articles with a heading and a list.
4. `<footer>` with a copyright `<p>`.
5. At least one escaped entity somewhere in the text.

Then run the audit below.

> [!TIP]
> **The semantic audit** — the checklist worth memorizing:
> 1. Exactly one `<main>`?
> 2. Does every `<section>` and `<article>` have a heading?
> 3. Is every image either inside a `<figure>` or explained by its `alt`?
> 4. Does every link text say where it goes?
> 5. Is heading order correct — no jumping from `<h2>` to `<h4>`?
> 6. Any raw `&` or `<` in the text that isn't markup?
>
> If a page passes those six questions, it is in better shape than most pages on the web.

---

## 🧩 Element Selection Cheat Sheet

| You want… | Use | Not |
| :--- | :--- | :--- |
| The top banner of a page or a section | `<header>` | `<div>` |
| The unique central content | `<main>` | `<div id="content">` |
| Self-contained content (post, guide, entry) | `<article>` | `<section>` |
| Related content that needs its page | `<section>` | `<div>` |
| Sidebar, pull quote, glossary | `<aside>` | `<div class="side">` |
| Major navigation links | `<nav>` | `<div>` of `<a>`s |
| Content with a caption | `<figure>` + `<figcaption>` | `<img>` alone |
| A date or time | `<time datetime>` | Bare text |

---

## XP Earned: Key Takeaways

- 🧠 Semantic elements cost nothing at runtime and pay off in **accessibility, SEO and maintenance**.
- 🎯 The selection question is always: *does this content make sense on its own?* → `<article>`. *Does it only make sense here?* → `<section>`.
- 🧭 `<header>` / `<main>` / `<footer>` describes a page's regions; `<nav>` and `<aside>` describe roles.
- 🏷️ Every landmark element gives screen readers a heading to jump between — that navigation is the whole point.
- 🔗 Link text is UI copy: it must say where the link goes.
- ⌨️ Escape `&`, `<`, `>`, `"` and `'` or the browser will misread your text as markup.

---

## Loot Table: Real-World Use Cases

- 🏠 Landing pages with a real header, main and footer
- 📰 News sites and blogs: `<article>` per post, `<aside>` for related links
- 📚 Documentation sites: `<nav>` for the table of contents, `<section>` per chapter
- 🛒 Product pages: `<figure>` for gallery images
- 🎮 Patch notes, boss guides and codex pages: `<article>` per entry, `<time>` for the patch date

---

## 🎮 Side Quests: Practice Exercises

1. Open any website you like and find its `<header>`, `<main>` and `<footer>`. Then ask: would `<aside>` be more correct anywhere?
2. Take an old page full of `<div>`s and replace each one with the semantic element that actually describes it. Note how many get `<section>` vs `<article>`.
3. Add a `<nav>` table of contents to an article, with `href="#..."` links to headings that carry `id`s.
4. Convert every "click here" link into one that describes its destination.
5. Find a raw `&` on a real website and watch what the browser does with it.
6. **Boss fight:** build `lore_archive.html` — `<header>` with `<nav>`, a `<main>` holding five `<article>` lore entries each with a `<figure>` (image + caption), a `<time>` and an `<aside>`, a `<section>` "Timeline of the Emberfall" and a `<footer>`. Then run the six-question semantic audit on your own page and fix everything it finds.

---

## 🔗 See Also

- [[00b - HTML Cheatsheet]] — the element catalog, now including the semantic set
- [[00c - HTML Cheatsheet II]] — attributes, entities and accessibility attributes
- [[01 - HTML Basics]] — the generic elements (`<p>`, `<a>`, `<img>`) the semantic ones build on
- [[02 - Structure & Attributes]] — when a `<div>` really is the right answer
- [[03 - Forms]] — forms are landmarks too: give them a `<section>`

---