# 03. Formularios

**Versión original en inglés:** [03 - Forms.md](03%20-%20Forms.md)

**Curso:** HTML
**Tema:** Formularios, tipos de `<input>`, correo y contraseña, validación (`minlength`, `maxlength`, `required`), campos numéricos
**Tags:** `#html` `#web-development` `#forms` `#inputs` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Lecciones-15_--_18_Parcial-7C5CFF?style=for-the-badge" alt="Lecciones 15 a 18">
  <img src="https://img.shields.io/badge/Estado-En_progreso-FFA500?style=for-the-badge" alt="En progreso">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #E34F26, #2DD4BF, #E34F26, transparent); margin: 24px 0;" />

Llegamos al capítulo en el que una página web deja de ser un documento y empieza a **preguntar algo al visitante**. Todos los formularios de registro, inicio de sesión, compra o creación de personaje que has usado alguna vez son un `<form>` con varios `<input>` dentro. La mejor noticia de este capítulo: el navegador hace gran parte de la validación **solo**, antes de ejecutar ni una línea de código.

> [!WARNING]
> **En progreso:** Esta nota cubre parcialmente las lecciones 15 a 18. La lección 18 (RSVP) aún
> está por completar — los campos `radio` y `checkbox` se mencionan, pero no están documentados
> en detalle todavía. El resto del capítulo se irá ampliando más adelante.

---

## 15. Google

### Formularios

¿Qué tienen en común las páginas de registro, inicio de sesión y compra? Todas **recogen datos del usuario**. Desde una barra de búsqueda hasta el inicio de sesión en una app, los formularios forman parte de nuestra vida digital diaria.

¿Cómo funciona un formulario?

1. El usuario introduce información.
2. Pulsa el botón "Enviar" ("Submit").
3. Esa información se envía a algún sitio para procesarse.

Para crear un formulario usamos el elemento `<form>`:

```html
<form action="" method="">
  <!-- Aquí irán los campos del formulario -->
</form>
```

Dos atributos importantes en `<form>`:

| Atributo | Propósito |
| :--- | :--- |
| `action` | Indica **a dónde** se envían los datos al pulsar Enviar |
| `method` | Indica **cómo** se envían los datos (normalmente `"post"` o `"get"`) |

> [!NOTE]
> En los ejemplos de este capítulo dejaremos `action` y `method` vacíos. El formulario se seguirá mostrando correctamente.

### Campos de entrada (`input`)

El elemento `<input>` es un **control interactivo** para introducir datos. Su atributo `type` determina qué tipo de campo es. Los dos más comunes:

```html
<form>
  <input type="text">
  <input type="submit">
</form>
```

- `"text"` crea una caja de texto sencilla.
- `"submit"` convierte ese `<input>` en un botón para enviar el formulario.

Por defecto, el botón de enviar dice "Submit" (Enviar). Podemos cambiar ese texto con el atributo `value`:

```html
<input type="submit" value="¡Enviar formulario!">
```

> [!NOTE]
> El elemento `<input>` es **autocerrado** (no lleva etiqueta de cierre).

> [!WARNING]
> Si `action` está vacío (`""`), el formulario no se envía a ningún sitio: la página se
> recarga y no ocurre nada visible. Mientras no tengamos un backend, ese comportamiento es
> correcto, no es un error.

### Ejercicio: Google

Vamos a recrear la barra de búsqueda original de Google en `google.html`. Partimos de este código:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Google</title>
  </head>
  <body>
    <!-- Aquí va el formulario -->
  </body>
</html>
```

Sustituye el comentario por un `<form>` (puedes dejar `action` y `method` vacíos) y añade dentro:

- Un párrafo `<p>` con el texto "¡Busca en la web con Google!"
- Un `<input type="text">` para la búsqueda.
- Uno o dos saltos de línea `<br>`.
- Un `<input type="submit" value="Buscar con Google">`.

```html
<form action="" method="">
  <p>¡Busca en la web con Google!</p>
  <input type="text">
  <br><br>
  <input type="submit" value="Buscar con Google">
