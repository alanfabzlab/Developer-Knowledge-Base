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
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #E34F26, #2DD4BF, #E34F26, transparent); margin: 24px 0;" />

El primer capítulo del lenguaje que da estructura a cualquier página web. Al terminarlo
escribirás una página de tu grupo favorito desde cero — con encabezados, texto formateado,
listas, un enlace y una imagen — y sabrás cómo inspeccionar cualquier página de Internet
para averiguar cómo está construida. La referencia de elementos y etiquetas está en
[[00b - Chuleta de HTML]].

> [!NOTE]
> **Todo el capítulo en una frase**
> HTML no *dibuja* nada y no *ejecuta* nada. Lo que hace es **etiquetar** contenido: este
> fragmento de texto es un encabezado, este otro es un elemento de lista, este tercero es un
> enlace. Todo lo demás que el navegador deba hacer llegará después, con CSS y JavaScript.

---

## 01. Shooting Star

> [!NOTE]
> **Información clave**
> **HTML** (**H**yper**T**ext **M**arkup **L**anguage) fue creado por **Tim Berners-Lee** en 1991 como la base de la World Wide Web. Hoy, todas las páginas web del mundo usan HTML.

HTML es un **lenguaje de marcado**: marca el contenido de una página web y le dice al navegador qué es cada fragmento.

### Las tres tecnologías principales de la web

| Tecnología | Rol |
| :--- | :--- |
| **HTML** | Crea la **estructura** de una página web |
| **CSS** | Da **estilo** a la página |
| **JavaScript** | La hace **interactiva** |

Este curso se centra en HTML. Los archivos que crearemos usan la extensión **`.html`**.

### Editor de código

Un **editor de código** es un editor de texto con el que podemos escribir, editar y ejecutar código.

### Ejercicio: Misión 01: Generar tu primera página

Escribe estas dos líneas en tu editor, cambia el texto de ejemplo y pulsa **Run**:

```html
<h2>Escribe la fecha</h2>
<p>Escribe tu deseo</p>
```

- Sustituye `Escribe la fecha` por la fecha de hoy.
- Sustituye `Escribe tu deseo` por un deseo.

Acabas de crear tu primera página web con HTML.

> [!TIP]
> Los archivos de este módulo son simples `.html` en una carpeta. No necesitas instalar nada
> ni compilar nada — en [[02 - Sistema de Archivos]] ves cómo navegar a esa carpeta y abrir
> el archivo en el navegador.

---

## 02. Elemental

### Elementos

Los **elementos** son los bloques más pequeños del lenguaje. Un elemento suele estar formado por una **etiqueta de apertura**, el **contenido** y una **etiqueta de cierre**. Una **etiqueta** va entre corchetes angulares.

```html
<p>¡Hola Mundo!</p>
```

- `<p>` es la etiqueta de apertura.
- `¡Hola Mundo!` es el contenido.
- `</p>` es la etiqueta de cierre.

El elemento **párrafo** `<p>` le indica al navegador que ese contenido es un párrafo.

### El elemento `<body>`

```html
<body><p>👋 ¡Soy un nuevo desarrollador web!</p></body>
```

El elemento `<body>` define el "cuerpo" del documento HTML: contiene todo el contenido que queremos mostrar al usuario.

> [!NOTE]
> Solo puede haber **un** elemento `<body>` por archivo.

### Sangría

Sangrar el HTML no es obligatorio, pero sí una buena práctica: facilita la lectura y muestra los **niveles de anidamiento**. Recomendamos **dos espacios** por nivel de sangría.

```html
<body>
  <p>👋 ¡Soy un nuevo desarrollador web!</p>
</body>
```

### Misión: Pergamino Elemental

Crea `elemental.html` para mostrar los cuatro elementos de la antigua Grecia (Fuego, Agua, Tierra, Aire) en el navegador, bien sangrado.

```html
<body>
  <p>Fuego</p>
  <p>Agua</p>
  <p>Tierra</p>
  <p>Aire</p>
</body>
```

---

## 03. Periódico

### Encabezados

HTML tiene **seis niveles de encabezados**, de `<h1>` a `<h6>`. `<h1>` es el más grande y `<h6>` el más pequeño.

