# 08. Fondos y Shorthands

**Versión original en inglés:** [08 - Backgrounds & Shorthands.md](08%20-%20Backgrounds%20&%20Shorthands.md)

**Curso:** CSS
**Tema:** `text-decoration` en profundidad, `background-color`, `background-image`, `background-size` y `background-repeat`, los shorthands `border` y `font`, y el proyecto final de invitación
**Tags:** `#css` `#web-development` `#backgrounds` `#shorthand` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-F7DF1E?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-36_--_41-7C5CFF?style=for-the-badge" alt="Lecciones 36 a 41">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Dos mitades: las **decoraciones** — control completo de `text-decoration` y propiedades
de fondo — y los **shorthands** — `border` y `font` como declaraciones de una línea que
comprimen cuatro líneas de CSS en una. El capítulo cierra con una pantalla de invitación:
una invitación a la fiesta de lanzamiento de Emberfall estilizada exactamente con esas
herramientas. Referencia: [[00b - Chuleta de CSS]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Los shorthands son la forma que tiene CSS de decir "ya sabes la versión larga" — una
> declaración (`border: 3px dashed #f00`) que empaqueta cuatro, siempre que respetes el
> orden y los valores obligatorios.

---

## 36. Decoración, en Profundidad

`text-decoration` controla las líneas decorativas que se añaden a los elementos de texto,
y acepta **cuatro sub-valores** — o el shorthand que los combina:

| Sub-valor | Opciones |
| :--- | :--- |
| **Línea** | `underline`, `overline`, `line-through` |
| **Estilo** | `solid`, `wavy`, `dotted`, `dashed`, `double` |
| **Color** | Con nombre, Hex o RGB |
| **Grosor** | En píxeles, p. ej. `2px` |

```css
/* Subrayado personalizado para indicadores de error tipo corrector */
span {
  text-decoration: underline wavy red 2px;
}
```

Léelo de izquierda a derecha: *línea, estilo, color, grosor*. Cualquiera puede omitirse —
el shorthand solo recuerda lo que le des.

> [!NOTE]
> Los parciales funcionan: `text-decoration: underline` es perfectamente válido y es el
> más sencillo de la familia. El shorthand no es "todo o nada".

---

## 37. Fondos

### `background-color`

Aplica un color de fondo sólido. Acepta las mismas tres notaciones que `color`:

```css
div {
  background-color: red;            /* Color con nombre */
  background-color: rgb(0, 0, 255); /* Función RGB */
  background-color: #ffff00;        /* Hexadecimal */
}
```

### `background-image` y Reglas de Pantalla

Las imágenes pueden fijarse como fondo de un elemento con la función `url()`:

```css
#inner {
  width: 400px;
  height: 400px;
  background-image: url("https://images.unsplash.com/photo-...");
  background-size: cover;
  background-repeat: no-repeat;
}
```

| Propiedad | Valores | Efecto |
| :--- | :--- | :--- |
| `background-size` | `contain` / `cover` | `contain` ajusta la imagen entera dentro; `cover` rellena la caja y recorta el sobrante |
| `background-repeat` | `no-repeat` / `repeat` | `no-repeat` dibuja la imagen una vez; `repeat` la repite en mosaico |

> [!WARNING]
> El valor predeterminado `repeat` es la razón por la que una imagen de fondo de pronto
> se repite por toda la página. Para un fondo único casi siempre quieres `cover` **y**
> `no-repeat` a la vez.

---

## 38. El Shorthand `border`

La propiedad `border` es un shorthand que combina **grosor, estilo y color** en una sola
declaración.

### Versión larga vs. Shorthand

```css
/* Versión larga */
span {
  border-width: 3px;
  border-style: dashed;
  border-color: #ff0000;
}

/* Shorthand — la misma regla, una línea */
span {
  border: 3px dashed #ff0000;
}
```

| Pieza | Qué hace |
| :--- | :--- |
| `border-width` | El grosor, en unidades como `px` |
| `border-style` | `solid`, `dashed`, `dotted`, `double`, `groove`, `ridge`… |
| `border-color` | Con nombre, `rgb()` o Hex |

> [!IMPORTANT]
> `border` necesita un **estilo** para renderizarse: `border: 3px red;` sin estilo es
> invisible, porque el estilo predeterminado es `none`. El grosor y el color sin estilo
> son fantasmas.

---

## 39. El Shorthand `font`

La propiedad `font` declara varios ajustes tipográficos en una sola línea.

### Reglas de Sintaxis

- **Valores obligatorios:** `font-size` y `font-family` — sin ellos, el shorthand se niega a existir.
- **Regla de orden:** los valores opcionales como `font-weight` deben ir **antes** de `font-size`.
- **Fuente de respaldo:** termina siempre con una familia genérica (`sans-serif`, `cursive`…).

### Versión larga vs. Shorthand

```css
/* Versión larga */
span {
  font-family: Georgia, serif;
  font-weight: 800;
  font-size: 12px;
}

/* Shorthand — peso primero, luego tamaño, luego familia */
span {
  font: 800 12px Georgia, serif;
}
```

> [!CAUTION]
> **Compatibilidad entre navegadores**
> Algunos sub-valores de los shorthands se comportan de forma inconsistente entre
> navegadores — Safari en particular tiene sus propias ideas sobre ciertos valores de
> `text-decoration`. Los shorthands ahorran líneas; no perdonan. Prueba los exóticos en
> cada plataforma que publiques.

### Práctica: Bordes y Fuentes Juntos

```css
h1 {
  border: 2px solid black;
}

p {
  font: bold 18px Arial, sans-serif;
}
```

Fíjate en que `bold` es un peso con palabra clave que sustituye a `700`, situado en la
casilla de *peso* antes de `18px` — la regla de orden en acción.

---

## 40. Contenedores Anidados

Los fondos y los shorthands brillan cuando los elementos viven dentro de otros elementos.
Considera un marco de pergamino y su obra interior:

### HTML

```html
<div id="outer">
  <div id="inner"></div>
</div>
```

### CSS

```css
#outer {
  width: 500px;
  height: 500px;
  background-color: lightskyblue;
}

#inner {
  width: 400px;
  height: 400px;
  background-image: url("https://images.unsplash.com/photo-...");
  background-size: cover;
  background-repeat: no-repeat;
}
```

`#inner` mide 400px. Su fondo se pinta con `cover`, así que la obra llena toda la caja y
recorta lo que no cabe — en una ventana a mitad de tamaño, el mismo código sigue llenando
la caja. El contenedor (`#outer`) se queda como un color de fondo discreto.

> [!NOTE]
> Este patrón de dos cajas es cada avatar-sobre-banner, icono-sobre-marco y viñeta-sobre-
> captura de la UI de un juego. Elige el color exterior y decide después cómo debe encajar
> la imagen interior.

---

## 41. Invitación de la Fiesta

### Checkpoint: Resumen del Capítulo

- `text-decoration`: línea + estilo + color + grosor, en una declaración.
- Fondos: `background-color` para rellenos sólidos; `background-image` + `size` +
  `repeat` para obra de arte.
- `border: width style color` y `font: weight size family` comprimen las versiones largas.

### Proyecto: Estás Invitado

Una invitación estilizada para la fiesta de lanzamiento de Emberfall. El HTML es pura
estructura — cada gramo de estilo viene de los dos shorthands que acabas de aprender.

#### HTML (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Invitación</title>
</head>
<body>
  <div id="invite-wrapper">
    <h1>¡Estás Invitado!</h1>
    <div id="invite-text">
      <p>
        Ven con nosotros a una noche de brasas, risas y buena compañía en la fiesta de
        lanzamiento más esperada del año. Nos alegra invitarte a nuestra soirée
        exclusiva, donde se reencuentran los grupos de Cinderlight Fest y el estudio
        enseña la primera build jugable de la expansión Salas Profundas.
      </p>
      <p>
        Habrá música en vivo con The Ashen Choir, cócteles de brasa exclusivos y un
        primer vistazo al artbook. El código de vestimenta es aventurero casual — ven
        disfrazado de tu clase favorita.
      </p>
      <p>¡No podemos esperar para verte allí!</p>
    </div>
    <p id="itinerary">
      Fecha: <br />
      Hora: <br />
      Lugar: <br />
      Confirma antes del <span>15 de octubre de 2026</span> para avisarnos de que vendrás.
    </p>
    <p>Atentamente,</p>
    <span>Alan</span>
  </div>
</body>
</html>
```

#### CSS (`styles.css`)

```css
#invite-wrapper {
  width: 50%;
  padding: 25px;
  background-color: #2b2b36;
  color: #ffffff;
  border: 2px solid #ff6b35;
  border-radius: 8px;
  margin: auto;
}

