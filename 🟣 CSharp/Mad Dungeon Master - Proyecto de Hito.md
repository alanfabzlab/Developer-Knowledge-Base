


# Proyecto de Hito: Mad Dungeon Master 👹

**Versión original en inglés:** [Mad Dungeon Master - Checkpoint Project.md](Mad%20Dungeon%20Master%20-%20Checkpoint%20Project.md)

**Curso:** C#
**Tema:** Proyecto de Hito: Generador de Guiones de Jefes
**Etiquetas:** `#csharp` `#checkpoint` `#console-app`


- **Lenguaje:** C# / .NET
- **Conceptos Aplicados:** `Console.ReadLine()`, interpolación y concatenación de cadenas, sentencias condicionales (`if/else`), operadores lógicos (`&&`, `||`), operadores relacionales (`==`, `!=`), bucles `while`.
- **Repositorio:** [MadDungeonMaster en GitHub](https://github.com/alanfabzlab/MadDungeonMaster)


---


## 📋 Descripción General del Proyecto
Una aplicación de consola interactiva basada en texto que pide al usuario distintas entradas para el enfrentamiento (nombre del jefe, crimen oscuro, adjetivo, arma del héroe, mazmorra, hora del día) y construye dinámicamente un monólogo de villano personalizado para un combate contra un jefe. Usa lógica condicional para alterar las líneas finales según la hora elegida y se ejecuta dentro de un bucle `while` principal para permitir partidas continuas.


## 🛠️ Código Fuente (`Program.cs`)

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
