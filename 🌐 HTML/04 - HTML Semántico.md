# 04. HTML Semántico

**Versión original en inglés:** [04 - Semantic HTML.md](04%20-%20Semantic%20HTML.md)

**Curso:** HTML
**Tema:** HTML semántico, `header`, `footer`, `main`, `article`, `section`, `aside`, `nav`, `figure`, `time`, enlaces accesibles, entidades
**Tags:** `#html` `#web-development` `#semantica` `#accesibilidad` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-19_--_24-7C5CFF?style=for-the-badge" alt="Lecciones 19 a 24">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=FF6B35&height=70&section=header" width="100%" alt="Ola de brasa" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #E34F26, #2DD4BF, #E34F26, transparent); margin: 24px 0;" />

Hasta ahora todas nuestras páginas han sido un `<div>` con texto dentro. Se ven bien y
funcionan, pero un navegador que ve `<div>` solo ve una caja. Este capítulo cambia esas cajas
por elementos que **dicen lo que son**: esto es la cabecera del juego, esto es la guía de la
misión, esto es la barra lateral con builds relacionadas. El resultado visual apenas cambia.
Todo lo demás, sí.

> [!NOTE]
> **Todo el capítulo en una frase**
> El HTML semántico es una promesa que le haces al navegador, a los lectores de pantalla, a
> los buscadores y a tu yo del futuro: *este elemento significa esto*. El resultado visual es
> casi un accidente — y por eso se omite tan a menudo.

---

## 19. HUD Superior

### Header, Main y Footer

Toda página moderna tiene la misma estructura de tres regiones, y HTML tiene un elemento para cada una:

- `<header>` — normalmente la parte superior de la página: logo, navegación, título. También puede ir dentro de un `<article>` o un `<section>`.
- `<main>` — el contenido único y central de la página. **Debería existir solo uno por página.**
- `<footer>` — normalmente la parte inferior: copyright, enlaces, autoría. También puede ir dentro de un `<article>` o un `<section>`.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Emberfall</title>
  </head>
  <body>
    <header>
      <h1>Emberfall</h1>
      <p>Un roguelike sobre morir en sitios interesantes.</p>
    </header>

    <main>
      <p>La partida empieza en la Bóveda de Brasa y acaba en las Salas Profundas.</p>
    </main>

    <footer>
      <p>© 2026 Emberfall Studio. Ningún jefe resultó herido de forma permanente.</p>
    </footer>
  </body>
</html>
```

> [!IMPORTANT]
> `<header>` y `<footer>` **no** son `<head>` y `<body>`. Viven dentro de `<body>`, se
> muestran en la página, y `<header>` no tiene ningún efecto especial sobre los metadatos del
> documento: sus únicos trabajos son la franja superior y, cuando está anidado, la cabecera de
> una sección o artículo.
>
> Un `<footer>` dentro de un `<article>` guarda la autoría, la fecha y las etiquetas de ese
> artículo — no el aviso legal del sitio. Son dos cosas distintas, luego dos elementos
> distintos.

> [!TIP]
> **Versión para videojuegos**
> `<header>` / `<main>` / `<footer>` es una distribución de pantalla. Un HUD, la vista del
> juego y la barra de menú son tres papeles en la misma escena, y darle a cada uno su elemento
> es la diferencia entre una pantalla que puedes maquetar por regiones y otra que solo puedes
> colocar a mano.

### Misión: Página de Bienvenida

Crea `header_footer.html`. Dentro de `<body>`, añade:

- Un `<header>` con un `<h1>` y un párrafo corto sobre tu sitio o proyecto.
- Un `<main>` con al menos dos párrafos (o un encabezado y varios párrafos).
- Un `<footer>` con un `<p>` que incluya el aviso de copyright.

Después comprueba en el navegador que las tres regiones aparecen en ese orden.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Emberfall</title>
  </head>
  <body>
    <header>
      <h1>Emberfall</h1>
      <p>Un roguelike sobre morir en sitios interesantes.</p>
    </header>

    <main>
      <h2>Versión 1.4</h2>
      <p>La Bóveda de Brasa tiene un jefe nuevo. Las Salas Profundas están más oscuras.</p>
      <p>No se reequilibró nada salvo lo que estaba roto.</p>
    </main>

    <footer>
      <p>© 2026 Emberfall Studio. Ningún jefe resultó herido de forma permanente.</p>
    </footer>
  </body>
</html>
```

