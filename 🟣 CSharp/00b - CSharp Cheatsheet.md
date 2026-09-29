
# C# Cheatsheet

**Spanish version:** [00b - Chuleta de CSharp.md](00b%20-%20Chuleta%20de%20CSharp.md)

**Course:** C#
**Topic:** Type System, Value vs Reference Types, Stack vs Heap, Syntax & Core Gotchas
**Tags:** `#csharp` `#cheatsheet` `#types` `#syntax` `#reference`

Quick reference for C# syntax and the type-system rules that trip up newcomers, using video game data as running examples.

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #512BD4, #B39DFF, #512BD4, transparent); margin: 24px 0;" />

## 🔹 Program Skeleton

CSharp

```csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Press Start");
    }
}
```

**Terminal Output:**

```text
Press Start
```

C# 10+ also accepts **top-level statements** — no class, no `Main`, the compiler generates the wrapper:

```csharp
Console.WriteLine("Press Start");
```

Only one file per project may use them, and you cannot mix them with an explicit `Program` class.

## 🔹 Comments

```csharp
// Single-line comment

/* Block comment
   spanning several lines */

/// <summary>XML doc comment that IntelliSense picks up.</summary>
```

## 🔹 Variables, `var` and `const`

```csharp
int controllers = 2;           // type is mandatory in C#
string currentClass = "Paladin";
double critChance = 0.25;
bool isHeadsetOn = true;

var playtime = 2041;           // inferred as int
const int MaxPartySize = 4;    // compile-time constant, cannot be reassigned
```

`var` is still **static typing**: the compiler fixes the type at compile time from the initializer, it is not JavaScript. It needs an initial value, and you cannot later assign a `string` to it.

## 🔹 Primitive Data Types

| Type | Size | Range / Precision | Typical game use |
| --- | --- | --- | --- |
| `bool` | 1 byte | `true` / `false` | `isInvincible` |
| `char` | 2 bytes | One Unicode character | `'A'` |
| `byte` | 1 byte | 0 to 255 | Colour channels, flags |
| `short` | 2 bytes | -32,768 to 32,767 | Small counters |
| `int` | 4 bytes | ±2.1 billion | **Default choice** for counters and damage |
| `long` | 8 bytes | ±9.2 quintillion | Timestamps, large currency |
| `float` | 4 bytes | ~7 significant digits | Positions — cheap for the GPU |
| `double` | 8 bytes | ~15-16 significant digits | **Default choice** for decimals |
| `decimal` | 16 bytes | 28-29 digits, exact base 10 | Money, never use `double` for gold |
| `string` | reference | Immutable text | Names, dialogue, item ids |

Every numeric type has an unsigned twin (`uint`, `ulong`, `byte`...). Underscores are allowed in literals for readability: `2_048` is `2048`.

## 🔹 Value Types vs Reference Types

This is the single most important rule in the language.

| | Value type | Reference type |
| --- | --- | --- |
| Examples | `int`, `double`, `bool`, `char`, `struct`, `enum` | `string`, `class`, `array`, `delegate`, `interface` |
| Lives on | The **stack** — fast, freed when the scope ends | The **heap** — managed by the garbage collector |
| Assignment | Copies the **value** | Copies the **reference** (the address) |
| Default when unassigned | `0`, `false` | `null` |
| Nullable form | `int?` | `string?` |
| `==` compares | The contents | The reference identity (`string` is the exception) |

**Value types duplicate. Reference types share.** A `struct` behaves like an `int`; a `class` behaves like a handle.

CSharp

```csharp
using System;

class Program
{
    static void Main()
    {
        int swordDamage = 25;
        int axeDamage = swordDamage;  // copies the value

        axeDamage = 60;

        Console.WriteLine(swordDamage);  // 25 — untouched
        Console.WriteLine(axeDamage);    // 60
    }
}
```

**Terminal Output:**

```text
25
60
```

Swap `int` for a class and the same three lines mutate one single object:

CSharp

```csharp
using System;

class Damage
{
    public int Amount;
}

class Program
{
    static void Main()
    {
        Damage sword = new Damage { Amount = 25 };
        Damage axe = sword;  // copies the reference, not the object

        axe.Amount = 60;

        Console.WriteLine(sword.Amount);  // 60 — two names, one object
        Console.WriteLine(axe.Amount);    // 60
    }
}
```

**Terminal Output:**

```text
60
60
```

Declare the same class as a `struct` and it prints `25` / `60` again, because structs are copied on assignment.

## 🔹 Nullables & Null Safety

