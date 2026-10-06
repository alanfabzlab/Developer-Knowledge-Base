# 02. Colores y Medidas

**Versión original en inglés:** [02 - Colors & Measurements.md](02%20-%20Colors%20&%20Measurements.md)

**Curso:** CSS
**Tema:** La propiedad `color`, colores con nombre, `rgb()`, hexadecimal, ancho y alto, unidades absolutas y unidades relativas
**Tags:** `#css` `#web-development` `#colors` `#units` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Lecciones-06_--_11-7C5CFF?style=for-the-badge" alt="Lecciones 06 a 11">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Dos alfabetos de estilos, enseñados juntos porque responden a la misma pregunta: *¿de qué
tamaño y de qué color?* Primero la paleta — colores con nombre, `rgb()` y hex — y después
la regla: píxeles, porcentajes, `em` y `rem`. Al terminar pintarás un gráfico de tipos de
daño en tres notaciones distintas y medirás el mismo sprite de dos maneras. Referencia
rápida: [[00b - Chuleta de CSS]].

> [!NOTE]
> **Todo el capítulo en una frase**
> El color y el tamaño son las dos propiedades que escribirás más que ninguna otra, así
> que conviene conocer tres formas de escribir un color y dos familias de unidades — una
> que nunca se mueve y otra que se adapta.

---

## 06. La Paleta

Una de las señales de identidad de cualquier página web es estilizarla con colores. En CSS,
los colores resaltan texto, rellenan fondos, dibujan bordes y pintan degradados.

Para dar color al **texto**, usamos la propiedad `color`:

```css
p {
  color: red;
}
```

### Colores con Nombre

Los navegadores admiten **140 colores con nombre** — `red`, `tomato`, `skyblue`,
`lightgreen`, `rebeccapurple` y otros 136. Son la forma más rápida de escribir un color y
la menos precisa para igualar uno: ningún color con nombre es "naranja de nuestra marca".

```css
h1 {
  color: tomato;
}

footer {
  background-color: lightgreen;
}
```

> [!NOTE]
> El color del texto es `color`; el color de fondo es `background-color`. Misma palabra,
> dos propiedades distintas — confundirlas es el equivalente CSS a pintar el marco en vez
> de la pared.

---

## 07. Mezclador RGB

`rgb()` representa la intensidad de **R**ed, **G**reen y **B**lue (rojo, verde y azul). Cada parámetro admite
un entero desde `0` (sin intensidad) hasta `255` (intensidad máxima).

```css
/* Rojo */
color: rgb(255, 0, 0);

/* Verde */
color: rgb(0, 255, 0);

/* Azul */
color: rgb(0, 0, 255);

/* Naranja Emberfall: rojo y verde, sin azul */
color: rgb(255, 107, 53);
```

Cada color de una pantalla es uno de estos tripletes. `rgb()` es lo que usas cuando un
diseñador te entrega "R: 255, G: 107, B: 53" — y lo que usarás *después* cuando quieras
transparencia, con su primo `rgba()`, donde un cuarto valor de `0` a `1` fija el alfa.

---

## 08. Runas Hexadecimales

Los colores también pueden escribirse en **hexadecimal**: un `#` seguido de **6
caracteres** — los dígitos `0`–`9` y las letras `a`–`f` (o `A`–`F`). Los tres pares son
rojo, verde y azul en ese orden, y cada par va de `00` a `ff` (= 0 a 255).

```css
color: #ff0000; /* Rojo   — igual que rgb(255, 0, 0) */
color: #008000; /* Verde  — igual que rgb(0, 128, 0) */
color: #0000ff; /* Azul   — igual que rgb(0, 0, 255) */
color: #ff6b35; /* Naranja Emberfall */
```

- `#ff0000` → par rojo `ff`, par verde `00`, par azul `00`.
- `#000` también es válido: una abreviatura de **3 dígitos** donde cada carácter se duplica
  (`#f00` = `#ff0000`).

> [!TIP]
> Mezclar mayúsculas y minúsculas funciona (`#FF6B35` y `#ff6b35` son el mismo color),
> pero elige una convención y manténla — todo el vault usa minúsculas.

### Misión: Gráfico de Daños

Tres tipos de daño, tres notaciones. Crea `index.html` y `styles.css`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Tipos de Daño</title>
</head>
<body>
  <h1>Los Tres Tipos de Daño Principales</h1>
  <h2 id="first-type">Fuego</h2>
  <h2 id="second-type">Veneno</h2>
  <h2 id="third-type">Escarcha</h2>
</body>
</html>
```

```css
/* Color con nombre */
#first-type {
  color: red;
}

/* Color rgb() */
#second-type {
  color: rgb(0, 128, 0);
}

