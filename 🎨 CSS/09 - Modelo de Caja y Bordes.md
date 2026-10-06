# 09. Modelo de Caja y Bordes

**Versión original en inglés:** [09 - Box Model & Borders.md](09%20-%20Box%20Model%20&%20Borders.md)

**Curso:** CSS
**Tema:** Las cuatro capas de la caja, inspeccionar la caja, la propiedad `border`, bordes por lado, `border-radius` y el marco del feed
**Tags:** `#css` `#web-development` `#box-model` `#borders` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-F7DF1E?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-42_--_46-7C5CFF?style=for-the-badge" alt="Lecciones 42 a 46">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

El modelo mental más importante de CSS: todo elemento de una página es una **caja** con
cuatro capas — contenido, padding, borde y margin — y cada regla de espaciado que escribas
manipula una de ellas. Este capítulo mapea las capas, te muestra cómo inspeccionar
cualquier caja en el navegador y domina la propiedad `border` en todas sus formas.
Referencia: [[00b - Chuleta de CSS]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Contenido dentro, padding a su alrededor, borde rodeando al padding, margin fuera —
> cuatro capas concéntricas que deciden dónde empieza, termina y se sienta un elemento
> respecto a sus vecinos.

---

## 42. Las Cuatro Capas

El Modelo de Caja de CSS define cómo se renderiza cada elemento como una caja rectangular.
De dentro a fuera:

| Capa | Qué contiene | Piensa en |
| :--- | :--- | :--- |
| **Caja de contenido** | El contenido real: texto, imágenes, medios | La propia habitación |
| **Caja de padding** | Espacio entre el contenido y el borde, *dentro* del elemento | Los muebles separados de las paredes |
| **Caja de borde** | El marco que envuelve la caja de padding | Las paredes |
| **Caja de margin** | Espacio vacío fuera del borde, que controla la distancia con los vecinos | El patio entre casas |

```css
div {
  padding: 20px;     /* espacio interior */
  border: 2px solid; /* el marco */
  margin: 10px;      /* espacio exterior */
}
```

Cada capa es opcional: padding cero, sin borde y margin cero son legales — y la caja
sigue existiendo, porque la capa de contenido siempre está.

> [!TIP]
> Cuando una maquetación "se ve mal", pregúntate *qué capa* está mintiendo. Demasiado
> pegado al borde → padding. Toca a su vecino → margin. Falta el marco → border. La
> pregunta apunta a la propiedad cada vez.

---

## 43. Inspeccionar la Caja

Los navegadores incluyen herramientas de desarrollo que inspeccionan las dimensiones y
las propiedades espaciales de un elemento — el profesor más rápido del módulo.

| Navegador | Cómo abrirlo |
| :--- | :--- |
| **Google Chrome** | Clic derecho en un elemento → *Inspect* → pestaña *Computed* |
| **Apple Safari** | Ajustes → Avanzado → marca *Mostrar funciones para desarrolladores web*; luego Develop → *Show Web Inspector* |

Dentro del panel de elementos encontrarás cuatro rectángulos anidados — el diagrama del
modelo de caja — que iluminan la capa exacta sobre la que pasas el cursor. Haz clic en
cualquier valor numérico y edítalo en vivo; la página se actualiza mientras miras.

> [!NOTE]
> El encabezado del módulo HTML (`[[01 - Fundamentos de HTML]]` Bonus Loot) abría las
> herramientas de desarrollo para el marcado. Aquí la misma herramienta muestra la
> *geometría*: pasa el cursor por el diagrama y observa cómo el resaltado pasa del
> contenido al padding, al borde y al margin.

---

## 44. La Propiedad `border`

El shorthand `border` combina **grosor, estilo y color** en una sola declaración.

### Versión larga vs. Shorthand

```css
/* Sintaxis larga */
h1 {
  border-width: 2px;
  border-style: solid;
  border-color: blue;
}

/* Sintaxis shorthand equivalente */
h1 {
  border: 2px solid blue;
}
```

| Propiedad clave | Opciones |
| :--- | :--- |
| `border-width` | Valores con unidad como `px` |
| `border-style` | `solid`, `dashed`, `dotted`, `double`, `groove`, `ridge` |
| `border-color` | Colores con nombre, `rgb()`, Hex |

### Los Estilos, Lado a Lado

| Estilo | Cómo se ve |
| :--- | :--- |
| `solid` | Una línea continua |
| `dashed` | Guiones cortos |
| `dotted` | Puntos |
| `double` | Dos líneas paralelas |
| `groove` / `ridge` | Efecto 3D tallado / en relieve |

> [!IMPORTANT]
> Como en [[08 - Fondos y Shorthands]], un borde sin **estilo** no se renderiza —
> `border: 2px blue` es un fantasma. Primero el estilo, luego el tamaño y el color.

---

## 45. Bordes por Lado y Esquinas Redondeadas

### Bordes Individuales

Cada lado puede estilizarse de forma independiente con propiedades direccionales:

```css
h1 {
  border-top: 5px dashed red;
  border-right: 5px dotted purple;
  border-bottom: 5px double yellow;
  border-left: 5px solid green;
}
```

Cuatro lados, cuatro identidades: `top`/`right`/`bottom`/`left` van en sentido horario
desde arriba.

### Border Radius

`border-radius` redondea las esquinas; los valores más altos crean bordes más redondos:

```css
h1 {
  border: 2px solid blue;
  border-radius: 5px;
}
```

Los extremos: `border-radius: 50%` sobre un elemento cuadrado hace un círculo — el
movimiento estándar para avatares e iconos de clase.

> [!NOTE]
> `border-radius` funciona también sin borde: redondea la caja de padding. Un avatar no
> necesita marco para ser redondo, solo un radio.

---

## 46. Marco del Feed

### Checkpoint: Resumen del Capítulo

- Cuatro capas: contenido → padding → borde → margin.
- La pestaña *Computed* de las herramientas de desarrollo muestra el diagrama de caja y
  edita valores en vivo.
- `border: width style color` — estilo obligatorio, lados estilizables por separado.
- `border-radius` redondea esquinas; `50%` convierte un cuadrado en un círculo.

### Proyecto: Marco de Tarjeta de Feed

Una tarjeta de feed social para jugadores de Emberfall, enmarcada con el modelo de caja.
El pase completo de espaciado (padding, margin, dimensiones) es el capítulo
[[10 - Espaciado y Box Sizing]] — aquí colocamos los bordes.

#### HTML (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Mi Feed</title>
</head>
<body>
  <div id="outside-wrapper">
    <img id="top-img" src="https://placehold.co/160" alt="Avatar del jugador" />

    <ul id="post-list">
      <h2>Mi Feed</h2>
      <li>
        <div class="post-wrapper">
          <img class="post-img" src="https://placehold.co/600x200" alt="El Archivo del Gremio al atardecer" />
          <p>¡Asaltamos el archivo! <b>#raidgremio</b> <b>#cazadelore</b></p>
        </div>
      </li>
      <hr />
      <li>
        <div class="post-wrapper">
          <img class="post-img" src="https://placehold.co/600x100" alt="Banner de victoria cooperativa" />
          <p>¡Carpe diem! <b>#wipe</b> <b>#inténtalo otra vez</b></p>
        </div>
      </li>
    </ul>
  </div>
</body>
</html>
```

#### CSS (`styles.css`)

```css
* {
  font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}

div {
  border: 2px solid grey;
}

#top-img {
  width: 10em;
  height: 10em;
  border: 12px solid green;
  border-radius: 50%;
}

