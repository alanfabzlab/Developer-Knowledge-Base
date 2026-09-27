
# 06. Methods in C#

**Course:** C#
**Topic:** Methods, Parameters & Return Values
**Tags:** `#csharp` `#methods` `#functions`


A method is a reusable block of code designed to perform a specific task. Methods help organize code, avoid duplication, and break down complex problems into modular pieces.

---


## 1. Array Processing Example (Loot Hoarder)

Before creating standalone methods, here is how multiple arrays are combined with loops to process data dynamically.

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


## 2. Declaring and Calling Methods

Every C# executable starts in the `Main()` method. Custom methods are defined outside of `Main()` but inside the class block.


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


## 3. Method Reusability

Calling a method multiple times executes its encapsulated logic without duplicating code.


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


## 4. Parameters vs. Arguments

Methods can accept external data to customize their execution using parameters.

### Definitions

- **Parameter:** The placeholder variable defined in the method signature (e.g., `string elixir`).
    
- **Argument:** The actual value passed into the method during its call (e.g., `"ember 🔥"`).
    


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


## 5. Multiple Parameters

Methods can accept multiple parameters of different data types, separated by commas. The arguments supplied at the call site must match the expected type and positional order.


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


## 6. Return Values

By default, methods marked with `void` do not return a value. To send data back to the calling scope, replace `void` with the desired return data type (`int`, `string`, `bool`, etc.) and use the `return` keyword.


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


## 7. Modular Composition (Calling All Raiders)

Breaking complex applications into specialized methods improves code maintainability and testability.


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
