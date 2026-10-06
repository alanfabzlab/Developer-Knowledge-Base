# 00b. Chuleta de CSS

**Versión original en inglés:** [00b - CSS Cheatsheet.md](00b%20-%20CSS%20Cheatsheet.md)

**Curso:** CSS
**Tema:** Referencia rápida de sintaxis CSS, selectores, colores, medidas, tipografía y pseudoelementos/pseudoclases usados en el módulo
**Tags:** `#css` `#web-development` `#cheatsheet` `#reference` `#styling` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Cubre-Capítulos_01_--_06-7C5CFF?style=for-the-badge" alt="Capítulos 01 a 06">
  <img src="https://img.shields.io/badge/Tipo-Chuleta-00C2A8?style=for-the-badge" alt="Chuleta">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Una página para la primera mitad del módulo. Toda regla de aquí se presentó en
[[01 - Fundamentos de CSS]], [[02 - Colores y Medidas]], [[03 - Selectores Pt. 1]],
[[04 - Selectores Pt. 2]], [[05 - Pseudoelementos]] o [[06 - Pseudoclases]] — nada en esta
hoja es nuevo. El modelo de caja, el espaciado, el posicionamiento y flexbox viven en
[[00c - Chuleta de CSS II]].

> [!TIP]
> Imprímela, o tenla en un panel dividido junto a tu editor. La forma más rápida de
> escribir mal CSS es adivinar el nombre de una propiedad de memoria — esta hoja existe
> para que nunca tengas que hacerlo.

**El hilo narrativo del módulo: Emberfall**, un roguelike de mazmorras. Cada ejercicio
estiliza una parte de su web compañera: la pantalla de título del héroe, el mapa del
mundo, el volante del festival, el horario de la academia, las cartas de campeones. La
sintaxis es la que publica un estudio real — solo cambian las palabras.

---

## 🔬 Anatomía de una Declaración

```css
p {
  color: #FF6B35;   /* propiedad: valor; */
  font-size: 18px;
}
```

| Parte | Ejemplo | Función |
| :--- | :--- | :--- |
| Selector | `p` | A qué elemento(s) se aplica la regla |
| Propiedad | `color` | Qué se está estilizando |
| Valor | `#FF6B35` | El nuevo ajuste |
| Declaración | `color: #FF6B35;` | Propiedad más valor, siempre terminando en `;` |
| Regla / bloque | todo el `{ ... }` | Selector más sus declaraciones |

> [!NOTE]
> La última declaración de un bloque puede omitir el `;`, pero nunca dependas de ese
> hábito — un punto y coma perdido pega la siguiente línea al valor anterior y la regla
> entera se rompe.

---

## 🔗 Añadir CSS a una Página

| Método | Dónde vive | Ideal para | Notas |
| :--- | :--- | :--- | :--- |
| **Externo** | `<link rel="stylesheet" href="styles.css">` en el `<head>` | Proyectos reales | **Prefiérelo siempre** — un archivo estiliza todo el sitio |
| **Interno** | `<style> ... </style>` en el `<head>` | Demos pequeños de una página | Solo estiliza ese archivo |
| **Inline** | `style="color: blue"` en el elemento | Trucos rápidos | Especificidad máxima; pelea contra toda otra regla |

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
</head>
<body>
  <h1 style="color: blue">Inline gana todas las peleas — evítalo.</h1>
</body>
</html>
```

---

## 🎯 Selectores

### Los Básicos

| Selector | Coincide con | Ejemplo |
| :--- | :--- | :--- |
| `element` | Cada elemento de esa etiqueta | `p { }` |
| `.class` | Cada elemento con ese atributo `class` | `.hero-title { }` |
| `#id` | El único elemento con ese atributo `id` | `#top-banner { }` |
| `*` | Todos los elementos | `* { margin: 0; }` |

> [!WARNING]
> El `id` debe ser único — uno por página, usado una vez. La `class` es reutilizable y
> lo más parecido que CSS tiene a un valor amistoso por defecto. Recurre a `#id` solo
> para anclas y elementos irrepetibles.

### Combinadores

| Combinador | Espacio | `>` | `+` | `~` |
| :--- | :--- | :--- | :--- | :--- |
| Nombre | Descendiente | Hijo | Hermano adyacente | Hermano general |
| Coincide con | cualquier descendiente | solo el hijo **directo** | solo el siguiente hermano | todos los hermanos posteriores |

```css
nav a { }          /* enlaces en cualquier lugar dentro de nav */
nav > a { }        /* enlaces que son hijos directos de nav */
h2 + p { }         /* el párrafo justo después de un h2 */
h2 ~ p { }         /* todos los párrafos después de un h2 en el mismo padre */
```

### Selectores de Atributo *(capítulo 04)*

