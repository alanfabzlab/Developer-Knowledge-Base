# 05. Pseudoelementos

**Versión original en inglés:** [05 - Pseudo-elements.md](05%20-%20Pseudo-elements.md)

**Curso:** CSS
**Tema:** `::first-letter` y `::first-line`, `::before` y `::after`, la propiedad `content`, tooltips, iconos de enlace y las reglas básicas
**Tags:** `#css` `#web-development` `#pseudo-elements` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-F7DF1E?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-21_--_25-7C5CFF?style=for-the-badge" alt="Lecciones 21 a 25">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Hasta ahora has estilizado elementos enteros. Los **pseudoelementos** te dejan mirar
*dentro* de un elemento — su primera letra, su primera línea, o contenido que ni siquiera
existe en el HTML — sin añadir una sola etiqueta. El capítulo hermano sobre estados es
[[06 - Pseudoclases]]; entre los dos puedes estilizar cualquier cosa que le suceda a un
elemento. Referencia: [[00b - Chuleta de CSS]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Un pseudoelemento selecciona una *parte* de un elemento — partes reales como
> `::first-letter` y partes inventadas como `::before` — escrito como `selector::nombre`
> con **doble dos puntos**.

---

## 21. Segunda Piel

Los pseudoelementos crean, seleccionan y estilizan partes específicas de un elemento HTML
sin marcado extra. Usan **doble dos puntos** `::` seguidos del nombre del pseudoelemento.

### Sintaxis básica

```css
selected-element::pseudo-element {
  /* Estilos CSS aquí */
}
```

> [!NOTE]
> CSS3 escribía estos con un solo dos puntos (`:first-letter`). El CSS moderno escribe
> doble (`::first-letter`), y los navegadores aún aceptan ambos — pero lo estándar que
> debes usar es el doble.

---

## 22. Letra Inicial, Línea Inicial

### `::first-letter`

Apunta a la primera letra del texto dentro de un elemento de nivel bloque — la clásica
letra inicial de toda novela de fantasía jamás impresa.

### `::first-line`

Apunta a la primera línea completa de texto dentro de un elemento de bloque. (Cuando
estrechas la ventana y el texto se parte, el navegador vuelve a decidir qué palabras son
"primera línea" — es una decisión de renderizado, no un conjunto fijo de palabras.)

```html
<p>La mazmorra de Emberfall abre al amanecer, y las linternas se apagan una a una.</p>
```

```css
p {
  width: 25%;
}

p::first-letter {
  font-size: 36px;
  font-family: 'Gill Sans', sans-serif;
  text-decoration: underline;
  text-decoration-color: black;
  color: #e01a18;
}

p::first-line {
  font-size: 1.5em;
}
```

El `<p>` del HTML queda intacto: ni un span contenedor, ni una clase extra. CSS fue
directo a la letra.

---

## 23. Before, After y la Propiedad `content`

`::before` y `::after` crean contenido decorativo o suplementario que se renderiza
**antes o después** del contenido real del elemento, usando la propiedad especial
`content`.

```css
selected-element::before {
  content: "Botín: ";
  /* Otros estilos aquí */
}

selected-element::after {
  content: " ✨";
  /* Otros estilos aquí */
}
```

- El pseudoelemento está **vacío** en el HTML — `content` es lo que pone texto dentro.
- Se puede estilizar de todo: tamaño, color, fondo, bordes, márgenes.

```css
p::after {
  content: " 📄";
}
```

> [!IMPORTANT]
> `content` es obligatorio. Una regla `::before` o `::after` sin `content` — ni siquiera
> `content: ""` — no renderiza nada, porque la caja en sí es lo que `content` crea.

---

## 24. Aplicaciones Prácticas

Considera este HTML:

```html
<p>
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements" target="_blank">Pseudoelementos</a>
  son palabras clave que se añaden a un selector y nos permiten estilizar una parte
  específica del elemento seleccionado.
</p>
```

### Aplicación A: Añadir un Tooltip

Combina un pseudoelemento con la pseudoclase `:hover` para hacer flotar una explicación
sobre un enlace — sin JavaScript y sin marcado extra.

Suponiendo que `body` tiene `position: relative`:

```css
body {
  position: relative;
}

a:hover::before {
  content: "Coincide cuando el usuario interactúa con un elemento mediante un dispositivo apuntador, sin activarlo necesariamente. Se dispara generalmente cuando el usuario pasa el cursor sobre un elemento.";
  position: absolute;
  top: 35px;
  bottom: 0;
  width: 15%;
  height: max-content;
  border: 2px solid;
  background-color: lightyellow;
  color: black;
  padding: 2px;
}
```

Pasa el cursor sobre el enlace y aparece una caja de ayuda; retíralo y desaparece. El
pseudoelemento vive entero en CSS.

> [!TIP]
> Los tooltips son la versión para game devs del codex al pasar el cursor: las
> estadísticas de objetos, el alcance de las habilidades y las pistas de recetas en
> cualquier pantalla de inventario son exactamente este patrón — texto que solo existe
> mientras el cursor lo pide.

### Aplicación B: Añadir un Icono

Decora el final de un hipervínculo dentro de un párrafo con un pequeño icono de enlace
externo:

```css
a::after {
  background-image: url("https://static-00.iconduck.com/assets.00/external-link-icon.png");
  background-size: 10px 10px;
  display: inline-block;
  width: 10px;
  height: 10px;
  content: "";
  margin-left: 2.5px;
}
```

Fíjate en las comillas vacías de `content: ""` — la caja se crea vacía y la imagen se pinta
dentro con `background-image` y `url()`. Cada enlace de la wiki recibe el icono sin una
sola etiqueta `<img>`.

---

## 25. Reglas Básicas

Dos reglas deciden si una regla de pseudoelemento es válida en absoluto.

### Regla 1: Un Solo Uso Por Elemento

El mismo pseudoelemento no puede usarse dos veces en el mismo elemento seleccionado. El
segundo bloque se ignora en silencio:

```css
/* NO VÁLIDO */
selected-element::before {
  content: "Esto";
  font-size: 1.5em;
}

selected-element::before {
  content: "No funcionará";
  background-color: green;
}

selected-element::first-letter {
  font-family: "Helvetica";
}

selected-element::first-letter {
  background-color: purple;
}
```

Escribe una sola regla `::before` por elemento y pon **todas** sus declaraciones dentro —
la duplicada no aporta nada y el navegador la descarta.

### Regla 2: El Pseudoelemento Va Al Final

Un pseudoelemento debe ser la parte final del selector:

```css
/* NO VÁLIDO */
p::after.class {
  content: " ¡Esto tampoco funciona!";
  text-decoration: underline;
}

/* VÁLIDO — el pseudoelemento está al final */
p.class::after {
  content: " ¡Esto sí funciona!";
  text-decoration: underline;
}
```

Puedes apuntar primero (`p.class`) y decorar después (`::after`); no puedes decorar
primero y apuntar después.

> [!WARNING]
> Una regla que rompe estas normas no lanza error — simplemente deja de existir. Cuando un
> pseudoelemento "no hace nada", busca una segunda regla con el mismo nombre y comprueba
> dónde se sitúa el `::` dentro del selector.

### Más Recursos

- [MDN: Pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements)
- Artículo extra: Pseudoclases → [[06 - Pseudoclases]]

---

## XP Earned: Lo que te llevas

- 🧬 `selector::nombre` con **doble dos puntos** selecciona una *parte* de un elemento.
- 🔠 `::first-letter` / `::first-line` estilizan la apertura de un bloque de texto.
- 📦 `::before` / `::after` inventan contenido — `content` es lo que lo hace aparecer.
- 💬 `a:hover::before` es un tooltip sin una línea de JavaScript.
- ⚠️ Un solo pseudoelemento por elemento, y debe cerrar el selector.

---

## Loot Table: Casos de Uso Reales

- 📖 Letras iniciales en artículos y páginas de lore
- 💬 Tooltips de estadísticas de objetos, alcance de habilidades y avisos de formulario
- 🔗 Iconos de enlace externo añadidos a cada ancla
- 🏷️ Etiquetas de precio, insignias "NOVEDAD" y asteriscos de campo obligatorio — todo inyectado por CSS

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Dale a todos los `<h2>` de una página un emoji decorativo en `::after`.
2. Crea un tooltip que aparezca al pasar el cursor sobre el nombre de un jefe.
3. Rediseña la letra inicial de un párrafo de lore — tamaño, color y tipografía.
4. Añade un asterisco después de cada etiqueta de campo obligatorio con `::after`.
5. **Pelea de jefe:** escribe una regla `::before` rota y luego otra intentando el mismo
   pseudoelemento — predice cuál gana y compruébalo en las herramientas de desarrollo.

---

## 🔗 Ver También

- [[06 - Pseudoclases]] — el capítulo hermano: estilizar por estado
- [[04 - Selectores Pt. 2]] — los selectores a los que se aplican estos pseudoelementos
- [[07 - Fuentes y Texto]] — qué hacer con las letras que acabas de seleccionar
- [[00c - Chuleta de CSS II]] — pseudoclases y pseudoelementos lado a lado

---
