

# Checkpoint Project: Mad Dungeon Master 👹

**Course:** C#
**Topic:** Checkpoint Project: Boss Script Generator
**Tags:** `#csharp` `#checkpoint` `#console-app`


- **Language:** C# / .NET
- **Concepts Applied:** `Console.ReadLine()`, string interpolation and concatenation, conditional statements (`if/else`), logical operators (`&&`, `||`), relational operators (`==`, `!=`), `while` loops.
- **Repository:** [MadDungeonMaster on GitHub](git@github.com:alanfabzlab/MadDungeonMaster.git)


---


## 📋 Project Overview
An interactive text-based console application that prompts the user for various encounter inputs (boss name, dark deed, adjective, hero weapon, dungeon, time of day) and dynamically builds a personalized villain monologue for a boss fight. It uses conditional logic to alter the final lines based on the chosen hour and runs inside a main `while` loop to support continuous playthroughs.


## 🛠️ Source Code (`Program.cs`)

```csharp
using System;

class MadDungeonMaster
{
    static void Main(string[] args)
    {
        bool keepRunning = true;

        while (keepRunning)
        {
            Console.Clear();
            Console.WriteLine("👹 Welcome to Mad Dungeon Master! ⚔️\n");

            Console.Write("Enter a boss name: ");
            string bossName = Console.ReadLine();

            Console.Write("Enter a dark deed: ");
            string darkDeed = Console.ReadLine();

            Console.Write("Enter an adjective: ");
            string adjective = Console.ReadLine();

            Console.Write("Enter a hero weapon: ");
            string heroWeapon = Console.ReadLine();

            Console.Write("Enter a dungeon name: ");
            string place = Console.ReadLine();

            Console.Write("Enter a time of day (e.g. night, morning): ");
            string timeOfDay = Console.ReadLine();

            Console.WriteLine("\n✨ Generating Your Boss Script ✨\n");

            Console.WriteLine($"Hear ye, travelers of {place}!");
            Console.WriteLine($"I am {bossName}, and I will {darkDeed} your hopes.");
            Console.WriteLine($"Bow before my {adjective} crown,");
            Console.WriteLine($"while your {heroWeapon} lies shattered at my feet.");

            if (timeOfDay.ToLower() == "night" || timeOfDay.ToLower() == "midnight")
            {
                Console.WriteLine($"When the twin moons rise, my reign begins at the {timeOfDay}.");
            }
            else if (timeOfDay.ToLower() == "morning" && adjective.ToLower() != "dark")
            {
                Console.WriteLine($"Good morning, hero! Even at this {timeOfDay}, you cannot outlevel me.");
            }
            else
            {
                Console.WriteLine($"Whatever the hour, the {timeOfDay} will not save you from my phase three.");
            }

            Console.WriteLine("\n⚔️ Your boss script is complete and ready for the arena!");

            Console.Write("\nWould you like to forge another encounter? (y/n): ");
            string response = Console.ReadLine().ToLower();

            if (response != "y" && response != "yes")
            {
                keepRunning = false;
                Console.WriteLine("\nThanks for using Mad Dungeon Master! 🚀");
            }
        }
    }
}
```
