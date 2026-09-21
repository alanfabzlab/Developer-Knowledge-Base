

# 03. Control Flow in C#

Control flow describes the order in which individual statements, instructions, or function calls are executed or evaluated. By default, code executes line-by-line from top to bottom, but control flow statements allow making decisions based on dynamic conditions.

---


## 1. Boolean Conditions & `if` Statements

An `if` statement executes a block of code only when a specified condition evaluates to `true`.


### Basic Syntax

```csharp
bool isConditionTrue = true;

if (isConditionTrue)
{
    Console.WriteLine("This code will execute.");
}
````


## 2. Comparison Operators

Comparison operators evaluate the relationship between two values and return a boolean result (`true` or `false`).

|**Operator**|**Description**|**Example (int x = 10)**|**Result**|
|---|---|---|---|
|`==`|Equal to|`x == 10`|`true`|
|`!=`|Not equal to|`x != 5`|`true`|
|`>`|Greater than|`x > 15`|`false`|
|`<`|Less than|`x < 20`|`true`|
|`>=`|Greater than or equal to|`x >= 10`|`true`|
|`<=`|Less than or equal to|`x <= 8`|`false`|



## 3. Branching with `else` and `else if`

When multiple potential paths exist, `else` and `else if` allow handling alternative conditions.

- **`else`**: Executes when all preceding `if` and `else if` conditions evaluate to `false`.
    
- **`else if`**: Evaluates sequential conditions top-to-bottom. Once a condition evaluates to `true`, its block executes and remaining conditions are skipped.
    


```csharp
int score = 85;

if (score >= 90)
{
    Console.WriteLine("Grade: A");
}
else if (score >= 80)
{
    Console.WriteLine("Grade: B");
}
else
{
    Console.WriteLine("Grade: C or lower");
}
```


## 4. Exercises

### Exercise 1: Weekend Plans

Introduction to simple boolean evaluation in control flow.


```csharp
using System;

class WeekendPlans
{
    static void Main()
    {
        bool rinkOpen = true;

        if (rinkOpen)
        {
            Console.WriteLine("Let's go skating, yippee!");
        }
    }
}
```

**Output:**


```text
Let's go skating, yippee!
```


### Exercise 2: The Reaper

Using comparison operators (`>=`) within an `if` statement.


```csharp
using System;

class TheReaper
{
    static void Main()
    {
        int spiceLevel = 7;

        if (spiceLevel >= 5)
        {
            Console.WriteLine("Ouch! My mouth is burning!");
        }
    }
}
```


**Output:**


```text
Ouch! My mouth is burning!
```


### Exercise 3: Plot Twist

Implementing binary conditional branching with `if` and `else`.


```csharp
using System;

class PlotTwist
{
    static void Main()
    {
        double compatibility = 0.85;

        if (compatibility > 0.75)
        {
            Console.WriteLine("Be vigilant. I love you. 💖");
        }
        else
        {
            Console.WriteLine("You're not a threat. You're just a man pretending to be one. ⚔️");
        }
    }
}
```


**Output:**


```text
Be vigilant. I love you. 💖
```


### Exercise 4: Basement Show

Handling multi-condition logic using `if`, `else if`, and `else`.


```csharp
using System;

class BasementShow
{
    static void Main()
    {
        int noiseLevel = 55;

        if (noiseLevel < 40)
        {
            Console.WriteLine("No complaints yet 🤫");
        }
        else if (noiseLevel <= 70)
        {
            Console.WriteLine("The neighbors are getting annoyed 🤨");
        }
        else
        {
            Console.WriteLine("We're gonna get shut down! 🚨");
        }
    }
}
```


**Output:**


```text
The neighbors are getting annoyed 🤨
```



---


## 5. Logical Operators

Logical operators allow combining multiple conditions within a single control flow evaluation.

| Operator | Name | Description | Example |
| :--- | :--- | :--- | :--- |
| `&&` | AND | Returns `true` only if **both** conditions evaluate to `true`. | `(age >= 21 && hasInvitation)` |
| `\|\|` | OR | Returns `true` if **at least one** condition evaluates to `true`. | `(isWeekend \|\| isHoliday)` |
| `!` | NOT | Reverses (flips) the boolean value of a condition. | `(!isLoggedIn)` |


---


## 6. Advanced Control Flow Exercises


### Exercise 5: Invite Only
Combining conditions using the logical AND (`&&`) operator.

```csharp
using System;

class InviteOnly
{
    static void Main()
    {
        int age = 22;
        bool hasInvitation = true;

        if (age > 21 && hasInvitation)
        {
            Console.WriteLine("Come on in!");
        }
        else
        {
            Console.WriteLine("Not tonight, buddy");
        }
    }
}
````


**Terminal Output:**


```text
Come on in!
```


### Exercise 6: Aura Checker

Combining user input parsing with conditional evaluations.


```csharp
using System;

class AuraChecker
{
    static void Main()
    {
        Console.Write("Enter a number from 1 to 10: ");
        int auraScore = Convert.ToInt32(Console.ReadLine());

        if (auraScore >= 8)
        {
            Console.WriteLine("Immaculate vibes ✨");
        }
        else
        {
            Console.WriteLine("I'm detecting some dark energy, but we can turn this around. 🔮");
        }
    }
}
```


**Terminal Output:**


```text
Enter a number from 1 to 10: 9
Immaculate vibes ✨
```


### Exercise 7: Love Hate Relationship

A complete program integrating user input, logical checks, and multi-branch control flow.


```csharp
using System;

class LoveHateRelationship
{
    static void Main()
    {
        Console.WriteLine("Do you prefer sweet or savory foods?");
        string answer = Console.ReadLine();

        if (answer == "sweet")
        {
            Console.WriteLine("THINGS YOU LOVE:");
            Console.WriteLine("1. Hot ramen on rainy days");
            Console.WriteLine("2. Clean code without bugs");
            Console.WriteLine("3. Quiet coffee shops");
            Console.WriteLine("4. Cozy mechanical keyboards");
        }
        else
        {
            Console.WriteLine("THINGS YOU HATE:");
            Console.WriteLine("1. Unhandled exceptions");
            Console.WriteLine("2. Slow Wi-Fi connections");
            Console.WriteLine("3. Unnecessary meetings");
            Console.WriteLine("4. Missing semicolons");
        }
    }
}
```


**Terminal Output:**


```text
Do you prefer sweet or savory foods?
sweet
THINGS YOU LOVE:
1. Hot ramen on rainy days
2. Clean code without bugs
3. Quiet coffee shops
4. Cozy mechanical keyboards
```