---

## 20. Artículo de la Guía

### `article`, `section` y `aside`

### `article`

Usa `<article>` para un contenido **autónomo** que seguiría teniendo sentido si se sacara de
la página y se leyera por separado. Noticias, entradas de blog y reseñas de productos cumplen
esta condición.

Para un artículo, suele ser buena práctica incluir un encabezado dentro del `<article>`, junto
con un `<footer>` con los metadatos (autoría, fecha de publicación, etiquetas).

```html
<article>
  <h2>Parche 1.4: El Guardián Despierta</h2>
  <p>El Guardián era un rumor en la Bóveda de Brasa. A partir del 1.4, el rumor tiene barra de vida.</p>
  <footer>
    <p>Publicado por <strong>Dev_Wanda</strong> el <time datetime="2026-03-14">14 de marzo de 2026</time></p>
  </footer>
</article>
```

> [!IMPORTANT]
> Un `<article>` no es específicamente una "entrada de blog". Es cualquier trozo de contenido
> que se sostiene solo: un hilo de foro, una ficha de producto con su propia reseña, una
> entrada de wiki, un comentario con suficiente sustancia como para citarlo aparte.

### `section`

Usa `<section>` para agrupar contenido relacionado que **no** se sostiene por sí solo: necesita
el contexto de la página que lo rodea.

En un `<section>` es muy recomendable tener un encabezado. Muchos desarrolladores argumentan
que una `<section>` sin encabezado es, en realidad, un `<div>`.

```html
<section>
  <h2>Estrategias de jefes</h2>
  <p>El Guardián se teletransporta en la tercera fase. Engáñalo con la segunda.</p>
</section>
```

> [!TIP]
> **Versión para videojuegos**
> Un `<article>` es una misión: autónoma, con su nombre, sus recompensas y su autoría. Un
> `<section>` es una zona: solo significa algo como parte del mapa. Esa distinción — "¿esto
> sigue teniendo sentido por sí solo?" — es la forma más rápida de elegir entre los dos, y
> también se aplica a los paneles de interfaz.

### `aside`

Usa `<aside>` para contenido **relacionado tangencialmente** con lo que lo rodea: una barra
lateral, una cita destacada, un glosario, un anuncio.

```html
<article>
  <h2>Parche 1.4: El Guardián Despierta</h2>
  <p>El Guardián era un rumor en la Bóveda de Brasa. A partir del 1.4, el rumor tiene barra de vida.</p>
  <aside>
    <h3>Builds relacionadas</h3>
    <ul>
      <li>Exploradora Prime — trampa y castigo</li>
      <li>Tanque Wanda — esponja de agro</li>
    </ul>
  </aside>
</article>
```

### Misión: Notas de Parche

Crea `patch_notes.html` con:

