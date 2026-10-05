
# Chuleta de C#

**Versión original en inglés:** [00b - CSharp Cheatsheet.md](00b%20-%20CSharp%20Cheatsheet.md)

**Curso:** C#
**Tema:** Sistema de Tipos, Tipos por Valor y por Referencia, Pila vs. Montículo, Sintaxis y Errores Comunes
**Etiquetas:** `#csharp` `#cheatsheet` `#types` `#syntax` `#reference`

Referencia rápida de la sintaxis de C# y de las reglas del sistema de tipos que sorprenden a quien llega al lenguaje, usando datos de videojuegos como ejemplos a lo largo de la nota.

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #512BD4, #B39DFF, #512BD4, transparent); margin: 24px 0;" />

## 🔹 Estructura del Programa

CSharp

```csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Pulsa Start");
    }
}
```

**Salida de la Terminal:**

```text
Pulsa Start
```

C# 10+ también acepta las **sentencias de nivel superior** — sin clase, sin `Main`, el compilador genera el contenedor por ti:

```csharp
Console.WriteLine("Pulsa Start");
```

Solo un archivo por proyecto puede usarlas, y no se pueden combinar con una clase `Program` explícita.

## 🔹 Comentarios

```csharp
// Comentario de una línea

/* Comentario de bloque
   que abarca varias líneas */

/// <summary>Comentario de documentación XML que IntelliSense recoge.</summary>
```

## 🔹 Variables, `var` y `const`

```csharp
int mandos = 2;            // el tipo es obligatorio en C#
string claseActual = "Paladín";
double probCritico = 0.25;
bool auricularesPuestos = true;

var tiempoJugado = 2041;         // inferido como int
const int MaxTamanoGrupo = 4;    // constante de compilación, no se puede reasignar
```

`var` sigue siendo **tipado estático**: el compilador fija el tipo en tiempo de compilación a partir del valor inicial, no es JavaScript. Necesita un valor inicial y después no puedes asignarle un `string`.

## 🔹 Tipos de Datos Primitivos

| Tipo | Tamaño | Rango / Precisión | Uso típico en videojuegos |
| --- | --- | --- | --- |
| `bool` | 1 byte | `true` / `false` | `esInvencible` |
| `char` | 2 bytes | Un carácter Unicode | `'A'` |
| `byte` | 1 byte | 0 a 255 | Canales de color, banderas |
| `short` | 2 bytes | -32,768 a 32,767 | Contadores pequeños |
| `int` | 4 bytes | ±2.1 mil millones | **Elección por defecto** para contadores y daño |
| `long` | 8 bytes | ±9.2 quintillones | Marcas de tiempo, moneda grande |
| `float` | 4 bytes | ~7 dígitos significativos | Posiciones: barato para la GPU |
| `double` | 8 bytes | ~15-16 dígitos significativos | **Elección por defecto** para decimales |
| `decimal` | 16 bytes | 28-29 dígitos, base 10 exacta | Dinero, nunca uses `double` para el oro |
| `string` | referencia | Texto inmutable | Nombres, diálogos, ids de objetos |

Cada tipo numérico tiene su gemelo sin signo (`uint`, `ulong`, `byte`...). Los gu bajos están permitidos en los literales para hacerlos legibles: `2_048` es `2048`.

## 🔹 Tipos por Valor vs. por Referencia

Esta es la regla más importante del lenguaje.

| | Tipo por valor | Tipo por referencia |
| --- | --- | --- |
| Ejemplos | `int`, `double`, `bool`, `char`, `struct`, `enum` | `string`, `class`, `array`, `delegate`, `interface` |
| Vive en | La **pila** — rápida, se libera al terminar el ámbito | El **montículo** — gestionado por el recolector de basura |
| Asignación | Copia el **valor** | Copia la **referencia** (la dirección) |
| Valor por defecto | `0`, `false` | `null` |
| Forma anulable | `int?` | `string?` |
| `==` compara | El contenido | La identidad de la referencia (`string` es la excepción) |

