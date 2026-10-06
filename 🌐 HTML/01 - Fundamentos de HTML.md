# 01. Fundamentos de HTML

**Versión original en inglés:** [01 - HTML Basics.md](01%20-%20HTML%20Basics.md)

**Curso:** HTML
**Tema:** Qué es HTML, elementos y etiquetas, encabezados, saltos de línea, formato de texto, listas, enlaces, imágenes y herramientas de desarrollo
**Tags:** `#html` `#web-development` `#basics` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Lecciones-01_--_07_%2B_Bonus-7C5CFF?style=for-the-badge" alt="Lecciones 01 a 07">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=7C5CFF&height=70&section=header" width="100%" alt="Ola violeta" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #E34F26, #2DD4BF, #E34F26, transparent); margin: 24px 0;" />

El primer capítulo del lenguaje que da estructura a cualquier página web. Al terminarlo
escribirás desde cero una **ficha de jefe** de Emberfall — con encabezados, texto formateado,
listas, un enlace y una imagen — y sabrás cómo inspeccionar cualquier página de Internet para
averiguar cómo está construida. La referencia de elementos y etiquetas está en
[[00b - Chuleta de HTML]].

> [!NOTE]
> **Todo el capítulo en una frase**
> HTML no *dibuja* nada y no *ejecuta* nada. Lo que hace es **etiquetar** contenido: este
> fragmento de texto es un encabezado, este otro es un elemento de lista, este tercero es un
> enlace. Todo lo demás que el navegador deba hacer llegará después, con CSS y JavaScript.

---

## 01. Moneda

> [!NOTE]
> **Información clave**
> **HTML** (**H**yper**T**ext **M**arkup **L**anguage) fue creado por **Tim Berners-Lee** en 1991 como la base de la World Wide Web. Hoy, todas las páginas web del mundo usan HTML.

HTML es un **lenguaje de marcado**: marca el contenido de una página web y le dice al navegador qué es cada fragmento.

### Las tres tecnologías principales de la web

| Tecnología | Rol | En la web de un juego |
| :--- | :--- | :--- |
| **HTML** | Crea la **estructura** de una página web | El esqueleto: qué paneles existen |
| **CSS** | Da **estilo** a la página | La piel: colores, tipografías, maquetación |
| **JavaScript** | La hace **interactiva** | El motor: barras de vida que se actualizan |

Este curso se centra en HTML. Los archivos que crearemos usan la extensión **`.html`**.

### Editor de código

Un **editor de código** es un editor de texto con el que podemos escribir, editar y ejecutar código.

### Misión: Secuencia de Arranque

Escribe estas dos líneas en tu editor, cambia el texto de ejemplo y pulsa **Run**:

```html
<h2>Emberfall 1.0 — fecha de lanzamiento</h2>
<p>Escribe tu frase de venta</p>
```

- Sustituye `Emberfall 1.0 — fecha de lanzamiento` por la fecha de hoy.
- Sustituye `Escribe tu frase de venta` por la frase de venta de tu juego.

Acabas de crear tu primera página web con HTML.

> [!TIP]
> Los archivos de este módulo son simples `.html` en una carpeta. No necesitas instalar nada
> ni compilar nada — en [[02 - El Árbol del Proyecto]] del módulo de Línea de Comandos ves cómo
> navegar a esa carpeta y abrir el archivo en el navegador.

---

## 02. Sistemas Centrales

### Elementos

Los **elementos** son los bloques más pequeños del lenguaje. Un elemento suele estar formado por una **etiqueta de apertura**, el **contenido** y una **etiqueta de cierre**. Una **etiqueta** va entre corchetes angulares.

```html
<p>Emberfall v1.0 ya está disponible.</p>
```

- `<p>` es la etiqueta de apertura.
- `Emberfall v1.0 ya está disponible.` es el contenido.
- `</p>` es la etiqueta de cierre.

El elemento **párrafo** `<p>` le indica al navegador que ese contenido es un párrafo.

### El elemento `<body>`

```html
<body><p>👋 ¡Nuevo héroe listo para Emberfall v1.0!</p></body>
```