```html
<h1>Encabezado nivel 1</h1>
<h2>Encabezado nivel 2</h2>
<h3>Encabezado nivel 3</h3>
<h4>Encabezado nivel 4</h4>
<h5>Encabezado nivel 5</h5>
<h6>Encabezado nivel 6</h6>
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
  <h1>Noticia de última hora</h1>
  <p>Un hombre de Florida roba una tienda con un caimán.<br>Deja unas Crocs de bebé atrás.</p>
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

### Misión: Crónica de la Taberna

Crea `newspaper.html` con lo que ocurría en las noticias el día en que naciste:

- Un encabezado `<h1>` con el título.
- Un encabezado `<h3>` con la fecha.
- Uno o varios párrafos `<p>` con la noticia.
- Saltos de línea `<br>` donde corresponda.

```html
<h1>El Diario</h1>
<h3>1 de enero de 2000</h3>
<p>Hoy ocurrieron grandes acontecimientos en el mundo.<br>Sustituye esto por titulares reales de tu fecha de nacimiento.</p>
```

---

## 04. Charla Corporativa

### Formato de texto

| Elemento | Efecto |
| :--- | :--- |
| `<b>` | Texto en **negrita** |
| `<i>` | Texto en *cursiva* |
| `<u>` | Texto <u>subrayado</u> |
| `<s>` | Texto ~~tachado~~ |

```html
<b>Este texto está en negrita.</b><br>
<i>Este texto está en cursiva.</i><br>
<u>Este texto está subrayado.</u><br>
<s>Este texto está tachado.</s><br>
```

> [!NOTE]
> `<b>` solo pone el texto en negrita por estilo. HTML también tiene `<strong>`, que indica
> que el contenido es **importante** y, además, lo muestra en negrita.

Todos los elementos juntos en un anuncio:

```html
<p>Recuerda que el <i>examen final</i> es <b>obligatorio</b>.<br>
Se celebrará el <u>lunes 14 de octubre</u> a las <s>19:00</s> 20:00 (hora EST).</p>
```

> [!NOTE]
> Estas etiquetas sirven para aprender, pero **no son la mejor práctica actual**. En el curso
> de CSS veremos la forma moderna de aplicar estilos.

### Misión: Anuncio del Gremio

Recrea un texto con jerga corporativa en `corporate.html` usando `<p>`, `<b>`, `<i>`, `<s>` y `<u>`.

```html
<p>
  <b>Aumentamos el ritmo y recortamos:</b> Tenemos una estrategia sólida para pasar de las <s>frutas bajas</s> a objetivos <i>críticos para la misión</i> que realmente marcan la diferencia. Es hora de <b>aumentar los ingresos</b> y, al mismo tiempo, <u>reducir los costes</u>. Esto es una victoria para todos: una victoria para nosotros y para <i>nuestros increíbles accionistas</i>.
</p>

<p>
  <b>P.D.</b> Tras varios meses con ventas récord, ¡estamos imprimiendo <b>camisetas de agradecimiento a los empleados</b>! Saldrán a la venta el lunes.
</p>
```

---

## 05. Sous-Chef

### Listas

HTML tiene dos tipos de listas:

- `<ul>` → Listas **desordenadas** (con viñetas)
- `<ol>` → Listas **ordenadas** (con números)

Cada elemento se envuelve en un `<li>` (**elemento de lista**).

```html
<ul>
  <li>🧺 Ir a la lavandería.</li>
  <li>🖥️ Programar 45 minutos.</li>
  <li>🛁 Darse un baño de espuma.</li>
</ul>
```

Usamos `<ul>` cuando el orden no importa. Para numerar los pasos, usamos `<ol>`:

```html
<ol>
  <li>🧺 Ir a la lavandería.</li>
  <li>🖥️ Programar 45 minutos.</li>
  <li>🛁 Darse un baño de espuma.</li>
</ol>
```

### Misión: Receta de Poción

Crea `chef.html` con una receta de poción que te apetezca: una lista **desordenada** para los ingredientes y una lista **ordenada** para los pasos.

```html
<h2>Ingredientes</h2>
<ul>
  <li>2 rebanadas de pan</li>
  <li>2 rebanadas de queso</li>
  <li>1 cucharada de mantequilla</li>
</ul>

<h2>Instrucciones</h2>
<ol>
  <li>Unta mantequilla en una cara de cada rebanada de pan.</li>
  <li>Coloca el queso entre las caras sin mantequilla.</li>
  <li>Calienta en una sartén a fuego medio hasta que esté dorado por ambos lados.</li>