| Selector | Coincide con |
| :--- | :--- |
| `[disabled]` | Elementos con el atributo (cualquier valor) |
| `[type="text"]` | Coincidencia exacta del valor |
| `[href^="https"]` | El valor empieza con `https` |
| `[src$=".png"]` | El valor termina con `.png` |
| `[class*="post"]` | El valor contiene `post` en cualquier parte |

### Agrupación y Cascada

```css
h1, h2, h3 {
  font-family: Georgia, serif; /* la coma = "y también" */
}
```

| Concepto | Regla |
| :--- | :--- |
| Cascada | Las reglas posteriores anulan a las anteriores con igual especificidad |
| Especificidad | `inline` > `#id` > `.class` > `element` |
| `!important` | Anula todo — y empieza una pelea que nadie gana; evítalo |
| `inherit` | Fija una propiedad al valor calculado del padre |

---

## 🎨 Colores

| Notación | Ejemplo | Cuándo |
| :--- | :--- | :--- |
| Nombre | `color: rebeccapurple;` | Demos rápidos; una paleta diminuta |
| `rgb()` | `color: rgb(255, 107, 53);` | Canales con valores 0–255 |
| `rgba()` | `color: rgba(255, 107, 53, 0.5);` | Añade transparencia en el 4º canal |
| Hex | `color: #FF6B35;` | La elección de cada día — `#F6B` es corto para `#FF66BB` |
| `hsl()` | `color: hsl(25, 100%, 60%);` | Tono 0–360, saturación/luminosidad en porcentajes |

> [!TIP]
> Elige una notación por proyecto. Mezclar `#FF6B35` y `rgb(255, 107, 53)` para el mismo
> naranja es como una hoja de estilos olvida su propia identidad.

---

## 📏 Medidas

```css
p {
  font-size: 18px;
  line-height: 1.5em;
}
```

| Unidad | Relativa a | Uso típico | Lente de game dev |
| :--- | :--- | :--- | :--- |
| `px` | nada (absoluta) | bordes, sombras, tamaños fijos pequeños | 1 píxel de UI |
| `em` | el font-size del propio elemento | padding, márgenes que escalan con el texto | hereda el "tamaño" de la fuente como una familia tipográfica |
| `rem` | el font-size de la raíz (`<html>`) | espaciado consistente en toda la página | escala global — una perilla para todo |
| `%` | la propiedad equivalente del padre | anchos, altos, radios | el 100% de la caja padre |
| `vw` / `vh` | 1% del ancho / alto del viewport | heros a pantalla completa, superposiciones | la vista de cámara |
| `ch` | el ancho del glifo `0` | párrafos con ancho de lectura | una celda de letra |
| `auto` | lo decide el navegador | centrado, imágenes, desbordes | "haz lo que el contenido necesite" |

> [!IMPORTANT]
> El `em` se compone con el anidamiento (un `1.2em` dentro de un `1.2em` son `1.44em`),
> que es exactamente por qué existe `rem`. Prefiere `rem` para el ritmo de toda la página
> y reserva `em` para escalas locales de componentes que deban seguir su propia fuente.

---

## ✍️ Tipografía

### La Pila de Fuentes

```css
body {
  font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}
```

El navegador recorre la lista de izquierda a derecha hasta encontrar una fuente instalada;
la genérica final (`sans-serif`, `serif`, `monospace`) debe existir siempre.

### Propiedades de Texto de un Vistazo

| Propiedad | Qué hace | Ejemplos |
| :--- | :--- | :--- |
| `font-family` | La pila de tipografías | `Georgia, serif` |
| `font-weight` | El grosor | `normal`, `bold`, `100`–`900` |
| `font-style` | La inclinación | `normal`, `italic` |
| `text-decoration` | Líneas sobre el texto | `none`, `underline`, `line-through` |
| `text-align` | Alineación dentro de su contenedor | `left`, `center`, `right`, `justify` |
| `text-transform` | Caja de las letras | `uppercase`, `lowercase`, `capitalize` |
| `letter-spacing` | Espacio entre caracteres | `2px`, `0.1em` |
| `line-height` | Espacio entre líneas | `1.5`, `24px` — sin unidad = multiplicador |
| `text-shadow` | Resplandor / sombra tras las letras | `2px 2px 4px rgba(0,0,0,0.5)` |

```css
h1 {
  font-family: Georgia, serif;
  font-weight: 800;
  letter-spacing: 2px;
  text-transform: uppercase;
  text-shadow: 2px 2px 0 #1b1b2f; /* el look de la pantalla de título de Emberfall */
}
```

> [!NOTE]
> Prefiere `rem` para `font-size` para que quienes suban el tamaño de fuente del
> navegador vean escalar todo el juego con ellos. La accesibilidad es una feature, no un
> parche.

---

## 👻 Pseudoelementos y Pseudoclases

### Pseudoelementos *(capítulo 05)*: estilizan *partes* de un elemento — sintaxis `::`