**Los tipos por valor duplican. Los tipos por referencia comparten.** Un `struct` se comporta como un `int`; una `class` se comporta como un asa.

CSharp

```csharp
using System;

class Program
{
    static void Main()
    {
        int danioEspada = 25;
        int danioHacha = danioEspada;  // copia el valor

        danioHacha = 60;

        Console.WriteLine(danioEspada);  // 25 — intacto
        Console.WriteLine(danioHacha);   // 60
    }
}
```

**Salida de la Terminal:**

```text
25
60
```

Cambia el `int` por una `class` y las mismas tres líneas mutan un único objeto:

CSharp

```csharp
using System;

class Damage
{
    public int Dano;
}

class Program
{
    static void Main()
    {
        Damage espada = new Damage { Dano = 25 };
        Damage hacha = espada;  // copia la referencia, no el objeto

        hacha.Dano = 60;

        Console.WriteLine(espada.Dano);  // 60 — dos nombres, un objeto
        Console.WriteLine(hacha.Dano);   // 60
    }
}
```

**Salida de la Terminal:**

```text
60
60
```

Declara la misma clase como `struct` y vuelve a imprimir `25` / `60`, porque los structs se copian al asignar.

## 🔹 Anulables y Seguridad ante Null

```csharp
int? danoExtra = null;         // un tipo por valor que admite null
string? etiquetaJugador = null;  // tipo por referencia, requiere <Nullable>enable</Nullable>

etiquetaJugador ??= "@nightowl";        // asigna solo mientras sea null → "@nightowl"
int total = (danoExtra ?? 0) + 25;      // 25 — ?? recurre al lado derecho

Console.WriteLine(etiquetaJugador.Length);        // lanza excepción si etiquetaJugador es null
Console.WriteLine(etiquetaJugador?.Length);       // 9 — se corta en null en vez de lanzar
Console.WriteLine(etiquetaJugador?.Length ?? 0);  // 9 — el 0 solo aparece cuando sí es null

if (danoExtra is not null) { /* ... */ }
```

## 🔹 Operadores

```csharp
// Aritméticos
int infligido = 23 + 18;         // 41
int restante = 30 - 8;            // 22
float escalado = 10 * 2.5f;       // 25
int oleadas = 76 % 4;             // 0  — módulo, igual que en Python
int xor = 2 ^ 3;                  // 1  — XOR bit a bit, NO es potencia
double potencia = Math.Pow(2, 3); // 8 — esto sí es la potencia

// División
int truncada = 23 / 2;      // 11 — la división entera trunca
double precisa = 23 / 2.0;  // 11.5

// Asignación compuesta
int bajas = 0;
bajas++;      // 1
bajas += 5;   // 6
bajas *= 2;   // 12

// Relacionales
a == b   // Igual que
a != b   // Distinto de
a > b    // Mayor que
a < b    // Menor que
a >= b   // Mayor o igual que
a <= b   // Menor o igual que

// Lógicos
a && b   // Y — ambos deben ser ciertos
a || b   // O — al menos uno debe ser cierto
!a       // Negación

// Ternario
string estado = hp > 0 ? "Vivo" : "Caido";
```

## 🔹 Cadenas e Interpolación

```csharp
string heroe = "Aria";

Console.WriteLine($"Bienvenida, {heroe}! Eres nivel {12}.");
Console.WriteLine($"Jefe en {90.0 / 60:0.0} min");   // 1.5 — especificador de formato
Console.WriteLine($"Critico: {0.25:P0}");             // 25%
Console.WriteLine($"Relleno: {42,5}|");              // alineado a la derecha, ancho 5
Console.WriteLine($"Hex: {255:X}");                  // FF

string ruta = @"C:\Games\Emberfall\saves";  // literal: las barras invertidas se quedan tal cual
string cita = "Ella dijo \"corre\".";
int longitud = heroe.Length;                   // 4
string[] palabras = heroe.Split(' ');          // ["Aria"]
string mayusculas = heroe.ToUpper();           // ARIA
```

Las cadenas son **inmutables**. `heroe[0] = 'b';` no compila — construye una cadena nueva y reasigna.

