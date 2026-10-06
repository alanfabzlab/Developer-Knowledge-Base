# 10. Espaciado y Box Sizing

**Versión original en inglés:** [10 - Spacing & Box Sizing.md](10%20-%20Spacing%20&%20Box%20Sizing.md)

**Curso:** CSS
**Tema:** La propiedad `padding`, la propiedad `margin`, centrado con `margin: auto`, `box-sizing: content-box` vs `border-box`, el reset universal y el proyecto final del Archivo del Gremio
**Tags:** `#css` `#web-development` `#box-model` `#spacing` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-F7DF1E?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-47_--_53-7C5CFF?style=for-the-badge" alt="Lecciones 47 a 53">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Los bordes eran el marco; ahora la habitación en sí: **padding** (aire *dentro*), **margin**
(espacio *fuera*), el sagrado truco de centrado `margin: auto`, y `box-sizing` — la
propiedad que decide si una caja de 100px se mantiene en 100px cuando le añades padding.
El capítulo cierra con el Archivo del Gremio, una página completa construida solo con el
modelo de caja. Referencia: [[00c - Chuleta de CSS II]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Padding empuja el contenido hacia dentro, margin empuja a los vecinos hacia fuera,
> `margin: auto` centra, y `box-sizing: border-box` mantiene honestos tus tamaños
> declarados cuando el padding se une a la fiesta.

---

## 47. La Caja de Padding

El padding es el espacio entre el contenido de un elemento y su borde — **dentro** del
elemento.

### Sintaxis larga

Cada lado puede fijarse por separado:

```css
padding-top: 5px;
padding-right: 10px;
padding-bottom: 15px;
padding-left: 20px;
```

### Sintaxis shorthand

La propiedad `padding` acepta hasta cuatro valores en **orden horario — Arriba → Derecha →
Abajo → Izquierda**:

```css
/* Arriba: 5px, Derecha: 10px, Abajo: 15px, Izquierda: 20px */
padding: 5px 10px 15px 20px;
```

Variaciones comunes:

```css
/* 40px a los cuatro lados */
padding: 40px;

/* 50px arriba, derecha e izquierda; nada abajo */
padding: 50px 50px 0px 50px;
```

> [!TIP]
> Memoriza el reloj: *12 → 3 → 6 → 9*. Cada pregunta de orden — padding, margin, lados
> del borde — se responde desde esa esfera.

---

## 48. La Caja de Margin

La **caja de margin** es la capa más externa del modelo de caja. Rodea el borde y crea
separación entre los elementos adyacentes.

Como el padding, los márgenes se declaran con longhands direccionales (`margin-top`,
`margin-right`, `margin-bottom`, `margin-left`) o con el shorthand `margin` en la misma
secuencia horaria:

```css
/* Arriba: 20px, Derecha: 10px, Abajo: 20px, Izquierda: 10px */
margin: 20px 10px 20px 10px;
```

```css
/* 40px a los cuatro lados */
margin: 40px;

/* 15px arriba/abajo, 0px izquierda/derecha */
margin: 15px 0;
```

> [!NOTE]
> Los márgenes aceptan **valores negativos** — acercan un elemento a su vecino, o
> solapan dos cajas a propósito. El padding no puede ser negativo; esa es la única
> diferencia real además de de quién es el espacio que cada uno ocupa.

---

## 49. Centrado con `margin: auto`

Para centrar un elemento de nivel bloque **horizontalmente** dentro de su contenedor,
combina `margin: auto` con un `width` explícito:

```css
#container-element {
  width: 300px;
  height: 300px;
  border: 3px solid;
}

#inner-element {
  width: 100px;
  height: 100px;
  border: 1px solid;
  background-color: orange;
  margin: auto; /* Centra horizontalmente dentro del contenedor */
}
```

El navegador reparte por igual el espacio horizontal sobrante entre los dos márgenes y la
caja flota hacia el centro.

> [!IMPORTANT]
> `margin: auto` sin `width` no hace nada visible: un elemento de bloque ya se estira para
> llenar el 100% del padre, así que no queda espacio sobrante que repartir. Primero el
> ancho, luego el centrado.

---

## 50. Box Sizing: `content-box` vs `border-box`

La propiedad `box-sizing` controla cómo se calculan el ancho y el alto totales de un
elemento.

| Valor de la propiedad | Fórmula | Comportamiento |
| :--- | :--- | :--- |
| `content-box` *(predeterminado)* | Ancho total = contenido + padding + borde | Añadir padding o bordes agranda el elemento más allá del ancho declarado |
| `border-box` | Ancho total = tamaño declarado; el padding y el borde se absorben dentro | La caja conserva su tamaño declarado; el contenido se encoge para hacer sitio |

### Comparación

Con `width: 150px`, `padding: 20px`, `border: 2px` declarados:

- **`content-box`**: ancho renderizado = 150 + (20 × 2) + (2 × 2) = **194px**.
- **`border-box`**: el ancho renderizado se queda en **150px**; el área de contenido se
  estrecha hasta 150 − 40 − 4 = **106px**.

```css
/* Predeterminado: el padding se suma al ancho */
.box { width: 150px; padding: 20px; }

/* Border-box: el padding se mete dentro de los 150px */
.border-box { width: 150px; padding: 20px; box-sizing: border-box; }
```

> [!WARNING]
> **Cómo se rompe una maquetación, lección 1**
> Dos columnas `content-box` que ambas reclaman `width: 50%` desbordan su padre en cuanto
> añades padding. `border-box` es la respuesta que usa prácticamente todo framework
> moderno — por eso el reset de abajo la convierte en el predeterminado.

---

## 51. El Reset Universal

Una práctica estándar del CSS moderno es aplicar un **reset universal del modelo de caja**
al principio de la hoja de estilos con el selector universal `*`:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```

Todo elemento empieza con espaciado cero y dimensiones honestas — así, el espaciado que
escribas después es el único que existe. Sin valores predeterminados del navegador que
sorprendan, sin un margin de 8px en `body` heredado de la nada.

> [!NOTE]
> `*` apunta a todos los elementos — descendientes incluidos — así que el reset corre
> antes que cualquier regla que escribas. Mantenlo como primera regla de un archivo y
> toda caja empieza desde el mismo lienzo en blanco.

---

## 52. Misión: Espaciado del Feed

Coge el feed enmarcado de [[09 - Modelo de Caja y Bordes]] y dale el pase completo de
espaciado.

#### CSS (`styles.css`)

```css
* {
  font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}

div {
  border: 2px solid grey;
}

#post-list {
  padding-right: 40px;
}

