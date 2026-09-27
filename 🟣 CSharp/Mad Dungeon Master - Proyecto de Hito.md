


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
        bool seguirEjecutando = true;

        while (seguirEjecutando)
        {
            Console.Clear();
            Console.WriteLine("👹 ¡Bienvenido a Mad Dungeon Master! ⚔️\n");

            Console.Write("Introduce el nombre del jefe: ");
            string nombreJefe = Console.ReadLine();

            Console.Write("Introduce un crimen oscuro: ");
            string crimenOscuro = Console.ReadLine();

            Console.Write("Introduce un adjetivo: ");
            string adjetivo = Console.ReadLine();

            Console.Write("Introduce el arma del héroe: ");
            string armaHeroe = Console.ReadLine();

            Console.Write("Introduce el nombre de la mazmorra: ");
            string lugar = Console.ReadLine();

            Console.Write("Introduce una hora del día (p. ej., noche, mañana): ");
            string horaDelDia = Console.ReadLine();

            Console.WriteLine("\n✨ Generando tu Guion de Jefe ✨\n");

            Console.WriteLine($"¡Oid, viajeros de {lugar}!");
            Console.WriteLine($"Soy {nombreJefe}, y con {crimenOscuro} destruiré tus esperanzas.");
            Console.WriteLine($"Inclínate ante mi corona {adjetivo},");
            Console.WriteLine($"mientras tu {armaHeroe} yace hecho pedazos a mis pies.");

            if (horaDelDia.ToLower() == "noche" || horaDelDia.ToLower() == "medianoche")
            {
                Console.WriteLine($"Cuando las lunas gemelas se alcen, mi reinado comienza en la {horaDelDia}.");
            }
            else if (horaDelDia.ToLower() == "mañana" && adjetivo.ToLower() != "oscuro")
            {
                Console.WriteLine($"¡Buenos días, héroe! Ni siquiera a esta {horaDelDia} puedes superarme.");
            }
            else
            {
                Console.WriteLine($"Sea cual sea la hora, la {horaDelDia} no te salvará de mi fase tres.");
            }

            Console.WriteLine("\n⚔️ ¡Tu guion de jefe está completo y listo para la arena!");

            Console.Write("\n¿Quieres forjar otro enfrentamiento? (y/n): ");
            string respuesta = Console.ReadLine().ToLower();

            if (respuesta != "y" && respuesta != "sí")
            {
                seguirEjecutando = false;
                Console.WriteLine("\n¡Gracias por usar Mad Dungeon Master! 🚀");
            }
        }
    }
}
```