El elemento `<body>` define el "cuerpo" del documento HTML: contiene todo el contenido que queremos mostrar al usuario.

> [!NOTE]
> Solo puede haber **un** elemento `<body>` por archivo.

### Sangría

Sangrar el HTML no es obligatorio, pero sí una buena práctica: facilita la lectura y muestra los **niveles de anidamiento**. Recomendamos **dos espacios** por nivel de sangría.

```html
<body>
  <p>👋 ¡Nuevo héroe listo para Emberfall v1.0!</p>
</body>
```

### Misión: Los Cuatro Sistemas

Crea `systems.html` para mostrar los cuatro sistemas que todo juego necesita (Entrada, Física, Audio, Renderizado) en el navegador, bien sangrado.

```html
<body>
  <p>Entrada</p>
  <p>Física</p>
  <p>Audio</p>
  <p>Renderizado</p>
</body>
```

---

## 03. Notas del Parche

### Encabezados

HTML tiene **seis niveles de encabezados**, de `<h1>` a `<h6>`. `<h1>` es el más grande y `<h6>` el más pequeño.

```html
<h1>Emberfall 1.4 — Las Salas Profundas</h1>
<h2>Contenido nuevo</h2>
<h3>Pasillos 5 a 9</h3>
<h4>Enemigos con farol</h4>
<h5>Notas del parche</h5>
<h6>Corregida una errata</h6>
```

> [!NOTE]
> Solo debe haber **un** elemento `<h1>` por archivo.

Los encabezados no sirven para cambiar el tamaño, sirven para la **estructura**: `<h2>`
significa "esto pertenece al `<h1>` anterior". Eso es lo que usan los lectores de pantalla y
los buscadores para entender de qué trata la página.

### Salto de línea

Pulsar `enter` dentro de un elemento no crea una nueva línea, porque **HTML colapsa los espacios y saltos de línea** dentro de los elementos. Para añadir un salto de línea usa la etiqueta `<br>`.

```html
<body>
  <h1>Parche 1.4</h1>
  <p>Se añadió el ala de las Salas Profundas.<br>Se corrigió el farol que no se apagaba.</p>
</body>
```

Una **etiqueta autocerrada** no necesita una etiqueta de cierre separada (no existe `</br>`).
`<br>` es la primera que vemos.

> [!WARNING]
> **El error más común**
> Pulsar `enter` dentro de un `<p>` parece correcto en el editor y, sin embargo, en el
> navegador aparece todo seguido. El espacio en blanco se **colapsa**: cualquier secuencia de
> espacios, tabuladores y saltos de línea dentro de un elemento se convierte en un único
> espacio. El único modo de romper una línea desde HTML es con `<br>`.

### Misión: Notas de Lanzamiento

Crea `patch_notes.html` con el registro de cambios del lanzamiento de tu juego:

- Un encabezado `<h1>` con el número de versión.
- Un encabezado `<h3>` con la fecha.
- Uno o varios párrafos `<p>` con el resumen.
- Saltos de línea `<br>` donde corresponda.

```html
<h1>Emberfall 1.4</h1>
<h3>14 de marzo de 2026</h3>
<p>Añade el ala de las Salas Profundas y dos minijefes nuevos.<br>Sustituye esto por tus propios cambios.</p>
```

---

## 04. Anuncio de Lanzamiento

### Formato de texto

| Elemento | Efecto |
| :--- | :--- |
| `<b>` | Texto en **negrita** |
| `<i>` | Texto en *cursiva* |
| `<u>` | Texto <u>subrayado</u> |
| `<s>` | Texto ~~tachado~~ |

```html
<b>Emberfall ya está disponible.</b><br>
<i>El mejor roguelike del año.</i><br>
<u>Demo gratuita disponible.</u><br>
<s>Precio de lanzamiento -90%</s><br>
```

> [!NOTE]
> `<b>` solo pone el texto en negrita por estilo. HTML también tiene `<strong>`, que indica
> que el contenido es **importante** y, además, lo muestra en negrita.

Todos los elementos juntos en un anuncio de tienda:

