# 07. Fuentes y Texto

**Versión original en inglés:** [07 - Fonts & Text.md](07%20-%20Fonts%20&%20Text.md)

**Curso:** CSS
**Tema:** Las cinco familias genéricas de fuente, `font-family` y respaldos, `font-size`, `font-weight`, `text-align` y `text-decoration`
**Tags:** `#css` `#web-development` `#fonts` `#typography` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-F7DF1E?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-31_--_35-7C5CFF?style=for-the-badge" alt="Lecciones 31 a 35">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Las fuentes cargan con casi todo el tono de una página, y la alineación con casi todo su
ritmo. Este capítulo cubre las cinco familias genéricas de fuente, cómo elegir una cara
*y* su respaldo, los ejes `font-size` y `font-weight`, y las propiedades de texto que
colocan y decoran las palabras. Al terminar habrás dado al eslogan de un juego un sistema
tipográfico de verdad. Referencia: [[00b - Chuleta de CSS]].

> [!NOTE]
> **Todo el capítulo en una frase**
> La tipografía son dos controles — *qué cara* (`font-family` + peso y tamaño) y *cómo se
> asienta el texto* (`text-align` / `text-decoration`) — y el stack de fuentes que
> escribas decide cómo se ve la página en una máquina que no tiene tu fuente.

---

## 31. Las Cinco Familias

CSS soporta **cinco familias genéricas de fuente** en los principales navegadores
("web-safe"), y cada dispositivo tiene al menos una cara de cada:

| Familia | Características | Ejemplos |
| :--- | :--- | :--- |
| **Serif** | Pequeños trazos decorativos en los extremos de las letras; legible en imprenta | Georgia, Times New Roman, Baskerville |
| **Sans-serif** | Sin trazos finales; aspecto moderno y limpio para medios digitales | Arial, Helvetica Neue, Open Sans |
| **Monospace** | Cada carácter ocupa el mismo ancho; hecha para programar | Consolas, Courier New, Lucida Console |
| **Cursive** | Aspecto manuscrito; toque personal y creativo | Brush Script MT, Lobster, Dancing Script |
| **Fantasy** | Glifos muy estilizados o decorativos; personalidad máxima | Impact, Chiller, Jokerman |

El atajo de decisión: **serif** para lectura larga, **sans-serif** para interfaces y HUD,
**monospace** para código y números, **cursive/fantasy** para títulos que deben sentirse
pintados a mano.

---

## 32. Elegir una Cara y su Respaldo

Para fijar las familias de fuente se usa la propiedad `font-family`, con cualquier número
de nombres en una lista separada por comas — el navegador prueba cada uno en orden hasta
que existe:

```css
p {
  font-family: Arial, sans-serif;
}
```

> [!IMPORTANT]
> Termina siempre el stack con una **familia genérica** (`sans-serif`, `serif`,
> `monospace`…). La genérica es la red de seguridad: si la máquina del visitante no tiene
> ninguna fuente concreta, elige igualmente una cara con el *clima* correcto en lugar de
> caer en algo aleatorio.

```css
h1 {
  font-family: "Brush Script MT", "Lobster", cursive;
}
```

Los nombres entre comillas contienen espacios; los nombres genéricos sin comillas nunca
necesitan comillas.

---

## 33. Dimensionar el Texto

`font-size` fija el tamaño del texto con unidades absolutas (`px`, `pt`) o relativas
(`%`, `em`, `rem`):

```css
/* Absoluto: el tamaño es fijo */
p {
  font-size: 12px;
}

/* Relativo: escala con su contexto */
p {
  font-size: 1.2em;
}
```

> [!WARNING]
> **Nota de accesibilidad**
> Favorece las unidades relativas para el texto de los párrafos: los navegadores pueden
> reescalar `%`/`em`/`rem` con la preferencia de fuente del usuario, mientras que `px` se
> niega. Y mantén el cuerpo más pequeño que los encabezados — el tamaño del encabezado es
> como los lectores construyen el esquema mental de la página.

---

## 34. Dar Peso al Texto

`font-weight` define el grosor con palabras clave o con valores numéricos de `100` a `900`:

| Rango | Sensación |
| :--- | :--- |
| Menos de 400 | Fino / ligero |
| 400 – 700 | Rango normal para texto de cuerpo (400 = regular, 700 = negrita) |
| Más de 700 | Pesado — titulares, números de daño |

```css
p {
  font-weight: 800;
}
```

