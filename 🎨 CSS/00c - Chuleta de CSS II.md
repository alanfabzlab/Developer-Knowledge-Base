# 00c. Chuleta de CSS II

**Versión original en inglés:** [00c - CSS Cheatsheet II.md](00c%20-%20CSS%20Cheatsheet%20II.md)

**Curso:** CSS
**Tema:** Referencia rápida de fondos, el modelo de caja, espaciado y dimensiones, display, posicionamiento, `z-index` y flexbox usados en el módulo
**Tags:** `#css` `#web-development` `#cheatsheet` `#reference` `#layout` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-F7DF1E?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Cubre-Capítulos_07_--_12-7C5CFF?style=for-the-badge" alt="Capítulos 07 a 12">
  <img src="https://img.shields.io/badge/Tipo-Chuleta-00C2A8?style=for-the-badge" alt="Chuleta">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Una página para la segunda mitad del módulo. Toda regla de aquí se presentó en
[[07 - Fuentes y Texto]], [[08 - Fondos y Shorthands]], [[09 - Modelo de Caja y Bordes]],
[[10 - Espaciado y Box Sizing]], [[11 - Display y Posicionamiento]] o [[12 - Flexbox ES]] —
nada en esta hoja es nuevo. Sintaxis, selectores, colores, unidades, tipografía y
pseudoelementos/pseudoclases viven en [[00b - Chuleta de CSS]].

> [!TIP]
> La maquetación es donde CSS se gana el sueldo — y donde se esconden las trampas. Cuando
> una página se niega a sentarse donde esperas, recorre aquí las secciones en orden:
> caja, espaciado, display, position, flex. Una de ellas está mintiendo.

**El hilo narrativo del módulo: Emberfall**, un roguelike de mazmorras. A mitad del módulo
las maquetaciones pasan de pantallas a páginas: la tarjeta de feed, el Archivo del Gremio,
el horario de la Academia, la colección de cartas de campeones. Las propiedades son las
que publica un estudio real — solo cambian las palabras.

---

## 🗺️ El Modelo de Caja

Todo elemento es una caja con cuatro capas concéntricas:

| Capa | De dentro a fuera | Controla | Propiedad |
| :--- | :--- | :--- | :--- |
| Contenido | el contenido real | el tamaño de la habitación | `width`, `height` |
| Padding | espacio *dentro* del borde | los muebles lejos de las paredes | `padding` |
| Borde | el marco | grosor, estilo y color de la pared | `border` |
| Margin | espacio *fuera* del borde | la distancia a los vecinos | `margin` |

### box-sizing: quién es dueño del tamaño declarado

```css
/* Predeterminado: el padding y el borde SE SUMAN al ancho/alto */
* {
  box-sizing: border-box; /* el reset moderno — el tamaño declarado se mantiene */
}
```

| Valor | Con `width: 150px` + `padding: 20px` renderiza |
| :--- | :--- |
| `content-box` | 150 + 40 = **194px** (el borde suma más) |
| `border-box` | **150px** — el padding se absorbe dentro |

> [!WARNING]
> La rotura clásica: `width: 50%` en dos columnas lado a lado, y entonces padding → ambas
> desbordan la fila. El reset universal `border-box` lo previene — ponlo en cada archivo.

---

## 🌄 Fondos *(capítulo 08)*

| Propiedad | Función | Ejemplo |
| :--- | :--- | :--- |
| `background-color` | Color base | `background-color: #1b1b2f;` |
| `background-image` | Capa de imagen | `background-image: url("bg.png");` |
| `background-repeat` | Mosaico | `no-repeat`, `repeat-x`, `repeat-y` |
| `background-position` | Ubicación | `center`, `top right`, `10px 20px` |
| `background-size` | Escalado | `cover` (recorta para llenar), `contain`, `100%` |

```css
.banner {
  background-image: url("https://placehold.co/1200x200/1b1b2f/ff6b35");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  height: 200px;
}
```

> [!NOTE]
> `cover` escala la imagen para cubrir todo el elemento (recortando el exceso); `contain`
> mete la imagen entera dentro (dejando bandas vacías). Elige según quién mande: el
> elemento o la imagen.

---

## 📐 Shorthands: El Reloj, en Una Línea

`border`, `margin` y `padding` comparten la misma gramática de 1 a 4 valores.
**Arriba → Derecha → Abajo → Izquierda**, en sentido horario desde las 12:

```css
padding: 10px;              /* los cuatro lados */
padding: 10px 20px;         /* vertical | horizontal */
padding: 10px 20px 30px;    /* arriba | horizontal | abajo */
padding: 10px 20px 30px 40px; /* arriba | derecha | abajo | izquierda */
border: 2px solid #333;     /* grosor | estilo | color — el estilo es OBLIGATORIO */
```

