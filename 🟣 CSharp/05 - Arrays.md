
# 05. Arrays in C#

An array is a fixed-size collection of elements of the same data type stored in contiguous memory positions.

---

## 1. Array Declaration & Initialization

Arrays are declared by specifying the data type followed by square brackets `[]`. Values are enclosed in curly braces `{}` and separated by commas.


### Key Characteristics
- **Fixed Size:** The number of elements is determined upon creation.
- **Type Safety:** All elements must match the declared data type.

```csharp
using System;

class ArrayFoundations
{
    static void Main()
    {
        // String array containing movie titles
        string[] movies = { "Interstellar", "Inception", "The Dark Knight", "Oppenheimer" };

        // Integer array containing corresponding ratings
        int[] ratings = { 10, 9, 9, 10 };
    }
}
````


## 2. Zero-Based Indexing

Elements inside an array are accessed using their numerical position (index) within square brackets `[index]`. C# arrays use zero-based indexing, meaning the first element is at index `0`.


```csharp
using System;

class Soundtracks
{
    static void Main()
    {
        string[] songs = 
        {
            "Starlight",
            "Midnight City",
            "Resonance",
            "Time",
            "Veridis Quo"
        };

        Console.WriteLine("Driving Scene:");
        Console.WriteLine(songs[0]); // Output: Starlight

        Console.WriteLine("Sad Scene:");
        Console.WriteLine(songs[2]); // Output: Resonance

        Console.WriteLine("Closing Credits:");
        Console.WriteLine(songs[4]); // Output: Veridis Quo
    }
}
```


## 3. Modifying Array Elements

Array elements can be updated after initialization by reassigning a new value directly to a specific index position.


```csharp
using System;

class LocalRecommendations
{
    static void Main()
    {
        string[] recommendations = { "Visit Palace of Fine Arts", "Eat Tacos", "Visit Frida Kahlo Museum" };

        // Update element at index 1
        recommendations[1] = "Eat Churros at El Moro";

        Console.WriteLine(recommendations[1]); // Output: Eat Churros at El Moro
    }
}
```
