

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

### Exercise 1: Desk Environment Variables
Declaring basic variables (`int`, `string`, `bool`) and printing their values to the console using string interpolation.

```csharp
using System;

class Typecast
{
    static void Main()
    {
        int monitors = 2;
        string currentDrink = "Coffee";
        bool isHeadphonesOn = true;

        Console.WriteLine($"Monitors: {monitors}");
        Console.WriteLine($"Drink: {currentDrink}");
        Console.WriteLine($"Headphones on: {isHeadphonesOn}");
    }
}
````


**Terminal Output:**


```text
Monitors: 2
Drink: Coffee
Headphones on: True
```

