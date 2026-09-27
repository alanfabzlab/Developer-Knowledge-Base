

# 04. Loops in C#

Loops are control flow structures used to repeat a block of code multiple times based on a specified condition. Instead of manually duplicating statements, loops automate execution cycles.


---


## 1. Loop Types Overview

C# primarily utilizes two core loop structures:
- **`while` loop**: Executes as long as its condition remains `true`.
- **`for` loop**: Executes a fixed number of times using an explicit counter variable.


---


## 2. The `while` Loop

A `while` loop checks a condition **before** each iteration. If the condition evaluates to `true`, the body executes; if `false`, execution stops and moves past the loop block.


### Syntax

```csharp
while (condition)
{
    // Code block to repeat
}
```


## 3. Exercises


### Exercise 1: Goblin Brawl

Demonstrating an interactive `while` loop controlled by user input until a specific exit keyword ("retreat") is encountered.


```csharp
using System;

class GoblinBrawl
{
    static void Main()
    {
        Console.WriteLine("Goblin incoming! 🧌");
        string input = Console.ReadLine();

        while (input != "retreat")
        {
            Console.WriteLine("Goblin incoming! 🧌");
            input = Console.ReadLine();
        }
    }
}
```


**Terminal Output:**


```text
Goblin incoming! 🧌
ahhh!
Goblin incoming! 🧌
no no no
Goblin incoming! 🧌
retreat
```



### Exercise 2: Poison Stacks

Demonstrating an interactive `while` loop that increments a variable (`poisonStacks`) and continues until the player inputs a specific string (`"antidote!"`).

```csharp
using System;

class PoisonStacks
{
    static void Main()
    {
        int poisonStacks = 1;

        Console.WriteLine($"The toxin spreads... stack {poisonStacks}");
        string input = Console.ReadLine();

        while (input != "antidote!")
        {
            poisonStacks++;
            Console.WriteLine($"The toxin spreads... stack {poisonStacks}");
            input = Console.ReadLine();
        }
    }
}
```


### Exercise 3: Spawn Wave

Demonstrating a counter-controlled `while` loop executing code a fixed number of times (4 iterations) using an incrementing counter (`count++`).


```csharp
using System;

class SpawnWave
{
    static void Main()
    {
        int count = 1;

        while (count <= 4)
        {
            Console.WriteLine("A skeleton spawns down the corridor! 💀");
            count++;
        }
    }
}
```


### Exercise 4: Stage Lights

Demonstrating a `for` loop combined with conditional statements (`if/else`) and the modulo operator (`%`) to alternate output based on odd and even iterations.


```csharp
using System;

class StageLights
{
    static void Main()
    {
        for (int i = 1; i <= 6; i++)
        {
            if (i % 2 != 0)
            {
                Console.WriteLine("Spotlight on! 💡");
            }
            else
            {
                Console.WriteLine("Spotlight on! 💡 Spotlight on! 💡");
            }
        }
    }
}
```


### Exercise 5: Pit Descent

Demonstrating a decrementing `for` loop that counts down from `0` to `-20` using the decrement operator (`depth--`).


```csharp
using System;

class PitDescent
{
    static void Main()
    {
        for (int depth = 0; depth >= -20; depth--)
        {
            Console.WriteLine(depth);
        }

        Console.WriteLine("The elevator crashes into the flooded basement...");
    }
}
```



### Exercise 6: Rage Meter

Demonstrating state mutation and compound operations inside a `for` loop to accumulate values across fixed iterations.

```csharp
using System;

class RageMeter
{
    static void Main()
    {
        int rageCharge = 0;

        for (int i = 0; i < 4; i++)
        {
            rageCharge += 7;
            Console.WriteLine($"Rage charge: {rageCharge}");
        }
    }
}
```



### Exercise 7: Say Proceed

Demonstrating dynamic loop control using user input inside a `while` loop, echoing every line the player types until a specific termination string is provided.


```csharp
using System;

class SayProceed
{
    static void Main()
    {
        string response = "";

        while (response != "proceed")
        {
            response = Console.ReadLine();

            if (response != "proceed")
            {
                Console.WriteLine(response);
            }
        }
    }
}
```


### Exercise 8: Locked Vault

Demonstrating a comprehensive `while` loop that tracks attempt counts while evaluating dynamic user input against a hardcoded secret phrase.


```csharp
using System;

class LockedVault
{
    static void Main()
    {
        string secretPhrase = "press start";
        string userInput = "";
        int attempts = 0;

        while (userInput != secretPhrase)
        {
            Console.Write("Enter the secret phrase: ");
            userInput = Console.ReadLine();
            attempts++;
        }

        Console.WriteLine("The vault door slides open, revealing a legendary blade.");
        Console.WriteLine($"It took {attempts} attempts to crack the safe.");
    }
}
```
