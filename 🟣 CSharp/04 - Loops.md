

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
````


## 3. Exercises


### Exercise 1: Tickle Monster

Demonstrating an interactive `while` loop controlled by user input until a specific exit keyword ("stop") is encountered.


```csharp
using System;

class TickleMonster
{
    static void Main()
    {
        Console.WriteLine("Tickle tickle 🧌");
        string input = Console.ReadLine();

        while (input != "stop")
        {
            Console.WriteLine("Tickle tickle 🧌");
            input = Console.ReadLine();
        }
    }
}
```


**Terminal Output:**


```text
Tickle tickle 🧌
ahhh!
Tickle tickle 🧌
no no no
Tickle tickle 🧌
stop
```



### Exercise 2: Disappearing Act

Demonstrating an interactive `while` loop that increments a variable (`invisibilityLevel`) and continues until the user inputs a specific string (`"compose yourself!"`).

```csharp
using System;

class DisappearingAct
{
    static void Main()
    {
        int invisibilityLevel = 1;

        Console.WriteLine($"You fade further out of existence... level {invisibilityLevel}");
        string input = Console.ReadLine();

        while (input != "compose yourself!")
        {
            invisibilityLevel++;
            Console.WriteLine($"You fade further out of existence... level {invisibilityLevel}");
            input = Console.ReadLine();
        }
    }
}
````


### Exercise 3: Robocaller

Demonstrating a counter-controlled `while` loop executing code a fixed number of times (4 iterations) using an incrementing counter (`count++`).


```csharp
using System;

class Robocaller
{
    static void Main()
    {
        int count = 1;

        while (count <= 4)
        {
            Console.WriteLine("This is Macintosh. We detected a virus on your computer.");
            count++;
        }
    }
}
```


### Exercise 4: In The Spotlight

Demonstrating a `for` loop combined with conditional statements (`if/else`) and the modulo operator (`%`) to alternate output based on odd and even iterations.


```csharp
using System;

class InTheSpotlight
{
    static void Main()
    {
        for (int i = 1; i <= 6; i++)
        {
            if (i % 2 != 0)
            {
                Console.WriteLine("Flash! 📸");
            }
            else
            {
                Console.WriteLine("Flash! 📸 Flash! 📸");
            }
        }
    }
}
```


### Exercise 5: Uno Reverse

Demonstrating a decrementing `for` loop that counts down from `0` to `-13` using the decrement operator (`floor--`).


```csharp
using System;

class UnoReverse
{
    static void Main()
    {
        for (int floor = 0; floor >= -13; floor--)
        {
            Console.WriteLine(floor);
        }

        Console.WriteLine("The doors open to something unfamiliar...");
    }
}
```



### Exercise 6: Mystery Machine

Demonstrating state mutation and compound operations inside a `for` loop to accumulate values across fixed iterations.

```csharp
using System;

class MysteryMachine
{
    static void Main()
    {
        int timeDistortion = 0;

        for (int i = 0; i < 5; i++)
        {
            timeDistortion += 3;
            Console.WriteLine($"Time distortion: {timeDistortion}");
        }
    }
}
````



### Exercise 7: Say Uncle

Demonstrating dynamic loop control using user input inside a `while` loop, filtering output conditionally until a specific termination string is provided.


```csharp
using System;

class SayUncle
{
    static void Main()
    {
        string response = "";

        while (response != "uncle")
        {
            response = Console.ReadLine();

            if (response != "uncle")
            {
                Console.WriteLine(response);
            }
        }
    }
}
```


### Exercise 8: Best Kept Secret

Demonstrating a comprehensive `while` loop that tracks iteration attempts while evaluating dynamic user input against a hardcoded secret phrase.


```csharp
using System;

class BestKeptSecret
{
    static void Main()
    {
        string secretPhrase = "open sesame";
        string userInput = "";
        int attempts = 0;

        while (userInput != secretPhrase)
        {
            Console.Write("Enter the secret phrase: ");
            userInput = Console.ReadLine();
            attempts++;
        }

        Console.WriteLine("The bookshelf shifts aside, revealing a hidden passageway.");
        Console.WriteLine($"It took {attempts} attempts to discover the passage.");
    }
}
```