1. Un `<article>` para el anuncio del parche, con un `<h2>` y dos párrafos.
2. Dentro del `<article>`, un `<footer>` con un `<p>` que nombre al autor y un atributo `datetime` en un elemento `<time>`.
3. Una `<section>` de "Cambios de balance" con un `<h2>` y una lista no ordenada de al menos tres cambios.
4. Un `<aside>` dentro del `<article>` con un `<h3>` y una lista de dos elementos relacionados.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Notas de parche — Emberfall</title>
  </head>
  <body>
    <main>
      <article>
        <h2>Parche 1.4: El Guardián Despierta</h2>
        <p>El Guardián era un rumor en la Bóveda de Brasa. A partir del 1.4, el rumor tiene barra de vida.</p>
        <p>La tercera fase se teletransporta. La cuarta no. Suerte.</p>

        <aside>
          <h3>Builds relacionadas</h3>
          <ul>
            <li>Exploradora Prime — trampa y castigo</li>
            <li>Tanque Wanda — esponja de agro</li>
          </ul>
        </aside>

        <footer>
          <p>Publicado por <strong>Dev_Wanda</strong> el <time datetime="2026-03-14">14 de marzo de 2026</time></p>
        </footer>
      </article>

      <section>
        <h2>Cambios de balance</h2>
        <ul>
          <li>Hoja de Brasa: daño 14 → 17</li>
          <li>Enfriamiento de la poción de vida: 30s → 20s</li>
          <li>La fase tres del Guardián ya no limpia el agro</li>
        </ul>
      </section>
    </main>
  </body>
</html>
```

---

## 21. Navegación del Sitio

### `nav`

Usa `<nav>` para los **enlaces de navegación principales**: el menú del sitio, una tabla de
contenidos, la paginación.

```html
<nav>
  <ul>
    <li><a href="/equipamientos">Equipamientos</a></li>
    <li><a href="/jefes">Jefes</a></li>
    <li><a href="/notas-de-parche">Notas de parche</a></li>
  </ul>
</nav>
```

Un `<nav>` no es cualquier grupo de enlaces. **Los enlaces dentro de un `<footer>` no necesitan
un `<nav>` que los envuelva.** Es para la navegación sustancial del sitio.

> [!NOTE]
> Se pueden tener varios elementos `<nav>`, y es algo habitual: uno para el menú principal,
> otro para la tabla de contenido de un artículo, otro para la paginación. La regla práctica
> es que cada uno sea una región de navegación real de la que el usuario depende para moverse.

> [!TIP]
> Una tabla de contenidos es el ejemplo más claro: es un `<nav>` con una lista de elementos
> `<a>` cuyos `href="#ancla"` apuntan a encabezados que tienen `id`. Ese mismo patrón es
> exactamente la estructura de un menú de pausa en un juego: una lista de destinos.

---

## 22. Galería de Objetos

### `figure` y `figcaption`

Usa `<figure>` para representar contenido autónomo: una ilustración, un diagrama, una foto,
un fragmento de código. A veces la figura lleva un pie que describe el contenido, y ese pie
puede ir envuelto en un elemento `<figcaption>`.

```html
<figure>
  <img src="https://placehold.co/300" alt="Mapa del mundo de Emberfall">
  <figcaption>Figura 1: El mundo exterior. Las Salas Profundas están en algún punto debajo.</figcaption>
</figure>
```

> [!NOTE]
> Un `<img>` no es un `<figure>`. La figura es *la cosa más su descripción*; la imagen es
> solo la cosa. Una tabla con pie, un fragmento de código con explicación o un diagrama
> funcionan igual de bien dentro de un `<figure>`.

### Enlaces accesibles

El texto de un enlace debe describir **a dónde lleva el enlace**. "Haz clic aquí" es un
callejón sin salida para cualquiera que navegue por voz o con un lector de pantalla: solo oye
"haz clic aquí" sin ningún destino.

```html
<a href="/jefes/guardian">La guía del jefe Guardián</a>
```

Evita también las URLs crudas como texto de enlace. Y nunca uses la propia URL como etiqueta:

```html
<!-- Mal -->
<a href="https://emberfall.example/wiki/guardian">https://emberfall.example/wiki/guardian</a>

