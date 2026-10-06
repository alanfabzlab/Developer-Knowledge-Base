# 12. Flexbox

**Versión original en inglés:** [12 - Flexbox.md](12%20-%20Flexbox.md)

**Curso:** CSS
**Tema:** El contenedor flex, ejes principal y cruzado, `flex-direction`, `flex-wrap`, `justify-content`, `gap`, `align-items`, `align-self`, `flex-basis`/`flex-grow`/`flex-shrink` y el proyecto final de la Colección de Cartas
**Tags:** `#css` `#web-development` `#layout` `#flexbox` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-AVANZADO-F7DF1E?style=for-the-badge" alt="Avanzado">
  <img src="https://img.shields.io/badge/Lecciones-61_--_66-7C5CFF?style=for-the-badge" alt="Lecciones 61 a 66">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

El último capítulo del módulo — y la herramienta de maquetación sobre la que se construye
el CSS moderno. Flexbox convierte cualquier elemento en un contenedor que **distribuye sus
hijos a lo largo de un eje**: espaciándolos, centrándolos, envolviéndolos y dejándoles
crecer y encogerse en proporción. De las barras de navegación a las rejillas de tarjetas y
hasta la Colección de Cartas final, un contenedor los gobierna a todos. Referencia:
[[00c - Chuleta de CSS II]].

> [!NOTE]
> **Todo el capítulo en una frase**
> `display: flex` en el padre, luego `justify-content`/`align-items` reparten los ítems a
> lo largo de los ejes principal/cruzado, y `flex` en los hijos decide quién crece.

---

## 61. El Contenedor Flex

```css
.container {
  display: flex;
}
```

Añadir `display: flex` a un padre lo convierte en un **contenedor flex**; sus hijos
directos se vuelven **flex items**. Una declaración reescribe las reglas de maquetación
del capítulo [[11 - Display y Posicionamiento]]: los ítems dejan de apilarse como bloques
planos y se alinean en una fila compartida, listos para ser ordenados, espaciados,
envueltos y redimensionados.

```css
.parent {
  display: flex;
  background: #1572B6;
  gap: 10px;
}

.child {
  background: #2DD4BF;
  padding: 16px;
  border-radius: 5px;
}
```

Sin más reglas, los tres hijos se sientan lado a lado, compartiendo automáticamente la
altura disponible en el eje cruzado.

> [!TIP]
> Todo lo que hay dentro de un contenedor flex es un flex item — pero solo los hijos
> *directos*. Los elementos anidados mantienen su propio comportamiento hasta que su
> propio padre se convierte en contenedor flex. Así compone flexbox: contenedores dentro
> de contenedores.

---

## 62. Ejes, Dirección y Envoltura

Flexbox piensa en **ejes**, no en filas y columnas. Dos propiedades los dirigen:

### flex-direction: qué eje es el "principal"

| Valor | El eje principal corre | Los ítems quedan |
| :--- | :--- | :--- |
| `row` *(predeterminado)* | izquierda → derecha | lado a lado |
| `row-reverse` | derecha → izquierda | lado a lado, invertidos |
| `column` | arriba → abajo | apilados |
| `column-reverse` | abajo → arriba | apilados, invertidos |

El **eje principal** es la dirección del flujo; el **eje cruzado** es perpendicular a él.

### flex-wrap: una línea o varias

```css
.container {
  flex-direction: row;
  flex-wrap: wrap; /* los ítems saltan a una línea nueva al desbordarse */
}
```

| Valor | Comportamiento |
| :--- | :--- |
| `nowrap` *(predeterminado)* | Todos los ítems se comprimen en una línea |
| `wrap` | Los ítems desbordan a líneas nuevas a lo largo del eje cruzado |
| `wrap-reverse` | Igual, pero las líneas nuevas crecen en la dirección cruzada opuesta |

> [!NOTE]
> Cambia `flex-direction` y los ejes se intercambian: en `column`, el "centrado
> horizontal" se vuelve vertical, y `wrap` deja caer los ítems en nuevas *columnas* en
> vez de filas. Todas las propiedades de flexbox de aquí en adelante son relativas al
> eje, no a la página.

---

## 63. justify-content: Distribuir el Eje Principal

`justify-content` distribuye los ítems **a lo largo del eje principal**, gestionando el
espacio sobrante cuando los ítems no llenan el contenedor:

```css
.container {
  display: flex;
  justify-content: space-between;
}
```

| Valor | Efecto |
| :--- | :--- |
| `flex-start` *(predeterminado)* | Apretados al inicio |
| `center` | Apretados en el medio |
| `flex-end` | Apretados al final |
| `space-between` | Huecos iguales; el primer y el último ítem tocan los bordes |
| `space-around` | Espacio igual alrededor de cada ítem (los bordes reciben medios huecos) |
| `space-evenly` | Espaciado totalmente uniforme en todas partes |

### El patrón de la barra de navegación

```css
nav {
  display: flex;
  justify-content: space-between; /* logo a la izquierda, acciones a la derecha */
  align-items: center;
  padding: 16px 32px;
  background: #1b1b2f;
  color: white;
}
```

