
# 02. Ingeniería de Prompts

**Versión original en inglés:** [02 - Prompt Engineering.md](02%20-%20Prompt%20Engineering.md)

**Curso:** GenAI
**Tema:** Prompts, especificidad, roles, prompting few-shot y chain-of-thought
**Tags:** `#genai` `#ai` `#llm` `#prompting` `#game-dev`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Un prompt no es una búsqueda. Es **toda** la entrada que recibe el modelo y —como quedó demostrado en [[01 - Cómo Piensa la IA]]— toda la salida es función de ella. Este capítulo convierte ese hecho en una herramienta: cuatro técnicas, aplicadas en orden, que pasan de una instrucción de una línea a un asistente reutilizable para un estudio de juegos.

---

## 7. El prompt lo es todo

> [!NOTE]
> Información clave
> Un **prompt** es el texto que enviamos a un modelo de IA. Es el único mando que tenemos. El modelo no sabe qué queremos hasta que se lo decimos.

Si un LLM es, en el fondo, un motor de predicción, ¿por qué preguntas parecidas dan respuestas tan distintas? Porque dos prompts distintos llevan a dos predicciones distintas.

| Prompt | Resultado |
| :--- | :--- |
| Explica los Flamin' Hot Cheetos | Un ensayo de 600 palabras con explicaciones largas y genéricas |
| Explica los Flamin' Hot Cheetos a un cocinero del siglo XVI. Máximo 100 palabras. | Corto, preciso, al grano |

Mismo modelo, misma pregunta de fondo, salida completamente distinta.

**Objetivo del capítulo:** aprender a escribir prompts que produzcan los resultados que queremos, construyendo un **Compañero de Estudio de Game Dev** que va desde una instrucción de una línea hasta una herramienta pulida y reutilizable que funciona con cualquier LLM.

---

## 8. Especificidad

Un prompt vago recibe una respuesta promedio. Sin instrucciones sobre longitud, formato o tono, el modelo promedia entre todas las personas que alguna vez hicieron una pregunta parecida en internet — y el resultado es un engrudo.

Es como entrar en la tienda de al lado y decir "dame un arma". Sin más detalle sales con una espada oxidada. Pide una **espada ropera para una build de pirata, a una mano, de nivel 30** y sales con lo correcto.

### Qué aporta un prompt específico

| Elemento | Ejemplo | Efecto |
| :--- | :--- | :--- |
| 👥 **Audiencia** | "para un programador que sabe Python básico" | No presupone conocimiento previo |
| 🎭 **Tono** | "con la voz de un dungeon master curtido" | Más carácter, más cercanía |
| 🧱 **Formato** | "Incluye una analogía y un ejemplo de código" | Estructura predecible |
| 📏 **Longitud** | "Máximo 100 palabras" | Se acaban los ensayos de 600 |

### Construyendo el Compañero de Estudio (v1)

Los prompts reutilizables usan un marcador como `{concept}`:

```text
Explica {concept} en español sencillo para alguien que sabe Python básico.
Usa una analogía y un ejemplo de código.
Máximo 100 palabras.
```

Compara el prompt malo (`Explica el patrón Estado`) con el específico (`Explica el patrón Estado en español sencillo para alguien que sabe Python básico...`) y nota cuánto más útil es la segunda respuesta.

---

## 9. Dale un rol

Cuando le hacemos una pregunta a una IA sin darle un rol, no elegimos ninguno: cae en una voz genérica de asistente que va a por el promedio. Darle un rol cambia esa voz por completo. Un rol le dice a la IA **quién debe ser** al responder.

| Prompt | Lo que obtienes |
| :--- | :--- |
| ¿Cómo me preparo para una game jam? | La persona promedio, con matices |
| Eres un desarrollador de juegos senior que ha publicado tres títulos comerciales y mentoriza a un estudio. ¿Cómo me preparo para una game jam? | Prioridades, plazos y errores de alguien que organiza esas maratonas |

La segunda respuesta usa el lenguaje, las prioridades y la experiencia de un profesional que lo ha hecho de verdad.

### Roles habituales

| Rol | Voz que obtienes |
| :--- | :--- |
| 👩‍🏫 **Profesor** | Didáctica y paso a paso |
| 📰 **Periodista** | Factual y concisa |
| 👶 **Niño de 5 años** | Lenguaje simple y ejemplos de juguete |
| 🎮 **Desarrollador de juegos senior** | Trade-offs, realidad del motor, experiencia real |

> [!NOTE]
> Los roles no le dan a la IA conocimiento nuevo. Le dan contexto sobre **cómo presentar** la información.

### Compañero de Estudio (v2)

