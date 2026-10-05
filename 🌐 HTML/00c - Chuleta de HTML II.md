# 00c. Chuleta de HTML II

**Versión original en inglés:** [00c - HTML Cheatsheet II.md](00c%20-%20HTML%20Cheatsheet%20II.md)

**Curso:** HTML
**Tema:** Atributos, `class` frente a `id`, bases de CSS dentro de HTML y campos de formulario
**Tags:** `#html` `#web-development` `#chuleta` `#atributos` `#formularios` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Cubre-Cap%C3%ADtulos_02_y_03-7C5CFF?style=for-the-badge" alt="Capítulos 02 y 03">
  <img src="https://img.shields.io/badge/Tipo-Chuleta-00C2A8?style=for-the-badge" alt="Chuleta">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #E34F26, #2DD4BF, #E34F26, transparent); margin: 24px 0;" />

La segunda mitad de la hoja de referencia: todo lo que personaliza un elemento. Los atributos
lo etiquetan, `class` e `id` lo nombran, `<style>` lo pinta y `<input>` lo hace interactivo.
[[00b - Chuleta de HTML]] cubre los propios elementos.

> [!NOTE]
> Un atributo es la única forma de configurar un elemento. No hay ningún modo de marcar un
> elemento como encabezado salvo usar el elemento correcto, y los atributos solo llevan ajustes.
> Mantener separados esos dos trabajos es toda la idea de esta hoja.

---

## 🏷️ Atributos

Un atributo es un par `nombre="valor"` dentro de la etiqueta de apertura:

```html
<elemento nombre="valor">Contenido</elemento>
```

| Atributo | Se usa en | Significado |
| :--- | :--- | :--- |
| `src` | `<img>` | Ruta del archivo / URL de la imagen |
| `alt` | `<img>` | Texto alternativo (accesibilidad, mostrado si la imagen falla) |
| `width` | `<img>` | Ancho de la imagen |
| `href` | `<a>` | A dónde lleva el enlace |
| `target="_blank"` | `<a>` | Abre el enlace en una nueva pestaña |
| `type` | `<ol>`, `<input>` | Estilo de numeración (`"a"`, `"i"`) o tipo de campo |
| `class` | cualquier elemento | Etiqueta compartida por muchos elementos (lista separada por espacios) |
| `id` | cualquier elemento | Etiqueta única (un solo elemento, sin espacios) |
| `style` | cualquier elemento | CSS en línea |
| `value` | `<input type="submit">` | Texto del botón |
| `minlength` / `maxlength` | `<input>` de texto | Número mínimo / máximo de caracteres |
| `required` | `<input>` | Debe rellenarse antes de enviar el formulario |
| `min` / `max` / `step` | `<input type="number">` | Rango y paso del número |
| `action` / `method` | `<form>` | Dónde y cómo se envían los datos del formulario |

Varios atributos pueden ir en la misma etiqueta, separados por espacios:

```html
<img src="limo-de-brasa.png" alt="Limo de brasa" width="300">
```

---

## 🆚 `class` frente a `id`

| | `class` | `id` |
| :--- | :--- | :--- |
| Cuántos por elemento | Muchos (`class="a b c"`) | Uno |
| Cuántos elementos lo comparten | Muchos | Uno (debe ser único) |
| Selector CSS | `.nombre` | `#nombre` |
| Destino de enlace | no | sí, con `href="#nombre"` |

Convención de nombres: minúsculas y palabras separadas por guiones (`tarjeta-amigo`).

> [!TIP]
> Puede haber muchos alumnos en una **clase**, pero cada alumno debe tener un **ID**
> único. Esa frase basta para recordar la diferencia.

---

## 🌳 Padres, hijos y hermanos

- **Padre:** contiene a otros elementos.
- **Hijo:** está directamente dentro de un padre.
- **Nieto:** está dentro de un hijo.
- **Hermanos:** comparten el mismo padre directo.

```text
<html>
└── <body>
    └── <ul>                <-- padre de los <li>
        ├── <li>Mario</li>  <-- hermano de los demás <li>
        └── <li>Luigi</li>
```

```mermaid
flowchart TD
    A["html"] --> B["head"]
    A --> C["body"]
    C --> D["p"]
    D --> E["i"]
    C --> F["ul"]
    F --> G["li 1"]
    F --> H["li 2"]
```

En ese árbol, `<head>` y `<body>` son hijos de `<html>`, `<i>` es hijo de `<p>` y nieto de
`<body>`, y los dos `<li>` son hermanos porque comparten el mismo padre.

---

## 🎨 CSS dentro de HTML