#post-list > li {
  list-style-type: none;
}

li > div {
  text-align: left;
}

#top-img {
  width: 10em;
  height: 10em;
  border: 12px solid green;
  border-radius: 50%;
}

#outside-wrapper {
  width: 90%;
  background-color: rgb(169, 206, 221);
  text-align: center;
}

.post-wrapper {
  text-align: left;
  background-color: #f5f5f5;
  border-radius: 5px;
  padding: 50px 50px 0px 50px; /* aire dentro de la tarjeta */
}

.post-img {
  width: 100%;
  border-radius: 5px;
}
```

Observa cómo cada regla toca una capa distinta del modelo de caja: `#post-list` gana
padding, `.post-wrapper` gana padding interior, y los marcadores de lista estilizados
desaparecen para que las tarjetas queden limpias — el espaciado, no los bordes, convirtió
una lista enmarcada en un feed.

> [!TIP]
> La rareza `padding: 50px 50px 0px 50px` es deliberada: la tarjeta respira por tres lados
> y deja que el siguiente divisor toque el borde inferior. Shorthand en sentido horario,
> asimetría intencionada — todo el arte del espaciado en una sola declaración.

---

## 53. Archivo del Gremio

### Checkpoint: Resumen del Capítulo

- Padding = aire dentro; margin = espacio fuera; ambos siguen el shorthand horario.
- `margin: auto` centra horizontalmente — con un `width` explícito.
- `box-sizing: border-box` mantiene honestos los tamaños declarados; `content-box` crece con el padding.
- El reset universal pone a cero los márgenes, el padding y fuerza `border-box` en todas partes.

### Proyecto: El Archivo del Gremio

Una página de inicio de biblioteca de gremio: navegación, texto de bienvenida, búsqueda en
el catálogo y las selecciones de la temporada. Estructura HTML5 semántica pura + una hoja
de estilos que es *solo* reglas del modelo de caja.

#### HTML (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Archivo del Gremio</title>
</head>
<body>
  <header>
    <nav>
      <h1>¡Bienvenido al Archivo del Gremio!</h1>
      <a class="nav-item" href="#welcome">Inicio</a>
      <a class="nav-item" href="#catalog-form">Buscar</a>
      <a class="nav-item" href="#staff-picks">Recomendados</a>
    </nav>
  </header>
  <main>
    <section id="welcome">
      <p>Guiado por nuestra dedicación al lore y al aprendizaje, el Archivo guarda cada
      tomo, mapa y entrada de bestiario de Emberfall bajo un mismo techo.</p>
    </section>
    <section id="catalog">
      <form id="catalog-form">
        <input id="catalog-input" type="text" placeholder="Buscar en el catálogo..." />
        <input id="form-btn" type="submit" value="Buscar" />
      </form>
    </section>
    <section id="staff-picks">
      <h2>Recomendados del Archivo</h2>
      <div class="staff-pick-row">
        <img class="staff-pick-img" src="https://placehold.co/160x240" alt="Portada: Linternas de las Salas Profundas" />
        <img class="staff-pick-img" src="https://placehold.co/160x240" alt="Portada: Guía de campo de los Slimes de Brasa" />
        <img class="staff-pick-img" src="https://placehold.co/160x240" alt="Portada: El Códice del Noveno Piso" />
      </div>
    </section>
  </main>