```html
<p>Este parche añade <i>Las Salas Profundas</i> y un <b>nuevo jefe</b>.<br>
El <u>bundle de reserva</u> ahora incluye el artebook, a <s>50€</s> 30€.</p>
```

> [!NOTE]
> Estas etiquetas sirven para aprender, pero **no son la mejor práctica actual**. En el curso
> de CSS veremos la forma moderna de aplicar estilos.

### Misión: Texto Promocional

Recrea el formato exacto del texto de una página de tienda en `announcement.html` usando `<p>`, `<b>`, `<i>`, `<s>` y `<u>`.

```html
<p>
  <b>Salas Profundas, ya disponibles:</b> Reconvertimos <s>el relleno de pasillos viejo</s> en un ala entero que te hará <i>grindear de verdad</i>. Botín nuevo, jefes nuevos y <b>un farol muy enfadado</b>. Consigue el <u>DLC Salas Profundas</u> con <i>descuento de lanzamiento</i>.
</p>

<p>
  <b>P.D.</b> Tras tres meses de beta, ¡estamos imprimiendo <b>los libros de arte de Emberfall</b>! Las reservas abren el lunes.
</p>
```

---

## 05. Receta de Forja

### Listas

HTML tiene dos tipos de listas:

- `<ul>` → Listas **desordenadas** (con viñetas)
- `<ol>` → Listas **ordenadas** (con números)

Cada elemento se envuelve en un `<li>` (**elemento de lista**).

```html
<ul>
  <li>🪨 Fragmento de brasa</li>
  <li>🍄 Champiñón de ceniza</li>
  <li>💧 Agua profunda</li>
</ul>
```

Usamos `<ul>` cuando el orden no importa. Para numerar los pasos, usamos `<ol>`:

```html
<ol>
  <li>🪨 Fragmento de brasa</li>
  <li>🍄 Champiñón de ceniza</li>
  <li>💧 Agua profunda</li>
</ol>
```

### Misión: Plano de Forja

Crea `recipe.html` con un objeto que te gustaría fabricar en tu juego: una lista **desordenada** para los ingredientes y una lista **ordenada** para los pasos de forja.

```html
<h2>Ingredientes</h2>
<ul>
  <li>1 fragmento de brasa</li>
  <li>2 champiñones de ceniza</li>
  <li>3 medidas de agua profunda</li>
</ul>

<h2>Pasos</h2>
<ol>
  <li>Funde el fragmento de brasa hasta que brille en naranja.</li>
  <li>Tritura los champiñones de ceniza hasta hacer un polvo fino.</li>
  <li>Vierte el agua profunda sobre el polvo y deja que reaccione.</li>
  <li>Martilla la mezcla hasta darle forma de hoja mientras aún está caliente.</li>
</ol>
```

> [!TIP]
> Esta estructura aparece en casi todas las pantallas de juego: un `<ul>` para estadísticas,
> un `<ol>` para pasos, una `<table>` para el resto. Un diario de misiones, una lista de
> habilidades y una baraja siguen exactamente esta forma.

---

## 06. Jefe Escapado

### Enlaces

Los **enlaces** son fundamentales para Internet: conectan páginas entre sí. El primer sitio web (1991) sigue en línea y está lleno de enlaces.

Usamos el elemento **ancla** `<a>` para crear un enlace a un texto:

```html
<a href="https://archive.org/web">Internet Archive</a>
```

- El texto dentro es lo que se ve.
- `href` (hyperlink reference) indica adónde lleva el enlace. Al hacer clic, el navegador va a esa dirección.

> [!NOTE]
> `href` también puede apuntar a un correo, a un teléfono o a un mensaje de texto con
> `mailto:`, `tel:` o `sms:`:

```html
<a href="mailto:parche@example.com">📧</a>
<a href="tel:212-555-0100">🤙</a>
<a href="sms:212-555-0123">💬</a>
```

### Imágenes

Usamos el elemento de imagen `<img>`:

```html
<p>Aquí hay una captura:</p>
<img src="https://example.com/jefe.png">
```

