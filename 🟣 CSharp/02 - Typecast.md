

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



## 3. Variables, String Concatenation & Basic Math

In C#, variables store data that can be joined with text using string concatenation or manipulated through standard arithmetic and modulo operators.


## 4. Additional Practice Exercises

### Exercise 2: Party Animal

Declaring and initializing variables with different primitive types (`string`, `int`, `double`, `bool`) to plan an event.


```csharp
using System;

class PartyAnimal
{
    static void Main()
    {
        string partyTheme = "Retro Gaming";
        int numberOfGuests = 15;
        double costPerGuest = 25.50;
        bool isSurpriseParty = true;

        Console.WriteLine($"Party Theme: {partyTheme}");
        Console.WriteLine($"Guests: {numberOfGuests}");
        Console.WriteLine($"Cost per Guest: ${costPerGuest}");
        Console.WriteLine($"Surprise Party: {isSurpriseParty}");
    }
}
```


**Terminal Output:**


```text
Party Theme: Retro Gaming
Guests: 15
Cost per Guest: $25.5
Surprise Party: True
```


### Exercise 3: Celebrity Crush

Demonstrating string concatenation by combining text strings with integer variables.


```csharp
using System;

class CelebrityCrush
{
    static void Main()
    {
        string name = "Lady Gaga";
        int year = 2008;

        Console.WriteLine(name + " is an incredibly talented artist.");
        Console.WriteLine("She rose to fame in " + year + " with her hit album The Fame.");
    }
}
```


**Terminal Output:**


```text
Lady Gaga is an incredibly talented artist.
She rose to fame in 2008 with her hit album The Fame.
```


### Exercise 4: Math Is Mathing

Performing integer division and using the modulo (`%`) operator to calculate bundle distribution and remainder.


```csharp
using System;

class MathIsMathing
{
    static void Main()
    {
        int totalPeople = 23;
        int ticketsPerBundle = 5;

        int fullBundles = totalPeople / ticketsPerBundle;
        int peopleWithoutTickets = totalPeople % ticketsPerBundle;

        Console.WriteLine($"Full bundles: {fullBundles}");
        Console.WriteLine($"People without tickets: {peopleWithoutTickets}");
    }
}
```


**Terminal Output:**


```text
Full bundles: 4
People without tickets: 3
```



## 5. Collecting User Input

In C#, user input is collected from the console using `Console.ReadLine()`. The input is always captured as a `string` by default.


### Standard String Input

```csharp
Console.WriteLine("What's your name?");
string name = Console.ReadLine();
Console.WriteLine($"Nice to meet you, {name}!");
````


### Converting String Input to Integer (`int`)

When numeric operations are required on user input, the captured `string` must be converted using `Convert.ToInt32()` or `int.Parse()`.


```csharp
Console.Write("Enter a number: ");
string input = Console.ReadLine();
int convertedValue = Convert.ToInt32(input);
```


## 6. Input & Conversion Exercises


### Exercise 5: Year of the X

Asking the user for their birth year, parsing the string input to an integer, and calculating the years remaining until their Chinese Zodiac year repeats (12-year cycle).


```csharp
using System;

class YearOfTheX
{
    static void Main()
    {
        Console.Write("Enter your birth year: ");
        int birthYear = Convert.ToInt32(Console.ReadLine());

        int currentYear = 2026;
        int yearsPassed = (currentYear - birthYear) % 12;
        int yearsUntilNext = (12 - yearsPassed) % 12;

        Console.WriteLine($"Years until your zodiac year happens again: {yearsUntilNext}");
    }
}
```


**Terminal Output:**


```text
Enter your birth year: 1996
Years until your zodiac year happens again: 2
```


### Exercise 6: Giant Plushie

Calculating how many giant plushies a user can redeem based on their arcade ticket balance and finding the remaining ticket count using division and modulo operations.


```csharp
using System;

class GiantPlushie
{
    static void Main()
    {
        Console.Write("How many tickets do you have? ");
        string input = Console.ReadLine();
        int userTickets = Convert.ToInt32(input);

        int plushieCost = 50;

        int totalPlushies = userTickets / plushieCost;
        int remainingTickets = userTickets % plushieCost;

        Console.WriteLine($"You can redeem: {totalPlushies} plushie(s)");
        Console.WriteLine($"Tickets left over: {remainingTickets}");
    }
}
```

**Terminal Output:**


```text
How many tickets do you have? 125
You can redeem: 2 plushie(s)
Tickets left over: 25
```