</ol>
```

> [!TIP]
> Esta estructura aparece en casi todas las pantallas de juego: un `<ul>` para estadísticas,
> un `<ol>` para pasos, una `<table>` para el resto. Un diario de misiones, una receta de poción, una
> lista de habilidades y una baraja siguen exactamente esta forma.

---

## 06. Mascota Perdida

### Enlaces

Los **enlaces** son fundamentales para Internet: conectan páginas entre sí. El primer sitio web (1991) sigue en línea y está lleno de enlaces.

Usamos el elemento **ancla** `<a>` para crear un enlace a un texto:

```html
<a href="https://archive.org/web">Internet Archive</a>
```

- El texto dentro es lo que se ve.
- `href` (hiperlink reference) indica adónde lleva el enlace. Al hacer clic, el navegador va a esa dirección.

> [!NOTE]
> `href` también puede apuntar a un correo, a un teléfono o a un mensaje de texto con
> `mailto:`, `tel:` o `sms:`:

```html
<a href="mailto:frankie@example.com">📧</a>
<a href="tel:212-555-0100">🤙</a>
<a href="sms:212-555-0123">💬</a>
```

### Imágenes

Usamos el elemento de imagen `<img>`:

```html
<p>Aquí hay una foto bonita:</p>
<img src="https://example.com/foto-bonita.jpg">
```

- `<img>` es otra **etiqueta autocerrada**.
- El atributo `src` ("source") indica la ruta del archivo de imagen.
- En la mayoría de sitios puedes hacer clic derecho en una imagen y elegir **Copiar dirección de imagen** para obtener esa ruta.

> [!IMPORTANT]
> Una imagen `<img>` sin `alt` es un error. Si la imagen no carga, el visitante ve un icono
> roto y no sabe qué debería aparecer — y un lector de pantalla anuncia el nombre del
> archivo en voz alta.

### Misión Secundaria: Compañero Desaparecido

Un amigo ha perdido a su compañero. Crea `pet.html` con:

- El nombre de la compañero.
- Una foto de la compañero con `<img>`.
- Una breve descripción.
- Información de contacto con `<a>`.

```html
<h1>Mascota perdida: Barnaby</h1>
<img src="https://placehold.co/300" alt="Perro perdido llamado Barnaby">
<p>Barnaby es un perro marrón y amistoso que desapareció anoche mientras llevaba un collar rojo.</p>
<a href="mailto:propietario@example.com">Contactar con el propietario</a>
```

---

## 07. Grupo Favorito

### Punto de Control: Recapitulación

- Elementos HTML, etiquetas y sangría.
- Encabezados: `<h1>` a `<h6>`.
- Párrafos y saltos de línea: `<p>`, `<br>`.
- Formato de texto: `<b>`, `<i>`, `<u>`, `<s>`.
- Listas desordenadas y ordenadas: `<ul>`, `<ol>`, `<li>`.
- Enlaces e imágenes: `<a>`, `<img>`.

### Proyecto: Grupo Favorito

Crea `band.html` sobre tu artista favorito, usando **todos** los elementos aprendidos y **al menos dos tipos de formato de texto**. Debe incluir:

- El nombre del artista.
- Una foto del artista o de su disco.
- Una breve descripción del artista.
- Un enlace a su sitio web oficial.
- Una lista desordenada con los miembros del grupo.
- Una lista ordenada con sus 5 canciones favoritas.

```html
<h1>Daft Punk</h1>
<img src="https://placehold.co/300" alt="Daft Punk">

<p>Daft Punk fue un <b>icónico dúo francés de música electrónica</b> formado en París. Alcanzaron un <i>éxito mundial</i> tanto en el synthpop como en la música house.</p>

<a href="https://daftpunk.com">Visitar su web oficial</a>

<h2>Miembros</h2>
<ul>
  <li>Thomas Bangalter</li>
  <li>Guy-Manuel de Homem-Christo</li>
</ul>

<h2>Mis 5 canciones favoritas</h2>
<ol>
  <li>One More Time</li>
  <li>Digital Love</li>
  <li>Harder, Better, Faster, Stronger</li>
  <li>Around the World</li>
  <li>Get Lucky</li>
</ol>
```

> [!TIP]
> **Versión para desarrollo de videojuegos**
> Esta ficha de banda de taberna es igual que una ficha de enemigo o de personaje. Cambia el
> encabezado por el nombre de la criatura, la descripción por el lore, la lista desordenada
> por sus habilidades y la lista ordenada por su botín. El capítulo [[02 - Estructura y Atributos]]
> toma esa ficha y le añade `class` e `id` para que una hoja de estilos pueda darle forma.

---

## Botín Extra:: Consola de Depuración

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
> cualquier página que te guste y lee las etiquetas que ha usado su creador. Diez minutos
> inspeccionando enseñan más que una hora adivinando.

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
- 📋 Recetas, listas de tareas y menús
- 🧑‍🎤 Páginas de perfil o de fans
- 🔗 Páginas de enlaces y portfolios sencillos
- 🎮 Fichas de enemigo, catálogos de objetos y diarios de misiones — el mismo marcado, otras palabras

---

## Misiones Secundarias: Ejercicios prácticos

1. Crea `bio.html` con un `<h1>`, dos párrafos y una lista con tus aficiones.
2. Añade un enlace a tu sitio favorito y otro con `mailto:` para enviarte un correo.
3. Usa los cuatro elementos de formato de texto en un mismo párrafo.
4. Abre las herramientas de desarrollo en cualquier página y cambia el texto de un encabezado.
5. **Desafío final:** crea `bestiario.html` con un `<h1>`, un `<h2>` por criatura, un `<img>` con `alt`, y para cada una: un `<ul>` con sus debilidades y un `<ol>` con su botín (al menos 3 criaturas).

---

## Ver también

- [[00b - Chuleta de HTML]] — todos los elementos de este capítulo en una sola página
- [[02 - Estructura y Atributos]] — siguiente capítulo: esqueleto de página, comentarios y atributos
- [[03 - Formularios]] — para recoger datos del usuario

---