- `<img>` es otra **etiqueta autocerrada**.
- El atributo `src` ("source") indica la ruta del archivo de imagen.
- En la mayoría de sitios puedes hacer clic derecho en una imagen y elegir **Copiar dirección de imagen** para obtener esa ruta.

> [!IMPORTANT]
> Una imagen `<img>` sin `alt` es un error. Si la imagen no carga, el visitante ve un icono
> roto y no sabe qué debería aparecer — y un lector de pantalla anuncia la ruta del archivo
> en voz alta.

### Misión: Tablero de Recompensas

El jefe de Emberfall "Guardián de la Novena Planta" se ha escapado de los archivos del juego. Crea `boss.html` con:

- El nombre del jefe.
- Una imagen del jefe con `<img>`.
- Una breve descripción.
- Información de contacto con `<a>`.

```html
<h1>Jefe desaparecido: Guardián de la Novena Planta</h1>
<img src="https://placehold.co/300" alt="Un guardián alto y blindado con un farol">
<p>Vista por última vez en las Salas Profundas. Suelta la Llave de Brasa al derrotarlo y está muy enfadado por ello.</p>
<a href="mailto:archivista@example.com">Informar de un avistamiento</a>
```

---

## 07. Ficha de Jefe

### Punto de Control: Recapitulación

- Elementos HTML, etiquetas y sangría.
- Encabezados: `<h1>` a `<h6>`.
- Párrafos y saltos de línea: `<p>`, `<br>`.
- Formato de texto: `<b>`, `<i>`, `<u>`, `<s>`.
- Listas desordenadas y ordenadas: `<ul>`, `<ol>`, `<li>`.
- Enlaces e imágenes: `<a>`, `<img>`.

### Proyecto: Ficha de Jefe

Crea `boss.html` sobre el jefe de tu propio juego, usando **todos** los elementos aprendidos y **al menos dos tipos de formato de texto**. Debe incluir:

- El nombre del jefe.
- Una imagen del jefe.
- Una breve descripción de su lore.
- Un enlace a la wiki o al devlog.
- Las fases en una lista desordenada.
- Sus 5 ataques principales en una lista ordenada.

```html
<h1>Guardián de la Novena Planta</h1>
<img src="https://placehold.co/300" alt="Guardián de la Novena Planta">

<p>El Guardián es un <b>minijefe de dos fases</b> que custodia la última puerta de las Salas Profundas. <i>Cambia de comportamiento al 50% de vida</i> y suelta el farol para luchar a oscuras.</p>

<a href="https://example.com/emberfall/guardian">Lee la entrada completa del códex</a>

<h2>Fases</h2>
<ul>
  <li>Fase 1 — Farol</li>
  <li>Fase 2 — Oscuridad</li>
</ul>

<h2>Mis 5 ataques principales</h2>
<ol>
  <li>Barrido de farol</li>
  <li>Proyectil de brasa</li>
  <li>Tajo de suelo</li>
  <li>Embestida a ciegas</li>
  <li>Colapso de la Novena Planta</li>
</ol>
```

> [!TIP]
> **Versión para desarrollo de videojuegos**
> Una ficha de jefe es una hoja de personaje: cambia el encabezado por el nombre del enemigo,
> la descripción por el lore, la lista desordenada por las fases y la ordenada por la lista de
> movimientos. Cada pantalla de datos de un juego es esta página con otras palabras. El
> capítulo [[02 - Estructura y Atributos]] toma esa ficha y le añade `class` e `id` para que
> una hoja de estilos pueda darle forma.

---

## Botín Extra:: Herramientas de Desarrollo

### Inspeccionar

Las **herramientas de desarrollo** nos permiten crear, probar y depurar páginas web. Todos los navegadores modernos incluyen estas herramientas integradas, que permiten **inspeccionar** cualquier sitio web y ver su código completo.