Una declaración y la marca se sienta en un extremo y los botones en el otro — sin trucos
de `position`, sin márgenes calculados.

> [!IMPORTANT]
> `justify-content` necesita **espacio libre** para distribuir. En un contenedor de ancho
> fijo lleno de ítems de ancho fijo no queda nada que espaciar. Cuando `space-between`
> parece no hacer nada, comprueba quién es dueño del ancho sobrante — suele ser el
> contenedor, no un `width` infinito en los ítems.

---

## 64. gap, align-items y align-self: El Eje Cruzado

### gap: canales entre ítems

`gap` reserva espacio uniforme entre los flex items — sin márgenes, sin excepciones de
primero/último:

```css
.container {
  display: flex;
  gap: 24px; /* también: gap: 16px 24px para valores de fila/columna */
}
```

### align-items: alineación del eje cruzado para todos

```css
.container {
  display: flex;
  align-items: center; /* predeterminado: stretch */
}
```

| Valor | Comportamiento en el eje cruzado |
| :--- | :--- |
| `stretch` *(predeterminado)* | Los ítems llenan la altura del contenedor |
| `center` | Los ítems abrazan el medio del eje cruzado |
| `flex-start` / `flex-end` | Los ítems abrazan el inicio / el final |

### La receta del centrado perfecto

```css
.container {
  display: flex;
  justify-content: center; /* eje principal */
  align-items: center;     /* eje cruzado */
}
```

Ambos ejes centrados, en dos líneas — el patrón de flexbox más usado del mundo.

### align-self: un ítem rebelde

`align-self` anula `align-items` para un solo ítem:

```css
.item-special {
  align-self: flex-end; /* este abraza el fondo; el resto sigue al contenedor */
}
```

> [!TIP]
> En un contenedor `row`, `justify-content` centra horizontalmente y `align-items`
> centra verticalmente. Cambia a `column` e intercambian sus papeles — las mismas dos
> propiedades, ejes recién asignados.

---

## 65. Dejar Crecer a los Ítems: flex-basis, flex-grow y flex-shrink

Tres propiedades deciden cómo se dimensionan los ítems a lo largo del eje principal —
normalmente escritas como un solo shorthand:

| Propiedad | Función | Valor típico |
| :--- | :--- | :--- |
| `flex-basis` | Tamaño inicial antes de distribuir | `auto`, `200px`, `30%` |
| `flex-grow` | Cuánto del *espacio libre* reclama un ítem | `0` (predeterminado), `1`, `2` |
| `flex-shrink` | Qué rápido devuelve espacio un ítem cuando la línea está apretada | `1` (predeterminado) |

```css
.sidebar { flex: 0 0 240px; } /* fijo: ni crece, ni encoge, siempre 240px */
.main    { flex: 1; }         /* grow 1: absorbe todo el espacio libre sobrante */
```

`flex: 1` es la forma corta de `flex: 1 1 0%` — empieza en cero y reclama partes iguales
de cada píxel libre. Dos hermanos con `flex: 1` dividen la fila al 50/50 sin importar el
viewport; el clásico diseño de barra lateral más contenido es solo esto.

> [!IMPORTANT]
> `flex-grow` reparte **espacio libre**, no proporciones exactas. Con `flex: 1` y
> `flex: 2`, el segundo ítem recibe *el doble del espacio extra*, no el doble del ancho —
> salvo que el basis sea `0%`, caso en el que grow *sí* se comporta como una proporción.

---

## 66. Colección de Cartas

### Checkpoint: Resumen del Capítulo

- `display: flex` en el padre convierte a los hijos en flex items sobre un eje compartido.
- `flex-direction` elige el eje principal; `flex-wrap` deja que los ítems desborden a líneas nuevas.
- `justify-content` espacia el eje principal; `align-items`/`align-self` gestionan el cruzado.
- `gap` reserva espacio uniforme; el shorthand `flex` controla basis, grow y shrink.

### Proyecto: La Colección de Cartas de Campeones

Una galería de coleccionista con los campeones de Emberfall: un nav flex, una fila de
héroe centrada, y una rejilla con wrap de cartas que se voltean al hacer clic (giro 3D en
CSS puro, una línea de JS).

#### HTML (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Colección de Cartas de Campeones</title>
</head>
<body>
  <nav>
    <span id="logo">⚔️ Campeones de Emberfall</span>
    <div id="nav-links">
      <a href="#">Colección</a>
      <a href="#">Duelos</a>
      <a href="#" class="btn-battle">Batalla</a>
    </div>
  </nav>

  <header class="hero">
    <h1>Colecciona. Voltea. Domina.</h1>
    <p>Cada campeón de Emberfall vive en esta baraja — haz clic en una carta para voltearla.</p>
  </header>

  <main class="collection">
    <div class="card">
      <div class="card-inner">
        <div class="card-face card-front">
          <img src="https://placehold.co/180x200/ff6b35/fff?text=Ember+Warden" alt="Guardián de Brasa" />
          <p><b>Guardián de Brasa</b></p>
        </div>
        <div class="card-face card-back-face">
          <p>🔥 +20 DMG de Fuego</p>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-inner">
        <div class="card-face card-front">
          <img src="https://placehold.co/180x200/2DD4BF/1b1b2f?text=Tide+Oracle" alt="Oráculo de la Marea" />
          <p><b>Oráculo de la Marea</b></p>
        </div>
        <div class="card-face card-back-face">
          <p>🌊 Cura 15 HP</p>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-inner">
        <div class="card-face card-front">
          <img src="https://placehold.co/180x200/7C5CFF/fff?text=Shadow+Trickster" alt="Tramposa Sombra" />
          <p><b>Tramposa Sombra</b></p>
        </div>
        <div class="card-face card-back-face">
          <p>🃏 Roba 1 carta</p>
        </div>
      </div>
    </div>
  </main>

  <script src="script.js"></script>