```csharp
int? bonusDamage = null;      // a value type that admits null
string? playerTag = null;     // reference type, needs <Nullable>enable</Nullable>

playerTag ??= "@nightowl";            // assigns only while null → "@nightowl"
int total = (bonusDamage ?? 0) + 25;  // 25 — ?? falls through to the right side

Console.WriteLine(playerTag.Length);        // throws if playerTag is null
Console.WriteLine(playerTag?.Length);       // 9 — short-circuits to null instead of throwing
Console.WriteLine(playerTag?.Length ?? 0);  // 9 — the 0 only shows up when it really is null

if (bonusDamage is not null) { /* ... */ }
```

## 🔹 Operators

```csharp
// Arithmetic
int dealt = 23 + 18;         // 41
int left = 30 - 8;           // 22
float scaled = 10 * 2.5f;    // 25
int waves = 76 % 4;          // 0  — modulo, same as Python
int xor = 2 ^ 3;             // 1  — bitwise XOR, NOT power
double power = Math.Pow(2, 3);  // 8 — this is the power

// Division
int truncated = 23 / 2;      // 11 — integer division truncates
double precise = 23 / 2.0;   // 11.5

// Compound assignment
int kills = 0;
kills++;      // 1
kills += 5;   // 6
kills *= 2;   // 12

// Relational
a == b   // Equal to
a != b   // Not equal to
a > b    // Greater than
a < b    // Less than
a >= b   // Greater than or equal to
a <= b   // Less than or equal to

// Logical
a && b   // And — both must be true
a || b   // Or — at least one must be true
!a       // Not

// Ternary
string status = hp > 0 ? "Alive" : "Down";
```

## 🔹 Strings & Interpolation

```csharp
string hero = "Aria";

Console.WriteLine($"Welcome, {hero}! You are level {12}.");
Console.WriteLine($"Boss in {90.0 / 60:0.0} min");   // 1.5 — format specifier
Console.WriteLine($"Crit: {0.25:P0}");               // 25%
Console.WriteLine($"Pad: {42,5}|");                  // right aligned, width 5
Console.WriteLine($"Hex: {255:X}");                  // FF

string path = @"C:\Games\Emberfall\saves";  // verbatim: backslashes stay literal
string quote = "She said \"run\".";
int length = hero.Length;                   // 4
string[] words = hero.Split(' ');           // ["Aria"]
string upper = hero.ToUpper();              // ARIA
```

Strings are **immutable**. `hero[0] = 'b';` does not compile — build a new string and reassign.

## 🔹 Arrays & `foreach`

```csharp
string[] loadout = { "Sword", "Shield", "Potion", "Rune" };

Console.WriteLine(loadout.Length);   // 4
Console.WriteLine(loadout[0]);        // Sword
Console.WriteLine(loadout[^1]);       // Potion — index from the end (C# 8+)

foreach (string item in loadout)
{
    Console.WriteLine(item);
}

int[] scores = { 42, 7, 91, 25 };
Array.Sort(scores);
int best = scores[^1];                       // 91
int position = Array.IndexOf(scores, 42);    // 2
int[] copy = (int[])scores.Clone();          // real copy, not a shared reference

int[] empty = new int[3];        // three zeros
int[] grid = new int[2, 2];      // rectangular: 2 rows x 2 columns
grid[1, 1] = 25;
```

Array size cannot change after creation. That is what `List<T>` is for.

## 🔹 Lists

```csharp
using System.Collections.Generic;

List<string> party = new List<string> { "Aria", "Kai", "Nyx" };

party.Add("Borin");          // append
party.Remove("Kai");         // remove by value
party.Insert(0, "Leader");   // insert at an index
bool present = party.Contains("Nyx");  // true
int size = party.Count;                // 4 — Count, not Length
string first = party[0];               // Leader
string last = party[^1];               // Borin
party.Sort();
party.Clear();
```

## 🔹 Control Flow

```csharp
if (hp > 50)
{
    Console.WriteLine("Healthy");
}
else if (hp > 20)
{
    Console.WriteLine("Wounded");
}
else
{
    Console.WriteLine("Critical");
}
```

