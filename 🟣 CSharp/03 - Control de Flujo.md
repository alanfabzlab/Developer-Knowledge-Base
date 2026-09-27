


# 03. Control de Flujo en C#

**Versión original en inglés:** [03 - Control Flow.md](03%20-%20Control%20Flow.md)

**Curso:** C#
**Tema:** Sentencias Condicionales y Control de Flujo
**Etiquetas:** `#csharp` `#control-flow` `#conditionals`


El control de flujo describe el orden en el que se ejecutan o evalúan sentencias, instrucciones o llamadas a función individuales. Por defecto, el código se ejecuta línea por línea de arriba abajo, pero las sentencias de control de flujo permiten tomar decisiones basadas en condiciones dinámicas.

---


## 1. Condiciones Booleanas y Sentencias `if`

Una sentencia `if` ejecuta un bloque de código solo cuando una condición especificada evalúa a `true`.


### Sintaxis Básica

```csharp
bool puertaAbierta = true;

if (puertaAbierta)
{
    Console.WriteLine("El grupo entra en la mazmorra.");
}
```


## 2. Operadores de Comparación

Los operadores de comparación evalúan la relación entre dos valores y devuelven un resultado booleano (`true` o `false`).

|**Operador**|**Descripción**|**Ejemplo (int x = 10)**|**Resultado**|
|---|---|---|---|
|`==`|Igual a|`x == 10`|`true`|
|`!=`|Distinto de|`x != 5`|`true`|
|`>`|Mayor que|`x > 15`|`false`|
|`<`|Menor que|`x < 20`|`true`|
|`>=`|Mayor o igual que|`x >= 10`|`true`|



## 3. Bifurcación con `else` y `else if`

Cuando existen múltiples caminos posibles, `else` y `else if` permiten gestionar condiciones alternativas.

- **`else`**: Se ejecuta cuando todas las condiciones `if` y `else if` anteriores evalúan a `false`.
    
- **`else if`**: Evalúa condiciones secuenciales de arriba abajo. Una vez que una condición evalúa a `true`, se ejecuta su bloque y se omiten las condiciones restantes.
    


```csharp
int puntuacion = 85;

if (puntuacion >= 90)
{
    Console.WriteLine("Rango: Platino");
}
else if (puntuacion >= 80)
{
    Console.WriteLine("Rango: Oro");
}
else
{
    Console.WriteLine("Rango: Plata o inferior");
}
```


## 4. Ejercicios

### Ejercicio 1: Noche de Incursión

Introducción a la evaluación booleana simple en el control de flujo.


```csharp
using System;

class RaidNight
{
    static void Main()
    {
        bool escuadraLista = true;

        if (escuadraLista)
        {
            Console.WriteLine("¡Vamos a hacer cola para la incursión, arriba!");
        }
    }
}
```

**Salida:**


```text
¡Vamos a hacer cola para la incursión, arriba!
```


### Ejercicio 2: Medidor de Aggro

Usar operadores de comparación (`>=`) dentro de una sentencia `if`.


```csharp
using System;

class AggroMeter
{
    static void Main()
    {
        int nivelAggro = 7;

        if (nivelAggro >= 5)
        {
            Console.WriteLine("¡Toda la zona se está poniendo roja!");
        }
    }
}
```


**Salida:**


```text
¡Toda la zona se está poniendo roja!
```


### Ejercicio 3: Tirada Crítica

Implementar bifurcación condicional binaria con `if` y `else`.


```csharp
using System;

class CriticalRoll
{
    static void Main()
    {
        double probCritica = 0.85;

        if (probCritica > 0.75)
        {
            Console.WriteLine("¡Golpe crítico! El enemigo se marea. 💥");
        }
        else
        {
            Console.WriteLine("Golpe de refilón. El enemigo da un traspié. ⚔️");
        }
    }
}
```


**Salida:**


```text
¡Golpe crítico! El enemigo se marea. 💥
```


### Ejercicio 4: Nivel de Peligro

Manejar lógica de múltiples condiciones usando `if`, `else if` y `else`.