```text
Eres un desarrollador de juegos senior y arquitecto de software.
Explicas código a programadores que ya trabajan, y nunca usas jerga
sin definirla antes.

Explica {concept} en español sencillo para alguien que sabe Python básico.
Usa una analogía y un ejemplo de código.
Máximo 100 palabras.
```

Prueba otros roles —"Eres un dungeon master curtido que ha dirigido cien campañas"— y observa cómo cambia la entrega, y después recupera la versión de arriba.

---

## 10. Enséñale, no le digas

Decirle al modelo que "use un cierto estilo" es lotería. **Mostrarle** ejemplos es mucho más fiable: después de verlos, el modelo reproduce el formato casi exactamente.

| Técnica | Ejemplos dados |
| :--- | :--- |
| **Zero-shot** | 0 — solo la instrucción |
| **One-shot** | 1 |
| **Few-shot** | unos cuantos |
| **Many-shot** | muchos |

### Añadiendo ejemplos

```text
Eres un desarrollador de juegos senior y arquitecto de software.
Explicas código a programadores que ya trabajan, y nunca usas jerga
sin definirla antes.

Aquí tienes dos ejemplos de cómo quiero que se expliquen los conceptos:

CONCEPTO: object pooling (agrupación de objetos)
ANALOGÍA: Un cubo de flechas. En vez de forjar una flecha nueva en cada
disparo, disparas las que ya tienes y las recoges al impactar.
CÓDIGO:
pool = []
def acquire():
    return pool.pop() if pool else Bullet()
def release(bullet):
    pool.append(bullet)

CONCEPTO: el patrón Estado
ANALOGÍA: Una barra de vida que solo admite uno de sus propios estados:
vivo, aturdido, muerto. Cada estado sabe qué movimientos permite.
CÓDIGO:
class State:
    def update(self, player):
        raise NotImplementedError

class Alive(State):
    def update(self, player):
        player.run()

Explica {concept}.
```

La respuesta ahora sigue el formato de los ejemplos casi exacto: `CONCEPTO`, `ANALOGÍA`, `CÓDIGO`, en ese orden. Few-shot es una de las formas más fiables de conseguir salida consistente de un LLM.

Prueba con otros conceptos —delta time, sistemas entidad-componente, frustum culling—. ¿Se mantiene el formato?

> [!TIP]
> Dos ejemplos bien elegidos valen más que diez instrucciones. Si la salida se sigue desviando, añade otro ejemplo antes de añadir otra frase a las instrucciones.

---

## 11. Piensa paso a paso

### Chain-of-Thought

El prompting de **cadena de pensamiento** (CoT) pide al modelo que razone sobre pasos intermedios antes de dar una respuesta final. La frase que inició toda la técnica es célebre por lo simple que es — *"Vamos paso a paso."*. Hay muchos papers sobre ello, y la mayor parte del beneficio viene de esas pocas palabras.

> [!WARNING]
> **Trampa**
> Razonar en voz alta no resuelve problemas enormes. Puedes pedirle a un modelo que piense paso a paso cómo construir un clon de Discord; esa tarea sigue estando fuera de su alcance. El CoT sirve para obtener mejores respuestas en tareas que el modelo ya podría hacer por su cuenta.

### Añadiendo un paso de pensamiento

```text
Eres un asesor financiero que ayuda a un cliente a decidir sus inversiones.

PREGUNTA: ¿Invierto en acciones o en bonos?
PIENSA: Compara riesgo, rentabilidad esperada y horizonte temporal.
RECOMENDACIÓN: Las acciones pueden crecer más pero fluctúan más...

Analiza {question}.
Piensa paso a paso:
- ¿Qué factores importan más?
- ¿Qué puede salir mal?
```

### Compañero de Estudio (v3)

```text
Para el concepto nuevo, piensa primero paso a paso:
- ¿A qué objeto cotidiano se parece más?
- ¿Cuál es el error más común que comete un programador con él?
- ¿Dónde aparece en un juego?

Después escribe la respuesta siguiendo el formato de los ejemplos de arriba.
```

> [!NOTE]
> El chain-of-thought ayuda sobre todo en conceptos difíciles (decoradores, generadores, layouts de memoria). En los fáciles ayuda mucho menos — así que elige con cuidado qué prompt usar.

---

## 12. Resumen de la capítulo

| Técnica | Idea |
| :--- | :--- |
| 🎯 **Especificidad** | Declara audiencia, tono, formato y longitud |
| 🎭 **Role prompting** | Dile a la IA quién debe ser |
| 📚 **Few-shot** | Muestra ejemplos de la salida que quieres |
| 🧠 **Chain-of-thought** | Razona sobre pasos intermedios |

Las mismas cuatro técnicas funcionan dentro de la mayoría de productos de IA que ya has usado.