| Propiedad | Qué agrupa el shorthand | Pieza obligatoria |
| :--- | :--- | :--- |
| `padding` / `margin` | los cuatro lados, en sentido horario | el/los valor(es) de tamaño |
| `border` | grosor + estilo + color | **estilo** — sin estilo, no renderiza |
| `background` | color + imagen + position + size… | un color o una imagen |
| `font` | estilo + peso + tamaño/interlineado + familia | tamaño y familia |

> [!TIP]
> Lee `border: 2px solid blue` en voz alta como "grosor estilo color" y el shorthand no
> volverá a sorprenderte. El reloj responde a toda pregunta de orden en esta hoja.

---

## 📏 Espaciado y Dimensiones *(capítulo 10)*

### La Gramática Completa de Padding/Margin

| Declaración | Efecto |
| :--- | :--- |
| `margin: 20px` | 20px por todas partes |
| `margin: 20px 10px` | 20px arriba/abajo, 10px izquierda/derecha |
| `margin: 10px 20px 30px` | arriba, luego horizontal, luego abajo |
| `margin: 10px 20px 30px 40px` | arriba, derecha, abajo, izquierda |
| `margin: 0 auto` | 0 vertical, **centrado horizontalmente** — necesita un `width` |

### Las Reglas Que Importan

| Regla | Significado |
| :--- | :--- |
| `margin: auto` | Centra un bloque horizontalmente **solo con un `width` declarado** |
| Márgenes negativos | Acercan cajas o las solapan; el padding jamás puede ser negativo |
| `width: 100%` + margin | Desborda el padre — el `width` ya lo llena; amplía con padding mejor |
| `rem` vs `em` | `rem` = escala raíz (toda la página); `em` = escala local (se compone al anidar) |

```css
/* El reset universal: toda caja empieza igual */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```

---

## 🧱 Display *(capítulo 11)*

| Valor | Flujo | Ancho/alto | Uso |
| :--- | :--- | :--- | :--- |
| `block` *(predeterminado en div, p, h1…)* | línea propia, apila | se respeta | secciones, tarjetas |
| `inline` *(predeterminado en span, a, b…)* | misma línea que sus hermanos | se ignora | corridas de texto |
| `inline-block` | misma línea | **se respeta** | píldoras de nav, iconos, botones |
| `none` | eliminado por completo de la página | — | ocultar |

> [!NOTE]
> `display: none` elimina el elemento *y su espacio*; `visibility: hidden` conserva el
> espacio pero no muestra nada. Los menús de depuración, los toggles rápidos y los estados
> colapsados usan ambos.

---

## 📌 Position *(capítulo 11)*

| Valor | Anclado a | ¿Sale del flujo normal? | Uso típico |
| :--- | :--- | :--- | :--- |
| `static` *(predeterminado)* | — | no | la línea base |
| `relative` | su propio sitio normal | no | empujes; **el ancestro posicionado** |
| `absolute` | el ancestro **posicionado** más cercano | sí | insignias, esquinas, superposiciones |
| `fixed` | el viewport | sí | volver arriba, chat, nav persistente |
| `sticky` | su padre, tras un umbral de scroll | no (hasta fijarse) | encabezados de sección, de tabla |

```css
/* absolute responde al ancestro posicionado más cercano */
.card { position: relative; }

.badge {
  position: absolute;
  top: 10px;
  right: 10px;
}
```

| Offset | Significado |
| :--- | :--- |
| `top` / `bottom` | Distancia desde el borde superior / inferior del ancla |
| `left` / `right` | Distancia desde el borde izquierdo / derecho del ancla |
| `z-index` | Orden de apilamiento **solo en elementos posicionados** — más alto = encima |

> [!WARNING]
> Un elemento `absolute` **sin ancestro posicionado** se ancla a la página y el resto del
> contenido lo ignora por completo — si una insignia "vuela a la esquina del documento",
> el bug es el `position: relative` que falta.

---

## 📦 Flexbox *(capítulo 12)*

### En el Contenedor

```css
.container {
  display: flex;              /* una línea convierte a los hijos en flex items */
  flex-direction: row;        /* row | row-reverse | column | column-reverse — el eje principal */
  flex-wrap: wrap;            /* nowrap | wrap | wrap-reverse */
  justify-content: center;    /* eje principal: start | center | end | space-between | space-around | space-evenly */
  align-items: center;        /* eje cruzado: stretch | center | start | end */
  gap: 16px;                  /* espacio uniforme entre ítems */
}
```

