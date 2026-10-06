# 01. Fundamentos de CSS

**Versión original en inglés:** [01 - CSS Basics.md](01%20-%20CSS%20Basics.md)

**Curso:** CSS
**Tema:** Qué es CSS, anatomía de una regla, conectar la hoja de estilos, comentarios de desarrollo y tu primera pantalla con estilo
**Tags:** `#css` `#web-development` `#basics` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Lecciones-01_--_05-7C5CFF?style=for-the-badge" alt="Lecciones 01 a 05">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

El primer capítulo del lenguaje que pinta la web. HTML dio a Emberfall su esqueleto;
este módulo le da la piel — colores, tipografías, maquetación y animaciones. Al terminar
este capítulo habrás convertido una pantalla de título sin estilos en un banner de jefe
terminado. La referencia de selectores para todo lo que viene:
[[00b - Chuleta de CSS]].

> [!NOTE]
> **Todo el capítulo en una frase**
> CSS no *contiene* contenido y no *ejecuta* lógica. Lo que hace es **describir la
> apariencia**: este encabezado es rojo, este panel tiene 20px de aire, estas tarjetas
> se colocan en fila. El marcado se queda donde HTML lo dejó — CSS decide cómo *se ve*.

---

## 01. Moneda

> [!NOTE]
> **Información clave**
> **CSS** (**C**ascading **S**tyle **S**heets) fue propuesto por **Håkon Wium Lie** en 1994
> y se convirtió en recomendación del W3C en 1996. Hoy, da estilo a todas las páginas web
> del mundo.

CSS es un **lenguaje de estilos**: pinta una página con colores, tipografías,
maquetación y animaciones, mientras HTML sigue describiendo qué es cada pieza de contenido.

### Las tres tecnologías principales de la web

| Tecnología | Rol | En la web de un juego |
| :--- | :--- | :--- |
| **HTML** | Crea la **estructura** | El esqueleto: qué paneles existen en la HUD |
| **CSS** | Da **estilo** a la apariencia | La piel: colores, tipografías, maquetación |
| **JavaScript** | La hace **interactiva** | El motor: barras de vida que se actualizan |

Este módulo se centra en CSS. Los archivos que crearemos usan la extensión **`.css`**.

### Misión: Antes y Después

Abre cualquier página que quieras, haz clic derecho sobre el encabezado principal y elige
**Inspect**. En el panel *Styles* verás reglas como `color: tomato;` — eso es CSS, en
vivo. Borra una de esas reglas y la página cambiará delante de ti. Recarga para devolverla.

Acabas de ver a CSS hacer su único trabajo: cambiar cómo se ve algo sin tocar lo que dice.

---

## 02. Anatomía de una Regla

En CSS escribimos **reglas** que definen cómo se estilizan los elementos HTML de una página.

### Estructura de una regla CSS

```css
selector {
  property: value;
}
```

| Parte | Ejemplo | Qué hace |
| :--- | :--- | :--- |
| **Selector** | `h1` | Identifica el (los) elemento(s) HTML a estilizar (`div`, `p`, `h1`…) |
| **Bloque de declaraciones** | `{ … }` | Las llaves que contienen una o más declaraciones |
| **Propiedad** | `color` | *Qué* aspecto del elemento cambia |
| **Valor** | `tomato` | *Cómo* cambia ese aspecto |
| **Declaración** | `color: tomato;` | Un par `propiedad: valor;` — siempre termina en `;` |

```css
h1 {
  color: tomato;
  font-size: 32px;
}
```

Dos declaraciones viven dentro de un bloque: el `<h1>` de la página se vuelve rojo tomate
*Y* crece hasta 32 píxeles de alto. Cada declaración necesita su punto y coma — la última
incluida, porque la siguiente regla que escribas no esperará a que te acuerdes.

> [!WARNING]
> **El error que todos cometen una vez**
> Un `;` que falta o un `:` disperso se traga el resto del bloque en silencio. El
> navegador no lanza un error — simplemente descarta las declaraciones después de la
> errata y renderiza la página a medio estilizar. Si una regla "no hace nada", revisa
> primero la puntuación de la regla de *encima*.

---

## 03. Conectando

Un archivo `.css` no hace nada por sí solo: la página HTML tiene que decirle dónde vive.
La conexión vive en el `<head>` mediante un elemento `<link>`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Emberfall — Pantalla de Título</title>
</head>
<body>
  <h1>Emberfall</h1>
