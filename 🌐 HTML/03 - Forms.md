# 03. Forms

**Spanish version:** [03 - Formularios.md](03%20-%20Formularios.md)

**Course:** HTML
**Topic:** Forms, `<input>` Types, Email & Password, Validation (`minlength`, `maxlength`, `required`), Number Inputs
**Tags:** `#html` `#web-development` `#forms` `#inputs` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Lessons-15_--_18_Partial-7C5CFF?style=for-the-badge" alt="Lessons 15 to 18">
  <img src="https://img.shields.io/badge/Status-Work_in_progress-FFA500?style=for-the-badge" alt="Work in progress">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #E34F26, #2DD4BF, #E34F26, transparent); margin: 24px 0;" />

The chapter where a web page stops being a document and starts **asking the visitor something**. Every Sign Up, Login, Checkout and character-creation screen you have ever used is a `<form>` with `<input>`s inside. The best news in this chapter: the browser validates most of it for free, before a single line of your code runs.

> [!WARNING]
> **Work in progress:** this note covers lessons 15 to 18 (partially). Lesson 18 (RSVP) is
> still in flight — radio and checkbox inputs are announced, not yet documented — and the rest
> of the chapter will be added later.

---

## 15. Google

### Forms

What do Sign Up, Login and Checkout pages have in common? They all **collect user input data**. From a search bar to signing in to your favorite app, forms are part of everyday digital life.

How a form works:

1. The user enters some information.
2. The user presses a "Submit" button.
3. The info gets sent somewhere and processed.

To create a form, use the `<form>` element:

```html
<form action="" method="">
  <!-- More code will go here -->
</form>
```

Two attributes are used with `<form>`:

| Attribute | Purpose |
| :--- | :--- |
| `action` | Specifies **where** the form data is sent after submitting |
| `method` | Specifies **how** the form data is processed (usually `"post"` or `"get"`) |

> [!NOTE]
> For the rest of the chapter, `action` and `method` won't appear in the examples. The forms still render just fine.

### Inputs

The `<input>` element is an **interactive control** for entering data. Its `type` attribute determines the kind of input. The two used most often:

```html
<form>
  <input type="text">
  <input type="submit">
</form>
```

- `"text"` renders a plain textbox.
- `"submit"` turns the `<input>` into a button for submitting the form data.

By default the submit button says "Submit". Change its text with the `value` attribute:

```html
<input type="submit" value="Submit Form!">
```

> [!NOTE]
> The `<input>` element uses a **self-closing** tag.

> [!WARNING]
> `action=""` with an empty value means "submit nowhere". The page reloads and nothing
> happens — which looks exactly like "my form is broken". Until a backend exists, that is
> correct behavior, not a bug.

### Quest: Search Portal

Recreate the original Google search bar in `google.html`. Starting from this code:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Google</title>
  </head>
  <body>
    <!-- Form code goes here -->
  </body>
</html>
```

Replace the comment with a `<form>` element (set `action` and `method` to `""` or leave them out) and add inside:

- A `<p>` with "Search the web using Google!"
- An `<input>` with the `type` set to `"text"`.
- One or two `<br>` line breaks.
- Another `<input>` with `type="submit"` (its text should say "Google Search").

```html
<form action="" method="">
  <p>Search the web using Google!</p>
  <input type="text">
  <br><br>
  <input type="submit" value="Google Search">
</form>
```

> [!NOTE]
> If we submit this form, nothing will happen, because we haven't told the form where to send the data.

---

## 16. Sign Up v1

### Input Types

How do we make sure the right data goes into a form? If a form asks for an email, how can it tell that it's a *valid* email address containing an `@`? HTML forms have several **built-in input types**. Two of them:

### Email

```html
<input type="email">
<input type="submit">
```

It checks whether the submitted value is a valid email address. If the `@` is missing, the browser shows an error message ("Please include an '@' in the email address...").

### Password

```html
<input type="password">
<input type="submit">
```

The text entered is **hidden** and displayed as dots.

There are many other `<input>` types in HTML forms (check the complete list in the MDN docs).

> [!IMPORTANT]
> All the `<input>` elements should be placed inside a **single** `<form>` element. Think of the `<form>` as an **envelope** that contains all the data we want to send to the server.

### Quest: Character Creation I

Create `sign_up.html` with a classic sign up page: a "Sign Up" heading, Username, Email and Password fields, and a Submit button. Start from:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Sign Up</title>
  </head>
  <body>
    <form>
      <h2>Sign Up</h2>

      Username:<br>
      <!-- Text input -->
      <br><br>

      Email:<br>
      <!-- Email input -->
      <br><br>

      Password:<br>
      <!-- Password input -->
      <br><br>

      <!-- Submit input -->
    </form>
  </body>
</html>
```

Replace the comments with `<input>` elements (a username, an email, a password and a submit button):

```html
<form>
  <h2>Sign Up</h2>

  Username:<br>
  <input type="text">
  <br><br>

  Email:<br>
  <input type="email">
  <br><br>

  Password:<br>
  <input type="password">
  <br><br>

  <input type="submit">
</form>
```

> [!TIP]
> `type="email"` and `type="password"` are the cheapest validation in web development: one
> attribute each, and the browser blocks submission on its own. `type="number"` will do the
> same for digits in lesson 18.

---

## 17. Sign Up v2

### Minlength & Maxlength

Beyond input types, we can further **validate** inputs with these attributes:

- `minlength`: sets the **minimum** number of characters.
- `maxlength`: sets the **maximum** number of characters.

