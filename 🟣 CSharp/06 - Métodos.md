
# 06. Métodos en C#

**Versión original en inglés:** [06 - Methods.md](06%20-%20Methods.md)

**Curso:** C#
**Tema:** Métodos, Parámetros y Valores de Retorno
**Etiquetas:** `#csharp` `#methods` `#functions`


Un método es un bloque de código reutilizable diseñado para realizar una tarea específica. Los métodos ayudan a organizar el código, evitar la duplicación y dividir los problemas complejos en piezas modulares.

---


## 1. Ejemplo de Procesamiento de Arreglos (Loot Hoarder)

Antes de crear métodos independientes, aquí se muestra cómo se combinan varios arreglos con bucles para procesar datos de forma dinámica.

```csharp
using System;

class LootHoarder
{
    static void Main()
    {
        string[] supplies = { "Health Potions", "Mana Potions", "Elixirs", "Antidotes", "Bomb Runes" };
        int[] quantities = { 12, 30, 8, 25, 16 };

        // Updating an inventory value directly via index
        quantities[0] = 15;

        int totalSupplies = 0;

        for (int i = 0; i < supplies.Length; i++)
        {
            Console.WriteLine($"{supplies[i]} - {quantities[i]}");
            totalSupplies += quantities[i];
        }

        Console.WriteLine($"Total supplies: {totalSupplies}");
    }
}
```


## 2. Declarar y Llamar Métodos

Todo ejecutable de C# comienza en el método `Main()`. Los métodos personalizados se definen fuera de `Main()` pero dentro del bloque de la clase.


```csharp
using System;

class LevelUpFanfare
{
    static void Main()
    {
        // Calling the custom method
        VictoryPose();
    }

    // Method declaration
    static void VictoryPose()
    {
        Console.WriteLine("The champion raises the trophy!");
        Console.WriteLine("Victory! 🏆");
    }
}
```


## 3. Reutilización de Métodos

Llamar a un método varias veces ejecuta su lógica encapsulada sin duplicar código.


```csharp
using System;

class CrowdChant
{
    static void Main()
    {
        // Calling Chant() 5 times
        Chant();
        Chant();
        Chant();
        Chant();
        Chant();
    }

    static void Chant()
    {
        Console.WriteLine("Chant with me!");
    }
}
```


## 4. Parámetros vs. Argumentos

Los métodos pueden aceptar datos externos para personalizar su ejecución usando parámetros.

### Definiciones

- **Parámetro:** La variable auxiliar definida en la firma del método (p. ej., `string elixir`).
    
- **Argumento:** El valor real que se pasa al método durante su llamada (p. ej., `"ember 🔥"`).
    


```csharp
using System;

class BuffMenu
{
    static void Main()
    {
        // "ember 🔥", "frost ❄️", and "lightning ⚡" are ARGUMENTS
        BrewElixir("ember 🔥");
        BrewElixir("frost ❄️");
        BrewElixir("lightning ⚡");
    }

    // 'elixir' is the PARAMETER
    static void BrewElixir(string elixir)
    {
        Console.WriteLine($"Brewing a {elixir} elixir for the whole party!");
    }
}
```


## 5. Múltiples Parámetros

Los métodos pueden aceptar múltiples parámetros de distintos tipos de dato, separados por comas. Los argumentos suministrados en el punto de llamada deben coincidir con el tipo esperado y con el orden posicional.


```csharp
using System;

class PrizeSplit
{
    static void Main()
    {
        CalculateCost("Sunken Keep", 150, 4, 4);
        CalculateCost("Shadow Crypt", 200, 3, 3);
    }

    static void CalculateCost(string dungeonName, int goldPerFloor, int floorsCleared, int partySize)
    {
        int totalGold = goldPerFloor * floorsCleared;
        int goldPerHero = totalGold / partySize;

        Console.WriteLine($"Dungeon: {dungeonName}");
        Console.WriteLine($"Gold per hero: ${goldPerHero}");
    }
}
```


## 6. Valores de Retorno

De forma predeterminada, los métodos marcados con `void` no devuelven ningún valor. Para enviar datos de vuelta al ámbito que llama, reemplaza `void` por el tipo de dato de retorno deseado (`int`, `string`, `bool`, etc.) y usa la palabra clave `return`.


```csharp
using System;

class QuestProgress
{
    static void Main()
    {
        int xpRemaining = XpToNextLevel(35000, 50000);
        Console.WriteLine(xpRemaining);
    }

    static int XpToNextLevel(int currentXp, int xpToNextLevel)
    {
        return xpToNextLevel - currentXp;
    }
}
```


## 7. Composición Modular (Calling All Raiders)

Dividir las aplicaciones complejas en métodos especializados mejora la mantenibilidad y la testeabilidad del código.


```csharp
using System;

class CallingAllRaiders
{
    static void Main()
    {
        int squads = CalculateSquads(36, 6);
        int hours = CalculateHours(12, 18);
        string briefing = CreateBriefing("Dragon Siege", squads, hours);

        Console.WriteLine(briefing);
    }

    static int CalculateSquads(int raiders, int squadSize)
    {
        return raiders / squadSize;
    }

    static int CalculateHours(int startHour, int endHour)
    {
        return endHour - startHour;
    }

    static string CreateBriefing(string eventName, int squads, int hours)
    {
        return $"{eventName} starts at 6 PM!\nWe'll raid for {hours} hours with {squads} squads. See you at the gate!";
    }
}
```
