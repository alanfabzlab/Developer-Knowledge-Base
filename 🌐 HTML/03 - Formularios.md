# 03. Formularios

**Versión original en inglés:** [03 - Forms.md](03%20-%20Forms.md)

**Curso:** HTML
**Tema:** Formularios, tipos de `<input>`, email y contraseña, validación (`minlength`, `maxlength`, `required`), campos numéricos, radio y checkbox
**Tags:** `#html` `#web-development` `#formularios` `#inputs` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Lecciones-15_--_18-7C5CFF?style=for-the-badge" alt="Lecciones 15 a 18">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=FF6B35&height=70&section=header" width="100%" alt="Ola de brasa" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #E34F26, #2DD4BF, #E34F26, transparent); margin: 24px 0;" />

El capítulo donde una página web deja de ser un documento y empieza a **preguntarle algo al
jugador**. Cada pantalla de registro, login, creación de personaje o editor de equipamiento
que has usado es un `<form>` con `<input>`s dentro. La mejor noticia de este capítulo: el
navegador valida casi todo gratis, antes incluso de que se ejecute una sola línea de tu código.

> [!NOTE]
> **Por qué a los estudios les encantan los formularios nativos**
> Una ficha de personaje, una invitación al grupo, un editor de loadout, un formulario para
> subir mods: todos son el mismo problema — recoger datos escritos, comprobar que tienen
> sentido y enviarlos a algún sitio. HTML lleva esta maquinaria desde 1995, y la capa de UI de
> tu motor de juegos es casi siempre un envoltorio alrededor de esto.

---

## 15. Portal de Búsqueda

### Formularios

¿Qué tienen en común las páginas de registro, login y creación de personaje? Todos **recogen datos del usuario**. Desde una barra de búsqueda hasta iniciar sesión en tu juego favorito, los formularios son parte de la vida digital cotidiana.

Así funciona un formulario:

1. El usuario escribe cierta información.
2. El usuario pulsa un botón de "Enviar".
3. La información se envía a algún sitio y se procesa.

Para crear un formulario, usamos el elemento `<form>`:

```html
<form action="" method="">
  <!-- Aquí irá más código -->
</form>
```

Se usan dos atributos con `<form>`:

| Atributo | Función |
| :--- | :--- |
| `action` | Especifica **dónde** se envían los datos al enviar el formulario |
| `method` | Especifica **cómo** se procesan los datos (normalmente `"post"` o `"get"`) |

> [!NOTE]
> En el resto del capítulo, `action` y `method` no aparecerán en los ejemplos. Los formularios se siguen viendo bien.

### Los campos `<input>`

El elemento `<input>` es un **control interactivo** para introducir datos. Su atributo `type` determina qué tipo de campo es. Los dos más usados:

```html
<form>
  <input type="text">
  <input type="submit">
</form>
```

- `"text"` crea una caja de texto normal.
- `"submit"` convierte el `<input>` en un botón para enviar los datos.

Por defecto, el botón dice "Submit". Cambia su texto con el atributo `value`:

```html
<input type="submit" value="¡Entrar en la Forja!">
```

> [!NOTE]
> El elemento `<input>` usa una etiqueta **auto-cerrada**.

> [!WARNING]
> `action=""` con valor vacío significa "enviar a ninguna parte". La página se recarga y no
> ocurre nada — que es exactamente lo que parece "mi formulario está roto". Hasta que exista
> un backend, ese es el comportamiento correcto, no un error.

### Misión: Portal de Búsqueda

Recrea la barra de búsqueda original de Google en `google.html`. Parte de este código:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Búsqueda en la wiki de Emberfall</title>
  </head>
  <body>
    <!-- Aquí va el código del formulario -->
  </body>
</html>
```

Sustituye el comentario por un elemento `<form>` (pon `action` y `method` a `""` o quítalos) y añade dentro:

- Un `<p>` con "¡Busca en la wiki de Emberfall!"
- Un `<input>` con el `type` puesto a `"text"`.
- Uno o dos saltos de línea `<br>`.
- Otro `<input>` con `type="submit"` (el texto debe decir "Buscar en la wiki").

```html
<form action="" method="">
  <p>¡Busca en la wiki de Emberfall!</p>
  <input type="text">
  <br><br>
  <input type="submit" value="Buscar en la wiki">
