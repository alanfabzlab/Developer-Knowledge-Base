

# 03. Control Flow in C#

Control flow describes the order in which individual statements, instructions, or function calls are executed or evaluated. By default, code executes line-by-line from top to bottom, but control flow statements allow making decisions based on dynamic conditions.

---


## 1. Boolean Conditions & `if` Statements

An `if` statement executes a block of code only when a specified condition evaluates to `true`.


### Basic Syntax

```csharp
bool isGateOpen = true;

if (isGateOpen)
{
    Console.WriteLine("The party steps into the dungeon.");
}
```


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
    Console.WriteLine("Rank: Platinum");
}
else if (score >= 80)
{
    Console.WriteLine("Rank: Gold");
}
else
{
    Console.WriteLine("Rank: Silver or lower");
}
```


## 4. Exercises

### Exercise 1: Raid Night

Introduction to simple boolean evaluation in control flow.


```csharp
using System;

class RaidNight
{
    static void Main()
    {
        bool squadIsReady = true;

        if (squadIsReady)
        {
            Console.WriteLine("Let's queue for the raid, yippee!");
        }
    }
}
```

**Output:**


```text
Let's queue for the raid, yippee!
```


### Exercise 2: Aggro Meter

Using comparison operators (`>=`) within an `if` statement.


```csharp
using System;

class AggroMeter
{
    static void Main()
    {
        int aggroLevel = 7;

        if (aggroLevel >= 5)
        {
            Console.WriteLine("The whole zone is turning red!");
        }
    }
}
```


**Output:**


```text
The whole zone is turning red!
```


### Exercise 3: Critical Roll

Implementing binary conditional branching with `if` and `else`.


```csharp
using System;

class CriticalRoll
{
    static void Main()
    {
        double critChance = 0.85;

        if (critChance > 0.75)
        {
            Console.WriteLine("Critical hit! The enemy reels. 💥");
        }
        else
        {
            Console.WriteLine("Glancing blow. The enemy staggers. ⚔️");
        }
    }
}
```


**Output:**


```text
Critical hit! The enemy reels. 💥
```


### Exercise 4: Danger Level

Handling multi-condition logic using `if`, `else if`, and `else`.


```csharp
using System;

class DangerLevel
{
    static void Main()
    {
        int dangerLevel = 55;

        if (dangerLevel < 40)
        {
            Console.WriteLine("Quiet zone, nothing spawns yet 🤫");
        }
        else if (dangerLevel <= 70)
        {
            Console.WriteLine("Enemies are swarming the camp 🧟");
        }
        else
        {
            Console.WriteLine("We are about to get wiped out! 🚨");
        }
    }
}
```


**Output:**


```text
Enemies are swarming the camp 🧟
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


### Exercise 5: Guild Gate
Combining conditions using the logical AND (`&&`) operator.

```csharp
using System;

class GuildGate
{
    static void Main()
    {
        int playerLevel = 22;
        bool hasGuildPass = true;

        if (playerLevel > 21 && hasGuildPass)
        {
            Console.WriteLine("Welcome to the guild hall!");
        }
        else
        {
            Console.WriteLine("Come back when you are stronger, newbie");
        }
    }
}
```


**Terminal Output:**


```text
Welcome to the guild hall!
```


### Exercise 6: Rarity Pull

Combining user input parsing with conditional evaluations.


```csharp
using System;

class RarityPull
{
    static void Main()
    {
        Console.Write("Enter your rarity tier from 1 to 10: ");
        int rarityTier = Convert.ToInt32(Console.ReadLine());

        if (rarityTier >= 8)
        {
            Console.WriteLine("LEGENDARY DROP! The whole lobby is staring. ✨");
        }
        else
        {
            Console.WriteLine("Common trash... the summoning circle laughs at you. 🔮");
        }
    }
}
```


**Terminal Output:**


```text
Enter your rarity tier from 1 to 10: 9
LEGENDARY DROP! The whole lobby is staring. ✨
```


### Exercise 7: Buff or Debuff

A complete program integrating user input, logical checks, and multi-branch control flow.


```csharp
using System;

class BuffOrDebuff
{
    static void Main()
    {
        Console.Write("Do you wield a sword or a staff?");
        string answer = Console.ReadLine();

        if (answer == "sword")
        {
            Console.WriteLine("YOUR BUFFS:");
            Console.WriteLine("1. Crit damage on the final hit");
            Console.WriteLine("2. Frame-perfect parries");
            Console.WriteLine("3. Campfire resting bonuses");
            Console.WriteLine("4. A save point in every dungeon");
        }
        else
        {
            Console.WriteLine("YOUR DEBUFFS:");
            Console.WriteLine("1. Missing jump inputs");
            Console.WriteLine("2. Lag spikes on the final boss");
            Console.WriteLine("3. Grindy filler quests");
            Console.WriteLine("4. Soft-locked cutscenes");
        }
    }
}
```


**Terminal Output:**


```text
Do you wield a sword or a staff?
sword
YOUR BUFFS:
1. Crit damage on the final hit
2. Frame-perfect parries
3. Campfire resting bonuses
4. A save point in every dungeon
```
