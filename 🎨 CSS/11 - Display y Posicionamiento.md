# 11. Display y Posicionamiento

**Versión original en inglés:** [11 - Display & Positioning.md](11%20-%20Display%20&%20Positioning.md)

**Curso:** CSS
**Tema:** `display: block` vs `inline` vs `inline-block`, flujo normal, `position: static`, `relative`, `absolute`, `fixed`, `sticky`, `z-index` y el proyecto final de la Academia
**Tags:** `#css` `#web-development` `#layout` `#positioning` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-F7DF1E?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-54_--_60-7C5CFF?style=for-the-badge" alt="Lecciones 54 a 60">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Dos cajas en una página pueden sentarse, deslizarse, fijarse o solaparse — este capítulo
es la sala de control. **Display** decide cómo se comporta una caja entre sus hermanas;
**position** decide dónde se coloca — en el flujo normal, empujada, anclada a un ancestro,
pegada al viewport o atascada a mitad del scroll. El proyecto final ensambla los cinco
valores de `position` más `z-index` en una página de academia. Referencia:
[[00c - Chuleta de CSS II]].

> [!NOTE]
> **Todo el capítulo en una frase**
> `static` fluye, `relative` empuja, `absolute` ancla, `fixed` fija al viewport,
> `sticky` fluye y luego fija — y `z-index` decide quién gana cuando dos cajas chocan.

---

## 54. Display: Block, Inline e Inline-Block

Todo elemento HTML lleva un valor de `display` predeterminado. Las tres estrellas:

| Display | Comportamiento de flujo | Comportamiento de ancho | Ejemplos |
| :--- | :--- | :--- | :--- |
| `block` | Línea propia, se apilan en vertical | Llena el ancho del padre por defecto; acepta `width`/`height` | `<div>`, `<h1>`, `<p>`, `<section>` |
| `inline` | Se sienta en la misma línea que sus hermanos | Abraza el contenido; `width`/`height` no tienen efecto | `<span>`, `<a>`, `<em>`, `<b>` |
| `inline-block` | Misma línea que sus hermanos | Acepta `width`/`height` y márgenes | Iconos, píldoras de navegación, botones |

```css
/* Enlaces tipo bloque que comparten línea y obedecen dimensiones */
a {
  display: inline-block;
  width: 120px;
  padding: 8px;
  border: 1px solid #333;
}
```

> [!TIP]
> La navegación del Archivo del Gremio de [[10 - Espaciado y Box Sizing]] hizo
> exactamente esto: tres enlaces `inline-block` que toman padding, ancho y márgenes
> mientras se mantienen en una fila.

---

## 55. Flujo Normal y `position: static`

Dentro de todo documento HTML el navegador coloca los elementos en una cascada predecible
llamada **flujo normal**: los hermanos de nivel bloque se apilan de arriba a abajo, el
contenido inline llena línea a línea, de izquierda a derecha.

`position: static` es el valor predeterminado — la caja ocupa su lugar natural, en flujo,
e ignora las propiedades de desplazamiento `top`, `right`, `bottom` y `left`:

```css
div {
  position: static; /* predeterminado; los offsets no tienen efecto */
}
```

> [!NOTE]
> Nunca escribas `position: static` en hojas de estilos reales — ya es el valor por
> defecto. Aparece en tutoriales como la *línea base*: todo otro valor parte de aquí y
> anula el flujo normal a su manera.

---

## 56. `position: relative`

`relative` mantiene la caja **en flujo normal** — su espacio original se conserva — pero
permite que las propiedades de desplazamiento la empujen desde donde habría estado:

```css
#div-1 {
  position: relative;
  left: 50px;  /* desplazada 50px a la derecha desde su sitio normal */
  top: 10px;   /* desplazada 10px hacia abajo */
}
```

Piénsalo así: *rendereízame en mi hueco habitual y luego empújame* — el hueco vacío sigue
perteneciendo a la caja, así que los vecinos no se mueven para ocuparlo.

> [!IMPORTANT]
> `relative` es también el compañero de baile de `absolute`: un ancestro posicionado. Los
> elementos con `position: relative` (y sin offsets) son la forma más común de darle a un
> hijo `absolute` un ancla, como muestra la lección 57.

---

## 57. `position: absolute`

`absolute` **saca la caja del flujo normal** — el espacio que ocupaba colapsa y los
hermanos se meten — y la fija al ancestro **posicionado** más cercano: el ancestro más
próximo cuyo `position` sea cualquier cosa menos `static`. Sin ese ancestro, se ancla al
bloque contenedor inicial (el viewport al inicio del documento).

