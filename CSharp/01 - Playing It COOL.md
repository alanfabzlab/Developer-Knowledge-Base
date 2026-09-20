
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