| Navegador | Nombre | Cómo abrirlo | Atajo de teclado |
| :--- | :--- | :--- | :--- |
| **Google Chrome** | DevTools | Clic derecho > "Inspeccionar" | `ctrl` + `shift` + `c` (Windows/Linux); `cmd` + `option` + `i` (macOS) |
| **Apple Safari** | Safari Develop | Menú > Preferencias > Avanzado > Mostrar menú Desarrollar | `option` + `cmd` + `c` |
| **Mozilla Firefox** | Firefox Developer Tools | Menú > Más herramientas > Herramientas para desarrolladores web | `ctrl` + `shift` + `i` (Windows/Linux); `cmd` + `option` + `i` (macOS) |

Cómo abrirlas paso a paso:

- **Chrome:** haz clic derecho en la página y elige "Inspeccionar". Pulsa el icono de la flecha (selector de elementos) en la esquina superior izquierda y pasa el ratón por un elemento para inspeccionarlo.
- **Safari:** activa el menú Desarrollar en Preferencias > Avanzado. Después, Desarrollar > Mostrar inspector web.
- **Firefox:** abre el menú (tres líneas) > Más herramientas > Herramientas para desarrolladores web.

### Características más útiles

- Inspeccionar y resaltar elementos HTML para ver su información y estilos.
- Una **consola** para escribir y ejecutar JavaScript directamente en el navegador.
- Un **modo responsive** para ver cómo se renderiza la página en distintos tamaños de pantalla.

### Extra: Truco divertido

Desde el panel "Elements" (Elementos) puedes hacer doble clic en el código HTML y cambiar el texto de cualquier elemento. Verás el cambio al instante. No has "hackeado" la web: al recargar la página todo vuelve a su estado original, pero es un truco muy útil para aprender.

### Más recursos

- Documentación de Chrome DevTools
- Información sobre las herramientas de desarrollo de Safari
- Documentación de Firefox Developer Tools

> [!TIP]
> Las herramientas de desarrollo son la forma más rápida de aprender HTML. Inspecciona
> cualquier página de un juego que te guste y lee las etiquetas que ha usado su creador. Diez
> minutos inspeccionando enseñan más que una hora adivinando.

---

## XP Obtenida: Conclusiones clave

- 🧱 **Elementos** = etiqueta de apertura + contenido + etiqueta de cierre.
- 📐 **Sangría** con dos espacios para mostrar el anidamiento.
- 🔠 Seis niveles de encabezados, pero solo **un `<h1>`** por archivo.
- ↩️ `<br>` y `<img>` son **etiquetas autocerradas**.
- 🖍️ `<b>`, `<i>`, `<u>`, `<s>` dan formato al texto (la forma moderna es con CSS).
- 📋 `<ul>` para viñetas, `<ol>` para números, `<li>` para cada elemento.
- 🔗 `<a href>` para enlaces, `<img src>` para imágenes.
- 🔍 Las herramientas de desarrollo nos permiten inspeccionar cualquier página.

---

## Botín: Casos de uso reales

- 📰 Artículos, blogs y páginas de noticias
- 📋 Recetas de crafteo, registros de misiones y menús de mercader
- 🧑‍🎤 Páginas de perfil o de fans
- 🔗 Páginas de enlaces y portfolios sencillos
- 🎮 Fichas de jefe, catálogos de objetos y notas de parche — el mismo marcado, otras palabras

---

## Misiones Secundarias: Ejercicios prácticos

1. Crea un `bio.html` con un `<h1>`, dos párrafos y una lista con tus aficiones.
2. Añade un enlace a tu sitio favorito y otro con `mailto:` para enviarte un correo.
3. Usa los cuatro elementos de formato de texto en un mismo párrafo.
4. Abre las herramientas de desarrollo en cualquier página y cambia el texto de un encabezado.
5. **Desafío final:** crea `bestiario.html` con un `<h1>`, un `<h2>` por criatura, un `<img>` con `alt`, y para cada una: un `<ul>` con sus debilidades y un `<ol>` con su botín (al menos 3 criaturas).

---

## Ver también

- [[00b - Chuleta de HTML]] — todos los elementos de este capítulo en una sola página
- [[02 - Estructura y Atributos]] — siguiente capítulo: esqueleto de página, comentarios y atributos
- [[03 - Formularios]] — para recoger datos del usuario
- [[04 - HTML Semántico]] — para darle a la página una maquetación con sentido

---