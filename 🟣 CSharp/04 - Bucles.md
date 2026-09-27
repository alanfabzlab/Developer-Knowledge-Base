


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
while (condicion)
{
    // Bloque de código a repetir
}
```


## 3. Ejercicios


### Ejercicio 1: Pelea con Goblins

Demostrar un bucle `while` interactivo controlado por la entrada del usuario hasta que se encuentre una palabra clave de salida específica ("retirada").


```csharp
using System;

class GoblinBrawl
{
    static void Main()
    {
        Console.WriteLine("¡Llega un duende! 🧌");
        string entrada = Console.ReadLine();

        while (entrada != "retirada")
        {
            Console.WriteLine("¡Llega un duende! 🧌");
            entrada = Console.ReadLine();
        }
    }
}
```


**Salida de la Terminal:**


```text
¡Llega un duende! 🧌
ahhh!
¡Llega un duende! 🧌
no no no
¡Llega un duende! 🧌
retirada
```



### Ejercicio 2: Acumulaciones de Veneno

Demostrar un bucle `while` interactivo que incrementa una variable (`acumulacionVeneno`) y continúa hasta que el jugador introduce una cadena específica (`"antídoto!"`).

```csharp
using System;

class PoisonStacks
{
    static void Main()
    {
        int acumulacionVeneno = 1;

        Console.WriteLine($"La toxina se extiende... acumulación {acumulacionVeneno}");
        string entrada = Console.ReadLine();

        while (entrada != "antídoto!")
        {
            acumulacionVeneno++;
            Console.WriteLine($"La toxina se extiende... acumulación {acumulacionVeneno}");
            entrada = Console.ReadLine();
        }
    }
}
```


### Ejercicio 3: Ola de Aparición

Demostrar un bucle `while` controlado por un contador que ejecuta el código un número fijo de veces (4 iteraciones) usando un contador que se incrementa (`contador++`).


```csharp
using System;

class SpawnWave
{
    static void Main()
    {
        int contador = 1;

        while (contador <= 4)
        {
            Console.WriteLine("¡Aparece un esqueleto al final del pasillo! 💀");
            contador++;
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
                Console.WriteLine("¡Foco encendido! 💡");
            }
            else
            {
                Console.WriteLine("¡Foco encendido! 💡 ¡Foco encendido! 💡");
            }
        }
    }
}
```


### Ejercicio 5: Descenso al Foso

Demostrar un bucle `for` con decremento que cuenta hacia atrás desde `0` hasta `-20` usando el operador de decremento (`profundidad--`).


```csharp
using System;

class PitDescent
{
    static void Main()
    {
        for (int profundidad = 0; profundidad >= -20; profundidad--)
        {
            Console.WriteLine(profundidad);
        }

        Console.WriteLine("El ascensor se estrella contra el sótano inundado...");
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
        int cargaFuria = 0;

        for (int i = 0; i < 4; i++)
        {
            cargaFuria += 7;
            Console.WriteLine($"Carga de furia: {cargaFuria}");
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
        string respuesta = "";

        while (respuesta != "proceder")
        {
            respuesta = Console.ReadLine();

            if (respuesta != "proceder")
            {
                Console.WriteLine(respuesta);
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
        string fraseSecreta = "pulsa start";
        string entradaUsuario = "";
        int intentos = 0;

        while (entradaUsuario != fraseSecreta)
        {
            Console.Write("Introduce la frase secreta: ");
            entradaUsuario = Console.ReadLine();
            intentos++;
        }

        Console.WriteLine("La puerta de la bóveda se desliza y revela una hoja legendaria.");
        Console.WriteLine($"Hicieron falta {intentos} intentos para abrir la caja fuerte.");
    }
}
```
