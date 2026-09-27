
# 06. Métodos en C#

**Versión original en inglés:** [06 - Methods.md](06%20-%20Methods.md)

**Curso:** C#
**Tema:** Métodos, Parámetros y Valores de Retorno
**Etiquetas:** `#csharp` `#methods` `#functions`


Un método es un bloque de código reutilizable diseñado para realizar una tarea específica. Los métodos ayudan a organizar el código, evitar la duplicación y dividir los problemas complejos en piezas modulares.

---


## 1. Ejemplo de Procesamiento de Arreglos (Loot Hoarder)

Antes de crear métodos independientes, aquí se muestra cómo se combinan varios arreglos con bucles para procesar datos de forma dinámica.

```csharp
using System;

class LootHoarder
{
    static void Main()
    {
        string[] suministros = { "Pociónes de Salud", "Pociónes de Maná", "Elixires", "Antídotos", "Runas de Bomba" };
        int[] cantidades = { 12, 30, 8, 25, 16 };

        // Updating an inventory value directly via index
        cantidades[0] = 15;

        int totalSuministros = 0;

        for (int i = 0; i < suministros.Length; i++)
        {
            Console.WriteLine($"{suministros[i]} - {cantidades[i]}");
            totalSuministros += cantidades[i];
        }

        Console.WriteLine($"Suministros totales: {totalSuministros}");
    }
}
```


## 2. Declarar y Llamar Métodos

Todo ejecutable de C# comienza en el método `Main()`. Los métodos personalizados se definen fuera de `Main()` pero dentro del bloque de la clase.


```csharp
using System;

class LevelUpFanfare
{
    static void Main()
    {
        // Calling the custom method
        VictoryPose();
    }

    // Method declaration
    static void VictoryPose()
    {
        Console.WriteLine("¡El campeón levanta el trofeo!");
        Console.WriteLine("¡Victoria! 🏆");
    }
}
```


## 3. Reutilización de Métodos

Llamar a un método varias veces ejecuta su lógica encapsulada sin duplicar código.


```csharp
using System;

class CrowdChant
{
    static void Main()
    {
        // Calling Chant() 5 times
        Chant();
        Chant();
        Chant();
        Chant();
        Chant();
    }

    static void Chant()
    {
        Console.WriteLine("¡Canta conmigo!");
    }
}
```


## 4. Parámetros vs. Argumentos

Los métodos pueden aceptar datos externos para personalizar su ejecución usando parámetros.

### Definiciones

- **Parámetro:** La variable auxiliar definida en la firma del método (p. ej., `string elixir`).
    
- **Argumento:** El valor real que se pasa al método durante su llamada (p. ej., `"ember 🔥"`).
    


```csharp
using System;

class BuffMenu
{
    static void Main()
    {
        // "ember 🔥", "frost ❄️", and "lightning ⚡" are ARGUMENTS
        BrewElixir("ember 🔥");
        BrewElixir("frost ❄️");
        BrewElixir("lightning ⚡");
    }

    // 'elixir' is the PARAMETER
    static void BrewElixir(string elixir)
    {
        Console.WriteLine($"¡Preparando un {elixir} para todo el grupo!");
    }
}
```


## 5. Múltiples Parámetros

Los métodos pueden aceptar múltiples parámetros de distintos tipos de dato, separados por comas. Los argumentos suministrados en el punto de llamada deben coincidir con el tipo esperado y con el orden posicional.


```csharp
using System;

class PrizeSplit
{
    static void Main()
    {
        CalculateCost("Fortaleza Hundida", 150, 4, 4);
        CalculateCost("Cripta Sombría", 200, 3, 3);
    }

    static void CalculateCost(string nombreMazmorra, int oroPorPiso, int pisosSuperados, int tamañoGrupo)
    {
        int oroTotal = oroPorPiso * pisosSuperados;
        int oroPorHeroe = oroTotal / tamañoGrupo;

        Console.WriteLine($"Mazmorra: {nombreMazmorra}");
        Console.WriteLine($"Oro por héroe: ${oroPorHeroe}");
    }
}
```


## 6. Valores de Retorno

De forma predeterminada, los métodos marcados con `void` no devuelven ningún valor. Para enviar datos de vuelta al ámbito que llama, reemplaza `void` por el tipo de dato de retorno deseado (`int`, `string`, `bool`, etc.) y usa la palabra clave `return`.


```csharp
using System;

class QuestProgress
{
    static void Main()
    {
        int xpRestante = XpToNextLevel(35000, 50000);
        Console.WriteLine(xpRestante);
    }

    static int XpToNextLevel(int xpActual, int xpParaSiguienteNivel)
    {
        return xpParaSiguienteNivel - xpActual;
    }
}
```


## 7. Composición Modular (Calling All Raiders)

Dividir las aplicaciones complejas en métodos especializados mejora la mantenibilidad y la testeabilidad del código.


```csharp
using System;

class CallingAllRaiders
{
    static void Main()
    {
        int escuadrones = CalculateSquads(36, 6);
        int horas = CalculateHours(12, 18);
        string informe = CreateBriefing("Asedio del Dragón", escuadrones, horas);

        Console.WriteLine(informe);
    }

    static int CalculateSquads(int incursores, int tamañoEscuadra)
    {
        return incursores / tamañoEscuadra;
    }

    static int CalculateHours(int horaInicio, int horaFin)
    {
        return horaFin - horaInicio;
    }

    static string CreateBriefing(string nombreEvento, int escuadrones, int horas)
    {
        return $"{nombreEvento} empieza a las 6 PM!\n¡Incursionaremos durante {horas} horas con {escuadrones} escuadrones. ¡Nos vemos en la puerta!";
    }
}
```