</form>
```

> [!NOTE]
> Si enviamos este formulario, no ocurre nada, porque no le hemos dicho adónde enviar los datos.

---

## 16. Creación de Personaje I

### Tipos de `input`

¿Cómo nos aseguramos de que los datos correctos lleguen a un formulario? Si un formulario pide
un email, ¿cómo sabe si es un email *válido* que contiene una `@`? Los formularios de HTML
tienen varios **tipos de campo integrados**. Dos de ellos:

### Email

```html
<input type="email">
<input type="submit">
```

Comprueba si el valor enviado es una dirección de email válida. Si falta la `@`, el navegador
muestra un error ("Por favor, incluye una '@' en la dirección de correo electrónico...").

### Contraseña

```html
<input type="password">
<input type="submit">
```

El texto escrito queda **oculto** y se muestra como puntos.

Existen muchos más tipos de `<input>` en los formularios de HTML (consulta la lista completa
en la documentación de MDN).

> [!IMPORTANT]
> Todos los elementos `<input>` deben colocarse dentro de un **único** elemento `<form>`.
> Piensa en `<form>` como un **sobre** que contiene todos los datos que queremos enviar al
> servidor.

### Misión: Creación de Personaje I

Crea `sign_up.html` con una página de registro clásica: un encabezado "Sign Up", campos de
Usuario, Email y Contraseña, y un botón de enviar. Parte de:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Sign Up</title>
  </head>
  <body>
    <form>
      <h2>Sign Up</h2>

      Usuario:<br>
      <!-- Campo de texto -->
      <br><br>

      Email:<br>
      <!-- Campo de email -->
      <br><br>

      Contraseña:<br>
      <!-- Campo de contraseña -->
      <br><br>

      <!-- Botón de enviar -->
    </form>
  </body>
</html>
```

Sustituye los comentarios por elementos `<input>` (uno de texto, uno de email, uno de
contraseña y un botón de enviar):

```html
<form>
  <h2>Sign Up</h2>

  Usuario:<br>
  <input type="text">
  <br><br>

  Email:<br>
  <input type="email">
  <br><br>

  Contraseña:<br>
  <input type="password">
  <br><br>

  <input type="submit">
</form>
```

> [!TIP]
> `type="email"` y `type="password"` son la validación más barata del desarrollo web: un
> atributo cada uno y el navegador bloquea el envío por su cuenta. `type="number"` hará lo
> mismo con los dígitos en la lección 18.

---

## 17. Creación de Personaje II

### Minlength y Maxlength

Además de los tipos de campo, podemos **validar** con estos atributos:

- `minlength`: fija el número **mínimo** de caracteres.
- `maxlength`: fija el número **máximo** de caracteres.

```html
<input type="password" minlength="4" maxlength="10">
```

El usuario no puede escribir más de 10 caracteres, y aparece un error si intenta enviar menos
de 4.

### Datos obligatorios

Algunos formularios exigen datos antes de poder enviarse. El atributo `required` lo impone:

```html
<form>
  Nombre del héroe: <input type="text" required>
  <br><br>
  Elemento favorito: <input type="text">
  <input type="submit">
</form>
```

El `<input>` de "Nombre del héroe" está marcado como obligatorio. Si se deja vacío, el
navegador bloquea el envío y señala el campo vacío.

> [!WARNING]
> `maxlength` **no es validación**. Detiene la pulsación de teclas; no dice nada sobre si el
> valor tiene sentido. `minlength` es el atributo que bloquea el envío. Usa ambos cuando
> quieras el tope de teclas *y* la regla aplicada.

### Misión: Creación de Personaje II

Vuelve a `sign_up.html` y añade validación:

- Da al campo **usuario** un `minlength` de 3 y un `maxlength` de 20.
- Da a **contraseña** un `minlength` de 8 y un `maxlength` de 64.
- Marca usuario, email y contraseña como **obligatorios**.

¡Después intenta enviar el formulario con datos incorrectos!

```html
Usuario:<br>
<input type="text" minlength="3" maxlength="20" required>
<br><br>

Email:<br>
<input type="email" required>
<br><br>

Contraseña:<br>
<input type="password" minlength="8" maxlength="64" required>
<br><br>

<input type="submit">
```

> [!TIP]
> **Versión para videojuegos**
> Esta es la pantalla de creación de personaje. Un `minlength="3"` en el nombre del jugador
> y un `minlength="8"` en la contraseña son las mismas dos líneas que un cliente validaría
> antes de abrir un socket... salvo que el navegador las hace gratis, en todos los idiomas y
> sin dependencias.

---

## 18. Confirmación de Raid

### Campo numérico (`number`)

En muchos formularios necesitamos pedir números: el nivel de un personaje, la cantidad de
botiquines que compras en una tienda, etc. Para eso usamos `type="number"`:

```html
<input type="number">
```

Al pasar el cursor por encima, aparecen dos flechitas (arriba y abajo) para aumentar o disminuir el valor.

Por defecto, esas flechas aumentan o disminuyen en **1**. Podemos cambiar ese paso con el atributo `step`:

```html
<input type="number" step="2">
```

También podemos establecer un valor mínimo y máximo con `min` y `max`:

```html
<input type="number" min="0" max="67">
```

