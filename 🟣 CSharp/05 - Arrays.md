
# 05. Arrays in C#

**Course:** C#
**Topic:** Arrays & Collection Access
**Tags:** `#csharp` `#arrays` `#collections`


An array is a fixed-size collection of elements of the same data type stored in contiguous memory positions.

---

## 1. Array Declaration & Initialization

Arrays are declared by specifying the data type followed by square brackets `[]`. Values are enclosed in curly braces `{}` and separated by commas.


### Key Characteristics
- **Fixed Size:** The number of elements is determined upon creation.
- **Type Safety:** All elements must match the declared data type.

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


## 2. Zero-Based Indexing

Elements inside an array are accessed using their numerical position (index) within square brackets `[index]`. C# arrays use zero-based indexing, meaning the first element is at index `0`.


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


## 3. Modifying Array Elements

Array elements can be updated after initialization by reassigning a new value directly to a specific index position.


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


## 4. Empty Arrays & Fixed Capacity

When the size of an array is known in advance but values are not yet available, specify its length using the `new` keyword. Attempting to access or assign values outside the allocated bounds throws an `IndexOutOfRangeException`.


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


## 5. Iterating Over Arrays with Loops

Instead of manually accessing each index, a `for` loop automates traversal through the collection.


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


## 6. Dynamic Loop Conditions with `.Length`

Hardcoding loop boundaries makes code rigid. The built-in `.Length` property returns the total number of elements in an array, allowing loops to adapt dynamically if the array size changes.


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