| Pseudoelemento | Estiliza | Ejemplo |
| :--- | :--- | :--- |
| `::before` | Contenido generado *antes* del elemento | `quote::before { content: "»"; }` |
| `::after` | Contenido generado *después* del elemento | `a::after { content: " ↪"; }` |
| `::first-line` | La primera línea formateada del texto | capitulares de párrafo |
| `::first-letter` | La primera letra | `text-transform: uppercase` |
| `::selection` | El texto que el usuario resalta | colores de resaltado a medida |
| `::marker` | El bullet/número de un ítem de lista | viñetas recoloreadas |

```css
p::first-letter {
  font-size: 2em;       /* capitular */
  font-weight: bold;
}
```

> [!IMPORTANT]
> `::before` y `::after` no renderizan **nada sin `content`** — un `content: ""` vacío
> sigue contando como valor, pero omítelo y el pseudoelemento es un fantasma.

### Pseudoclases *(capítulo 06)*: estilizan *estados* de un elemento — sintaxis `:`

| Pseudoclase | Se aplica cuando |
| :--- | :--- |
| `:hover` | El puntero está sobre el elemento |
| `:active` | El elemento se está pulsando |
| `:focus` | El elemento tiene el foco (teclado o clic) |
| `:visited` | Un enlace ya ha sido visitado |
| `:root` | La raíz del documento — aquí viven las variables CSS |
| `:nth-child(n)` | El elemento es el hijo número *n* de su padre |
| `:not(selector)` | El elemento **no** coincide con el selector |

### El Orden Que Importa: LoVe/HAte

```css
a:link      { color: blue; }
a:visited   { color: purple; }
a:hover     { color: orange; }
a:active    { color: red; }
```

Las pseudoclases de estado de enlace comparten especificidad, así que decide la cascada —
y gana la última. Escríbelas en este orden exacto o `:hover` puede perder silenciosamente
contra `:visited`.

---

## ⚠️ Trampas Que Vale la Pena Memorizar

| Trampa | Qué ocurre en realidad |
| :--- | :--- |
| Falta el `;` en la primera declaración | La siguiente línea se pega al valor y la regla se rompe |
| Usar `#id` en todas partes | La especificidad sube, las reglas posteriores dejan de funcionar, refactorizar duele |
| `p { }` y `.intro { }` sobre el mismo elemento | Gana la clase; la cascada no es un concurso de popularidad |
| `!important` para "arreglar" un conflicto | Gana hoy y toda regla futura necesitará su propio `!important` |
| `border: 2px blue` sin estilo | No renderiza nada — el estilo es obligatorio |
| `::before` sin `content` | No renderiza nada — el content es obligatorio |
| `:hover` escrito después de `:visited` | El estilo hover se anula en silencio; mantén el orden LoVe/HAte |
| `font-size` en `px` en todas partes | El texto se niega a escalar con los ajustes de fuente; prefiere `rem` |
| Añadir padding a una columna `width: 50%` | La columna desborda — `box-sizing` es la solución ([[00c - Chuleta de CSS II]]) |
| Mezclar `em` y `rem` | Los `em` anidados se componen; elige `rem` para el ritmo global |

---

## 🎮 La Versión de Una Página

Todas las declaraciones de esta hoja en un bloque — la pantalla de título de Emberfall:

```css
* { margin: 0; padding: 0; }

body {
  font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  font-size: 18px;
  line-height: 1.5;
  background: #1b1b2f;
}

.hero-title {
  color: #FF6B35;
  font-family: Georgia, serif;
  font-weight: 800;
  font-size: 3rem;
  letter-spacing: 4px;
  text-transform: uppercase;
  text-shadow: 3px 3px 0 #000;
}

.hero-title::first-letter {
  font-size: 1.4em; /* capitular */
}

.btn-start {
  background: #2DD4BF;
  color: #1b1b2f;
  font-weight: 700;
  border: 2px solid #fff;
  padding: 12px 24px;
}

.btn-start:hover {
  background: #7C5CFF;
  color: #fff;
}

.btn-start:active {
  transform: translateY(2px); /* la sensación de "pulsado" */
}

nav > a {
  color: #fff;
  text-decoration: none;
  letter-spacing: 1px;
}

a:visited { color: #c4b5fd; }
a:hover   { color: #FF6B35; }
a:active  { color: #fff; }
```

---

## 🔗 Ver También

- [[00c - Chuleta de CSS II]] — modelo de caja, espaciado, display, posicionamiento, flexbox
- [[01 - Fundamentos de CSS]] — sintaxis, cómo añadir CSS, la cascada
- [[02 - Colores y Medidas]] — las tablas completas de colores y unidades
- [[03 - Selectores Pt. 1]] — selectores de tipo, clase, id y especificidad
- [[04 - Selectores Pt. 2]] — combinadores y selectores de atributo
- [[05 - Pseudoelementos]] — `::before`, `::after` y amigos, en profundidad
- [[06 - Pseudoclases]] — estados, `:nth-child()` y el orden LoVe/HAte

---