| Propiedad | Eje | Espacia… |
| :--- | :--- | :--- |
| `justify-content` | principal | la línea de ítems |
| `align-items` | cruzado | todos los ítems |
| `align-self` | cruzado | **un** ítem (anula `align-items`) |
| `gap` | ambos | los canales entre ítems |

```css
/* La receta del centrado perfecto — ambos ejes, dos líneas */
.hero {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

### En los Ítems

```css
.item {
  flex: 1;           /* flex-grow: 1 — reclama partes iguales del espacio libre */
  flex: 0 0 200px;   /* grow-0 shrink-0 basis-200px — ítem fijo */
  align-self: end;   /* anula la regla del eje cruzado del contenedor */
  order: -1;         /* reordena sin tocar el HTML */
}
```

| Propiedad del ítem | Función | Shorthand |
| :--- | :--- | :--- |
| `flex-grow` | parte del *espacio libre* (0 = nunca) | `flex: 1 1 0%` |
| `flex-shrink` | qué rápido devuelve espacio (1 = predeterminado) | parte de `flex` |
| `flex-basis` | tamaño inicial antes de distribuir | `flex: 1` ≈ `1 1 0%` |

> [!IMPORTANT]
> `flex-grow` reparte **espacio libre**, no proporciones: `flex: 1` contra `flex: 2` le da
> al segundo ítem el doble de *extra*, no el doble del ancho — salvo que `flex-basis: 0%`
> convierta al grow en una proporción real.

---

## ⚠️ Trampas Que Vale la Pena Memorizar

| Trampa | Qué ocurre en realidad |
| :--- | :--- |
| `width: 50%` + padding (content-box) | Ambas columnas desbordan la fila — `border-box` |
| `margin: auto` sin width | Nada se mueve — no hay espacio sobrante que repartir |
| `border: 2px blue` (sin estilo) | No renderiza ningún borde; el estilo es obligatorio |
| `absolute` sin ancestro posicionado | El elemento se ancla a la página; los hermanos lo ignoran |
| `z-index` en un elemento `static` | Se ignora — z-index solo funciona en elementos posicionados/flex |
| `justify-content` cuando los ítems llenan la fila | No hay nada que distribuir — el espacio libre debe existir primero |
| `flex: 1` con `flex-wrap` | Los ítems crecen para llenar la *primera* línea y dejan huecos al final |
| `display: none` cuando querías "oculto" | La maquetación colapsa — usa `visibility: hidden` para conservar el espacio |
| `background-size: contain` en una cabecera | Aparecen bandas vacías — `cover` suele ser la respuesta del banner |
| Sticky que se escapa con el scroll | Un padre `relative` más alto que el viewport se come el pin del sticky |

---

## 🎮 La Versión de Una Página

Todas las reglas de maquetación de esta hoja, en un bloque — la pantalla de batalla:

```css
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  display: flex;              /* toda la pantalla es un shell de app en flex */
  height: 100vh;
  font-family: 'Segoe UI', Roboto, Arial, sans-serif;
  background: #1b1b2f;
}

#hud {
  position: fixed;            /* fijado a la parte superior de la pantalla */
  top: 0; left: 0; right: 0;
  background: #333;
  color: #fff;
  padding: 8px 16px;
  z-index: 100;
}

main {
  flex: 1;                    /* absorbe todo el ancho restante */
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 16px;
  padding: 64px 24px 24px;    /* despeja el HUD fijo */
}

#sidebar {
  flex: 0 0 200px;            /* barra lateral de ancho fijo */
  border-right: 2px solid #555;
  padding: 16px;
}

.card {
  position: relative;
  width: 160px;
  height: 220px;
  border: 2px solid #FF6B35;
  border-radius: 8px;
  background-image: url("champion.png");
  background-size: cover;
  background-position: center;
}

.card .hp {
  position: absolute;         /* insignia en la esquina de la tarjeta */
  bottom: 8px;
  left: 8px;
  background: #2DD4BF;
  border-radius: 4px;
  padding: 2px 8px;
}

.lesson-title {
  position: sticky;           /* se fija mientras su sección hace scroll */
  top: 48px;
  background: #7C5CFF;
  color: #fff;
  padding: 8px;
}
```

---

## 🔗 Ver También

- [[00b - Chuleta de CSS]] — sintaxis, selectores, colores, unidades, tipografía, pseudo
- [[08 - Fondos y Shorthands]] — las tablas completas de fondos y shorthands
- [[09 - Modelo de Caja y Bordes]] — las cuatro capas y todos los estilos de borde
- [[10 - Espaciado y Box Sizing]] — la gramática de padding/margin y `box-sizing`
- [[11 - Display y Posicionamiento]] — display, los cinco valores de position, `z-index`
- [[12 - Flexbox ES]] — propiedades de contenedor e ítems, con el capstone de cartas

---