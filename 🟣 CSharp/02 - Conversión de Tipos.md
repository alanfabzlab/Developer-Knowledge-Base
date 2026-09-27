

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
        int mandos = 2;
        string claseActual = "Paladín";
        bool auricularesPuestos = true;

        Console.WriteLine($"Mandos: {mandos}");
        Console.WriteLine($"Clase: {claseActual}");
        Console.WriteLine($"Auriculares puestos: {auricularesPuestos}");
    }
}
```


**Salida de la Terminal:**


```text
Mandos: 2
Clase: Paladín
Auriculares puestos: True
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
        string objetivoIncursion = "Hidra del Vacío";
        int tamanoEscuadra = 15;
        double costoPorJugador = 25.50;
        bool incursionACiegas = true;

        Console.WriteLine($"Objetivo de la incursión: {objetivoIncursion}");
        Console.WriteLine($"Tamaño de la escuadra: {tamanoEscuadra}");
        Console.WriteLine($"Costo por jugador: ${costoPorJugador}");
        Console.WriteLine($"Incursión a ciegas: {incursionACiegas}");
    }
}
```


**Salida de la Terminal:**


```text
Objetivo de la incursión: Hidra del Vacío
Tamaño de la escuadra: 15
Costo por jugador: $25.5
Incursión a ciegas: True
```


### Ejercicio 3: Orígenes de la Leyenda

Demostrar la concatenación de cadenas combinando cadenas de texto con variables enteras.


```csharp
using System;

class LegendOrigins
{
    static void Main()
    {
        string nombre = "Aria la Audaz";
        int anio = 1994;

        Console.WriteLine(nombre + " es un héroe increíblemente legendario.");
        Console.WriteLine("Alcanzó la fama en " + anio + " durante el Asedio de la Caída de Brasa.");
    }
}
```


**Salida de la Terminal:**


```text
Aria la Audaz es un héroe increíblemente legendario.
Alcanzó la fama en 1994 durante el Asedio de la Caída de Brasa.
```


### Ejercicio 4: Reparto del Botín

Realizar división entera y usar el operador de módulo (`%`) para distribuir el oro entre los cofres y hallar el resto.


```csharp
using System;

class LootSplit
{
    static void Main()
    {
        int oroTotal = 23;
        int oroPorCofre = 5;

        int cofresLlenos = oroTotal / oroPorCofre;
        int oroRestante = oroTotal % oroPorCofre;

        Console.WriteLine($"Cofres llenos: {cofresLlenos}");
        Console.WriteLine($"Oro restante: {oroRestante}");
    }
}
```


**Salida de la Terminal:**


```text
Cofres llenos: 4
Oro restante: 3
```



## 5. Recopilar la Entrada del Usuario

En C#, la entrada del usuario se recopila desde la consola usando `Console.ReadLine()`. La entrada siempre se captura como `string` por defecto.


### Entrada de Cadena Estándar

```csharp
Console.Write("¿Cuál es el nombre de tu héroe?");
string nombreHeroe = Console.ReadLine();
Console.WriteLine($"¡Bienvenido a la fiesta, {nombreHeroe}!");
```


### Convertir la Entrada de Cadena a Entero (`int`)

Cuando se requieren operaciones numéricas sobre la entrada del usuario, la cadena `string` capturada debe convertirse usando `Convert.ToInt32()` o `int.Parse()`.


```csharp
Console.Write("Introduce un valor de daño: ");
string entrada = Console.ReadLine();
int danio = Convert.ToInt32(entrada);
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
        Console.Write("Introduce el año de nacimiento de tu personaje: ");
        int anioNacimiento = Convert.ToInt32(Console.ReadLine());

        int anioActual = 2026;
        int aniosEnCiclo = (anioActual - anioNacimiento) % 12;
        int aniosParaAlineacion = (12 - aniosEnCiclo) % 12;

        Console.WriteLine($"Años hasta que las runas se realineen con tu signo: {aniosParaAlineacion}");
    }
}
```


**Salida de la Terminal:**


```text
Introduce el año de nacimiento de tu personaje: 2004
Años hasta que las runas se realineen con tu signo: 2
```


### Ejercicio 6: Invocación Gacha

Calcular cuántas veces un jugador puede invocar en un banner de invocación según su saldo de cristales y hallar los cristales sobrantes usando operaciones de división y módulo.


```csharp
using System;

class GachaSummon
{
    static void Main()
    {
        Console.Write("¿Cuántos cristales tienes? ");
        string entrada = Console.ReadLine();
        int cristales = Convert.ToInt32(entrada);

        int costoInvocacion = 50;

        int invocacionesTotales = cristales / costoInvocacion;
        int cristalesRestantes = cristales % costoInvocacion;

        Console.WriteLine($"Puedes invocar: {invocacionesTotales} vez/veces");
        Console.WriteLine($"Cristales restantes: {cristalesRestantes}");
    }
}
```

**Salida de la Terminal:**


```text
¿Cuántos cristales tienes? 275
Puedes invocar: 5 vez/veces
Cristales restantes: 25
```