/* Color hexadecimal */
#third-type {
  color: #0000ff;
}
```

Los mismos tres colores escritos de tres maneras — y al final del módulo nunca más te
preguntarás qué notación estás mirando.

---

## 09. La Regla: Unidades Absolutas

La mayoría de los elementos HTML tienen un tamaño predeterminado, con alto y ancho. En CSS
los cambiamos con las propiedades `width` y `height`:

```css
element {
  width: 10px;
  height: 10px;
}
```

Pero ¿qué es un `px`? Las unidades vienen en dos familias, y elegir la equivocada es como
se rompen las maquetaciones en la siguiente pantalla.

Las unidades absolutas son **fijas**: nunca cambian de tamaño, haga lo que haga el padre o
la pantalla.

| Unidad | Nombre | Uso |
| :--- | :--- | :--- |
| `px` | píxeles | La unidad absoluta más común — bordes, cajas fijas |
| `pt` | puntos | Impresión (1pt = 1/72 pulgada) |
| `cm` / `in` | centímetros / pulgadas | Soporte físico |

```css
#badge {
  width: 100px;
  height: 100px;
}
```

> [!WARNING]
> Fijar el **alto** con unidades absolutas es la forma clásica de que el contenido escape
> de su caja. Escribe `height: 100px` bajo un párrafo y observa el texto desbordar el borde
> cuando se parte en una tercera línea. Mejor deja que el alto crezca, o usa unidades
> relativas.

## 10. La Regla: Unidades Relativas

Las unidades relativas **cambian cuando algo más cambia** — el elemento padre, o la raíz
del propio documento.

| Unidad | Relativa a | Uso típico |
| :--- | :--- | :--- |
| `%` | El tamaño del elemento **padre** | `width: 50%` — la mitad de lo que sea el padre |
| `em` | El tamaño de fuente **del propio elemento** (o del padre, al heredarse) | Relleno que escala con el texto |
| `rem` | El tamaño de fuente de la raíz **`<html>`** (16px por defecto) | Espaciado que escala con toda la página |

```css
/* La mitad del padre, siempre */
#relative {
  width: 50%;
}

/* 1.2 veces el tamaño de fuente de este elemento */
p {
  font-size: 1.2em;
}

/* 2 veces el tamaño raíz = 32px por defecto */
h1 {
  font-size: 2rem;
}
```

> [!NOTE]
> `em` se acumula: un texto de `1.2em` dentro de un contenedor de `1.2em` se renderiza a
> 1.44× el tamaño raíz. `rem` nunca se acumula — siempre mide desde `<html>`. Cuando
> quieras "el doble del valor por defecto de la página", quieres `rem`.

## 11. Misión: Dimensionar Sprites

El mismo recurso, dos filosofías. Crea `index.html` + `styles.css`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Medidas</title>
</head>
<body>
  <h2>Unidades Absolutas</h2>
  <img id="absolute" src="https://placehold.co/96" alt="Sprite de fuego" />

  <h2>Unidades Relativas</h2>
  <img id="relative" src="https://placehold.co/96" alt="Sprite de fuego" />
</body>
</html>
```

```css
#absolute {
  width: 100px;
}

#relative {
  width: 50%;
}
```

Redimensiona la ventana: el primer sprite ni se mueve un píxel, el segundo respira con su
contenedor. Esa única diferencia es el diseño responsive esperando a que la desbloquees.

---

## XP Earned: Lo que te llevas

- 🎨 Tres formas de escribir un color: **con nombre**, **`rgb(r, g, b)`**, **`#rrggbb`** —
  las tres describen el mismo rojo.
- 🌈 Hex va de `00`–`ff` por canal; `#f00` es la abreviatura de `#ff0000`.
- 📏 `width` / `height` aceptan cualquier unidad; la familia que elijas decide qué
  sobrevive a un redimensionado.
- 🧱 Las unidades **absolutas** (`px`, `pt`, `cm`) nunca cambian. Las **relativas**
  (`%`, `em`, `rem`) cambian con el padre, la fuente o la raíz.
- ⚠️ Un `height` absoluto es la forma clásica de hacer que el texto desborde su propia caja.

---

## Loot Table: Casos de Uso Reales

- 🎨 Paletas de marca: un código hex por color, reutilizado en todo el sitio
- 📊 Gráficos y insignias donde los colores deben coincidir exactamente
- 🖼️ Miniaturas y avatares medidos en `px`, rejillas fluidas medidas en `%`
- 📝 Escalas tipográficas construidas en `rem` para que toda la página se redimensione a la vez

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Escribe el color `teal` como nombre, como `rgb()` y como hex — comprueba que los tres se ven igual.
2. Dale a un `<div>` `width: 50%` y arrastra el borde del navegador; luego dale `width: 300px` y repite.
3. Fija un `height` a un párrafo, añade texto hasta desbordarlo y borra el `height`.
4. Expresa 32px como `rem` (raíz = 16px).
5. **Pelea de jefe:** crea `palette.html` — cinco elementos, cinco colores, cada notación
   usada al menos una vez, más un elemento medido en `px` y otro en `%`.

---

## 🔗 Ver También

- [[01 - Fundamentos de CSS]] — reglas, selectores y el enlace a la hoja de estilos
- [[03 - Selectores Pt. 1]] — apuntar el color exactamente a los elementos que quieres
- [[07 - Fuentes y Texto]] — donde el color se encuentra con la tipografía
- [[08 - Fondos y Shorthands]] — `background-color`, `background-image` y compañía

---