</body>
</html>
```

#### CSS (`styles.css`)

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}

/* Nav: space-between separa el logo y los enlaces */
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 32px;
  background: #1b1b2f;
  color: white;
}

#nav-links {
  display: flex;
  gap: 20px;
  align-items: center;
}

.btn-battle {
  background: #ff6b35;
  color: white;
  padding: 8px 16px;
  border-radius: 5px;
}

/* Hero: ambos ejes centrados */
.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 48px;
  text-align: center;
}

/* Colección: rejilla con wrap y canales uniformes */
.collection {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 24px;
  padding: 24px;
}

/* Carta con giro 3D */
.card {
  width: 180px;
  height: 260px;
  perspective: 1000px; /* profundidad para la rotación 3D */
}

.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.6s;
}

.card.flipped .card-inner {
  transform: rotateY(180deg);
}

.card-face {
  position: absolute;
  inset: 0;
  backface-visibility: hidden; /* oculta la cara que queda de espaldas */
  border: 2px solid #333;
  border-radius: 8px;
  text-align: center;
  padding: 8px;
}

.card-front {
  background: #f5f5f5;
}

.card-back-face {
  transform: rotateY(180deg);
  background: #1b1b2f;
  color: white;
}
```

#### JS (`script.js`)

```js
// Haz clic en cualquier carta para voltearla: añade/elimina la clase 'flipped'
const cards = document.querySelectorAll('.card');

cards.forEach(card => {
  card.addEventListener('click', () => {
    card.classList.toggle('flipped');
  });
});
```

Lee la página con ojos de flexbox: el nav usa `space-between` + `align-items`; el hero
centra ambos ejes; la colección es una rejilla con `wrap` distribuida con `center` y
`gap`; y el volteo es un flex item girando en 3D con `perspective` y `preserve-3d`. Cada
pregunta de maquetación que este módulo abrió — cómo se sientan, espacian, apilan y
solapan las cajas — tiene ahora una respuesta de flexbox. La baraja está completa.

> [!TIP]
> **Versión para game devs**
> Cambia campeones por objetos: botones de filtro en una barra `space-between`, una
> rejilla `wrap` de iconos de botín y cartas volteables como tooltips. Flexbox es la
> pantalla de inventario de la web — y el jefe final de este módulo. GG.

---

## XP Earned: Lo que te llevas

- 📐 `display: flex` en el padre; los hijos se vuelven ítems en un eje compartido.
- 🧭 `flex-direction` elige el eje principal; `wrap` gestiona las líneas de desborde.
- ⚖️ `justify-content` espacia el eje principal; `align-items`/`align-self` el cruzado.
- 🔗 `gap` = canales uniformes; `flex: 1` = crece y comparte el espacio libre.
- 🃏 Rejillas de cartas, barras de navegación, heros centrados — un contenedor para reinarlos a todos.

---

## Loot Table: Casos de Uso Reales

- 🧭 Barras de navegación y toolbars con `space-between`
- 🎯 Secciones hero centradas en ambos ejes
- 🃏 Galerías de cartas, dashboards y rejillas de inventario con `wrap` + `gap`
- 📐 Estructuras de barra lateral + contenido con `flex: 1`

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Construye un nav `space-between` y observa cómo `gap` reemplaza tus hacks de márgenes.
2. Centra una caja con `justify-content: center` + `align-items: center`; cambia el contenedor a `column` y explica el intercambio.
3. Haz dos columnas `flex: 1`, luego cambia una a `flex: 2` y mide la división.
4. Convierte una fila de cinco tarjetas fijas en una galería responsive con `wrap` y `gap: 16px`.
5. **Pelea de jefe:** construye una pantalla de batalla completa — barra lateral fija
   (`flex: 0 0 200px`), campo de juego centrado, mano de cartas con `wrap` y volteo al
   hacer clic, y una barra HUD `space-between` arriba.

---

## 🔗 Ver También

- [[11 - Display y Posicionamiento]] — las reglas de flujo que flex reemplaza
- [[10 - Espaciado y Box Sizing]] — las dimensiones y el `box-sizing` que heredan los flex items
- [[00c - Chuleta de CSS II]] — todas las propiedades flex en una página
- [[00b - Chuleta de CSS]] — la tarjeta de referencia completa de CSS

---