## 🔹 Arreglos y `foreach`

```csharp
string[] equipamiento = { "Espada", "Escudo", "Poción", "Runa" };

Console.WriteLine(equipamiento.Length);   // 4
Console.WriteLine(equipamiento[0]);        // Espada
Console.WriteLine(equipamiento[^1]);       // Poción — índice desde el final (C# 8+)

foreach (string objeto in equipamiento)
{
    Console.WriteLine(objeto);
}

int[] puntuaciones = { 42, 7, 91, 25 };
Array.Sort(puntuaciones);
int mejor = puntuaciones[^1];                    // 91
int posicion = Array.IndexOf(puntuaciones, 42);  // 2
int[] copia = (int[])puntuaciones.Clone();       // copia real, no una referencia compartida

int[] vacio = new int[3];          // tres ceros
int[] cuadricula = new int[2, 2];  // rectangular: 2 filas x 2 columnas
cuadricula[1, 1] = 25;
```

El tamaño de un arreglo no puede cambiar después de crearlo. Para eso existe `List<T>`.

## 🔹 Listas

```csharp
using System.Collections.Generic;

List<string> grupo = new List<string> { "Aria", "Kai", "Nyx" };

grupo.Add("Borin");          // agregar
grupo.Remove("Kai");         // eliminar por valor
grupo.Insert(0, "Líder");    // insertar en un índice
bool presente = grupo.Contains("Nyx");  // true
int tamano = grupo.Count;                // 4 — Count, no Length
string primero = grupo[0];               // Líder
string ultimo = grupo[^1];               // Borin
grupo.Sort();
grupo.Clear();
```

## 🔹 Control de Flujo

```csharp
if (hp > 50)
{
    Console.WriteLine("Saludable");
}
else if (hp > 20)
{
    Console.WriteLine("Herido");
}
else
{
    Console.WriteLine("Crítico");
}
```

