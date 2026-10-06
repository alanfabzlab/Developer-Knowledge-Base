# 06. Pseudoclases

**Versión original en inglés:** [06 - Pseudo-classes.md](06%20-%20Pseudo-classes.md)

**Curso:** CSS
**Tema:** Estados de elemento, pseudoclases de enlaces (`:hover`, `:visited`), de campos (`:checked`) y de hijos (`:first-child`, `:last-child`, `:nth-child`)
**Tags:** `#css` `#web-development` `#pseudo-classes` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-F7DF1E?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-26_--_30-7C5CFF?style=for-the-badge" alt="Lecciones 26 a 30">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Los pseudoelementos estilizaban las *partes* de un elemento; las **pseudoclases**
estilizan sus *estados*. Un botón en reposo, un botón con el cursor encima, un enlace ya
visitado, el quinto elemento de un registro de misiones: mismo elemento, momento distinto,
estilo distinto. El capítulo hermano sobre partes es [[05 - Pseudoelementos]]. Referencia:
[[00b - Chuleta de CSS]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Una pseudoclase selecciona un elemento *en un estado concreto* — `a:hover`,
> `li:first-child`, `input:checked` — escrita como `selector:nombre` con **un solo dos
> puntos**, y a diferencia de los pseudoelementos, las pseudoclases nunca crean contenido.

---

## 26. Todo Elemento Tiene Humores

Algunos elementos HTML cambian de estado según cómo interactúe el usuario con la página:

- Pasar el cursor sobre un enlace o un botón.
- Un enlace que cambia de color *después* de hacer clic y de haberlo visitado.
- La posición de un hijo entre sus hermanos — primero, último o en medio.

```css
selector:pseudo-class {
  /* estilos aquí */
}
```

Un selector normal, dos puntos `:`, y el nombre de la pseudoclase. El estado cambia y el
estilo lo sigue — el equivalente CSS de un botón que se ilumina cuando lo miras.

> [!TIP]
> La traducción al diseño de juegos: las pseudoclases son *feedback de entrada*. Cada vez
> que un jugador pasa el cursor o hace clic y la interfaz reacciona, al menos una
> pseudoclase está haciendo el trabajo. Son cómo las interfaces comunican "esto está vivo".

---

## 27. Enlaces: Memoria Viva

Algunas de las pseudoclases más comunes están unidas al elemento `<a>`, porque un enlace
tiene estados ricos.

### `:hover`

Los estilos se aplican solo mientras el cursor está sobre el elemento:

```css
a:hover {
  background-color: yellow;
  color: red;
}
```

> [!NOTE]
> El mismo `:hover` funciona en `<button>` y en cualquier otro elemento interactivo —
> hover es un estado, no una exclusiva de los enlaces.

### `:visited`

Los estilos se aplican después de hacer clic en el enlace y visitarlo. Los navegadores
limitan lo que `:visited` puede cambiar (color y un par de propiedades decorativas) para
que una página no pueda espiar tu historial de navegación:

```css
a:visited {
  color: purple;
}
```

> [!WARNING]
> **El orden importa.** `:visited` anula en silencio los estilos anteriores. El orden
> clásico de los estados del enlace es *LoVe/HAte* — `:link`, `:visited`, `:hover`,
> `:active` — así que escribe las reglas de hover y active **después** de la regla de
> visited, o el estado posterior nunca se mostrará.

---

## 28. Campos: Despiertos y Seleccionados

El elemento `<input>` también responde a `:hover`:

```css
input:hover {
  background-color: green;
}
```

Y para las casillas de verificación y los botones de radio existe `:checked` — el estado
de "esta casilla está marcada", perfecto para alternar opciones:

```css
input:checked {
  outline: 2px solid blue;
}
```

> [!NOTE]
> Para ser precisos puedes acotarlo: `input[type="checkbox"]:checked` o
> `input[type="radio"]:checked`. Mismo estado, objetivo explícito.

### Misión: Pantalla de Ajustes

Crea un interruptor de ajustes: una casilla que cambie visiblemente cuando el jugador
active una opción.

```html
<label>
  <input type="checkbox" />
  Modo noche
</label>
```

```css
input:checked {
  outline: 2px solid #ff6b35;
  box-shadow: 0 0 4px #ff6b35;
}
```

Marca la casilla y el contorno se enciende. Desmárcala y se apaga — sin JavaScript.

---

## 29. La Fila del Grupo

Las pseudoclases también apuntan a **elementos hijo** concretos desde un padre. Conoce al
grupo:

```html
<ul>
  <li>Mara, la Tejelamas</li>
  <li>Thorne, la Artífice</li>
  <li>Piper, la Exploradora</li>
  <li>Grum, el Baluarte</li>
  <li>Halcyon, la Sabia</li>
  <li>Bash, el Herrero</li>
  <li>Snee, la Alquimista</li>
</ul>
```

### `:first-child`

Selecciona el primer hijo directo de un padre — el líder del grupo en la fila:

```css
li:first-child {
  border: 2px solid purple;
}
```

### `:last-child`

Selecciona el último hijo directo — el que sujeta la puerta:

```css
li:last-child {
  border: 2px solid purple;
}
```

### `:nth-child()`

Aplica estilos según **posición o patrón**, y acepta un argumento entre paréntesis:

```css
/* Por posición (índice base 1): el quinto héroe */
li:nth-child(5) {
  border: 2px solid purple;
}

/* Por palabra clave: los héroes impares */
li:nth-child(odd) {
  border: 2px solid purple;
}

/* Los pares también funcionan, y las fórmulas como 2n+1 */
li:nth-child(even) {
  background-color: #1b1b2f;
  color: #f5f5f5;
}
```

> [!NOTE]
> `nth-child` cuenta desde **1**, no desde 0: `:first-child` y `:nth-child(1)` son el
> mismo elemento, y `odd` significa las posiciones 1, 3, 5… Aplicar rayas de cebra a una
> tabla o un registro de misiones es una línea: `li:nth-child(even) { background… }`.

### Misión: Registro de Misiones a Rayas

Coge cualquier lista de siete héroes y ponla a rayas:

```css
li:nth-child(even) {
  background-color: #2b2b36;
  color: #ffffff;
}
```

La legibilidad de todo un registro con una sola regla — la tabla de misiones de tu juego
se publica con esta línea exacta dentro.

---

## 30. Resumen de Estados

### Checkpoint: Qué Hace Cada Pseudoclase

| Pseudoclase | Selecciona | Uso más común |
| :--- | :--- | :--- |
| `:hover` | El elemento bajo el cursor | Feedback de botones y enlaces |
| `:visited` | El enlace ya clicado | Color de "ya estuve aquí" |
| `:checked` | La casilla/radio marcada | Alternadores de opciones, ajustes |
| `:first-child` | El primer hijo directo | Énfasis del elemento líder |
| `:last-child` | El último hijo directo | Énfasis del elemento de cierre |
| `:nth-child(n)` | Hijo por posición (`odd`, `even`, `2n+1`) | Listas a rayas, patrones de cuadrícula |

> [!WARNING]
> **Pseudoclase contra pseudoelemento, en 30 segundos**
> `:hover` — un dos puntos — *estado del elemento entero*. `::before` — doble dos puntos —
> *una parte del elemento*. Uno narra, el otro disecciona; mezcla los dos puntos y la regla
> deja de coincidir en silencio.

### Más Recursos

- [MDN: Pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes)
- Artículo extra: Pseudoelementos → [[05 - Pseudoelementos]]
- Todos en una sola hoja: [[00c - Chuleta de CSS II]]

---

## XP Earned: Lo que te llevas

- 🎭 Una pseudoclase estiliza un elemento **en un estado**: `selector:nombre`.
- 🖱️ `:hover` es el feedback universal; `:visited` recuerda dónde clicaste.
- ✅ `:checked` estiliza casillas y radios marcados.
- 👥 `:first-child` / `:last-child` / `:nth-child()` eligen hijos por posición.
- 🦓 `:nth-child(even)` pone una lista entera a rayas en una línea.
- ➡️ Un dos puntos = estado (pseudoclase); doble dos puntos = parte (pseudoelemento).

---

## Loot Table: Casos de Uso Reales

- 🎮 Estados de hover en botones, tarjetas e iconos de habilidad
- ⚙️ Alternadores de ajustes y filtros con `:checked`
- 📜 Registros de misiones, tablas e inventarios a rayas
- 🧭 Enlaces de navegación que muestran dónde ya has estado

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Construye tres botones con estilos `:hover` distintos.
2. Fuerza un color de enlace visitado y comprueba que DevTools coincide.
3. Pon a rayas un registro de grupo de 10 filas con una sola regla `:nth-child`.
4. Añade un resaltado `:checked` a un grupo de radio de opciones de dificultad.
5. **Pelea de jefe:** recrea una pantalla de ajustes — casilla de modo noche, grupo de
   radio de volumen — entera con pseudoclases, sin JavaScript.

---

## 🔗 Ver También

- [[05 - Pseudoelementos]] — las partes, estilizadas con doble dos puntos
- [[04 - Selectores Pt. 2]] — los selectores que portan estos estados
- [[07 - Fuentes y Texto]] — qué hacen los estilos de hover con la tipografía
- [[00c - Chuleta de CSS II]] — la tabla completa de estados

---