### En línea, con el atributo `style`

```html
<span style="color:red; text-decoration:underline;">rojo</span>
```

La propiedad y el valor se separan con `:`; varios estilos se separan con `;`.

### Con el elemento `<style>` en `<head>`

```html
<style>
  span { text-decoration: underline; }    /* por elemento */
  .ranger-div { width: 50%; }             /* por clase    */
  #red-ranger { background-color: red; }   /* por id       */
</style>
```

| Selector | Coincide con |
| :--- | :--- |
| `span` | Todos los elementos `<span>` |
| `.ranger-div` | Elementos con `class="ranger-div"` |
| `#red-ranger` | El elemento con `id="red-ranger"` |

### Propiedades imprescindibles al principio

| Propiedad | Ejemplo | Efecto |
| :--- | :--- | :--- |
| `color` | `color: blue;` | Color del texto |
| `background-color` | `background-color: pink;` | Color de fondo |
| `width` / `height` | `width: 50%; height: 100px;` | Tamaño |
| `text-align` | `text-align: center;` | Alineación del texto |
| `border` | `border: 3px solid blue;` | Borde |
| `margin` | `margin: auto;` | Espacio exterior |
| `display` | `display: inline-block;` | Cómo se distribuye el elemento |
| `text-decoration` | `text-decoration: underline;` | Subrayado, tachado, etc. |

> [!WARNING]
> Los atributos `style` en línea solo tienen sentido para un valor puntual que nadie va a
> cambiar dos veces. En cuanto una regla aparece en más de un elemento, ponla en un bloque
> `<style>` — y, cuando avance el curso, en su propio archivo CSS.

---

## 📝 Campos de formulario

| Campo | Código | Comportamiento |
| :--- | :--- | :--- |
| Texto | `<input type="text">` | Caja de texto sencilla |
| Correo | `<input type="email">` | Comprueba que haya un `@` válido |
| Contraseña | `<input type="password">` | Oculta el texto con puntos |
| Número | `<input type="number" min="0" max="67" step="2">` | Permite números con flechas y límites |
| Enviar | `<input type="submit" value="Enviar">` | Botón para enviar el formulario |

```html
<form>
  Nombre de usuario:<br>
  <input type="text" minlength="3" maxlength="20" required>
  <br><br>
  Correo electrónico:<br>
  <input type="email" required>
  <br><br>
  Contraseña:<br>
  <input type="password" minlength="8" maxlength="64" required>
  <br><br>
  <input type="submit">
</form>
```

| Atributo de `<form>` | Valor | Significado |
| :--- | :--- | :--- |
| `action` | `""` o una URL | A dónde van los datos al enviar |
| `method` | `"get"` / `"post"` | Cómo se envían los datos |

Todos los `<input>` deben estar dentro de **un único** `<form>`: el formulario es el sobre
que lleva todos los valores al servidor.

---

## ✅ Buenas prácticas

- Indentar con **dos espacios**.
- Un solo `<h1>` y un solo `<body>` por archivo.
- Escribir siempre texto `alt` para las imágenes.
- Usar comentarios con moderación y eliminarlos cuando ya no sirven.
- Mantener cada `<input>` dentro de un solo `<form>`.
- Preferir CSS a `<b>`, `<i>`, `<u>` y `<s>` para el estilo (se ve en el curso de CSS).

---

## ⚠️ Trampas que conviene memorizar

| Trampa | Qué ocurre realmente |
| :--- | :--- |
| Dos elementos comparten un `id` | El salto `href="#id"` y el selector `#id` solo alcanzan el primero |
| Usar mayúsculas en `id` o `class` | El selector `.ciudad` no coincide con `class="Ciudad"` |
| `id="mi id"` con un espacio | El destino del enlace se rompe — `id` no admite espacios |
| `style="color:red"` sin comillas | Funciona en muchos navegadores, pero falla si el valor lleva espacios |
| Olvidar `:` o `;` en `style` | La declaración siguiente se descarta en silencio |
| `<input>` fuera de `<form>` | Se muestra, pero pulsar Intro no envía nada |
| Pensar que `maxlength` valida | Solo limita la escritura; para bloquear el envío necesitas `minlength` |
| Dar estilo con `<b>` e `<i>` | Mal uso semántico que tendrás que deshacer en el curso de CSS |

---

## 🔗 Ver también

- [[00b - Chuleta de HTML]] — elementos, etiquetas, comentarios y tipos de enlace
- [[02 - Estructura y Atributos]] — dónde se introducen `class`, `id` y `<style>`
- [[03 - Formularios]] — campos, tipos y validación, lección a lección

---