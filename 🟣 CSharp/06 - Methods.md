
# 06. Methods in C#

A method is a reusable block of code designed to perform a specific task. Methods help organize code, avoid duplication, and break down complex problems into modular pieces.

---


## 1. Array Processing Example (Doomsday Prepper)

Before creating standalone methods, here is how multiple arrays are combined with loops to process data dynamically.

```csharp
using System;

class DoomsdayPrepper
{
    static void Main()
    {
        string[] supplies = { "Water bottles", "Canned food", "Batteries", "First aid kits", "Flashlights" };
        int[] quantities = { 20, 18, 32, 8, 10 };

        // Updating an inventory value directly via index
        quantities[0] = 24;

        int totalSupplies = 0;

        for (int i = 0; i < supplies.Length; i++)
        {
            Console.WriteLine($"{supplies[i]} - {quantities[i]}");
            totalSupplies += quantities[i];
        }

        Console.WriteLine($"Total supplies: {totalSupplies}");
    }
}
````


## 2. Declaring and Calling Methods

Every C# executable starts in the `Main()` method. Custom methods are defined outside of `Main()` but inside the class block.


```csharp
using System;

class MeetTheMethods
{
    static void Main()
    {
        // Calling the custom method
        MoodRing();
    }

    // Method declaration
    static void MoodRing()
    {
        Console.WriteLine("Feeling unbothered!");
        Console.WriteLine("Blue 💙");
    }
}
```


## 3. Method Reusability

Calling a method multiple times executes its encapsulated logic without duplicating code.


```csharp
using System;

class MakeSomeNoise
{
    static void Main()
    {
        // Calling Hype() 5 times
        Hype();
        Hype();
        Hype();
        Hype();
        Hype();
    }

    static void Hype()
    {
        Console.WriteLine("Make some noise!");
    }
}
```


## 4. Parameters vs. Arguments

Methods can accept external data to customize their execution using parameters.

### Definitions

- **Parameter:** The placeholder variable defined in the method signature (e.g., `string food`).
    
- **Argument:** The actual value passed into the method during its call (e.g., `"peanuts 🥜"`).
    


```csharp
using System;

class TheCookout
{
    static void Main()
    {
        // "wheat 🌾", "peanuts 🥜", and "cheese 🧀" are ARGUMENTS
        Allergies("wheat 🌾");
        Allergies("peanuts 🥜");
        Allergies("cheese 🧀");
    }

    // 'food' is the PARAMETER
    static void Allergies(string food)
    {
        Console.WriteLine($"We'll make sure to provide snacks that don't contain {food}!");
    }
}
```

