

# 02. Conversión de Tipos

**Versión original en inglés:** [02 - Typecast.md](02%20-%20Typecast.md)

**Curso:** C#
**Tema:** Variables, Tipos de Datos Primitivos, Conversión de Tipos y Operadores
**Etiquetas:** `#csharp` `#typecast` `#variables` `#operators`



## 1. Variables y Tipos de Datos Primitivos

Una variable es un contenedor de almacenamiento con nombre que guarda datos en memoria. Toda variable en C# requiere un tipo de dato explícito, un nombre y un valor asignado.


### Tipos de Datos Comunes
* **`int`**: Números enteros sin decimales (positivos o negativos).
* **`double`**: Números decimales de punto flotante.
* **`string`**: Secuencia de caracteres usada para almacenar texto (admite Unicode y emojis).
* **`bool`**: Valores booleanos que representan estados de verdad (`true` o `false`).


---


## 2. Ejercicios de Práctica

### Ejercicio 1: Pantalla de Equipamiento
Declarar variables básicas (`int`, `string`, `bool`) para una pantalla de personaje e imprimir sus valores en la consola usando interpolación de cadenas.

```csharp
using System;

class LoadoutScreen
{
    static void Main()
    {
        int controllers = 2;
        string currentClass = "Paladin";
        bool isHeadsetOn = true;

        Console.WriteLine($"Controllers: {controllers}");
        Console.WriteLine($"Class: {currentClass}");
        Console.WriteLine($"Headset on: {isHeadsetOn}");
    }
}
```


**Salida de la Terminal:**


```text
Controllers: 2
Class: Paladin
Headset on: True
```



## 3. Variables, Concatenación de Cadenas y Matemáticas Básicas

En C#, las variables almacenan datos que se pueden unir con texto mediante concatenación de cadenas o manipular con operadores aritméticos y de módulo estándar.


## 4. Ejercicios Adicionales de Práctica

### Ejercicio 2: Planificación de Incursión

Declarar e inicializar variables con distintos tipos primitivos (`string`, `int`, `double`, `bool`) para planificar una incursión en una mazmorra.


```csharp
using System;

class RaidPlanning
{
    static void Main()
    {
        string raidTarget = "Void Hydra";
        int squadSize = 15;
        double costPerPlayer = 25.50;
        bool isBlindRaid = true;

        Console.WriteLine($"Raid Target: {raidTarget}");
        Console.WriteLine($"Squad Size: {squadSize}");
        Console.WriteLine($"Cost per Player: ${costPerPlayer}");
        Console.WriteLine($"Blind Raid: {isBlindRaid}");
    }
}
```


**Salida de la Terminal:**


```text
Raid Target: Void Hydra
Squad Size: 15
Cost per Player: $25.5
Blind Raid: True
```


### Ejercicio 3: Orígenes de la Leyenda

Demostrar la concatenación de cadenas combinando cadenas de texto con variables enteras.


```csharp
using System;

class LegendOrigins
{
    static void Main()
    {
        string name = "Aria the Bold";
        int year = 1994;

        Console.WriteLine(name + " is an incredibly legendary hero.");
        Console.WriteLine("She rose to fame in " + year + " during the Siege of Emberfall.");
    }
}
```


**Salida de la Terminal:**


```text
Aria the Bold is an incredibly legendary hero.
She rose to fame in 1994 during the Siege of Emberfall.
```


### Ejercicio 4: Reparto del Botín

Realizar división entera y usar el operador de módulo (`%`) para distribuir el oro entre los cofres y hallar el resto.


```csharp
using System;

class LootSplit
{
    static void Main()
    {
        int totalGold = 23;
        int goldPerChest = 5;

        int fullChests = totalGold / goldPerChest;
        int leftoverGold = totalGold % goldPerChest;

        Console.WriteLine($"Full chests: {fullChests}");
        Console.WriteLine($"Gold left over: {leftoverGold}");
    }
}
```


**Salida de la Terminal:**


```text
Full chests: 4
Gold left over: 3
```



## 5. Recopilar la Entrada del Usuario

En C#, la entrada del usuario se recopila desde la consola usando `Console.ReadLine()`. La entrada siempre se captura como `string` por defecto.


### Entrada de Cadena Estándar

```csharp
Console.Write("What's your hero name?");
string heroName = Console.ReadLine();
Console.WriteLine($"Welcome to the party, {heroName}!");
```


### Convertir la Entrada de Cadena a Entero (`int`)

Cuando se requieren operaciones numéricas sobre la entrada del usuario, la cadena `string` capturada debe convertirse usando `Convert.ToInt32()` o `int.Parse()`.


```csharp
Console.Write("Enter a damage value: ");
string input = Console.ReadLine();
int damage = Convert.ToInt32(input);
```


## 6. Ejercicios de Entrada y Conversión


### Ejercicio 5: Ciclo de Runas

Pedir al usuario el año de nacimiento de su personaje, convertir la entrada de cadena a un entero y calcular los años que faltan hasta que el ciclo de doce runas se realinee con su signo (ciclo de 12 años).


```csharp
using System;

class RuneCycle
{
    static void Main()
    {
        Console.Write("Enter your character's birth year: ");
        int birthYear = Convert.ToInt32(Console.ReadLine());

        int currentYear = 2026;
        int yearsIntoCycle = (currentYear - birthYear) % 12;
        int yearsUntilAlignment = (12 - yearsIntoCycle) % 12;

        Console.WriteLine($"Years until the runes realign for your sign: {yearsUntilAlignment}");
    }
}
```


**Salida de la Terminal:**


```text
Enter your character's birth year: 2004
Years until the runes realign for your sign: 2
```


### Ejercicio 6: Invocación Gacha

Calcular cuántas veces un jugador puede invocar en un banner de invocación según su saldo de cristales y hallar los cristales sobrantes usando operaciones de división y módulo.


```csharp
using System;

class GachaSummon
{
    static void Main()
    {
        Console.Write("How many crystals do you have? ");
        string input = Console.ReadLine();
        int crystals = Convert.ToInt32(input);

        int summonCost = 50;

        int totalSummons = crystals / summonCost;
        int remainingCrystals = crystals % summonCost;

        Console.WriteLine($"You can summon: {totalSummons} time(s)");
        Console.WriteLine($"Crystals left over: {remainingCrystals}");
    }
}
```

**Salida de la Terminal:**


```text
How many crystals do you have? 275
You can summon: 5 time(s)
Crystals left over: 25
```
