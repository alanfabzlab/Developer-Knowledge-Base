


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
bool isGateOpen = true;

if (isGateOpen)
{
    Console.WriteLine("The party steps into the dungeon.");
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
int score = 85;

if (score >= 90)
{
    Console.WriteLine("Rank: Platinum");
}
else if (score >= 80)
{
    Console.WriteLine("Rank: Gold");
}
else
{
    Console.WriteLine("Rank: Silver or lower");
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
        bool squadIsReady = true;

        if (squadIsReady)
        {
            Console.WriteLine("Let's queue for the raid, yippee!");
        }
    }
}
```

**Salida:**


```text
Let's queue for the raid, yippee!
```


### Ejercicio 2: Medidor de Aggro

Usar operadores de comparación (`>=`) dentro de una sentencia `if`.


```csharp
using System;

class AggroMeter
{
    static void Main()
    {
        int aggroLevel = 7;

        if (aggroLevel >= 5)
        {
            Console.WriteLine("The whole zone is turning red!");
        }
    }
}
```


**Salida:**


```text
The whole zone is turning red!
```


### Ejercicio 3: Tirada Crítica

Implementar bifurcación condicional binaria con `if` y `else`.


```csharp
using System;

class CriticalRoll
{
    static void Main()
    {
        double critChance = 0.85;

        if (critChance > 0.75)
        {
            Console.WriteLine("Critical hit! The enemy reels. 💥");
        }
        else
        {
            Console.WriteLine("Glancing blow. The enemy staggers. ⚔️");
        }
    }
}
```


**Salida:**


```text
Critical hit! The enemy reels. 💥
```


### Ejercicio 4: Nivel de Peligro

Manejar lógica de múltiples condiciones usando `if`, `else if` y `else`.


```csharp
using System;

class DangerLevel
{
    static void Main()
    {
        int dangerLevel = 55;

        if (dangerLevel < 40)
        {
            Console.WriteLine("Quiet zone, nothing spawns yet 🤫");
        }
        else if (dangerLevel <= 70)
        {
            Console.WriteLine("Enemies are swarming the camp 🧟");
        }
        else
        {
            Console.WriteLine("We are about to get wiped out! 🚨");
        }
    }
}
```


**Salida:**


```text
Enemies are swarming the camp 🧟
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
        int playerLevel = 22;
        bool hasGuildPass = true;

        if (playerLevel > 21 && hasGuildPass)
        {
            Console.WriteLine("Welcome to the guild hall!");
        }
        else
        {
            Console.WriteLine("Come back when you are stronger, newbie");
        }
    }
}
```


**Salida de la Terminal:**


```text
Welcome to the guild hall!
```


### Ejercicio 6: Tirada de Rareza

Combinar el análisis de la entrada del usuario con evaluaciones condicionales.


```csharp
using System;

class RarityPull
{
    static void Main()
    {
        Console.Write("Enter your rarity tier from 1 to 10: ");
        int rarityTier = Convert.ToInt32(Console.ReadLine());

        if (rarityTier >= 8)
        {
            Console.WriteLine("LEGENDARY DROP! The whole lobby is staring. ✨");
        }
        else
        {
            Console.WriteLine("Common trash... the summoning circle laughs at you. 🔮");
        }
    }
}
```


**Salida de la Terminal:**


```text
Enter your rarity tier from 1 to 10: 9
LEGENDARY DROP! The whole lobby is staring. ✨
```


### Ejercicio 7: Beneficio o Perjuicio

Un programa completo que integra entrada del usuario, comprobaciones lógicas y control de flujo de múltiples ramas.


```csharp
using System;

class BuffOrDebuff
{
    static void Main()
    {
        Console.Write("Do you wield a sword or a staff?");
        string answer = Console.ReadLine();

        if (answer == "sword")
        {
            Console.WriteLine("YOUR BUFFS:");
            Console.WriteLine("1. Crit damage on the final hit");
            Console.WriteLine("2. Frame-perfect parries");
            Console.WriteLine("3. Campfire resting bonuses");
            Console.WriteLine("4. A save point in every dungeon");
        }
        else
        {
            Console.WriteLine("YOUR DEBUFFS:");
            Console.WriteLine("1. Missing jump inputs");
            Console.WriteLine("2. Lag spikes on the final boss");
            Console.WriteLine("3. Grindy filler quests");
            Console.WriteLine("4. Soft-locked cutscenes");
        }
    }
}
```


**Salida de la Terminal:**


```text
Do you wield a sword or a staff?
sword
YOUR BUFFS:
1. Crit damage on the final hit
2. Frame-perfect parries
3. Campfire resting bonuses
4. A save point in every dungeon
```
