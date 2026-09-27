

# 02. Typecast


## 1. Variables & Primitive Data Types

A variable is a named storage container that holds data in memory. Every variable in C# requires a explicit data type, a name, and an assigned value.


### Common Data Types
* **`int`**: Whole numbers (integers) without decimals (positive or negative).
* **`double`**: Floating-point decimal numbers.
* **`string`**: Sequence of characters used for storing text (supports Unicode & emojis).
* **`bool`**: Boolean values representing truth states (`true` or `false`).


---


## 2. Practice Exercises

### Exercise 1: Loadout Screen
Declaring basic variables (`int`, `string`, `bool`) for a character screen and printing their values to the console using string interpolation.

```csharp
using System;

class LoadoutScreen
{
    static void Main()
    {
        int controllers = 2;
        string currentClass = "Paladin";
        bool isHeadsetOn = true;

        Console.WriteLine($"Controllers: {controllers}");
        Console.WriteLine($"Class: {currentClass}");
        Console.WriteLine($"Headset on: {isHeadsetOn}");
    }
}
```


**Terminal Output:**


```text
Controllers: 2
Class: Paladin
Headset on: True
```



## 3. Variables, String Concatenation & Basic Math

In C#, variables store data that can be joined with text using string concatenation or manipulated through standard arithmetic and modulo operators.


## 4. Additional Practice Exercises

### Exercise 2: Raid Planning

Declaring and initializing variables with different primitive types (`string`, `int`, `double`, `bool`) to plan a dungeon run.


```csharp
using System;

class RaidPlanning
{
    static void Main()
    {
        string raidTarget = "Void Hydra";
        int squadSize = 15;
        double costPerPlayer = 25.50;
        bool isBlindRaid = true;

        Console.WriteLine($"Raid Target: {raidTarget}");
        Console.WriteLine($"Squad Size: {squadSize}");
        Console.WriteLine($"Cost per Player: ${costPerPlayer}");
        Console.WriteLine($"Blind Raid: {isBlindRaid}");
    }
}
```


**Terminal Output:**


```text
Raid Target: Void Hydra
Squad Size: 15
Cost per Player: $25.5
Blind Raid: True
```


### Exercise 3: Legend Origins

Demonstrating string concatenation by combining text strings with integer variables.


```csharp
using System;

class LegendOrigins
{
    static void Main()
    {
        string name = "Aria the Bold";
        int year = 1994;

        Console.WriteLine(name + " is an incredibly legendary hero.");
        Console.WriteLine("She rose to fame in " + year + " during the Siege of Emberfall.");
    }
}
```


**Terminal Output:**


```text
Aria the Bold is an incredibly legendary hero.
She rose to fame in 1994 during the Siege of Emberfall.
```


### Exercise 4: Loot Split

Performing integer division and using the modulo (`%`) operator to distribute gold between chests and find the remainder.


```csharp
using System;

class LootSplit
{
    static void Main()
    {
        int totalGold = 23;
        int goldPerChest = 5;

        int fullChests = totalGold / goldPerChest;
        int leftoverGold = totalGold % goldPerChest;

        Console.WriteLine($"Full chests: {fullChests}");
        Console.WriteLine($"Gold left over: {leftoverGold}");
    }
}
```


**Terminal Output:**


```text
Full chests: 4
Gold left over: 3
```



## 5. Collecting User Input

In C#, user input is collected from the console using `Console.ReadLine()`. The input is always captured as a `string` by default.


### Standard String Input

```csharp
Console.Write("What's your hero name?");
string heroName = Console.ReadLine();
Console.WriteLine($"Welcome to the party, {heroName}!");
```


### Converting String Input to Integer (`int`)

When numeric operations are required on user input, the captured `string` must be converted using `Convert.ToInt32()` or `int.Parse()`.


```csharp
Console.Write("Enter a damage value: ");
string input = Console.ReadLine();
int damage = Convert.ToInt32(input);
```


## 6. Input & Conversion Exercises


### Exercise 5: Rune Cycle

Asking the user for the birth year of their character, parsing the string input to an integer, and calculating the years remaining until the twelve-rune cycle realigns for their sign (12-year cycle).


```csharp
using System;

class RuneCycle
{
    static void Main()
    {
        Console.Write("Enter your character's birth year: ");
        int birthYear = Convert.ToInt32(Console.ReadLine());

        int currentYear = 2026;
        int yearsIntoCycle = (currentYear - birthYear) % 12;
        int yearsUntilAlignment = (12 - yearsIntoCycle) % 12;

        Console.WriteLine($"Years until the runes realign for your sign: {yearsUntilAlignment}");
    }
}
```


**Terminal Output:**


```text
Enter your character's birth year: 2004
Years until the runes realign for your sign: 2
```


### Exercise 6: Gacha Summon

Calculating how many times a player can pull on a summoning banner based on their crystal balance and finding the leftover crystals using division and modulo operations.


```csharp
using System;

class GachaSummon
{
    static void Main()
    {
        Console.Write("How many crystals do you have? ");
        string input = Console.ReadLine();
        int crystals = Convert.ToInt32(input);

        int summonCost = 50;

        int totalSummons = crystals / summonCost;
        int remainingCrystals = crystals % summonCost;

        Console.WriteLine($"You can summon: {totalSummons} time(s)");
        Console.WriteLine($"Crystals left over: {remainingCrystals}");
    }
}
```

**Terminal Output:**


```text
How many crystals do you have? 275
You can summon: 5 time(s)
Crystals left over: 25
```