Prueba a introducir `1000` en un campo con `max="67"` y mira qué pasa: el navegador lo marca
como inválido.

> [!NOTE]
> `min` y `max` **no impiden escribir** un número mayor o menor con el teclado: solo lo marcan
> como inválido en el envío. Las flechas sí respetan esos límites.

### Campo de opción (`radio`)

Los campos `radio` permiten elegir **una** opción de una lista. Es lo que se llama "elegir una de varias".

```html
<form>
  <p>¿Vienes a la incursión?</p>

  <label for="si">Sí 🗡️</label>
  <input type="radio" id="si" name="asistencia" value="si">

  <label for="no">No 😴</label>
  <input type="radio" id="no" name="asistencia" value="no">

  <input type="submit">
</form>
```

Dos cosas hacen que los radios funcionen como grupo:

- El **mismo valor de `name`** (`asistencia`): es lo que los une como una elección exclusiva.
- Un **`id` diferente** para cada uno: es lo que apunta la `<label>`.

Al pulsar una `<label>` se activa el campo al que apunta, y por eso cada radio necesita su `for`.

> [!IMPORTANT]
> Los radios con el mismo `name` pero sin `<label>` son inútiles con el ratón: solo puedes
> acertar a un punto de 13 píxeles. En los radios y checkboxes las etiquetas no son
> decoración, son el área de clic.

### Casilla de verificación (`checkbox`)

Los checkboxes permiten elegir **una, varias o ninguna** opción. Es lo que se llama "elegir varias de varias".

```html
<form>
  <p>¿Qué objetos llevas a la incursión?</p>

  <input type="checkbox" id="pocion" name="objetos" value="pocion">
  <label for="pocion">Poción de vida 🧪</label>

  <input type="checkbox" id="cuerda" name="objetos" value="cuerda">
  <label for="cuerda">Cuerda 🪢</label>

  <input type="checkbox" id="antorcha" name="objetos" value="antorcha">
  <label for="antorcha">Antorcha 🔦</label>

  <input type="submit">
</form>
```

Los checkboxes comparten `name="objetos"` para pertenecer al mismo grupo, pero a diferencia de
los radios son **independientes**: puedes marcar los tres.

> [!TIP]
> La regla práctica: los radios son **excluyentes entre sí**, los checkboxes se **acumulan**.
> Si elegir una opción debería desmarcar las demás, es un radio. Si las opciones se suman, es
> un checkbox.

### Misión: Confirmación de Raid

Crea `rsvp.html`: la inscripción del grupo para la próxima partida de Emberfall. Parte de:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>RSVP</title>
  </head>
  <body>
    <form>
      <h2>RSVP</h2>
      <p>¡Únete a la incursión y graba tu nombre en el salón de la fama de Emberfall ...</p>
      <br>
      Nombre: <!-- Campo de texto aquí -->
      <br><br>
      ¿Vas a venir?<br>
      <!-- 3 campos radio aquí, compartiendo el mismo name -->
      <br><br>
      Algo que quieras traer para la partida ...<br>
      <!-- 3 o 5 casillas checkbox aquí -->
      <br><br>
      <!-- Botón de enviar aquí -->
    </form>
  </body>
</html>
```

Añade:

1. Un **campo de texto** para el nombre.
2. **Tres campos `radio`** para "¿Vas a venir?": `"si"`, `"quiza"` y `"necesito una build primero"`, todos con `name="asistencia"`.
3. **Tres o cinco casillas `checkbox`** para los objetos que lleva tu grupo, todas con `name="objetos"`.
4. Dale a cada campo una `<label>` con su `for` correspondiente, y añade un **botón de enviar**.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>RSVP</title>
  </head>
  <body>
    <form>
      <h2>RSVP</h2>
      <p>¡Únete a la incursión y graba tu nombre en el salón de la fama de Emberfall ...</p>
      <br>
      Nombre: <input type="text" id="nombre-jugador" required>
      <br><br>
      ¿Vas a venir?<br>
      <input type="radio" id="asistencia-si" name="asistencia" value="si">
      <label for="asistencia-si">Definitivamente ⚔️</label>
      <input type="radio" id="asistencia-quiza" name="asistencia" value="quiza">
      <label for="asistencia-quiza">A ver 😐</label>
      <input type="radio" id="asistencia-no" name="asistencia" value="no">
      <label for="asistencia-no">Necesito una build primero 📖</label>
      <br><br>
      Algo que quieras traer para la partida ...<br>
      <input type="checkbox" id="objeto-pocion" name="objetos" value="pocion">
      <label for="objeto-pocion">Poción de vida 🧪</label>
      <input type="checkbox" id="objeto-cuerda" name="objetos" value="cuerda">
      <label for="objeto-cuerda">Cuerda 🪢</label>
      <input type="checkbox" id="objeto-antorcha" name="objetos" value="antorcha">
      <label for="objeto-antorcha">Antorcha 🔦</label>
      <input type="checkbox" id="objeto-mapa" name="objetos" value="mapa">
      <label for="objeto-mapa">Mapa de la mazmorra 🗺️</label>
      <input type="checkbox" id="objeto-campana" name="objetos" value="campana">
      <label for="objeto-campana">Campana de aviso 🔔</label>
      <br><br>
      <input type="submit" value="¡Apúntame!">
    </form>
  </body>
</html>
```

