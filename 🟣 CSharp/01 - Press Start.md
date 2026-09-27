
# 01. Press Start

> [!INFO] Metadata
> **Course:** C#
> **Topic:** Environment Setup, IDE Configuration & First Program
> **Tags:** `#csharp` `#setup` `#fundamentals`



## 1. Introduction to C#

C# (pronounced "C sharp") was created in 1999 at Microsoft during the development of the .NET Framework. It was originally named **COOL** (*C-like Object Oriented Language*), but that name was scrapped due to trademark issues.

It is a simple, general-purpose, object-oriented programming language that uses the `.cs` file extension.


### Core Applications
* **Game Development** (Unity Engine, Godot with C# bindings)
* **Multiplayer Services** (leaderboards, matchmaking, and inventory APIs)
* **Desktop Tools & Game Launchers**
* **Cloud Computing**

---


## 2. Program Structure

Every standard C# console application follows a foundational boilerplate structure:

CSharp

```csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, Champion!");
    }
}
```


### Components Breakdown

- **`using System;`**: Grants access to built-in namespaces and system utility methods provided by C#.
    
- **`class Program`**: Organizes code inside a class container. Every console program requires at least one class wrapper.
    
- **`static void Main()`**: The primary entry point where program execution begins top-to-bottom.
    
- **`Console.WriteLine()`**: Standard method to output text to the console window followed by a line break.
    
- **`;` (Semicolon)**: Required standard statement terminator in C#.
    


## 3. Practice Exercises


### Exercise 1: Boot Sequence

Writing the basic structure to print a welcome message when the game starts.


```csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Welcome to the Realm!");
    }
}
```

**Terminal Output:**


```text
Welcome to the Realm!
```

### Exercise 2: Hero Profile

Printing character details using string output in `Console.WriteLine()`.


```csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Aria - Half-Elf Ranger");
    }
}
```


**Terminal Output:**


```text
Aria - Half-Elf Ranger
```


### Exercise 3: Quest Log

Printing multi-line structured text using consecutive output statements.


```csharp
using System;

class QuestLog
{
    static void Main()
    {
        Console.WriteLine("Quest Log - Day 27 of Emberfall");
        Console.WriteLine("-------------------------------");
        Console.WriteLine("A floating citadel rose above the Glass Sea.");
        Console.WriteLine("Its towers were forged from crystal and storm.");
        Console.WriteLine("I found a sealed gate behind the moon fountain.");
        Console.WriteLine("Before I could reach the boss room, I got disconnected.");
    }
}
```


**Terminal Output:**


```text
Quest Log - Day 27 of Emberfall
-------------------------------
A floating citadel rose above the Glass Sea.
Its towers were forged from crystal and storm.
I found a sealed gate behind the moon fountain.
Before I could reach the boss room, I got disconnected.
```



## 4. Comments in C#

Comments are notes written in code that the compiler completely ignores. They help explain logic for developers.

* **Single-line Comments**: Start with two forward slashes (`//`).
* **Multi-line Comments**: Enclosed between `/*` and `*/`.

---


## 5. Additional Practice Exercises


### Exercise 4: Nerdy Rant
Using single-line and multi-line comments to document a game design opinion and its reasoning.

```csharp
using System;

class NerdyRant
{
    static void Main()
    {
        /* Boss rush mode is the purest expression of skill.
           You only bring one build, so you better know it! */
        // I think the hardest difficulty should unlock after your first clear.
    }
}
```


**Terminal Output:**

_(Note: Comments produce no output in the terminal.)_


### Exercise 5: Recruitment Poster

Creating a personal guild advertisement using comments and structured `Console.WriteLine()` statements.


```csharp
using System;

class RecruitmentPoster
{
    static void Main()
    {
        /* 
        Recruitment poster for a gaming guild
        I wanna find my dream party
        So I made this poster!
        */

        // Headline to grab attention
        Console.WriteLine("JOIN MY GUILD! 🤝");

        // Introduce yourself
        Console.WriteLine("Hi, I'm Aria!");

        // State your interest
        Console.WriteLine("I love game design and level building.");

        // Favorite pastime
        Console.WriteLine("I enjoy speedrunning Hollow Knight and modding classic games.");

        // Call to action
        Console.WriteLine("Let's squad up and build cool worlds together! 🚀");
    }
}
```


**Terminal Output:**


```text
JOIN MY GUILD! 🤝
Hi, I'm Aria!
I love game design and level building.
I enjoy speedrunning Hollow Knight and modding classic games.
Let's squad up and build cool worlds together! 🚀
```