<!-- Bien -->
<a href="https://emberfall.example/wiki/guardian">La guía del jefe Guardián</a>
```

> [!IMPORTANT]
> Un enlace que se abre en una pestaña nueva debería decirlo. Si no, quien lo pulsa pierde su
> sitio sin aviso. Lo mismo vale para los enlaces que descargan un archivo o que disparan algo
> inesperado: anúncialo en el texto del enlace, no en un tooltip que nadie ve.

### `time`

Usa `<time>` cuando el contenido sea una fecha, una hora o ambas. El atributo `datetime`
guarda el valor legible por máquina; el texto interior es lo que mejor se lea para una persona.

```html
<p>El parche 1.4 salió el <time datetime="2026-03-14T18:00:00Z">14 de marzo de 2026 a las 18:00 UTC</time>.</p>
```

Sin `datetime`, `<time>` sigue marcando el texto como fecha para estilos y análisis, pero la
forma legible por máquina es lo que lo hace útil.

### Misión: Galería de Jefes

Crea `bosses.html` con:

1. Un `<nav>` arriba con al menos tres enlaces a `#guardian`, `#bruja-hielo` y `#dorado`.
2. Un `<main>` con un `<article>` por jefe, cada uno con un `<h2>` que lleve su `id` correspondiente.
3. Dentro de cada `<article>`, un `<figure>` con un `<img>` (con `alt`) y su `<figcaption>`.
4. Dentro del primer `<article>`, un `<p>` con un elemento `<time datetime="...">` para la fecha del último nerf.
5. Un enlace externo cuyo texto describa el destino: ni "haz clic aquí" ni una URL cruda.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Jefes — Emberfall</title>
  </head>
  <body>
    <nav>
      <ul>
        <li><a href="#guardian">El Guardián</a></li>
        <li><a href="#bruja-hielo">La Bruja de Hielo</a></li>
        <li><a href="#dorado">El Dorado</a></li>
      </ul>
    </nav>

    <main>
      <article>
        <h2 id="guardian">El Guardián</h2>
        <p>La tercera fase se teletransporta. Engáñalo con la segunda. Último nerf el <time datetime="2026-03-14">14 de marzo de 2026</time>.</p>
        <figure>
          <img src="https://placehold.co/300" alt="El Guardián sosteniendo un farol">
          <figcaption>Figura 1: El Guardián, a mitad de la fase tres.</figcaption>
        </figure>
      </article>

      <article>
        <h2 id="bruja-hielo">La Bruja de Hielo</h2>
        <figure>
          <img src="https://placehold.co/300" alt="La Bruja de Hielo rodeada de esquirlas">
          <figcaption>Figura 2: Congela, no te dejes congelar.</figcaption>
        </figure>
      </article>

      <article>
        <h2 id="dorado">El Dorado</h2>
        <figure>
          <img src="https://placehold.co/300" alt="El Dorado con armadura dorada">
          <figcaption>Figura 3: Cada pieza es un debuff.</figcaption>
        </figure>
        <a href="https://emberfall.example/wiki/el-dorado">La página completa del Dorado en la wiki</a>
      </article>
    </main>
  </body>
