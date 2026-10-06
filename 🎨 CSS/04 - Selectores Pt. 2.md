# 04. Selectores Pt. 2

**Versión original en inglés:** [04 - Selectors Pt. 2.md](04%20-%20Selectors%20Pt.%202.md)

**Curso:** CSS
**Tema:** Selectores agrupados, combinador de hijo, ejercicios de práctica y el volante final Cinderlight Fest
**Tags:** `#css` `#web-development` `#selectors` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE_A_INTERMEDIO-6CC24A?style=for-the-badge" alt="De principiante a intermedio">
  <img src="https://img.shields.io/badge/Lecciones-17_--_20-7C5CFF?style=for-the-badge" alt="Lecciones 17 a 20">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Dos formas de apuntar más inteligentemente: el **grouping** escribe una regla para varios
destinos en vez de copiarla tres veces, y el **combinador de hijo** alcanza el interior de
un padre sin arrastrar a todos los descendientes. El capítulo termina con un proyecto
completo — un volante de festival construido con HTML semántico y solo los selectores que
ya dominas. Referencia: [[00b - Chuleta de CSS]].

> [!NOTE]
> **Todo el capítulo en una frase**
> El grouping ahorra teclas; los combinadores ahorran precisión — juntos mantienen una
> hoja de estilo corta para leerla y afilada en la que confiar.

---

## 17. Grouping

El **grouping** aplica las mismas reglas de estilo a **varios selectores a la vez**,
evitando duplicar código. Los selectores se separan con comas.

```css
ul, ol {
  border: 1px solid;
  width: 200px;
}
```

Una regla, ambas listas enmarcadas. Sin grouping escribirías las mismas dos declaraciones
dos veces — y luego las recordarías *otra vez* el día que cambies el color del borde.

```css
/* Tres copias de la misma regla — no lo hagas */
ul { border: 1px solid; }
ol { border: 1px solid; }
li { border: 1px solid; }
```

---

## 18. Combinador de Hijo

El **combinador de hijo** `>` selecciona los **hijos directos** dentro de un elemento
padre, dando especificidad precisa sin excesos.

```css
ul > li {
  text-decoration: underline wavy 3px brown;
}
```

`ul > li` coincide con un `<li>` cuyo padre inmediato es un `<ul>` — y se salta el `<li>`
anidado tres `<div>` más abajo, al que una regla descendente simple también habría atrapado.

| Patrón | Coincide con |
| :--- | :--- |
| `ul li` | Cada `li` *en cualquier lugar* dentro del `ul` (descendiente) |
| `ul > li` | Solo los `li` hijos directos del `ul` (hijo directo) |

> [!TIP]
> La diferencia importa en cuanto anidas listas, tarjetas o acordeones: las reglas
> descendentes se filtran por cada capa, las de hijo se detienen en la primera. Recurre a
> `>` cuando los elementos más profundos deban conservar su propio estilo.

---

## 19. Misión: Reinos y Mares

Todo lo visto hasta ahora, en un solo documento: grouping para los marcos comunes, reglas
separadas para la paleta, combinadores de hijo para las decoraciones.

### HTML (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Reinos y Mares</title>
</head>
<body>
  <h2>Reinos de Emberfall 🏰</h2>
  <ul>
    <li>Ciénaga de Ceniza</li>
    <li>Yermos de Brasa</li>
    <li>Salas Profundas</li>
    <li>Pantano del Ocaso</li>
    <li>Alcance Norte</li>
    <li>Alta Fragua</li>
    <li>Vega de Piedranegra</li>
  </ul>

  <h2>Mazmorras por Profundidad ⛏️</h2>
  <ol>
    <li>La Aguja Agrietada</li>
    <li>Archivo Inundado</li>
    <li>Madrigueras de la Linterna</li>
    <li>El Horno Hundido</li>
    <li>Noveno Piso</li>
  </ol>
</body>
</html>
```

### CSS (`styles.css`)

```css
/* 1. Grouping: un marco para ambas listas */
ul, ol {
  border: 1px solid;
  width: 200px;
}

/* 2. Paleta específica por lista */
ul {
  background-color: lightgreen;
}

ol {
  background-color: skyblue;
  color: white;
}

/* 3. Combinadores de hijo para los elementos */
ul > li {
  text-decoration: underline wavy 3px brown;
}