> [!TIP]
> **Versión para videojuegos**
> `name="asistencia"` es la clave y `value` es lo que se guarda asociado a ella. Al enviar
> este formulario, el navegador lo serializa en texto plano — `asistencia=quiza&objetos=cuerda&objetos=antorcha`.
> Ese formato clave/valor es el antepasado de cada archivo de guardado, archivo de
> configuración y petición de red que tu motor haya escrito.

---

## 🧩 El Vocabulario de los Formularios

| Campo | Código | Valida |
| :--- | :--- | :--- |
| Texto | `<input type="text">` | Nada por sí solo |
| Email | `<input type="email">` | Debe parecer una dirección válida |
| Contraseña | `<input type="password">` | Oculta el texto; combínalo con `minlength` |
| Número | `<input type="number">` | Dígitos, con `min` / `max` / `step` |
| Radio | `<input type="radio" name="x" id="y">` | Elección exclusiva dentro del grupo |
| Checkbox | `<input type="checkbox" name="x" id="y">` | Interruptor independiente |
| Enviar | `<input type="submit" value="Enviar">` | — |

| Restricción | Se aplica a | Qué hace |
| :--- | :--- | :--- |
| `required` | Cualquier `<input>` | Bloquea el envío si está vacío |
| `minlength` | Campos de texto | Caracteres mínimos antes de poder enviar |
| `maxlength` | Campos de texto | Tope de caracteres que se pueden escribir |
| `min` / `max` | `<input type="number">` | Valor mínimo y máximo aceptado |
| `step` | `<input type="number">` | Incremento de las flechas y salto obligatorio del valor |
| `name` | Radio, checkbox | Agrupa campos en un mismo conjunto enviado |
| `for` | `<label>` | Apunta la etiqueta al campo que describe |

---

## XP Obtenida: Conclusiones clave

- 📝 Un **formulario** recoge datos y los envía a algún sitio (`action`) de cierta manera (`method`).
- 🔤 `<input type="text">`, `"email"`, `"password"`, `"number"`, `"radio"`, `"checkbox"` y `"submit"` cubren lo básico.
- ✅ El navegador valida gratis: `email` comprueba la `@`, `minlength`/`maxlength` la longitud, `required` bloquea campos vacíos, `min`/`max` limitan los números.
- 🎯 Los radios comparten `name` para volverse excluyentes; los checkboxes comparten `name` pero siguen siendo independientes.
- 🏷️ Cada radio y cada checkbox necesita una `<label>` cuyo `for` coincida con el `id` del campo.
- 📦 Mantén todos los `<input>` dentro de un mismo `<form>`.

---

## Botín: Casos de uso reales

- 🔍 Barras de búsqueda
- 👤 Páginas de registro y login
- 🎟️ Formularios de inscripción y confirmación (RSVP)
- 🛒 Páginas de pago
- 🎮 Creación de personajes, invitaciones de grupo y editores de equipamiento: todo formulario es una mini ficha de personaje

---

## Misiones Secundarias: Ejercicios prácticos

1. Construye una página de login con email y contraseña, ambos obligatorios.
2. Haz un campo numérico para la edad que solo acepte valores del 0 al 120.
3. Crea un formulario de contacto con nombre, email y un texto personalizado para el botón.
4. Añade un grupo de radios "dificultad" (Historia / Normal / Pesadilla) y comprueba que solo se puede elegir uno.
5. Intenta enviar cada formulario con datos inválidos y lee los mensajes del navegador.
6. **Desafío final:** construye `character_sheet.html` — un campo de texto para el nombre (`minlength="2"`, `maxlength="16"`), un campo de email para la cuenta, un campo numérico para el nivel (`min="1"`, `max="99"`), un grupo de radios para la clase (Exploradora / Tanque / Mago), un campo de contraseña (`minlength="8"`) y un botón que diga "Crear personaje".

---

## Ver también

- [[00c - Chuleta de HTML II]] — tabla de referencia de campos y restricciones
- [[02 - Estructura y Atributos]] — `class` e `id` para agrupar y dar estilo a un formulario
- [[01 - Fundamentos de HTML]] — los elementos con los que se construye un formulario
- [[04 - HTML Semántico]] — por qué un formulario va dentro de un `<section>` y por qué las etiquetas importan

---