</form>
```

> [!NOTE]
> Al enviar este formulario no pasa nada, porque aún no le hemos indicado a dónde enviar los datos.

---

## 16. Registro v1

### Tipos de `input`

¿Cómo nos aseguramos de que el usuario introduce el tipo de dato correcto? Por ejemplo, si pedimos un correo electrónico, ¿cómo comprobamos que contiene un `@`? HTML tiene varios **tipos de `input`** con validación integrada.

### Correo electrónico (`email`)

```html
<input type="email">
<input type="submit">
```

Este tipo comprueba que el valor introducido tenga aspecto de correo electrónico (que contenga `@`). Si falta, el navegador muestra un mensaje de error: "Por favor, incluye un `@` en la dirección de correo electrónico...".

### Contraseña (`password`)

```html
<input type="password">
<input type="submit">
```

El texto que escribes queda **oculto** y se muestra con puntos.

Hay muchos más tipos de `<input>` en HTML. Puedes consultar el resto en la documentación de MDN.

> [!IMPORTANT]
> Todos los campos `<input>` deben estar dentro de **un único** elemento `<form>`. Piensa en
> `<form>` como un sobre: recoge todos los datos y los envía juntos.

### Ejercicio: Registro v1

Crea `sign_up.html` con un formulario clásico de registro: un encabezado "Regístrate", campos para nombre de usuario, correo electrónico y contraseña, y un botón de enviar. Parte de este código:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Registro</title>
  </head>
  <body>
    <form>
      <h2>Regístrate</h2>

      Nombre de usuario:<br>
      <!-- Campo de texto -->
      <br><br>

      Correo electrónico:<br>
      <!-- Campo de correo -->
      <br><br>

      Contraseña:<br>
      <!-- Campo de contraseña -->
      <br><br>

      <!-- Botón de enviar -->
    </form>
  </body>
</html>
```

Sustituye los comentarios por los `<input>` correspondientes:

```html
<form>
  <h2>Regístrate</h2>

  Nombre de usuario:<br>
  <input type="text">
  <br><br>

  Correo electrónico:<br>
  <input type="email">
  <br><br>

  Contraseña:<br>
  <input type="password">
  <br><br>

  <input type="submit">
</form>
```

> [!TIP]
> `type="email"` y `type="password"` son la validación más barata que existe: un solo
> atributo y el navegador ya bloquea envíos incorrectos. Esto nos ahorra muchísimo trabajo.

---

## 17. Registro v2

### Longitud mínima y máxima (`minlength` y `maxlength`)

Podemos afinar la validación con estos atributos:

- `minlength`: número **mínimo** de caracteres obligatorios.
- `maxlength`: número **máximo** de caracteres permitidos.

```html
<input type="password" minlength="4" maxlength="10">
```

Con esto, el usuario no podrá escribir más de 10 caracteres, y si intenta enviar el formulario con menos de 4, el navegador le mostrará un error.

### Campo obligatorio (`required`)

Para que un campo sea obligatorio antes de enviar el formulario, usamos el atributo `required`:

```html
<form>
  Nombre: <input type="text" required>
  <br><br>
  Color favorito: <input type="text">
  <input type="submit">
</form>
```

En este ejemplo, "Nombre" es obligatorio. Si se deja vacío, el navegador impide el envío y resalta ese campo.

> [!WARNING]
> `maxlength` **no es validación de envío**: solo limita lo que puedes teclear. `minlength`
> sí bloquea el envío si no se alcanza. Usa ambos cuando quieras imponer un rango de
> caracteres.

### Ejercicio: Registro v2

Vuelve a editar `sign_up.html` y añade validación:

- Al **nombre de usuario**: `minlength="3"` y `maxlength="20"`.
- A la **contraseña**: `minlength="8"` y `maxlength="64"`.
- Haz que el nombre de usuario, el correo electrónico y la contraseña sean **obligatorios** (`required`).

¡Prueba a enviar el formulario con datos incorrectos para ver los mensajes del navegador!

```html
Nombre de usuario:<br>
<input type="text" minlength="3" maxlength="20" required>
<br><br>

Correo electrónico:<br>
<input type="email" required>
<br><br>

Contraseña:<br>
<input type="password" minlength="8" maxlength="64" required>
<br><br>

<input type="submit">
```

> [!TIP]
> **Versión para videojuegos**
> Esto es exactamente una pantalla de creación de personaje: `minlength="3"` para el nombre
> del jugador y `minlength="8"` para la contraseña. El navegador lo valida gratis, en cualquier
> idioma y sin código extra.

---

## 18. RSVP *(en progreso)*

### Campo numérico (`number`)

En muchos formularios necesitamos pedir números: edad, número de asistentes, cantidad de objetos, etc. Para eso usamos `type="number"`:

```html
<input type="number">
```

Al pasar el cursor por encima, aparecen dos flechitas (arriba y abajo) para aumentar o disminuir el valor.

Por defecto, esas flechas aumentan/disminuyen en **1**. Podemos cambiar ese paso con el atributo `step`:

```html
<input type="number" step="2">
```

También podemos establecer un valor mínimo y máximo con `min` y `max`:

```html
<input type="number" min="0" max="67">
```

Prueba a introducir `1000` en un campo con `max="67"`: el navegador marcará ese valor como inválido al intentar enviarlo.

> [!NOTE]
> `min` y `max` **no impiden escribir** un número mayor o menor con el teclado: solo lo marcan
> como inválido en el envío. Las flechas sí respetan esos límites.

### Vista previa del ejercicio: RSVP

El ejercicio `rsvp.html` pedirá: nombre, si vienes o no (botones de opción `radio`), restricciones alimentarias (casillas `checkbox`) y un botón de enviar. Ese contenido se ampliará en próximas versiones de esta nota.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Confirmación de asistencia</title>
  </head>
  <body>
    <form>
      <h2>RSVP</h2>
      <p>¡Ven a celebrar este día tan especial!</p>
      <br>
      Nombre: <!-- Campo de texto aquí -->
      <br><br>
      ¿Vas a venir?<br>
      <!-- 3 botones radio aquí -->
      <br><br>
      ¿Alguna restricción alimentaria?<br>
      <!-- Casillas checkbox aquí -->
      <br><br>
      <!-- Botón de enviar aquí -->
    </form>
  </body>
</html>
```

*(Este ejercicio se completará en una futura actualización de la nota.)*

---

## Vocabulario de formularios (resumen)

| Tipo | Código | Qué valida |
| :--- | :--- | :--- |
| Texto | `<input type="text">` | Nada por defecto |
| Correo | `<input type="email">` | Debe tener formato de correo válido |
| Contraseña | `<input type="password">` | Oculta el texto (úsalo con `minlength`) |
| Número | `<input type="number">` | Solo números, con `min`, `max` y `step` |
| Enviar | `<input type="submit" value="Enviar">` | Envía el formulario |

| Atributo de validación | Aplica a | Qué hace |
| :--- | :--- | :--- |
| `required` | Cualquier `<input>` | Hace el campo obligatorio |
| `minlength` | Campos de texto | Longitud mínima para poder enviar |
| `maxlength` | Campos de texto | Longitud máxima permitida al escribir |
| `min` / `max` | `<input type="number">` | Valor mínimo/máximo permitido |
| `step` | `<input type="number">` | Paso para las flechas |

---

## Conclusiones clave

- 📝 Un **formulario** recoge datos y los envía a algún sitio (`action`) de una forma determinada (`method`).
- 🔤 Los tipos básicos: `text`, `email`, `password`, `number` y `submit`.
- ✅ El navegador valida gratis: `email` comprueba el `@`, `minlength`/`maxlength` controlan la longitud, `required` impide campos vacíos, `min`/`max` limitan números.
- 📦 Todos los `<input>` deben estar dentro de un único `<form>`.

---

## Casos de uso habituales

- 🔍 Barras de búsqueda
- 👤 Formularios de registro e inicio de sesión
- 🎟️ RSVP y formularios de inscripción
- 🛒 Páginas de compra
- 🎮 Creación de personaje, invitaciones al equipo o selección de equipamiento

---

## Ejercicios prácticos

1. Crea una página de inicio de sesión con correo y contraseña, ambos obligatorios.
2. Haz un campo numérico para la edad que solo acepte valores entre 0 y 120.
3. Crea un formulario de contacto con nombre, correo y un botón de enviar personalizado.
4. Prueba a enviar cada formulario con datos inválidos y lee los mensajes del navegador.
5. **Desafío final:** crea `hoja_de_personaje.html` — un campo de texto para el nombre (`minlength="2"`, `maxlength="16"`), un campo de correo, un campo numérico para el nivel (`min="1"`, `max="99"`), un campo de contraseña (`minlength="8"`) y un botón que diga "Crear personaje".

---

## Ver también

- [[00c - Chuleta de HTML II]] — tabla de referencia con campos y restricciones
- [[02 - Estructura y Atributos]] — `class` e `id` para organizar y dar estilo a formularios
- [[01 - Fundamentos de HTML]] — los elementos con los que construimos un formulario

---