</body>
</html>
```

#### CSS (`styles.css`)

```css
/* Reset universal y estilos base */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  width: 100%;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  text-align: center;
}

header {
  background-image: url("https://placehold.co/1200x200/1b1b2f/ff6b35?text=Guild+Archive");
  background-size: cover;
  background-repeat: no-repeat;
  height: 200px;
}

/* Reglas de cabecera y navegación */
h1 {
  margin-top: 10px;
  margin-bottom: 10px;
}

.nav-item {
  display: inline-block;
  width: 33%;
  border: 1px solid #333;
  border-radius: 5px;
  padding: 5px;
  margin: 10px;
}

/* Márgenes estructurales */
main {
  margin-top: 20px;
}

section {
  margin-top: 10px;
  margin-bottom: 10px;
}

/* Alineación del contenido del párrafo */
#welcome > p {
  text-align: center;
  margin-left: 5em;
  margin-right: 5em;
}

/* Campos del formulario de búsqueda */
#catalog-input, #form-btn {
  text-align: center;
  font-size: 1.25rem;
  font-weight: 800;
  padding: 8px;
}

#catalog-input {
  border: 2px solid #000;
  width: 37.5%;
}

/* Sección de recomendados e imágenes de portada */
#staff-picks {
  text-align: center;
}

.staff-pick-img {
  border: 1px solid #000;
  border-radius: 0 7px 7px 0; /* efecto lomo de libro: redondea solo el borde derecho */
  width: 10em;
  height: 15em;
  margin: 10px;
}
```

Lee los números como jugadas del modelo de caja: los márgenes horizontales en `em` del
texto de bienvenida lo mantienen legible a cualquier tamaño de fuente; `inline-block`
permite que los enlaces de navegación tomen ancho, padding y márgenes mientras siguen en
una línea; el `border-radius` asimétrico da forma de lomo a los tomos. Una hoja de
estilos, un modelo mental: cada regla es una capa de una caja.

> [!TIP]
> **Versión para game devs**
> Cambia "Recomendados" por "Botín de Temporada", los tomos por tarjetas de botín y
> "Buscar" por el filtro de inventario — la página es una tienda. Al modelo de caja no le
> importa qué contiene; solo se pone de acuerdo sobre las cajas.

---

## XP Earned: Lo que te llevas

- 🧽 **Padding** = aire dentro; **margin** = espacio fuera; ambos van en sentido horario.
- 🎯 `margin: auto` centra horizontalmente **con un `width`**.
- 📏 `content-box` crece con el padding; `border-box` lo absorbe dentro del tamaño declarado.
- 🧹 El reset universal — `margin: 0; padding: 0; box-sizing: border-box` — empieza con todas las cajas iguales.
- 🛠️ Una hoja de estilos puede ser 100% reglas del modelo de caja y publicar una página entera.

---

## Loot Table: Casos de Uso Reales

- 📚 Páginas de inicio de archivos, redacciones y tiendas
- 🔍 Barras de búsqueda y filas de filtros con aire para respirar
- 🎨 Portadas de libros, álbumes y colecciones con radio de lomo
- 🎮 Pantallas de tienda, entradas de codex y páginas de botín de temporada

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Escribe `padding` de 10px a todos los lados y luego 10px/20px/30px/40px — di el orden del reloj en voz alta.
2. Centra una caja de 200px en un padre a todo el ancho con `margin: auto`; quita el width y explica el salto.
3. Compara un panel `content-box` de 150px con uno `border-box` de 150px, ambos con 20px de padding.
4. Reinicia una página con la regla universal y enumera cada cambio de maquetación.
5. **Pelea de jefe:** estiliza una página `guild-members.html` — sección de bienvenida,
   formulario de búsqueda y una fila frontal de tres tarjetas — usando solo propiedades
   del modelo de caja, sin posicionamiento.

---

## 🔗 Ver También

- [[09 - Modelo de Caja y Bordes]] — las cuatro capas donde viven estas propiedades
- [[11 - Display y Posicionamiento]] — cómo fluyen las cajas en la página
- [[00c - Chuleta de CSS II]] — espaciado y dimensiones en una página
- [[08 - Fondos y Shorthands]] — el shorthand de borde sobre el que se apoya esta página

---