</html>
```

---

## 23. Sala de Escape

### Entidades y escapes

HTML tiene un conjunto de caracteres especiales llamados **entidades**, que sustituyen a
caracteres que no existen en texto plano o que HTML interpreta como marcado.

Para mostrar un carácter que **HTML usa en su sintaxis**, añade un ampersand `&`, un
identificador y un punto y coma. Estos son algunos:

| Carácter | Entidad | Se muestra |
| :--- | :--- | :--- |
| `&` | `&amp;` | `&` |
| `<` | `&lt;` | `<` |
| `>` | `&gt;` | `>` |
| `"` | `&quot;` | `"` |
| `'` | `&apos;` | `'` |

```html
<p>&lt;p&gt; es el elemento de párrafo, no una etiqueta.</p>
<p>Exploradora y Tanque hacen un buen equipo.</p>
```

Cuando un carácter como `é` o `¡` no necesita escape (los archivos HTML modernos son UTF-8
por defecto), puedes usar el carácter directamente:

```html
<p>Chispa lleva una llama. 🦙</p>
```

Existen otras entidades para caracteres sin tecla en el teclado — `&copy;` (©), `&nbsp;`
(espacio duro), `&hellip;` (…). La lista completa está en la referencia de MDN.

> [!WARNING]
> El error clásico: escribir `Arco & Flecha` en HTML puro, con el ampersand sin escapar.
> El navegador lee `& Flecha` como una entidad que no reconoce y se la come o la imprime
> literalmente — por eso esa parte del párrafo desaparece sin previo aviso. Lo mismo
> pasa con cualquier `<` que quieras mostrar como texto: escribe `&lt;` en su lugar.

> [!IMPORTANT]
> Dentro del valor de un atributo que contiene texto con comillas — `alt="la "gran" espada"` —
> las comillas internas cierran el atributo antes de tiempo y el resto se convierte en
> atributos basura. Usa `&quot;`, o cambia el atributo a comillas simples.

### Misión: Sala de Escape

Crea `escape_room.html` con cuatro párrafos:

1. Texto que contenga `<` y `>` usados como símbolos, no como etiquetas.
2. Texto que contenga un ampersand (`&`).
3. Un párrafo cuyo atributo `alt` (o `title`) contenga una palabra entre comillas.
4. Un párrafo con un espacio duro (`&nbsp;`) entre dos palabras, más una elipsis.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Sala de Escape</title>
  </head>
  <body>
    <p>Los cofres sueltan botín entre los niveles 3 y 5, nunca por debajo del 3.</p>
    <p>Arco &amp; Flecha hacen un buen equipo. Mago &amp; Curandera también.</p>
    <p><img src="https://placehold.co/100" alt="La &quot;gran&quot; espada"></p>
    <p>Trae&nbsp;un farol. Y espera&nbsp;que el Guardián siga dormido&nbsp;...</p>
  </body>
</html>
```

---

## 24. Salón de la Fama

### Punto de Control: Recapitulación

- `<header>` y `<footer>` son las regiones superior e inferior de una página — **no** `<head>` y `<body>`.
- `<main>` contiene el contenido central único; debería haber exactamente uno.
- `<article>` es contenido autónomo. `<section>` es contenido que necesita su página para tener sentido.
- `<aside>` es contenido relacionado tangencialmente: barras laterales, citas, glosarios.
- `<nav>` envuelve la navegación principal, no cualquier grupo de enlaces.
- `<figure>` empareja contenido con un `<figcaption>` opcional.
- El texto del enlace debe decir a dónde lleva.
- `<time datetime="...">` marca fechas y horas.
- Escapa `&`, `<`, `>`, `"` y `'` con entidades.

### Proyecto: Salón de la Fama

Tu última misión: una página **semánticamente correcta de arriba abajo**, con cada región
etiquetada por el elemento correcto.

Crea `hall_of_fame.html`:

1. `<header>` con un `<h1>` y un `<nav>` (lista de tres enlaces a `#primero`, `#segundo`, `#tercero`).
2. `<main>` con **tres** elementos `<article>`, cada uno con su `id`, y cada uno conteniendo:
   - un `<h2>`,
   - un `<figure>` con un `<img>` y un `<figcaption>`,
   - un `<p>` que mencione una fecha dentro de un `<time datetime>`,
   - un `<aside>` con información relacionada.
3. Una `<section>` después de los artículos, con un encabezado y una lista.
4. `<footer>` con un `<p>` de copyright.
5. Al menos una entidad escapada en el texto.

Después pasa la auditoría que viene a continuación.

> [!TIP]
> **La auditoría semántica**: la lista de comprobación que merece la pena memorizar:
> 1. ¿Exactamente un `<main>`?
> 2. ¿Cada `<section>` y cada `<article>` tiene un encabezado?
> 3. ¿Cada imagen está dentro de un `<figure>` o explicada por su `alt`?
> 4. ¿El texto de cada enlace dice a dónde lleva?
> 5. ¿El orden de encabezados es correcto — sin saltar de `<h2>` a `<h4>`?
> 6. ¿Hay algún `&` o `<` crudo en el texto que no sea marcado?
>
> Si una página pasa esas seis preguntas, está mejor construida que la mayoría de páginas de
> internet.

