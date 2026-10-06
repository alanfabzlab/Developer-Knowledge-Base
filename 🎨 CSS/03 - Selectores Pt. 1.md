# 03. Selectores Pt. 1

**Versión original en inglés:** [03 - Selectors Pt. 1.md](03%20-%20Selectors%20Pt.%201.md)

**Curso:** CSS
**Tema:** Qué son los selectores, selectores de tipo, selectores de clase, selectores de ID y apuntado combinado
**Tags:** `#css` `#web-development` `#selectors` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Lecciones-12_--_16-7C5CFF?style=for-the-badge" alt="Lecciones 12 a 16">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Una regla vale lo que vale su puntería. Este capítulo trata de la primera mitad de toda
regla que escribirás — el **selector** — y de las tres armas que lleva todo desarrollador:
tipo, clase e ID. También aprenderás **targeting**, la técnica de encadenarlas hasta que
una regla acierte exactamente a un elemento de la página. Referencia:
[[00b - Chuleta de CSS]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Los selectores responden *¿qué elementos?* — por nombre de etiqueta (`div`), por
> etiqueta de clase (`.class`) o por nombre único (`#id`) — y combinarlos hace que la
> respuesta sea más precisa.

---

## 12. Fijado de Blanco

Los **selectores** determinan qué elemento(s) HTML se estilizan. Todo lo que hay a la
izquierda del `{` en una regla es un selector; todo lo de dentro es la pintura.

```css
/* "Todos los <p> de la página" */
p {
  color: dimgray;
}
```

Tres familias de selectores cubren casi todo:

| Familia | Cómo se escribe | Selecciona | Piensa en ello como |
| :--- | :--- | :--- | :--- |
| **Tipo** | `div` | Todos los elementos con esa etiqueta | Un cargo: "todos los ingenieros" |
| **Clase** | `.class-name` | Cualquier elemento que lleve esa clase | Un uniforme: "quien esté de guardia" |
| **ID** | `#id-name` | El único elemento con ese id | Una chapa de nombre: una sola persona |

---

## 13. Selector de Tipo

El **selector de tipo** (también llamado selector de *elemento* o de *etiqueta*) elige
todos los elementos que coinciden por nombre de etiqueta.

```css
div {
  /* Aplicado a todos los elementos <div> */
}

p {
  /* Aplicado a todos los elementos <p> */
}
```

Sin punto, sin almohadilla — solo el nombre de la etiqueta. Es el pincel más amplio que
tienes, lo que lo hace perfecto para los valores predeterminados de toda la página:

```css
body {
  font-family: Arial, sans-serif;
  background-color: #1b1b2f;
}
```

> [!TIP]
> Define una sola vez con selectores de tipo las reglas aburridas y de página completa
> (`body`, `h1`, `p`), y recurre a clases e IDs siempre que algo necesite *romper* el
> valor predeterminado. Menos anulaciones, menos sorpresas.

---

## 14. Selector de Clase

Un **selector de clase** se escribe con un **punto** `.` y apunta a todo elemento cuyo
atributo `class` coincida — que pueden ser tantos como quieras.

```html
<p class="line">Las grietas arden más brillante.</p>
<p class="line">La ceniza lo recuerda todo.</p>
<p>No estoy estilizado.</p>
```

```css
.line {
  /* Aplicado a todos los elementos con class="line" */
}
```

Las clases son el caballo de batalla de CSS: reutilizables, apilables
(`class="line active"`) y felices de aparecer en todos los elementos que desees.

---

## 15. Selector de ID

Un **selector de ID** se escribe con una **almohadilla** `#` y apunta al único elemento
cuyo atributo `id` coincida. HTML permite cada id una sola vez por archivo.

```html
<p id="victory">¡Victoria!</p>
```

```css
#victory {
  /* Aplicado al único elemento con id="victory" */
}
```

> [!WARNING]
> **class frente a id**
> Una clase es un *rol* que cualquier elemento puede llevar; un id es un *nombre* que solo
> un elemento puede tener. Reutilizar un id en varios elementos es HTML inválido y rompe
> en silencio la unicidad que prometen los selectores `#id`. ¿Necesitas estilizar tres
> cosas igual? Para eso existen las clases.

---

## 16. Apuntado Combinado (Targeting)

El **targeting** sube la especificidad encadenando tipos de elemento con clases o IDs, de
modo que una regla solo se aplica a elementos que cumplan *todas* las partes.

```css
div.line {
  /* Solo elementos <div> que además tienen class="line" */
}

div#victory {
  /* Solo el <div> que tiene id="victory" */
}
```

| Selector | Coincide con | Especificidad |
| :--- | :--- | :--- |
| `p` | Todos los párrafos | Baja |
| `.line` | Todos los elementos con `class="line"` | Media |
| `#victory` | El elemento con `id="victory"` | Alta |
| `p.line` | Los párrafos que *también* son `.line` | Más alta |
| `p#line` | El único párrafo que es `#victory` | Máxima |

Piensa en un control de seguridad: cuanto más insignias exiges, menos gente pasa — y la
regla no se aplica a nadie más.

### Misión: Trabalenguas del Reino

Practica con las tres familias a la vez. Crea `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Selectores</title>
</head>
<body>
  <div>
    <p class="line" id="rifts">Las grietas son rojas.</p>
    <p class="line" id="runes">Las runas son azules.</p>
    <p class="line" id="potions">Las pociones son dulces.</p>
    <p class="line">¡Y tú también!</p>
  </div>
</body>
</html>
```

Y `styles.css`:

```css
/* Selector de tipo */
div {
  border: 1px solid;
  text-align: center;
}

/* Selector de clase */
.line {
  width: 50%;
  margin: auto;
  padding: 10px 0;
  text-decoration: underline;
}

/* Selectores de ID */
#rifts {
  background-color: red;
}

#runes {
  background-color: violet;
}

#potions {
  background-color: beige;
}
```

Lee el CSS de arriba abajo: la regla `div` enmarca las *cuatro* líneas, la clase `.line`
las centra y subraya a *todas*, y los tres IDs pintan exactamente una cada uno. Mismo
elemento, tres selectores distintos apilándose encima — así se construyen exactamente las
hojas de estilo reales.

> [!NOTE]
> Cuando dos reglas apuntan al mismo elemento, gana la más específica: `#rifts` vencería a
> `.line` en el color de fondo siempre. La especificidad es el tema oculto del siguiente
> capítulo y la razón por la que `04 - Selectores Pt. 2` enseña a repartir reglas *entre*
> elementos con grouping en lugar de apilarlas todas sobre uno.

---

## XP Earned: Lo que te llevas

- 🎯 Los selectores deciden **qué** elementos pinta la regla.
- 🔖 **Tipo** = nombre de etiqueta desnudo, el pincel más amplio.
- 🏷️ **Clase** = punto inicial, reutilizable en cualquier cantidad de elementos.
- 🏷️ **ID** = almohadilla inicial, único por archivo — un solo elemento.
- 🎯 **Targeting** = encadenarlos (`div.line`, `p#line`) para ganar precisión.
- 🥇 El selector más específico gana cuando dos reglas chocan.

---

## Loot Table: Casos de Uso Reales

- 🧾 Tipografía de página completa definida una vez en `body` y en las etiquetas de encabezado
- 🏷️ Estilos reutilizables de botones, tarjetas e insignias con clases
- 🎯 Secciones héroe y modales puntuales dirigidos por id
- 🎮 Marcos de grupo, filas de misiones y ranuras de inventario: una clase por tipo de fila, un id por pantalla

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Estiliza todos los `<h2>` de una página con un selector de tipo y luego anula uno con una clase.
2. Dale `class="card"` a tres elementos y `id="featured"` a uno; estiliza ambos.
3. Escribe un selector que acierte solo a los `<p>` dentro de `class="line"`.
4. Descubre quién gana: `.line` vs `#rifts` vs `p.line` — escríbelos.
5. **Pelea de jefe:** crea `roster.html` — un `<div>` con seis líneas `<p class="hero">`,
   cada una con un `id` único, estilizadas por las tres familias de selectores.

---

## 🔗 Ver También

- [[00b - Chuleta de CSS]] — la tabla de selectores de este capítulo
- [[02 - Colores y Medidas]] — capítulo anterior: paletas y unidades
- [[04 - Selectores Pt. 2]] — grouping, combinadores de hijo y el volante final
- [[06 - Pseudoclases]] — seleccionar por *estado* en vez de por nombre

---