La **expresión** `switch` reemplaza a la mayoría de sentencias `switch` (patrones relacionales de C# 9+):

```csharp
string rango = puntuacion switch
{
    >= 90 => "S",
    >= 80 => "A",
    >= 70 => "B",
    _ => "C"
};
```

La sentencia `switch` clásica todavía existe y necesita un `break` en cada caso:

```csharp
switch (elemento)
{
    case "fuego":
        dano = 30;
        break;
    default:
        dano = 10;
        break;
}
```

## 🔹 Bucles

```csharp
string[] oleada = { "Goblin", "Ogro", "Espectro" };

for (int ronda = 1; ronda <= 3; ronda++) { }

int intentos = 0;
while (intentos < 3) { intentos++; }

do { } while (intentos > 0);   // se ejecuta al menos una vez

foreach (string enemigo in oleada) { }

break;      // sale del bucle por completo
continue;   // salta a la siguiente iteración
```

## 🔹 Métodos

```csharp
using System;

class Combat
{
    static int AplicarDano(int hp, int entrante)  // devuelve un valor
    {
        return hp - entrante;
    }

    static bool EstaVivo(int hp) => hp > 0;       // cuerpo de expresión

    static int Tirar(int caras = 20)              // parámetro por defecto
    {
        return Random.Shared.Next(1, caras + 1);
    }

    // out: devuelve una bandera de éxito y escribe el valor analizado
    static bool TryGetSlot(string entrada, out int ranura)
    {
        return int.TryParse(entrada, out ranura);
    }

    // params: acepta cualquier cantidad de argumentos
    static int Total(params int[] valores)
    {
        int suma = 0;
        foreach (int v in valores) { suma += v; }
        return suma;
    }

    static void Main()
    {
        Console.WriteLine(AplicarDano(100, 35));  // 65
        Console.WriteLine(EstaVivo(0));           // False
        Console.WriteLine(Total(1, 2, 3, 4));     // 10
    }
}
```

## 🔹 Números Aleatorios

```csharp
using System;

// .NET 6+ — compartido, seguro entre hilos, sin reservas de memoria
int d20 = Random.Shared.Next(1, 21);            // 1 a 20 — el límite superior es EXCLUSIVO
int cualquiera = Random.Shared.Next();          // 0 a int.MaxValue
double porcentaje = Random.Shared.NextDouble(); // 0.0 a 1.0
bool critico = Random.Shared.NextDouble() < 0.25;

// Estilo antiguo — una instancia, reutilizada
var rng = new Random();
int nivelBotin = rng.Next(0, 4);               // 0, 1, 2 o 3
```

## 🔹 Errores Comunes

| Trampa | Qué ocurre realmente | Solución |
| --- | --- | --- |
| `int a = 23 / 2;` | `11`, no `11.5` — la división entera trunca | escribe `23 / 2.0` |
| `0.1 + 0.2 == 0.3` | `false` — los flotantes binarios no pueden guardar esto exacto | usa `decimal` para el oro |
| `s[0] = 'b';` sobre un `string` | Error de compilación — las cadenas son inmutables | reasigna `s`, o usa `StringBuilder` |
| `if (unInt == null)` | Advertencia CS0472 — un `int` no anulable nunca es `null` | decláralo `int?` |
| Dos variables de tipo clase | Mutar una se ve reflejada en la otra | `.Clone()` o copia los campos |
| `int.MaxValue + 1` | Da la vuelta en silencio a `int.MinValue` — `unchecked` es el valor por defecto | envuélvelo en `checked { }` |
| `Convert.ToInt32("abc")` | Lanza `FormatException` | usa `int.TryParse` |
| `foreach` sobre una lista `null` | `NullReferenceException` | valida el null antes de iterar |
| Olvidar `using System;` | `Console` no se resuelve | agrega el `using` |

## 🔹 Viniendo de Python

| Python                           | C#                                                       |
| -------------------------------- | -------------------------------------------------------- |
| `print(x)`                       | `Console.WriteLine(x)`                                   |
| `input("Nombre? ")`              | `Console.Write("Nombre? ")` y luego `Console.ReadLine()` |
| `int(x)` / `str(x)`              | `Convert.ToInt32(x)` / `x.ToString()`                    |
| `True` / `False` / `None`        | `true` / `false` / `null`                                |
| `len(s)` / `len(a)` / `len(lst)` | `s.Length` / `a.Length` / `lst.Count`                    |
| `for i in range(n)`              | `for (int i = 0; i < n; i++)`                            |
| `a ** b`                         | `Math.Pow(a, b)`                                         |
| `a % b`                          | `a % b` — idéntico                                       |
| `f"{x}"`                         | `$"{x}"`                                                 |
| `list` / `dict`                  | `List<T>` / `Dictionary<K, V>`                           |
| `# comentario`                   | `// comentario` — y `/* bloque */` también funciona      |
| `"12"` -> `int`                  | `int.Parse(s)` o `int.TryParse(s, out int n)`            |
| `len(x) == 0` en una lista       | `list.Count == 0`                                        |
| `//` (división entera)           | `23 / 2` da `11` — C# no tiene operador `//`             |

## 🔹 Constantes Útiles

```csharp
int.MaxValue        // 2147483647
int.MinValue        // -2147483648
long.MaxValue       // 9223372036854775807
double.NaN          // no es un número — NaN != NaN, compara con double.IsNaN
double.PositiveInfinity
double.Epsilon      // el double positivo más pequeño, unos 4.9e-324
char.MaxValue       // el carácter más grande, U+FFFF
```

## 🔹 Resumen en Una Página

- Cada instrucción termina con `;` y cada bloque con llaves `{}`.
- Los tipos son explícitos salvo que escribas `var` — y `var` sigue siendo tipado en compilación.
- `struct` copia, `class` comparte. Este es el bug detrás de la mayoría de los momentos "lo cambié y cambió allá".
- Los tipos por valor usan `0`/`false` por defecto, los por referencia `null`.
- `Next(a, b)` excluye `b`.
- `int / int` es división entera. Casi siempre es un error en las matemáticas del juego.
- `string` es un tipo por referencia, pero inmutable, y `==` compara su contenido.
