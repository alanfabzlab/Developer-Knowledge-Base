


# 04. Bucles en C#

**Versión original en inglés:** [04 - Loops.md](04%20-%20Loops.md)

**Curso:** C#
**Tema:** Estructuras de Bucle
**Etiquetas:** `#csharp` `#loops` `#iteration`


Los bucles son estructuras de control de flujo que se usan para repetir un bloque de código varias veces según una condición especificada. En lugar de duplicar manualmente las sentencias, los bucles automatizan los ciclos de ejecución.


---


## 1. Visión General de Tipos de Bucle

C# utiliza principalmente dos estructuras de bucle principales:
- **Bucle `while`**: Se ejecuta mientras su condición siga siendo `true`.
- **Bucle `for`**: Se ejecuta un número fijo de veces usando una variable de contador explícita.


---


## 2. El Bucle `while`

Un bucle `while` evalúa una condición **antes** de cada iteración. Si la condición evalúa a `true`, se ejecuta el cuerpo; si evalúa a `false`, la ejecución se detiene y pasa más allá del bloque del bucle.


### Sintaxis

```csharp
while (condition)
{
    // Code block to repeat
}
```


## 3. Ejercicios


### Ejercicio 1: Pelea con Goblins

Demostrar un bucle `while` interactivo controlado por la entrada del usuario hasta que se encuentre una palabra clave de salida específica ("retreat").


```csharp
using System;

class GoblinBrawl
{
    static void Main()
    {
        Console.WriteLine("Goblin incoming! 🧌");
        string input = Console.ReadLine();

        while (input != "retreat")
        {
            Console.WriteLine("Goblin incoming! 🧌");
            input = Console.ReadLine();
        }
    }
}
```


**Salida de la Terminal:**


```text
Goblin incoming! 🧌
ahhh!
Goblin incoming! 🧌
no no no
Goblin incoming! 🧌
retreat
```



### Ejercicio 2: Acumulaciones de Veneno

Demostrar un bucle `while` interactivo que incrementa una variable (`poisonStacks`) y continúa hasta que el jugador introduce una cadena específica (`"antidote!"`).

```csharp
using System;

class PoisonStacks
{
    static void Main()
    {
        int poisonStacks = 1;

        Console.WriteLine($"The toxin spreads... stack {poisonStacks}");
        string input = Console.ReadLine();

        while (input != "antidote!")
        {
            poisonStacks++;
            Console.WriteLine($"The toxin spreads... stack {poisonStacks}");
            input = Console.ReadLine();
        }
    }
}
```


### Ejercicio 3: Ola de Aparición

Demostrar un bucle `while` controlado por un contador que ejecuta el código un número fijo de veces (4 iteraciones) usando un contador que se incrementa (`count++`).


```csharp
using System;

class SpawnWave
{
    static void Main()
    {
        int count = 1;

        while (count <= 4)
        {
            Console.WriteLine("A skeleton spawns down the corridor! 💀");
            count++;
        }
    }
}
```


### Ejercicio 4: Luces de Escenario

Demostrar un bucle `for` combinado con sentencias condicionales (`if/else`) y el operador de módulo (`%`) para alternar la salida según iteraciones impares y pares.


```csharp
using System;

class StageLights
{
    static void Main()
    {
        for (int i = 1; i <= 6; i++)
        {
            if (i % 2 != 0)
            {
                Console.WriteLine("Spotlight on! 💡");
            }
            else
            {
                Console.WriteLine("Spotlight on! 💡 Spotlight on! 💡");
            }
        }
    }
}
```


### Ejercicio 5: Descenso al Foso

Demostrar un bucle `for` con decremento que cuenta hacia atrás desde `0` hasta `-20` usando el operador de decremento (`depth--`).


```csharp
using System;

class PitDescent
{
    static void Main()
    {
        for (int depth = 0; depth >= -20; depth--)
        {
            Console.WriteLine(depth);
        }

        Console.WriteLine("The elevator crashes into the flooded basement...");
    }
}
```



### Ejercicio 6: Medidor de Furia

Demostrar mutación de estado y operaciones compuestas dentro de un bucle `for` para acumular valores a lo largo de un número fijo de iteraciones.

```csharp
using System;

class RageMeter
{
    static void Main()
    {
        int rageCharge = 0;

        for (int i = 0; i < 4; i++)
        {
            rageCharge += 7;
            Console.WriteLine($"Rage charge: {rageCharge}");
        }
    }
}
```



### Ejercicio 7: Di Proceder

Demostrar control dinámico del bucle usando la entrada del usuario dentro de un bucle `while`, repitiendo cada línea que el jugador escribe hasta que se proporcione una cadena de terminación específica.


```csharp
using System;

class SayProceed
{
    static void Main()
    {
        string response = "";

        while (response != "proceed")
        {
            response = Console.ReadLine();

            if (response != "proceed")
            {
                Console.WriteLine(response);
            }
        }
    }
}
```


### Ejercicio 8: Bóveda Cerrada

Demostrar un bucle `while` completo que lleva la cuenta de los intentos mientras evalúa la entrada dinámica del usuario frente a una frase secreta codificada en el programa.


```csharp
using System;

class LockedVault
{
    static void Main()
    {
        string secretPhrase = "press start";
        string userInput = "";
        int attempts = 0;

        while (userInput != secretPhrase)
        {
            Console.Write("Enter the secret phrase: ");
            userInput = Console.ReadLine();
            attempts++;
        }

        Console.WriteLine("The vault door slides open, revealing a legendary blade.");
        Console.WriteLine($"It took {attempts} attempts to crack the safe.");
    }
}
```