```css
/* La tarjeta se convierte en el bloque contenedor */
.card {
  position: relative;
}

/* La insignia se pega a la esquina superior derecha de la tarjeta */
.badge {
  position: absolute;
  top: 10px;
  right: 10px;
}
```

El patrón clásico: `position: relative` en el padre, `position: absolute` en el hijo,
coordenadas `top`/`right` que responden a *"10px del borde superior del padre, 10px de su
borde derecho"*.

> [!WARNING]
> Una caja `absolute` **sin ancestro posicionado** se ancla a la página misma — y ningún
> otro contenido le reserva espacio. Comprueba siempre: si un elemento absoluto "vuela" a
> la esquina del documento, falta el ancestro posicionado más cercano.

---

## 58. `position: fixed`

`fixed` fija la caja **respecto al viewport**: se queda pegada a la misma posición de
pantalla mientras el resto de la página se desplaza bajo ella. Como `absolute`, sale del
flujo normal.

```css
/* Sigue visible en la esquina sin importar cuánto hagas scroll */
#back-to-top {
  position: fixed;
  right: 20px;
  bottom: 20px;
}
```

Usos clásicos: botones de volver arriba, widgets de chat, barras de navegación que nunca
abandonan la pantalla.

> [!TIP]
> Distingue `fixed` de `absolute`: `fixed` responde al **viewport**, `absolute` a su
> **ancestro posicionado**. Haz scroll y el elemento `fixed` se queda quieto; el `absolute`
> se desplaza con su contenedor.

---

## 59. `position: sticky` y `z-index`

### Sticky: primero fluye, luego fija

`sticky` vive en flujo normal hasta cruzar un umbral de scroll, y entonces se comporta
como `fixed` — **dentro de los límites de su padre**. Es relativo a su posición normal
hasta que se alcanza `top`/`bottom`; pasado ese punto, se fija hasta que el padre sale de
la vista.

```css
.sticky-header {
  position: sticky;
  top: 0; /* se fija al tope del viewport una vez que el scroll lo alcanza */
}
```

### z-index: el orden de apilamiento

Las cajas posicionadas pueden solaparse; `z-index` decide cuál gana. Los valores más
altos se pintan por encima:

```css
.box-a { position: absolute; z-index: 1; }
.box-b { position: absolute; z-index: 10; } /* se renderiza por encima de box-a */
```

| Valor de z-index | Significado |
| :--- | :--- |
| `auto` | Predeterminado; el orden del documento decide |
| `0`..`n` | Capa explícita; el número mayor se pinta sobre el menor |
| Negativo | Se pinta por debajo del contenido normal de la página |

> [!IMPORTANT]
> `z-index` solo funciona en elementos **posicionados** — las cajas `static` lo ignoran,
> ya que nunca pueden salir del flujo para apilarse. Si un `z-index` se empeña en no hacer
> nada, comprueba que el elemento (o un ítem de flex/grid) esté realmente posicionado.

---

## 60. La Maquetación de la Academia

### Checkpoint: Resumen del Capítulo

- `block` apila y llena; `inline` abraza una línea; `inline-block` abraza pero dimensiona.
- `static` = flujo normal; `relative` empuja pero conserva su hueco.
- `absolute` sale del flujo y ancla al ancestro posicionado más cercano.
- `fixed` fija al viewport; `sticky` fluye hasta su umbral y luego fija dentro de su padre.
- `z-index` ordena los elementos posicionados que se solapan.

### Proyecto: La Academia Emberfall

Una página de academia con scroll que usa todas las herramientas de posicionamiento: una
campana de notificaciones anclada a la cabecera, un encabezado de sección sticky, un
enlace fijo de "volver arriba" y tarjetas de lección solapadas que se apilan con
`z-index`.

#### HTML (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Academia Emberfall</title>
</head>
<body>
  <div id="top-banner">
    <h1>¡Bienvenido a la Academia Emberfall!</h1>
    <div id="notification-bell">
      🔔
      <span id="notif-count">3</span>
    </div>
  </div>

  <main id="curriculum">
    <section class="lesson">
      <h2 class="lesson-header">Lore y Lingüística</h2>
      <p>Morfología rúnica, dialectos de las Tierras de Ceniza y el silabario prohibido
      de la Corte de la Brasa.</p>
    </section>
    <section class="lesson">
      <h2 class="lesson-header">Tácticas de Combate</h2>
      <p>Ejercicios de formación, gestión de aggro en las Salas Profundas y primeros
      auxilios para wipes de grupo.</p>
    </section>
    <section class="lesson">
      <h2 class="lesson-header">Práctica de Encantamiento</h2>
      <p>Círculos rúnicos, presupuestos de maná y cuándo no poner runas de fuego en
      una antorcha.</p>
    </section>
  </main>

  <div class="overlap-banner">
    <div class="card card-back">Programa</div>
    <div class="card card-front">Horarios</div>
  </div>

  <footer>
    <a id="back-to-top" href="#top-banner">↑ Volver Arriba</a>
  </footer>
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

