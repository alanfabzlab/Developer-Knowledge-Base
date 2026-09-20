
# 01. Playing It COOL


## 1. Introduction to C#

C# (pronounced "C sharp") was created in 1999 at Microsoft during the development of the .NET Framework. It was originally named **COOL** (*C-like Object Oriented Language*), but that name was scrapped due to trademark issues.

It is a simple, general-purpose, object-oriented programming language that uses the `.cs` file extension.


### Core Applications
* **Game Development** (Unity Engine)
* **Web APIs**
* **Desktop Applications**
* **Cloud Computing**

---


## 2. Program Structure

Every standard C# console application follows a foundational boilerplate structure:

```csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, World!");
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


### Exercise 1: First Execution

Writing the basic structure to print a welcome message.


```csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Welcome to C#!");
    }
}
```

**Terminal Output:**


```text
Welcome to C#!
```

### Exercise 2: Name & Meaning

Printing personal details using string output in `Console.WriteLine()`.


```csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Alan - Handsome or Little Rock");
    }
}
```


**Terminal Output:**


```text
Alan - Handsome or Little Rock
```


### Exercise 3: Dream Journal

Printing multi-line structured text using consecutive output statements.


```csharp
using System;

class DreamJournal
{
    static void Main()
    {
        Console.WriteLine("Dream Journal - September 20th");
        Console.WriteLine("-----------------------------");
        Console.WriteLine("I was exploring a vast floating city in the sky.");
        Console.WriteLine("The buildings were made of crystal and light.");
        Console.WriteLine("I found a hidden portal behind a waterfall.");
        Console.WriteLine("Before I could step inside, I woke up.");
    }
}
```


**Terminal Output:**


```text
Dream Journal - September 20th
-----------------------------
I was exploring a vast floating city in the sky.
The buildings were made of crystal and light.
I found a hidden portal behind a waterfall.
Before I could step inside, I woke up.
```



## 4. Comments in C#

Comments are notes written in code that the compiler completely ignores. They help explain logic for developers.

* **Single-line Comments**: Start with two forward slashes (`//`).
* **Multi-line Comments**: Enclosed between `/*` and `*/`.

---


## 5. Additional Practice Exercises


### Exercise 4: Hot Take
Using single-line and multi-line comments to document an opinion and its reasoning.

```csharp
using System;

class HotTake
{
    static void Main()
    {
        /* Cowboy boots are stylish and comfy.
           You gotta be ready for anything, partner! */
        // I think more people should wear cowboy boots on a daily basis.
    }
}
```


**Terminal Output:**

_(Note: Comments produce no output in the terminal.)_


### Exercise 5: Personal Billboard

Creating a personal advertisement using comments and structured `Console.WriteLine()` statements.


```csharp
using System;

class PersonalBillboard
{
    static void Main()
    {
        /* 
        Personal billboard for friendship
        I wanna make new friends
        So I made this billboard!
        */

        // Headline to grab attention
        Console.WriteLine("BE MY FRIEND! 🤝");

        // Introduce yourself
        Console.WriteLine("Hi, I'm Alan!");

        // State your interest
        Console.WriteLine("I love video game development and coding.");

        // Favorite pastime
        Console.WriteLine("I enjoy playing League of Legends and building projects.");

        // Call to action
        Console.WriteLine("Let's connect and build cool stuff together! 🚀");
    }
}
```


**Terminal Output:**


```text
BE MY FRIEND! 🤝
Hi, I'm Alan!
I love video game development and coding.
I enjoy playing League of Legends and building projects.
Let's connect and build cool stuff together! 🚀
```