h1 {
  font-family: Arial, sans-serif;
  text-align: center;
}

#invite-text {
  width: 85%;
}

#itinerary {
  text-align: center;
}
```

> [!TIP]
> **Versión para game devs**
> El contenedor de la invitación es una tarjeta de inicio de misión; `#itinerary` es la
> lista de objetivos. Fecha, hora, lugar y una fecha límite de confirmación — tres líneas
> de información centradas — es la anatomía exacta de una pantalla de inscripción a raid.
> El capítulo [[09 - Modelo de Caja y Bordes]] explica por qué `padding`, `border` y
> `margin` se comportan como acaban de hacerlo.

---

## XP Earned: Lo que te llevas

- 📝 `text-decoration: underline wavy red 2px` — línea, estilo, color, grosor.
- 🖼️ `background-color` rellena; `background-image` + `size: cover` + `no-repeat` pinta.
- 🧱 `border: 3px dashed #ff0000` sustituye tres líneas largas — pero necesita un **estilo**.
- 🔤 `font: 800 12px Georgia, serif` empaqueta peso+tamaño+familia — tamaño y familia son
  obligatorios y el orden es fijo.
- 🧫 Cajas anidadas: color exterior, obra interior, `cover` decide el recorte.

---

## Loot Table: Casos de Uso Reales

- 🎨 Fondos, banners y parallax en páginas de juegos
- 🏷️ Marcos de tarjetas, bordes de botones e invitaciones/pantallas intermedias
- ✉️ Tarjetas de anuncio con una sola línea `font` por rol de texto
- 🖼️ Pares avatar/banner dimensionados con `cover` y un color de contenedor

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Escribe el mismo borde en versión larga y luego en shorthand — demuestra que el resultado coincide.
2. Fija una imagen de fondo con `contain` y luego con `cover` — describe la diferencia de recorte.
3. Dale a una caja de diálogo `font: 600 1.1rem Georgia, serif` y comprueba el requisito de orden.
4. Construye una segunda variante de invitación con borde `dashed` y otro fondo.
5. **Pelea de jefe:** reconstruye la invitación como una tarjeta de inscripción a raid —
   título, tres líneas de información, fecha límite de confirmación — usando solo los
   shorthands `border`, `font` y de fondo.

---

## 🔗 Ver También

- [[09 - Modelo de Caja y Bordes]] — por qué los bordes, el padding y el margin se comportan así
- [[07 - Fuentes y Texto]] — la versión larga detrás del shorthand `font`
- [[02 - Colores y Medidas]] — cada notación de color usada aquí, explicada
- [[10 - Espaciado y Box Sizing]] — padding y margin, lo que sigue

---