/* Un ancla para que los absolutos aterricen en la cabecera, no en la página */
#top-banner {
  position: relative;
  background-color: #1b1b2f;
  color: white;
  padding: 20px;
}

#notification-bell {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 1.5rem;
}

#notif-count {
  position: absolute;
  top: -5px;
  right: 5px;
  background: #ff6b35;
  border-radius: 50%;
  font-size: 0.8rem;
  padding: 2px 6px;
}

/* Los encabezados sticky se fijan mientras su sección se desplaza */
.lesson-header {
  position: sticky;
  top: 0;
  background: #1572B6;
  color: white;
  padding: 8px 16px;
}

main {
  padding: 20px;
}

.lesson {
  margin-bottom: 30px;
}

/* Tarjetas solapadas: z-index decide la ganadora */
.overlap-banner {
  position: relative;
  height: 120px;
  margin: 20px;
}

.card {
  position: absolute;
  width: 180px;
  padding: 16px;
  background: #2DD4BF;
  text-align: center;
}

.card-back {
  left: 60px;
  top: 10px;
  z-index: 1;
}

.card-front {
  left: 40px;
  top: 40px;
  z-index: 10;
}

/* Enlace fijo siempre visible */
#back-to-top {
  position: fixed;
  right: 20px;
  bottom: 20px;
  background: #7C5CFF;
  color: white;
  padding: 10px 14px;
  text-decoration: none;
  border-radius: 5px;
}
```

Lee la página como una pila de posiciones: la campana y su contador son `absolute` dentro
de la cabecera `relative`; los contadores de esa esquina sobreviven a cualquier edición de
la cabecera; los títulos `sticky` viajan con el scroll solo dentro de su sección; las dos
tarjetas se solapan con `z-index` 1 contra 10; el botón de volver arriba es `fixed` al
viewport y nunca se va.

> [!TIP]
> **Versión para game devs**
> Esto es un HUD: la campana es el rastreador de misiones, las tarjetas son el minimapa y
> los iconos de buffs, los encabezados sticky son las etiquetas flotantes del mundo, y el
> enlace de volver arriba es el botón del menú de pausa fijado en la esquina. El UI de
> pantalla funciona con reglas de `position`.

---

## XP Earned: Lo que te llevas

- 🧱 `block` apila, `inline` abraza, `inline-block` hace ambas cosas.
- 🗺️ `static` fluye; `relative` se desplaza en su sitio; `absolute` sale del flujo y ancla.
- 📌 `fixed` fija al viewport; `sticky` fija solo dentro de su padre tras su umbral.
- 🥇 `z-index` decide el orden del solape — solo en elementos posicionados.
- 🎓 Todo patrón de HUD — insignias, etiquetas flotantes, botones persistentes — es un valor de position.

---

## Loot Table: Casos de Uso Reales

- 🔔 Insignias de notificación y botones de esquina anclados a cabeceras
- 📌 Botones flotantes de volver arriba y widgets de chat
- 🧭 Encabezados de tabla y títulos de sección sticky que sobreviven al scroll
- 🃏 Tarjetas solapadas, tooltips y toasts gobernados por `z-index`

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Convierte tres enlaces `<a>` en píldoras de navegación `inline-block` y compara con `block` e `inline`.
2. Empuja una caja con offsets `relative` y confirma que su espacio original queda reservado.
3. Coloca una insignia `absolute` dentro de una tarjeta `relative`; luego quita `relative` y observa cómo vuela.
4. Crea un botón de esquina `fixed` y un encabezado de sección `sticky`, y haz scroll con ambos.
5. **Pelea de jefe:** construye una pantalla de raid — barra de vida fijada arriba, iconos
   de buffs solapados con z-index, una etiqueta sticky con el nombre del jefe y un botón
   `fixed` de "Abandonar Raid" en la esquina.

---

## 🔗 Ver También

- [[12 - Flexbox ES]] — la forma moderna de distribuir cajas a lo largo de un eje
- [[10 - Espaciado y Box Sizing]] — las reglas de espaciado que estos position desplazan
- [[09 - Modelo de Caja y Bordes]] — las capas que toda caja posicionada carga
- [[00c - Chuleta de CSS II]] — valores de display y position en una página

---