```csharp
using System;

class DangerLevel
{
    static void Main()
    {
        int nivelPeligro = 55;

        if (nivelPeligro < 40)
        {
            Console.WriteLine("Zona tranquila, todavía no aparece nada 🤫");
        }
        else if (nivelPeligro <= 70)
        {
            Console.WriteLine("¡Los enemigos están inundando el campamento! 🧟");
        }
        else
        {
            Console.WriteLine("¡Estamos a punto de ser aniquilados! 🚨");
        }
    }
}
```


**Salida:**


```text
¡Los enemigos están inundando el campamento! 🧟
```



---


## 5. Operadores Lógicos
Los operadores lógicos permiten combinar múltiples condiciones dentro de una misma evaluación de control de flujo.

| Operador | Nombre | Descripción | Ejemplo |
| :--- | :--- | :--- | :--- |
| `&&` | Y | Devuelve `true` solo si **ambas** condiciones evalúan a `true`. | `(age >= 21 && hasInvitation)` |
| `\|\|` | O | Devuelve `true` si **al menos una** condición evalúa a `true`. | `(isWeekend \|\| isHoliday)` |
| `!` | NO | Invierte (da la vuelta) el valor booleano de una condición. | `(!isLoggedIn)` |


---


## 6. Ejercicios Avanzados de Control de Flujo


### Ejercicio 5: Puerta del Gremio
Combinar condiciones usando el operador lógico AND (`&&`).

```csharp
using System;

class GuildGate
{
    static void Main()
    {
        int nivelJugador = 22;
        bool tienePaseGremio = true;

        if (nivelJugador > 21 && tienePaseGremio)
        {
            Console.WriteLine("¡Bienvenido al salón del gremio!");
        }
        else
        {
            Console.WriteLine("Vuelve cuando seas más fuerte, novato");
        }
    }
}
```


**Salida de la Terminal:**


```text
¡Bienvenido al salón del gremio!
```


### Ejercicio 6: Tirada de Rareza

Combinar el análisis de la entrada del usuario con evaluaciones condicionales.


```csharp
using System;

class RarityPull
{
    static void Main()
    {
        Console.Write("Introduce tu nivel de rareza del 1 al 10: ");
        int nivelRareza = Convert.ToInt32(Console.ReadLine());

        if (nivelRareza >= 8)
        {
            Console.WriteLine("¡BOTÍN LEGENDARIO! Toda la sala está mirando. ✨");
        }
        else
        {
            Console.WriteLine("Basura común... el círculo de invocación se ríe de ti. 🔮");
        }
    }
}
```


**Salida de la Terminal:**


```text
Introduce tu nivel de rareza del 1 al 10: 9
¡BOTÍN LEGENDARIO! Toda la sala está mirando. ✨
```


### Ejercicio 7: Beneficio o Perjuicio

Un programa completo que integra entrada del usuario, comprobaciones lógicas y control de flujo de múltiples ramas.


```csharp
using System;

class BuffOrDebuff
{
    static void Main()
    {
        Console.Write("¿Empuntas una espada o un bastón?");
        string respuesta = Console.ReadLine();

        if (respuesta == "espada")
        {
            Console.WriteLine("TUS BUFFS:");
            Console.WriteLine("1. Daño crítico en el golpe final");
            Console.WriteLine("2. Parryas perfectas cuadro a cuadro");
            Console.WriteLine("3. Bonificaciones por descansar en la hoguera");
            Console.WriteLine("4. Un punto de guardado en cada mazmorra");
        }
        else
        {
            Console.WriteLine("TUS DEBUFFS:");
            Console.WriteLine("1. Pulsaciones de salto perdidas");
            Console.WriteLine("2. Tirones de lag en el jefe final");
            Console.WriteLine("3. Misiones de relleno tediosas");
            Console.WriteLine("4. Cinemáticas con bloqueo suave");
        }
    }
}
```


**Salida de la Terminal:**


```text
¿Empuntas una espada o un bastón?
espada
TUS BUFFS:
1. Daño crítico en el golpe final
2. Parryas perfectas cuadro a cuadro
3. Bonificaciones por descansar en la hoguera
4. Un punto de guardado en cada mazmorra
```
