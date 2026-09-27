
# 05. Arreglos en C#

**Versión original en inglés:** [05 - Arrays.md](05%20-%20Arrays.md)

**Curso:** C#
**Tema:** Arreglos y Acceso a Colecciones
**Etiquetas:** `#csharp` `#arrays` `#collections`


Un arreglo es una colección de tamaño fijo de elementos del mismo tipo de dato, almacenados en posiciones de memoria contiguas.

---

## 1. Declaración e Inicialización de Arreglos

Los arreglos se declaran especificando el tipo de dato seguido de corchetes `[]`. Los valores se encierran entre llaves `{}` y se separan por comas.


### Características Clave
- **Tamaño Fijo:** El número de elementos se determina en el momento de la creación.
- **Seguridad de Tipos:** Todos los elementos deben coincidir con el tipo de dato declarado.

```csharp
using System;

class ArrayFoundations
{
    static void Main()
    {
        // Arreglo de strings con nombres de jefes
        string[] jefes = { "Guardián del Tiempo", "Segador del Vacío", "Coloso de Hierro", "Reina de Escarcha" };

        // Arreglo de enteros con los niveles de amenaza correspondientes
        int[] nivelesAmenaza = { 10, 9, 8, 10 };
    }
}
```


## 2. Indexación Basada en Cero

Los elementos dentro de un arreglo se acceden usando su posición numérica (índice) entre corchetes `[index]`. Los arreglos en C# usan indexación basada en cero, lo que significa que el primer elemento está en el índice `0`.


```csharp
using System;

class BossThemes
{
    static void Main()
    {
        string[] temas = 
        {
            "Obertura del Reino",
            "Taberna del Ocaso",
            "Cavernas Resonantes",
            "Tema del Menú de Tienda",
            "Concierto del Jefe Final"
        };

        Console.WriteLine("Cinematografía de apertura:");
        Console.WriteLine(temas[0]); // Salida: Obertura del Reino

        Console.WriteLine("Ruinas Subterráneas:");
        Console.WriteLine(temas[2]); // Salida: Cavernas Resonantes

        Console.WriteLine("Jefe Final:");
        Console.WriteLine(temas[4]); // Salida: Concierto del Jefe Final
    }
}
```


## 3. Modificar Elementos de un Arreglo

Los elementos de un arreglo se pueden actualizar después de la inicialización reasignando un nuevo valor directamente a una posición de índice concreta.


```csharp
using System;

class QuestBoard
{
    static void Main()
    {
        string[] misiones = { "Mata al Espectro de Arena", "Extrae 5 mineral de hierro", "Entrega una poción de curación" };

        // Actualiza el elemento en el índice 1
        misiones[1] = "Extrae 12 mineral de hierro";

        Console.WriteLine(misiones[1]); // Salida: Extrae 12 mineral de hierro
    }
}
```


## 4. Arreglos Vacíos y Capacidad Fija

Cuando el tamaño de un arreglo se conoce de antemano pero los valores aún no están disponibles, se especifica su longitud usando la palabra clave `new`. Intentar acceder o asignar valores fuera de los límites asignados lanza una `IndexOutOfRangeException`.


```csharp
using System;

class ArenaBracket
{
    static void Main()
    {
        // Reserva espacio para 64 elementos de tipo string
        string[] partidas = new string[64];

        // Asignando valores después
        partidas[0] = "Gremio de Hierro vs Gremio de Brasa";
        partidas[1] = "Gremio del Vacío vs Gremio de la Tormenta";
    }
}
```


## 5. Iterar sobre Arreglos con Bucles

En lugar de acceder manualmente a cada índice, un bucle `for` automatiza el recorrido de la colección.


```csharp
using System;

class PartyChat
{
    static void Main()
    {
        string[] mensajes = {
            "Kaz: ¿quién trae pociones de escarcha esta noche???",
            "Mira: yo no, tengo que fabricar el bastón nuevo",
            "Dev: únansesssss",
            "Sol: mejor hago la incursión sin parar la verdad",
            "Rin: ¡nos vemos a todos en la puerta!"
        };

        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine(mensajes[i]);
        }
    }
}
```


## 6. Condiciones de Bucle Dinámicas con `.Length`

Codificar los límites del bucle a mano hace que el código sea rígido. La propiedad integrada `.Length` devuelve el número total de elementos de un arreglo, permitiendo que los bucles se adapten dinámicamente si cambia el tamaño del arreglo.


```csharp
using System;

class InventoryBag
{
    static void Main()
    {
        string[] objetos = {
            "Poción de Salud",
            "Poción de Maná",
            "Runa de Bomba",
            "Mineral de Hierro",
            "Pergamino de Teletransporte",
            "Llave Dorada"
        };

        // .Length se evalúa dinámicamente a 6
        for (int i = 0; i < objetos.Length; i++)
        {
            Console.WriteLine(objetos[i]);
        }
    }
}
```