```html
<input type="password" minlength="4" maxlength="10">
```

The user can't type past 10 characters, and an error message appears if they try to submit fewer than 4.

### Required Data

Some forms require input before they can be submitted. The `required` attribute enforces this:

```html
<form>
  Name: <input type="text" required>
  <br><br>
  Favorite Color: <input type="text">
  <input type="submit">
</form>
```

Here the "Name" `<input>` is marked as required. If it is left blank, the browser blocks the submission and points at the empty field.

> [!WARNING]
> `maxlength` is **not** validation. It stops the keystroke; it says nothing about whether the
> value is any good. `minlength` is the attribute that blocks submission. Use both when you
> want the keystroke cap *and* the rule enforced.

### Quest: Character Creation II

Revisit `sign_up.html` and add some form validation:

- Give **username** a `minlength` of 3 and a `maxlength` of 20.
- Give **password** a `minlength` of 8 and a `maxlength` of 64.
- Make the username, email and password **required**.

Then try submitting the form with incorrect inputs!

```html
Username:<br>
<input type="text" minlength="3" maxlength="20" required>
<br><br>

Email:<br>
<input type="email" required>
<br><br>

Password:<br>
<input type="password" minlength="8" maxlength="64" required>
<br><br>

<input type="submit">
```

> [!TIP]
> **Game dev version**
> This is the character creation screen. `minlength="3"` on a player name and
> `minlength="8"` on a password are the same two lines a client would validate before it ever
> opens a socket — except the browser does them for free, in every language, with no
> dependencies.

---

## 18. RSVP *(in progress)*

### Input Type: Number

Numbers may be involved in forms, from a person's age to the number of items bought at a store. To prompt for numbers:

```html
<input type="number">
```

When the cursor hovers over this input, "up" and "down" arrow buttons appear on the right side.

By default these buttons move the number up or down by **1**. The `step` attribute changes that:

```html
<input type="number" step="2">
```

The `max` and `min` attributes set how high or low the input can go:

```html
<input type="number" min="0" max="67">
```

Try entering `1000` in an input with `max="67"` and see what happens: the browser flags it as invalid.

> [!NOTE]
> `max` and `min` do not stop you from *typing* `1000` — they flag the value as invalid when
> you submit. The arrows respect them; the keyboard does not.

### Quest Preview: Raid RSVP

The starter file for `rsvp.html` hints at what comes next in the chapter: a text input for the name, a group of **radio inputs** ("Are you coming?"), **checkbox inputs** (dietary restrictions) and a submit button.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>RSVP</title>
  </head>
  <body>
    <form>
      <h2>RSVP</h2>
      <p>Come and make our special day ...</p>
      <br>
      Name: <!-- Text input here -->
      <br><br>
      Are you coming?<br>
      <!-- 3 radio inputs here, sharing ... -->
      <br><br>
      Any dietary restrictions for main ...
      <!-- 3 or 5 checkbox inputs here -->
      <br><br>
      <!-- Submit input here -->
    </form>
  </body>
</html>
```

*(Text is cut off in the original screenshots. The solution and the rest of the chapter are still pending.)*

---

## 🧩 The Form Vocabulary So Far

| Input | Code | Validates |
| :--- | :--- | :--- |
| Text | `<input type="text">` | Nothing by itself |
| Email | `<input type="email">` | Must contain a valid-looking address |
| Password | `<input type="password">` | Hidden; pair with `minlength` |
| Number | `<input type="number">` | Digits, with `min` / `max` / `step` |
| Submit | `<input type="submit" value="Send">` | — |

| Constraint | Applies to | What it does |
| :--- | :--- | :--- |
| `required` | Any `<input>` | Blocks submission when empty |
| `minlength` | Text-like inputs | Minimum characters before it will submit |
| `maxlength` | Text-like inputs | Caps how many characters can be typed |
| `min` / `max` | `<input type="number">` | Lowest and highest accepted value |
| `step` | `<input type="number">` | Increment for the arrows, and the gap the value must fall on |

---

## XP Earned: Key Takeaways

- 📝 A **form** collects input and sends it somewhere (`action`) in a certain way (`method`).
- 🔤 `<input type="text">`, `"email"`, `"password"`, `"number"` and `"submit"` cover the basics.
- ✅ Browsers validate for free: `email` checks the `@`, `minlength`/`maxlength` check length, `required` blocks empty fields, `min`/`max` limit numbers.
- 📦 Keep all `<input>` elements inside one `<form>`.

---

## Loot Table: Real-World Use Cases

- 🔍 Search bars
- 👤 Sign up and login pages
- 🎟️ RSVP and registration forms
- 🛒 Checkout pages
- 🎮 Character creation, party invites and loadout builders — every form is a small character sheet

---

## 🎮 Side Quests: Practice Exercises

1. Build a login page with email and password, both required.
2. Make a number input for age that only accepts 0 to 120.
3. Create a contact form with name, email and a custom submit button text.
4. Try submitting each form with invalid data and read the browser messages.
5. **Boss fight:** build `character_sheet.html` — a text input for the name (`minlength="2"`, `maxlength="16"`), an email input for the account, a number input for level (`min="1"`, `max="99"`), a password input (`minlength="8"`) and a submit button that says "Create Character".

---

## 🔗 See Also

- [[00c - HTML Cheatsheet II]] — the input and constraint reference table
- [[02 - Structure & Attributes]] — `class` and `id` for grouping and styling a form
- [[01 - HTML Basics]] — the elements a form is built from

---