</body>
</html>
```

- `href="styles.css"` — la ruta a la hoja de estilos, junto al archivo `.html`.
- `rel="stylesheet"` — le dice al navegador *qué tipo* de recurso es.

> [!NOTE]
> Dos archivos, una conexión: `index.html` guarda las palabras, `styles.css` guarda la
> pintura. Mantenlos lado a lado en la misma carpeta y la ruta relativa se reduce a un
> solo nombre de archivo.

### Misión: Primera Regla

Crea `styles.css` junto a tu página y pinta la pantalla de título:

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

Recarga la página. Fondo de mazmorra oscuro, título naranja brasa — tu primera hoja de
estilos está viva.

---

## 04. Comentarios de Desarrollo

Los comentarios de CSS los ignora el navegador; existen para quien lea el archivo después —
normalmente tú, dentro de seis meses.

```css
/* Los comentarios en CSS van entre barras inclinadas y asteriscos. */

h1 {
  /* Esta declaración está comentada: ahora mismo no hace nada. */
  color: tomato;
}
```

Todo lo que esté entre `/*` y `*/` es invisible para el navegador, así que un comentario
puede documentar una regla o desactivarla temporalmente mientras experimentas.

> [!TIP]
> Comentar una declaración en lugar de borrarla es el depurador más barato que existe:
> si el fallo desaparece, el comentario te acababa de decir qué línea era la culpable.

---

## 05. Pantalla de Título

### Checkpoint: Resumen del Capítulo

- **CSS** pinta; HTML contiene el contenido, JavaScript ejecuta lógica.
- Una regla es `selector { property: value; }` y cada declaración termina en `;`.
- `<link href="styles.css" rel="stylesheet">` conecta los dos archivos.
- `/* … */` escribe un comentario que el navegador ignora.

### Proyecto: Pantalla de Título de Jefe

Crea `index.html` + `styles.css` para la pantalla de título de tu propio juego: un
encabezado héroe, una imagen de jefe y un pie con lema — todo estilizado desde el archivo
externo.

### HTML (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Emberfall — Pantalla del Guardián</title>
</head>
<body>
  <main>
    <section id="hero-copy">
      <h1>Emberfall</h1>
      <p>El Guardián del Noveno Piso te espera.</p>
    </section>
    <section id="hero-img">
      <figure>
        <img src="https://placehold.co/250" alt="Un guardián alto y armado sosteniendo una linterna." width="250" />
      </figure>
    </section>
    <footer>
      <p>Un roguelike en la tradición de Emberfall</p>
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
> **Versión para game devs**
> Esta es la estructura de toda pantalla de inicio jamás publicada: un contenedor
> centrado, una imagen héroe con esquinas redondeadas y una franja de pie. El capítulo
> [[02 - Colores y Medidas]] te entrega la paleta — colores con nombre, `rgb()` y hex —
> para cambiar mis valores predeterminados por los tuyos.

---

## XP Earned: Lo que te llevas

- 🎨 **CSS** = Cascading Style Sheets: colores, tipografías, maquetación, animación.
- 🧩 Una regla es **selector + bloque de declaraciones**; cada declaración es `propiedad: valor;`.
- ⛓️ `<link href="styles.css" rel="stylesheet">` conecta la página con su pintura.
- 🔚 Cada declaración termina en `;` — una que falta mata en silencio el resto del bloque.
- 💬 `/* comentario */` es invisible para el navegador y útil para humanos.

---

## Loot Table: Casos de Uso Reales

- 🎮 Pantallas de inicio, skins de HUD y tiendas de juegos
- 📰 Blogs temáticos, landings y portafolios
- 🎨 Renovaciones de marca: mismo HTML, nueva hoja de estilos, nueva identidad
- 🧪 Prototipos: estilizar una página sin tocar una sola línea de marcado

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Escribe una regla que pinte todos los `<p>` de una página de un color distinto.
2. Comenta esa regla y comprueba que el texto vuelve a negro.
3. Añade un segundo enlace de hoja de estilos y demuestra que gana el último.
4. Reconstruye la pantalla de título de arriba con la paleta de tu juego.
5. **Pelea de jefe:** estiliza una página `patch_notes.html` — fondo oscuro, encabezados
   `<h2>` naranjas, pie verde — usando solo un archivo `.css` externo.

---

## 🔗 Ver También

- [[00b - Chuleta de CSS]] — selectores y sintaxis en una sola página
- [[02 - Colores y Medidas]] — siguiente capítulo: paletas y unidades
- [[03 - Selectores Pt. 1]] — apuntar las reglas que ya sabes escribir
- [[01 - Fundamentos de HTML]] — el marcado que este módulo estiliza

---