> [!NOTE]
> 400 y 700 son los pesos que la mayoría de archivos de fuente contienen de verdad; los
> valores intermedios los sintetiza el navegador cuando la cara no los tiene. Pide `800`
> y obtendrás "negrita, y algo más".

### Misión: Cinco Familias

Pon el conocimiento de familias en una página. Crea `index.html` y `styles.css`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Cinco Familias</title>
</head>
<body>
  <p>Hello world! Aprendiendo fuentes y estilos CSS.</p>
</body>
</html>
```

```css
p {
  font-family: Arial, sans-serif;
  font-size: 18px;
  font-weight: 600;
}
```

Un párrafo, tres decisiones: una cara limpia de interfaz, un tamaño legible, peso
media-negrita. Esa línea base es de donde partirá toda la HUD del vault.

---

## 35. Colocar el Texto

### `text-align`

Controla la **alineación horizontal** del contenido inline dentro de un bloque:

```css
#left-align {
  text-align: left; /* Predeterminado */
}

#center-align {
  text-align: center;
}

#right-align {
  text-align: right;
}
```

También existe `justify` (ambos márgenes alineados, estilo periódico) — genial para
párrafos largos de lore, peligroso para pies cortos, donde estira los huecos entre
palabras hasta convertirlos en ríos.

### `text-decoration`

Añade decoraciones visuales — subrayados, sobre-rayados, tachados — al texto:

```css
p {
  text-decoration: underline;
}
```

La abreviatura acepta hasta cuatro valores (línea, estilo, color, grosor) — la caja de
herramientas completa está en [[08 - Fondos y Shorthands]].

### Misión: Revisión Ortográfica

Estiliza una línea con erratas deliberadas igual que un editor de texto marca los errores.
Crea `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Revisión Ortográfica</title>
</head>
<body>
  <h4>The quick <span>brwn</span> fox jumped <span>overthe</span> lazy dogs.</h4>
</body>
</html>
```

Y `styles.css`:

```css
h4 {
  text-align: center;
}

span {
  text-decoration: underline wavy red 2px;
}
```

Línea centrada, subrayados rojos ondulados exactamente donde viven las erratas. Esa única
declaración — `underline wavy red 2px` — es la misma receta que usan los editores reales,
y no necesita más HTML que los `<span>` que señalan los fallos.

> [!TIP]
> **Versión para game devs**
> Una caja de diálogo con `text-align: center` y un texto de ambiente en una familia de
> fuente distinta es el 80% del aspecto "cinematográfico" de los RPG. La alineación le
> dice al jugador dónde mirar; la familia de fuente le dice cómo sentirse.

---

## XP Earned: Lo que te llevas

- 🖋️ Cinco familias genéricas existen en todas partes: **serif, sans-serif, monospace, cursive, fantasy**.
- 🧱 `font-family` es un **stack**: nombres concretos primero, familia genérica al final.
- 📏 `font-size`: absoluto (`px`) fijo, relativo (`em`/`rem`) accesible.
- ⚖️ `font-weight`: 100–900; 400 normal, 700 negrita.
- 🧭 `text-align` coloca las líneas; `text-decoration` las decora.
- 🦊 Una línea — `underline wavy red 2px` — es un resaltado de revisión completo.

---

## Loot Table: Casos de Uso Reales

- 🎮 Base de HUD: stack sans-serif, `18px`, peso `600`
- 📜 Páginas de lore: serif para lectura larga, `justify` para ambos márgenes
- 💻 Extractos de código: monospace con el mismo ancho en cada glifo
- 🏷️ Pantallas de título: cursive/fantasy para el texto de portada que debe sentirse pintado

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Escribe un stack de tres fuentes que termine en una familia genérica; pruébalo con la primera fuente ausente.
2. Fija el mismo texto a `12px`, `1em` y `1rem` — mide la diferencia.
3. Centra un encabezado, alinea un pie a la derecha y justifica un párrafo.
4. Reconstruye la página de revisión ortográfica con `dashed` en lugar de `wavy`.
5. **Pelea de jefe:** crea `hud.html` — un título de misión en fantasy, cuerpo en
   sans-serif `600`, texto de ambiente centrado y un nombre de héroe con errata marcado
   en rojo ondulado.

---

## 🔗 Ver También

- [[08 - Fondos y Shorthands]] — las abreviaturas completas de `text-decoration` y `font`
- [[02 - Colores y Medidas]] — las unidades que consume `font-size`
- [[05 - Pseudoelementos]] — letras iniciales para tus párrafos de lore
- [[00b - Chuleta de CSS]] — fuentes y texto en una página

---