---

## 🧩 Chuleta de Elección de Elemento

| Si quieres… | Usa | No uses |
| :--- | :--- | :--- |
| La franja superior de la página o de una sección | `<header>` | `<div>` |
| El contenido central único | `<main>` | `<div id="contenido">` |
| Contenido autónomo (entrada, guía, ficha) | `<article>` | `<section>` |
| Contenido relacionado que necesita su página | `<section>` | `<div>` |
| Barra lateral, cita destacada, glosario | `<aside>` | `<div class="lateral">` |
| Enlaces de navegación principales | `<nav>` | `<div>` de `<a>` |
| Contenido con pie de figura | `<figure>` + `<figcaption>` | `<img>` suelto |
| Una fecha o una hora | `<time datetime>` | Texto suelto |

---

## XP Obtenida: Conclusiones clave

- 🧠 Los elementos semánticos no cuestan nada en tiempo de ejecución y pagan en **accesibilidad, SEO y mantenimiento**.
- 🎯 La pregunta de selección siempre es: *¿este contenido tiene sentido por sí solo?* → `<article>`. *¿Solo tiene sentido aquí?* → `<section>`.
- 🧭 `<header>` / `<main>` / `<footer>` describen las regiones de una página; `<nav>` y `<aside>` describen papeles.
- 🏷️ Cada elemento de landmark da a los lectores de pantalla un punto entre el que saltar — esa navegación es el objetivo.
- 🔗 El texto de un enlace es texto de interfaz: debe decir a dónde lleva.
- ⌨️ Escapa `&`, `<`, `>`, `"` y `'`, o el navegador leerá tu texto como marcado.

---

## Botín: Casos de uso reales

- 🏠 Páginas de bienvenida con cabecera, contenido y footer reales
- 📰 Sitios de noticias y blogs: un `<article>` por entrada, `<aside>` para enlaces relacionados
- 📚 Sitios de documentación: `<nav>` para la tabla de contenidos, `<section>` por capítulo
- 🛒 Páginas de producto: `<figure>` para las imágenes de la galería
- 🎮 Notas de parche, guías de jefes y páginas de códex: un `<article>` por entrada, `<time>` para la fecha del parche

---

## Misiones Secundarias: Ejercicios prácticos

1. Abre cualquier web que te guste y localiza su `<header>`, `<main>` y `<footer>`. Luego pregúntate: ¿habría algún `<aside>` más correcto?
2. Toma una página antigua llena de `<div>` y sustituye cada uno por el elemento semántico que lo describe de verdad. Fíjate en cuántos acaban siendo `<section>` y cuántos `<article>`.
3. Añade un `<nav>` con tabla de contenidos a un artículo, con enlaces `href="#..."` a encabezados que tengan `id`.
4. Convierte cada enlace "haz clic aquí" en uno que describa su destino.
5. Busca un `&` crudo en una web real y observa qué hace el navegador con él.
6. **Desafío final:** construye `lore_archive.html` — un `<header>` con `<nav>`, un `<main>` con cinco `<article>` de entradas de lore cada uno con un `<figure>` (imagen + pie), un `<time>` y un `<aside>`, una `<section>` "Cronología de Emberfall" y un `<footer>`. Después pasa a tu propia página la auditoría de seis preguntas y corrige todo lo que encuentre.

---

## Ver también

- [[00b - Chuleta de HTML]] — el catálogo de elementos, ahora con el set semántico incluido
- [[00c - Chuleta de HTML II]] — atributos, entidades y atributos de accesibilidad
- [[01 - Fundamentos de HTML]] — los elementos genéricos (`<p>`, `<a>`, `<img>`) sobre los que se construyen los semánticos
- [[02 - Estructura y Atributos]] — cuándo un `<div>` sí es la respuesta correcta
- [[03 - Formularios]] — los formularios también son landmarks: dales un `<section>`

---