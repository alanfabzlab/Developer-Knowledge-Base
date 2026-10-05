# 00b. Chuleta de HTML

**Versión original en inglés:** [00b - HTML Cheatsheet.md](00b%20-%20HTML%20Cheatsheet.md)

**Curso:** HTML
**Tema:** Referencia rápida de los elementos, las etiquetas, los comentarios y los tipos de enlace del módulo
**Tags:** `#html` `#web-development` `#chuleta` `#referencia` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Cubre-Cap%C3%ADtulos_01_y_02-7C5CFF?style=for-the-badge" alt="Capítulos 01 y 02">
  <img src="https://img.shields.io/badge/Tipo-Chuleta-00C2A8?style=for-the-badge" alt="Chuleta">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #E34F26, #2DD4BF, #E34F26, transparent); margin: 24px 0;" />

Una sola página para todo el módulo. Cada elemento de esta chuleta se introdujo en [[01 - Fundamentos de HTML]] o en [[02 - Estructura y Atributos]]: aquí no hay nada nuevo. Los atributos, `class` frente a `id`, las bases de CSS y los campos de formulario están en [[00c - Chuleta de HTML II]].

> [!TIP]
> Imprímela o déjala en un panel divided junto a tu editor. Una página escrita sin comprobar
> el nombre de la etiqueta en esta hoja es como ocurre la sopa de `<div>`: anidar contenedores
> porque nada de la hoja parecía encajar.

---

## 🔬 Anatomía de un elemento

```html
<p class="intro">¡Hola Mundo!</p>
```

| Parte | Ejemplo | Qué hace el navegador |
| :--- | :--- | :--- |
| Etiqueta de apertura | `<p` | Anuncia un elemento y su tipo |
| Atributo | `class="intro"` | Ajuste extra, como `name="value"` |
| Corchete de cierre | `>` | Termina la etiqueta de apertura |
| Contenido | `¡Hola Mundo!` | Lo que se renderiza dentro del elemento |
| Etiqueta de cierre | `</p>` | Donde acaba el elemento — fíjate en la `/` |

> [!NOTE]
> Los atributos van **dentro** de la etiqueta de apertura, antes del `>`, y siempre con su
> valor entre comillas dobles: `<p class="intro">`, nunca `<p class=intro>`.

### Elementos vacíos (autocerrados)

Algunos elementos no tienen contenido y por tanto no tienen etiqueta de cierre. Se escriben
`<br>`, no `<br></br>`:

| Elemento | Nota |
| :--- | :--- |
| `<br>` | Salto de línea |
| `<img>` | Imagen |
| `<input>` | Control de formulario |
| `<hr>` | Línea horizontal |
| `<meta>` | Metadatos en `<head>` |

El `/>` de `<br />` es un residuo válido de XHTML, inofensivo en HTML5. `<br>` es la forma moderna.

---

## 🧱 Esqueleto de la página

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Título de la página</title>
    <style>
      /* Aquí va el CSS */
    </style>
  </head>
  <body>
    <!-- Aquí va el contenido visible -->
  </body>
</html>
```

| Línea | Para qué existe |
| :--- | :--- |
| `<!DOCTYPE html>` | Declara un documento HTML5; **no** tiene etiqueta de cierre |
| `<html>` | Elemento raíz; todo lo demás vive dentro |
| `<head>` | Información para el navegador — invisible en la página |
| `<title>` | El texto de la pestaña del navegador |
| `<body>` | Todo lo visible; exactamente uno por archivo |

---

## 🧰 Elementos

### Documento y estructura

| Elemento | Propósito |
| :--- | :--- |
| `<!DOCTYPE html>` | Declara un documento HTML5 (sin etiqueta de cierre) |
| `<html>` | Elemento raíz de la página |
| `<head>` | Información para el navegador, no visible en la página |
| `<title>` | Texto que se muestra en la pestaña del navegador |
| `<body>` | Todo el contenido visible (solo uno por archivo) |
| `<div>` | Contenedor de bloque genérico / sección |
| `<span>` | Contenedor en línea genérico |
| `<style>` | Estilos CSS de la página (en `<head>`) |
| `<link>` | Conecta un recurso externo (CSS, icono) |

### Texto

| Elemento | Propósito |
| :--- | :--- |
| `<h1>` a `<h6>` | Encabezados, de mayor a menor (solo un `<h1>` por archivo) |
| `<p>` | Párrafo |
| `<br>` | Salto de línea (autocerrado) |
| `<b>` / `<strong>` | Negrita / importancia |
| `<i>` | Cursiva |
| `<u>` | Subrayado |
| `<s>` | Tachado |

### Listas, enlaces y medios

| Elemento | Propósito |
| :--- | :--- |
| `<ul>` | Lista desordenada (con viñetas) |
| `<ol>` | Lista ordenada (con números) |
| `<li>` | Elemento de lista |
| `<a>` | Enlace (ancla) |
| `<img>` | Imagen (autocerrado) |

### Interacción

| Elemento | Propósito |
| :--- | :--- |
| `<form>` | Formulario que recopila datos del usuario |
| `<input>` | Control interactivo dentro de un formulario (autocerrado) |
| `<label>` | Texto que etiqueta a un campo |
| `<textarea>` | Campo de texto multilínea |
| `<select>` | Lista desplegable |

> [!TIP]
> `<b>`, `<i>`, `<u>` y `<s>` sirven para aprender, y el curso de CSS los sustituye por
> `font-weight`, `font-style` y `text-decoration`.úsalos igualmente y tu próxima hoja de
> estilos-Holandesas peleará contigo.

---

## 💬 Comentarios

```html
<!-- Comentario de una línea -->
<!--
  Comentario
  de varias líneas
