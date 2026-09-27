
# 05. Arreglos en C#

**Versión original en inglés:** [05 - Arrays.md](05%20-%20Arrays.md)

**Curso:** C#
**Tema:** Arreglos y Acceso a Colecciones
**Etiquetas:** `#csharp` `#arrays` `#collections`


Un arreglo es una colección de tamaño fijo de elementos del mismo tipo de dato, almacenados en posiciones de memoria contiguas.

---

## 1. Declaración e Inicialización de Arreglos

Los arreglos se declaran especificando el tipo de dato seguido de corchetes `[]`. Los valores se encierran entre llaves `{}` y se separan por comas.


### Características Clave
- **Tamaño Fijo:** El número de elementos se determina en el momento de la creación.
- **Seguridad de Tipos:** Todos los elementos deben coincidir con el tipo de dato declarado.

```csharp
using System;

class ArrayFoundations
{
    static void Main()
    {
        // String array containing boss names
        string[] bosses = { "Chrono Warden", "Void Reaper", "Iron Colossus", "Frost Queen" };

        // Integer array containing corresponding threat levels
        int[] threatLevels = { 10, 9, 8, 10 };
    }
}
```


## 2. Indexación Basada en Cero

Los elementos dentro de un arreglo se acceden usando su posición numérica (índice) entre corchetes `[index]`. Los arreglos en C# usan indexación basada en cero, lo que significa que el primer elemento está en el índice `0`.


```csharp
using System;

class BossThemes
{
    static void Main()
    {
        string[] themes = 
        {
            "Overture of the Kingdom",
            "Tavern at Dusk",
            "Echoing Caverns",
            "Shop Menu Theme",
            "Final Boss Concerto"
        };

        Console.WriteLine("Opening Cutscene:");
        Console.WriteLine(themes[0]); // Output: Overture of the Kingdom

        Console.WriteLine("Underground Ruins:");
        Console.WriteLine(themes[2]); // Output: Echoing Caverns

        Console.WriteLine("Final Boss:");
        Console.WriteLine(themes[4]); // Output: Final Boss Concerto
    }
}
```


## 3. Modificar Elementos de un Arreglo

Los elementos de un arreglo se pueden actualizar después de la inicialización reasignando un nuevo valor directamente a una posición de índice concreta.


```csharp
using System;

class QuestBoard
{
    static void Main()
    {
        string[] quests = { "Slay the Sand Wraith", "Mine 5 iron ore", "Deliver a healing potion" };

        // Update element at index 1
        quests[1] = "Mine 12 iron ore";

        Console.WriteLine(quests[1]); // Output: Mine 12 iron ore
    }
}
```


## 4. Arreglos Vacíos y Capacidad Fija

Cuando el tamaño de un arreglo se conoce de antemano pero los valores aún no están disponibles, se especifica su longitud usando la palabra clave `new`. Intentar acceder o asignar valores fuera de los límites asignados lanza una `IndexOutOfRangeException`.


```csharp
using System;

class ArenaBracket
{
    static void Main()
    {
        // Allocates space for 64 string elements
        string[] matches = new string[64];

        // Assigning values later
        matches[0] = "Guild Iron vs Guild Ember";
        matches[1] = "Guild Void vs Guild Storm";
    }
}
```


## 5. Iterar sobre Arreglos con Bucles

En lugar de acceder manualmente a cada índice, un bucle `for` automatiza el recorrido de la colección.


```csharp
using System;

class PartyChat
{
    static void Main()
    {
        string[] messages = {
            "Kaz: who brings frost potions tonight???",
            "Mira: not meeee i gotta craft the new staff",
            "Dev: join usssssss",
            "Sol: i should rly grind the raid instead tbh",
            "Rin: see you all at the gate!"
        };

        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine(messages[i]);
        }
    }
}
```


## 6. Condiciones de Bucle Dinámicas con `.Length`

Codificar los límites del bucle a mano hace que el código sea rígido. La propiedad integrada `.Length` devuelve el número total de elementos de un arreglo, permitiendo que los bucles se adapten dinámicamente si cambia el tamaño del arreglo.


```csharp
using System;

class InventoryBag
{
    static void Main()
    {
        string[] items = {
            "Health Potion",
            "Mana Potion",
            "Bomb Rune",
            "Iron Ore",
            "Teleport Scroll",
            "Golden Key"
        };

        // .Length dynamically evaluates to 6
        for (int i = 0; i < items.Length; i++)
        {
            Console.WriteLine(items[i]);
        }
    }
}
```
