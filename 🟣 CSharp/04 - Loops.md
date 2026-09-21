

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

