
# 00c. Chuleta de GenAI II

**Versión original en inglés:** [00c - GenAI Cheatsheet II.md](00c%20-%20GenAI%20Cheatsheet%20II.md)

**Curso:** GenAI
**Tema:** Patrones de prompt, representaciones vectoriales, matemática de similitud y lista de riesgos de la IA
**Tags:** `#genai` `#ai` `#llm` `#chuleta` `#prompting` `#safety`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

La segunda mitad del módulo en una página: cómo construir un prompt, cómo comparar vectores y qué revisar antes de que algo producido por una IA llegue a un jugador. Complemento de [[00b - Chuleta de GenAI]].

---

## 🎭 Bloques de Construcción de un Prompt

| Bloque | Pregúntate | Ejemplo |
| :--- | :--- | :--- |
| 🎭 **Rol** | ¿Quién es la IA? | Eres un desarrollador de juegos senior. |
| 👥 **Audiencia** | ¿Para quién es? | … para un programador que sabe Python básico. |
| 🧱 **Formato** | ¿Qué estructura? | Usa una analogía y un ejemplo de código. |
| 📏 **Longitud** | ¿Cuánto? | Máximo 100 palabras. |
| 🎨 **Tono** | ¿Qué voz? | En español casual, sin jerga. |
| 📚 **Ejemplos** | ¿Cómo se ve lo bueno? | Dos muestras de `CONCEPTO / ANALOGÍA / CÓDIGO`. |
| 🧠 **Razonamiento** | ¿En qué pensar primero? | Primero piensa paso a paso sobre… |

### Tipos de shots

| Tipo | Ejemplos dados |
| :--- | :--- |
| **Zero-shot** | 0 |
| **One-shot** | 1 |
| **Few-shot** | unos cuantos |
| **Many-shot** | muchos |

### Plantilla de Prompt Reutilizable

```text
Eres {role}.

Aquí tienes ejemplos de cómo quiero que se formateen las respuestas:
{example_1}
{example_2}

Para la nueva petición, piensa primero paso a paso sobre:
- {question_1}
- {question_2}

Después responde en el mismo formato que los ejemplos.
Máximo {n} palabras.

{request}
```

> [!NOTE]
> En Python, rellénala con `template.replace('{request}', request)` — **no** con `str.format()`. Un prompt lleno de ejemplos de código está lleno de llaves, y `format()` lee cada una como un campo.

> [!TIP]
> La ingeniería de prompts es iteración: ejecutar, leer con criterio, cambiar una cosa, ejecutar otra vez.

---

## 📐 Representaciones Vectoriales

| Método | Qué captura | Debilidad |
| :--- | :--- | :--- |
| **One-hot** | La identidad de una palabra | Cada par distinto queda igual de lejos |
| **Bolsa de palabras** | Conteos de palabras en un documento | Atada a palabras exactas; ignora orden, mayúsculas y significado |
| **Embeddings** | Significado (vectores densos y aprendidos) | Necesita un modelo entrenado |

---

## 📏 Matemática de Similitud

| Concepto | Fórmula / idea |
| :--- | :--- |
| **Distancia de Hamming** | El número de posiciones en las que dos vectores difieren |
| **Producto escalar** | $A \cdot B = \sum a_i \times b_i$ |
| **Magnitud** | $\|A\| = \sqrt{\sum a_i^2}$ |
| **Similitud coseno** | $(A \cdot B) / (\|A\| \times \|B\|)$ → `1` = misma dirección, `0` = nada en común |

**Ejemplo trabajado.** `[2, 1, 0]` frente a `[1, 1, 1]` → escalar `= 3`, $\|A\| \approx 2.236$, $\|B\| \approx 1.732$ → coseno `≈ 0.775`.

### Pipeline de Búsqueda Semántica

```text
consulta -> vector -> comparar con los vectores de los documentos (coseno) -> ordenar -> mejores resultados
```

El pipeline no cambia nunca. Lo único que cambia es cómo construyes los vectores.

---

## ⚠️ Dónde Falla la IA

| Riesgo | Qué ocurre | Defensa |
| :--- | :--- | :--- |
| 👻 **Alucinación** | Segura, plausible y equivocada | Verifica datos y fuentes |
| 🕰️ **Fecha de corte** | No conoce nada posterior a su fecha de entrenamiento | Usa búsqueda o RAG; comprueba las fechas |
| 💉 **Inyección de prompts** | El texto no confiable anula las instrucciones | Trata el contenido del usuario como datos; limita permisos |
| ⚖️ **Sesgo** | Refleja los desvíos de los datos de entrenamiento | Busca patrones; pide una salida equilibrada |
| 🐛 **Código con errores** | Plausible pero incorrecto | Lee cada línea, prueba los casos límite |

### Casos límite que hay que probar en el código de una IA

| Caso límite | Ejemplo |
| :--- | :--- |
| **Entrada vacía** | `[]`, `""`, `None` |
| **Valores extremos** | Un solo elemento, una entrada enorme |
| **Formato** | Mayúsculas, espacios, puntuación, tildes |
| **Fronteras** | Errores de una unidad (off-by-one) |
| **Fallos silenciosos** | Donde debería lanzar un error |
| **Tipo equivocado** | Un número donde se esperaba una cadena |

### Cuándo usar la IA

| ✅ Buen encaje | ❌ Mal encaje |
| :--- | :--- |
| Explicar, redactar, lluvia de ideas, resumir | Todo lo que tenga que ser exacto y no se pueda comprobar |
| Salida que puedes verificar rápido | Eventos recientes, datos precisos, matemáticas exactas |
| Remezclar material conocido | Advice legal o médico de alto riesgo |

**Flujo:** Genera → Ejecuta → Lee → Corrige. La salida es un borrador, no la respuesta final.

---

## 🛡️ Lista Antes de Publicar

- [ ] ¿He verificado los hechos, los nombres, las cifras y las citas?
- [ ] ¿El tema es posterior a la fecha de corte del modelo?
- [ ] ¿Hay texto no confiable dentro de mi prompt?
- [ ] ¿He probado los casos límite (vacío, enorme, raro, tipo equivocado)?
- [ ] ¿He revisado si hay estereotipos o suposiciones desiguales?
- [ ] ¿Hay una persona responsable de esta salida?

---