ol > li {
  text-decoration: underline dotted 3px indigo;
}
```

Cuatro técnicas de selector — tipo, id, grouping y `>` — en veinte líneas. Ese es todo el
vocabulario para el proyecto de abajo.

---

## 20. Volante de Festival

### Checkpoint: Resumen de Selectores

- Los selectores de **tipo** establecen los valores predeterminados de la página.
- **Clase** (`.name`) estiliza cualquier cantidad de elementos; **ID** (`#name`) estiliza uno.
- **Targeting** (`div.line`) los encadena para ganar especificidad.
- **Grouping** (`h1, h2`) comparte una regla entre selectores.
- **Combinador de hijo** (`ul > li`) se detiene en los hijos directos.

### Proyecto: Cinderlight Fest

Un volante de una página para el lanzamiento de la banda sonora de Emberfall — HTML
semántico (`main`, `header`, `section`, `footer`) pintado solo con los selectores anteriores.

#### HTML (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="styles.css" rel="stylesheet" />
  <title>Cinderlight Fest</title>
</head>
<body>
  <main>
    <header>
      <img src="https://placehold.co/600x200/1b1b2f/ff6b35?text=Cinderlight+Fest" alt="Banner del festival con el perfil de Emberfall" />
      <h1>Cinderlight Fest</h1>
    </header>

    <section id="night-1">
      <h2>The Ashen Choir</h2>
      <h3>Acto uno · Acto dos</h3>
      <p>
        <b>
          La noche de apertura es para el coro que compuso las Salas Profundas. Dos actos:
          primero los temas tranquilos de la linterna, y después la suite completa del
          Noveno Piso con percusión en vivo y un coro que jamás ha fallado una entrada.
        </b>
      </p>
    </section>

    <section id="night-2">
      <h2>Lil' Spark</h2>
      <h3>Acto uno · Acto dos</h3>
      <p>
        <b>
          El cierre chiptune. El acto uno remezcla los temas del mundo exterior que todos
          sabemos tararear; el acto dos estrena las pistas de la nueva expansión por
          primera vez, con los devs en primera fila tomando notas.
        </b>
      </p>
    </section>

    <footer>
      <p>Instalaciones artísticas de</p>
      <p><b>El Colectivo del Horno · Marrow &amp; Co · Studio Nightglass</b></p>
    </footer>
  </main>
</body>
</html>
```

#### CSS (`styles.css`)

```css
main {
  text-align: center;
  font-family: sans-serif;
}

header img {
  width: 100%;
  max-width: 600px;
}

/* Grouping: ambas noches comparten el mismo marco */
#night-1, #night-2 {
  margin: 20px 0;
  padding: 10px;
  border: 1px solid #1572B6;
  border-radius: 5px;
}

footer {
  margin-top: 30px;
  font-size: 0.9em;
}
```

> [!TIP]
> **Versión para game devs**
> Este volante es la plantilla de cada página de anuncio que publica un juego: fecha de
> lanzamiento, dos actos de noticias, créditos en el pie. Cambia `#night-1` por versiones
> de parche o jornadas de torneo y el marcado no cambia — solo los ids. Sigue
> [[05 - Pseudoelementos]]: decoración que no necesita ni una línea de HTML extra.

---

## XP Earned: Lo que te llevas

- 📎 **Grouping** = selectores separados por comas, una regla compartida.
- 🎯 **Combinador `>`** = solo hijos directos; un espacio simple coincide con descendientes.
- 🧩 Tipo + clase + id + grouping + `>` cubren la mayoría de los selectores reales.
- 🗞️ Una página final no necesita framework: HTML semántico y cinco tipos de selector.

---

## Loot Table: Casos de Uso Reales

- 📋 Marcos compartidos de tablas, listas y tarjetas en toda una página
- 🧭 Estilos de navegación que alcanzan los enlaces pero no los desplegables anidados
- 🎪 Volantes de eventos, festivales y notas de parche
- 🏷️ Una regla para cada `.btn`, una anulación para `#submit`

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Reescribe tres reglas idénticas como una sola regla agrupada.
2. Estiliza solo los `<a>` que son *hijos directos* de un `<nav>` — luego hazlos
   descendientes y observa cómo cambian los desplegables.
3. Dale el mismo marco a dos secciones con un selector de id agrupado.
4. Crea un volante `tournament.html` con un horario `#day-1, #day-2` agrupado.
5. **Pelea de jefe:** reconstruye el volante del festival con tu propio evento, usando
   cada familia de selectores de los capítulos 03 y 04 al menos una vez.

---

## 🔗 Ver También

- [[03 - Selectores Pt. 1]] — tipo, clase, id y targeting
- [[05 - Pseudoelementos]] — estilizar partes de un elemento sin marcado extra
- [[06 - Pseudoclases]] — estilizar elementos por estado
- [[11 - Display y Posicionamiento]] — dónde acaban en la página estos elementos seleccionados

---