### 🎮 El Compañero de Estudio de Game Dev, versión final

```text
Eres un desarrollador de juegos senior y arquitecto de software.
Explicas código a programadores que ya trabajan, y nunca usas jerga
sin definirla antes.

Aquí tienes dos ejemplos de cómo quiero que se expliquen los conceptos:

CONCEPTO: object pooling (agrupación de objetos)
ANALOGÍA: Un cubo de flechas. En vez de forjar una flecha nueva en cada
disparo, disparas las que ya tienes y las recoges al impactar.
CÓDIGO:
pool = []
def acquire():
    return pool.pop() if pool else Bullet()
def release(bullet):
    pool.append(bullet)

CONCEPTO: el patrón Estado
ANALOGÍA: Una barra de vida que solo admite uno de sus propios estados:
vivo, aturdido, muerto. Cada estado sabe qué movimientos permite.
CÓDIGO:
class State:
    def update(self, player):
        raise NotImplementedError

class Alive(State):
    def update(self, player):
        player.run()

Para el concepto nuevo, piensa primero paso a paso:
- ¿A qué objeto cotidiano se parece más?
- ¿Cuál es el error más común que comete un programador con él?
- ¿Dónde aparece en un juego?

Después escribe la respuesta en el mismo formato que los ejemplos de arriba.
Máximo 120 palabras.

Explica {concept}.
```

> [!NOTE]
> La habilidad real de la ingeniería de prompts es la **iteración**: ejecuta el prompt, lee la salida con criterio, encuentra el punto débil, cambia *una* cosa, ejecútalo otra vez. El primer borrador nunca es el último.

### Hito del proyecto: `prompts.py`

Un prompt es una cadena, así que guardarlo como tal es toda la tarea de ingeniería. Esto es `Loreforge/loreforge/prompts.py`:

```python
STUDY_BUDDY = """Eres un desarrollador de juegos senior y arquitecto de software.
Explicas código a programadores que ya trabajan, y nunca usas jerga
sin definirla antes.

Aquí tienes dos ejemplos de cómo quiero que se expliquen los conceptos:

CONCEPTO: object pooling (agrupación de objetos)
ANALOGÍA: Un cubo de flechas. En vez de forjar una flecha nueva en cada
disparo, disparas las que ya tienes y las recoges al impactar.
CÓDIGO:
pool = []
def acquire():
    return pool.pop() if pool else Bullet()
def release(bullet):
    pool.append(bullet)

Explica {concept}."""


def build_prompt(concept):
    """Rellena el marcador de una plantilla de prompt.

    Usa replace() en lugar de str.format(): la plantilla contiene ejemplos
    de código, y cualquier {llave} se leería como un campo de formato.
    """
    return STUDY_BUDDY.replace('{concept}', concept)


print(build_prompt('delta time')[-40:])
```

**Salida:**

```text
pool.append(bullet)

Explain delta time.
```

> [!WARNING]
> **Trampa**
> Una plantilla de prompt llena de código Python está llena de llaves. `TEMPLATE.format(concept=...)` lanza `KeyError` en cuanto un ejemplo contiene `{vida}` o `{0}`. Usa `str.replace()`, o mantén los ejemplos de código fuera de la cadena y concaténalos.

---

## Casos de Uso Comunes

- 🧑‍🏫 Tutores personalizados y herramientas de estudio
- 📝 Generación consistente de informes y correos
- 🧾 Extracción de datos estructurados — "extrae el nombre de la misión, la recompensa y el nivel de este documento de diseño"
- 🤝 Asistentes de soporte con una voz definida

---

## Conclusiones Clave

- 🎯 Un prompt vago saca el promedio; uno específico saca algo usable.
- 🎭 Un rol es contexto gratis — úsalo.
- 📚 Los ejemplos son más fiables que las instrucciones.
- 🧠 El chain-of-thought es para conceptos difíciles, no para todo.
- 🔁 El bucle que importa es: ejecutar, leer, cambiar una cosa, ejecutar otra vez.

---

## 🎮 Reto Extra

Construye el mismo prompt de cuatro técnicas para otro dominio —un **Guionista de Misiones**, un **Revisor de Código**, un **Pipeline de Localización**— y responde a estas preguntas sobre la marcha:

- 🎭 ¿Quién es la IA?
- 👥 ¿Para quién es la respuesta?
- 🧱 ¿Qué formato debe seguir la respuesta?
- 📏 ¿Cuánto debe durar?
- 📚 ¿Qué ejemplos puedo darle?
- 🧠 ¿Sobre qué debe pensar antes de responder?

No hay una única respuesta correcta ni palabras mágicas. El objetivo es un prompt que funcione de forma fiable **para ti**.

---