A `switch` **expression** replaces most `switch` statements (C# 9+ relational patterns):

```csharp
string rank = score switch
{
    >= 90 => "S",
    >= 80 => "A",
    >= 70 => "B",
    _ => "C"
};
```

The classic `switch` **statement** still exists and needs a `break` per case:

```csharp
switch (element)
{
    case "fire":
        damage = 30;
        break;
    default:
        damage = 10;
        break;
}
```

## 🔹 Loops

```csharp
string[] wave = { "Goblin", "Ogre", "Wraith" };

for (int round = 1; round <= 3; round++) { }

int attempts = 0;
while (attempts < 3) { attempts++; }

do { } while (attempts > 0);   // runs at least once

foreach (string enemy in wave) { }

break;      // leave the loop entirely
continue;   // jump to the next iteration
```

## 🔹 Methods

```csharp
using System;

class Combat
{
    static int ApplyDamage(int hp, int incoming)  // returns a value
    {
        return hp - incoming;
    }

    static bool IsAlive(int hp) => hp > 0;        // expression-bodied

    static int Roll(int sides = 20)               // default parameter
    {
        return Random.Shared.Next(1, sides + 1);
    }

    // out: returns a success flag and writes the parsed value
    static bool TryGetSlot(string input, out int slot)
    {
        return int.TryParse(input, out slot);
    }

    // params: accepts any number of arguments
    static int Total(params int[] values)
    {
        int sum = 0;
        foreach (int v in values) { sum += v; }
        return sum;
    }

    static void Main()
    {
        Console.WriteLine(ApplyDamage(100, 35));  // 65
        Console.WriteLine(IsAlive(0));            // False
        Console.WriteLine(Total(1, 2, 3, 4));      // 10
    }
}
```

## 🔹 Random

```csharp
using System;

// .NET 6+ — shared, thread-safe, no allocation
int d20 = Random.Shared.Next(1, 21);       // 1 to 20 — upper bound is EXCLUSIVE
int any = Random.Shared.Next();            // 0 to int.MaxValue
double pct = Random.Shared.NextDouble();   // 0.0 to 1.0
bool crit = Random.Shared.NextDouble() < 0.25;

// Older style — one instance, reused
var rng = new Random();
int lootTier = rng.Next(0, 4);            // 0, 1, 2 or 3
```

## 🔹 Common Gotchas

| Gotcha | What actually happens | Fix |
| --- | --- | --- |
| `int a = 23 / 2;` | `11`, not `11.5` — integer division truncates | write `23 / 2.0` |
| `0.1 + 0.2 == 0.3` | `false` — binary floats cannot hold these exactly | use `decimal` for gold |
| `s[0] = 'b';` on a `string` | Compile error — strings are immutable | reassign `s`, or use `StringBuilder` |
| `if (someInt == null)` | Warning CS0472 — a non-nullable `int` is never `null` | declare it `int?` |
| Two variables of a class type | Mutating one is visible through the other | `.Clone()` or copy the fields |
| `int.MaxValue + 1` | Silently wraps to `int.MinValue` — unchecked is the default | wrap it in `checked { }` |
| `Convert.ToInt32("abc")` | Throws `FormatException` | use `int.TryParse` |
| `foreach` over a `null` list | `NullReferenceException` | null-check before iterating |
| Forgetting `using System;` | `Console` does not resolve | add the `using` |

## 🔹 Coming From Python

| Python | C# |
| --- | --- |
| `print(x)` | `Console.WriteLine(x)` |
| `input("Name? ")` | `Console.Write("Name? ")` then `Console.ReadLine()` |
| `int(x)` / `str(x)` | `Convert.ToInt32(x)` / `x.ToString()` |
| `True` / `False` / `None` | `true` / `false` / `null` |
| `len(s)` / `len(a)` / `len(lst)` | `s.Length` / `a.Length` / `lst.Count` |
| `for i in range(n)` | `for (int i = 0; i < n; i++)` |
| `a ** b` | `Math.Pow(a, b)` |
| `a % b` | `a % b` — identical |
| `f"{x}"` | `$"{x}"` |
| `list` / `dict` | `List<T>` / `Dictionary<K, V>` |
| `# comment` | `// comment` — and `/* block */` also works |
| `"12"` -> `int` | `int.Parse(s)` or `int.TryParse(s, out int n)` |
| `len(x) == 0` on a list | `list.Count == 0` |
| `//` (floor division) | `23 / 2` gives `11` — C# has no `//` operator |

## 🔹 Useful Constants

```csharp
int.MaxValue        // 2147483647
int.MinValue        // -2147483648
long.MaxValue       // 9223372036854775807
double.NaN          // not a number — NaN != NaN, so compare with double.IsNaN
double.PositiveInfinity
double.Epsilon      // smallest positive double, about 4.9e-324
char.MaxValue       // the largest character, U+FFFF
```

## 🔹 One-Page Recall

- Every statement ends with `;` and every block with braces `{}`.
- Types are explicit unless you write `var` — and `var` is still compile-time typed.
- `struct` copies, `class` shares. This is the bug behind most "I changed it and it changed over there" moments.
- Value types default to `0`/`false`, reference types to `null`.
- `Next(a, b)` excludes `b`.
- `int / int` is integer division. Almost always a bug in game maths.
- `string` is a reference type, but immutable, and `==` compares its contents.
