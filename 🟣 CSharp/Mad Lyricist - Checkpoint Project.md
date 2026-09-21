

# Checkpoint Project: Mad Lyricist 🎤

- **Language:** C# / .NET
- **Concepts Applied:** `Console.ReadLine()`, string interpolation and concatenation, conditional statements (`if/else`), logical operators (`&&`, `||`), relational operators (`==`, `!=`), `while` loops.
- **Repository:** [MadLyricist on GitHub](https://github.com/alanfabzlab/MadLyricist)


---


## 📋 Project Overview
An interactive text-based console application that prompts the user for various grammatical inputs (noun, verb, adjective, object, place, time of day) and dynamically constructs a personalized song inspired by classic themes. It uses conditional logic to alter stanzas based on user inputs and runs inside a main `while` loop to support continuous playthroughs.


## 🛠️ Source Code (`Program.cs`)

```csharp
using System;

class MadLyricist
{
    static void Main(string[] args)
    {
        bool keepRunning = true;

        while (keepRunning)
        {
            Console.Clear();
            Console.WriteLine("🎤 Welcome to Mad Lyricist! 🎶\n");

            Console.Write("Enter a noun: ");
            string noun = Console.ReadLine();

            Console.Write("Enter a verb: ");
            string verb = Console.ReadLine();

            Console.Write("Enter an adjective: ");
            string adjective = Console.ReadLine();

            Console.Write("Enter an object: ");
            string objectItem = Console.ReadLine();

            Console.Write("Enter a place: ");
            string place = Console.ReadLine();

            Console.Write("Enter a time of day (e.g. night, morning): ");
            string timeOfDay = Console.ReadLine();

            Console.WriteLine("\n✨ Generating Your Song ✨\n");

            Console.WriteLine($"Twinkle, twinkle, little {noun},");
            Console.WriteLine($"How I {verb} what you are.");
            Console.WriteLine($"Up above the sky so {adjective},");
            Console.WriteLine($"Like a {objectItem} in the {place}.");

            if (timeOfDay.ToLower() == "night" || timeOfDay.ToLower() == "midnight")
            {
                Console.WriteLine($"When the blazing sun is gone, you shine bright until the {timeOfDay}.");
            }
            else if (timeOfDay.ToLower() == "morning" && adjective.ToLower() != "dark")
            {
                Console.WriteLine($"Good morning! Even in the early {timeOfDay}, you sparkle above.");
            }
            else
            {
                Console.WriteLine($"Whatever time of day, during the {timeOfDay}, your energy holds true.");
            }

            Console.WriteLine("\n🎶 Your lyrics are complete and ready for the charts!");

            Console.Write("\nWould you like to create another song? (y/n): ");
            string response = Console.ReadLine().ToLower();

            if (response != "y" && response != "yes")
            {
                keepRunning = false;
                Console.WriteLine("\nThanks for using Mad Lyricist! 🚀");
            }
        }
    }
}
````