.post-img {
  width: 100%;
  border-radius: 5px;
}
```

El avatar se convierte en un círculo con anillo verde con un solo `border-radius`; cada
tarjeta del feed queda enmarcada por el `div` genérico; la obra interior recibe un radio
suave de 5px. Los bordes ya están — el espaciado viene después.

> [!TIP]
> **Versión para game devs**
> Las tarjetas de feed, las placas de logros y los anuncios de botín se enmarcan igual:
> un anillo, un radio, un divisor. El `hr` entre publicaciones es lo que el modelo de caja
> llama "dos listados separados por una caja de margin fina". El capítulo
> [[10 - Espaciado y Box Sizing]] les da aire para respirar.

---

## XP Earned: Lo que te llevas

- 📦 Cuatro capas: **contenido → padding → borde → margin**, de dentro a fuera.
- 🔍 La pestaña *Computed* de DevTools = el diagrama del modelo de caja, editable en vivo.
- 🖼️ `border: width style color` — y sin estilo, el borde es invisible.
- 🧭 `border-top/right/bottom/left` estilizan lados sueltos; `border-radius` redondea esquinas.
- ⭕ `border-radius: 50%` convierte cuadrados en círculos.

---

## Loot Table: Casos de Uso Reales

- 🧑‍🤝‍🧑 Anillos de avatar e iconos de clase en cada pantalla de perfil
- 🏷️ Marcos de tarjetas, divisores y contornos de resaltado
- 📰 Feeds y líneas de tiempo con bordes por lado
- 🎮 Placas de logros, tarjetas de botín y marcos de lista de amigos

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Dibuja el modelo de caja de un `<p>` con padding, borde y margin — a mano y luego en DevTools.
2. Dale a una tarjeta cuatro lados con bordes diferentes.
3. Redondea solo las esquinas superiores de un banner con `border-radius` de dos valores.
4. Haz circular un avatar con `border-radius: 50%` y un anillo grueso de color.
5. **Pelea de jefe:** enmarca una tarjeta de membresía de gremio — avatar circular, dos
   publicaciones con divisores, obra interior redondeada — primero los bordes, sin reglas
   de espaciado todavía.

---

## 🔗 Ver También

- [[10 - Espaciado y Box Sizing]] — padding, margin, centrado y `box-sizing`
- [[08 - Fondos y Shorthands]] — donde nació el shorthand `border`
- [[02 - Colores y Medidas]] — unidades y notaciones de color para bordes
- [[00c - Chuleta de CSS II]] — el diagrama del modelo de caja en una página

---