-->
<p>Texto visible. <!-- Esta parte no se renderiza. --></p>
```

Los comentarios documentan la intención y también pueden ocultar código mientras experimentas.
Son además el sitio más fácil donde dejar una mentira: `<!-- arreglar esto luego -->` sobrevive
durante años.

---

## 🔗 Tipos de enlace

```html
<a href="https://example.com">Sitio web</a>
<a href="https://example.com" target="_blank">Abrir en una pestaña nueva</a>
<a href="mailto:nombre@example.com">Correo</a>
<a href="tel:212-555-0100">Teléfono</a>
<a href="sms:212-555-0123">Mensaje de texto</a>
<a href="#id-de-seccion">Saltar a una sección de la misma página</a>
```

| Valor de `href` | Abre |
| :--- | :--- |
| `https://…` | Otra página |
| `mailto:…` | El cliente de correo del visitante |
| `tel:…` | El teclado para marcar, en móviles |
| `sms:…` | El compositor de mensajes |
| `#id` | Un punto dentro de la misma página |

---

## 🪄 Atajos de las herramientas de desarrollo

| Navegador | Windows / Linux | macOS |
| :--- | :--- | :--- |
| Chrome | `ctrl` + `shift` + `c` | `cmd` + `option` + `i` |
| Safari | n/d | `option` + `cmd` + `c` |
| Firefox | `ctrl` + `shift` + `i` | `cmd` + `option` + `i` |

---

## ⚠️ Trampas que conviene memorizar

| Trampa | Qué ocurre realmente |
| :--- | :--- |
| Dos etiquetas `<h1>` | Nada se rompe, pero el documento pierde su título único |
| Dos etiquetas `<body>` | El navegador las fusiona en silencio; el archivo miente sobre su estructura |
| `alt` ausente en un `<img>` | Los lectores de pantalla anuncian el nombre del archivo, y una imagen rota no muestra nada útil |
| `<br></br>` | Aparece una etiqueta de cierre suelta como texto en algunos casos — `<br>` no tiene final |
| Indentar con tabuladores | Funciona, pero la vault y casi todos los equipos usan dos espacios |
| Anidar `<p>` dentro de `<p>` | HTML no válido; el navegador cierra el primer `<p>` y la maquetación se mueve |
| Pulsar `enter` para una nueva línea en HTML | Se ignora — usa `<br>`. HTML colapsa los espacios repetidos |
| Usar `<b>` para dar estilo | Funciona, y luego pelea con el curso de CSS. Usa CSS |

---

## 🎮 La versión en una sola página

Todo lo de esta hoja en un archivo — la entrada del bestiario de Emberfall:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Emberfall — Bestiario</title>
  </head>
  <body>
    <h1>Bestiario de Emberfall</h1>

    <h2>Limo de Brasa</h2>
    <img src="limo-de-brasa.png" alt="Un limo que brilla como lava">
    <p>Lento, frágil, se divide en dos limos más pequeños al morir.</p>

    <h3>Debilidades</h3>
    <ul>
      <li>Daño de frío</li>
      <li>Ataques físicos</li>
    </ul>

    <h3>Botín</h3>
    <ol>
      <li>Gel de limo</li>
      <li>Fragmento de brasa</li>
    </ol>

    <a href="https://example.com/limo-de-brasa">Entrada completa</a>
    <a href="mailto:archivista@example.com">Informar de una corrección</a>
  </body>
</html>
```

---

## 🔗 Ver también

- [[00c - Chuleta de HTML II]] — atributos, `class` vs `id`, base de CSS, campos de formulario
- [[01 - Fundamentos de HTML]] — dónde se presentan estos elementos, con ejercicios
- [[02 - Estructura y Atributos]] — esqueleto de página, comentarios, atributos y selectores
- [[03 - Formularios]] — los elementos interactivos, en profundidad

---