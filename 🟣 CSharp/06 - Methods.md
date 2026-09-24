
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


## 5. Multiple Parameters

Methods can accept multiple parameters of different data types, separated by commas. The arguments supplied at the call site must match the expected type and positional order.


```csharp
using System;

class TicketPool
{
    static void Main()
    {
        CalculateCost("Bad Bunny", 150, 4, 4);
        CalculateCost("Dua Lipa", 200, 3, 3);
    }

    static void CalculateCost(string artist, int ticketPrice, int numberOfTickets, int people)
    {
        int totalCost = ticketPrice * numberOfTickets;
        int costPerPerson = totalCost / people;

        Console.WriteLine($"Artist: {artist}");
        Console.WriteLine($"Cost per person: ${costPerPerson}");
    }
}
```


## 6. Return Values

By default, methods marked with `void` do not return a value. To send data back to the calling scope, replace `void` with the desired return data type (`int`, `string`, `bool`, etc.) and use the `return` keyword.


```csharp
using System;

class ReturnToSender
{
    static void Main()
    {
        int remainingPoints = PointsLeft(50000, 35000);
        Console.WriteLine(remainingPoints);
    }

    static int PointsLeft(int startingPoints, int pointsNeeded)
    {
        return startingPoints - pointsNeeded;
    }
}
```


## 7. Modular Composition (Calling All Hackers)

Breaking complex applications into specialized methods improves code maintainability and testability.


```csharp
using System;

class CallingAllHackers
{
    static void Main()
    {
        int teams = CalculateTeams(36, 6);
        int hours = CalculateHours(12, 18);
        string invite = CreateInvite("Boba and Booleans", teams, hours);

        Console.WriteLine(invite);
    }

    static int CalculateTeams(int attendees, int teamSize)
    {
        return attendees / teamSize;
    }

    static int CalculateHours(int startHour, int endHour)
    {
        return endHour - startHour;
    }

    static string CreateInvite(string eventName, int teams, int hours)
    {
        return $"{eventName} starts at 6 PM!\nWe'll hack for {hours} hours in {teams} teams. See you there!";
    }
}
```

