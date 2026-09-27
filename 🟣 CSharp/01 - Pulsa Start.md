
# 01. Pulsa Start

**Versión original en inglés:** [01 - Press Start.md](01%20-%20Press%20Start.md)

**Curso:** C#
**Tema:** Configuración del Entorno, Configuración del IDE y Primer Programa
**Etiquetas:** `#csharp` `#setup` `#fundamentals`



## 1. Introducción a C#

C# (pronunciado "C sharp") fue creado en 1999 en Microsoft durante el desarrollo de .NET Framework. Originalmente se llamaba **COOL** (*C-like Object Oriented Language*), pero ese nombre se descartó por problemas de marcas registradas.

Es un lenguaje de programación simple, de propósito general y orientado a objetos, que usa la extensión de archivo `.cs`.


### Aplicaciones Principales
* **Desarrollo de Juegos** (Unity Engine, Godot con enlaces a C#)
* **Servicios Multijugador** (tablas de clasificación, emparejamiento de jugadores y API de inventario)
* **Herramientas de Escritorio y Lanzadores de Juegos**
* **Computación en la Nube**

---


## 2. Estructura del Programa

Toda aplicación de consola estándar en C# sigue una estructura base:

CSharp

```csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("¡Hola, Campeón!");
    }
}
```


### Desglose de Componentes

- **`using System;`**: Da acceso a los espacios de nombres integrados y a los métodos de utilidad del sistema que proporciona C#.
    
- **`class Program`**: Organiza el código dentro de un contenedor de clase. Todo programa de consola requiere al menos una clase envolvente.
    
- **`static void Main()`**: El punto de entrada principal donde la ejecución del programa comienza de arriba abajo.
    
- **`Console.WriteLine()`**: Método estándar para imprimir texto en la ventana de consola seguido de un salto de línea.
    
- **`;` (Punto y coma)**: Terminador de sentencia estándar y obligatorio en C#.
    


## 3. Ejercicios de Práctica


### Ejercicio 1: Secuencia de Arranque

Escribir la estructura básica para imprimir un mensaje de bienvenida cuando arranca el juego.


```csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("¡Bienvenido al Reino!");
    }
}
```

**Salida de la Terminal:**


```text
¡Bienvenido al Reino!
```

### Ejercicio 2: Perfil del Héroe

Imprimir los detalles del personaje usando salida de cadena en `Console.WriteLine()`.


```csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Aria - Exploradora Semielfa");
    }
}
```


**Salida de la Terminal:**


```text
Aria - Exploradora Semielfa
```


### Ejercicio 3: Registro de Misiones

Imprimir texto estructurado de varias líneas usando sentencias de salida consecutivas.


```csharp
using System;

class QuestLog
{
    static void Main()
    {
        Console.WriteLine("Registro de Misiones - Día 27 de la Caída de Brasa");
        Console.WriteLine("-------------------------------");
        Console.WriteLine("Una ciudadela flotante surgió sobre el Mar de Cristal.");
        Console.WriteLine("Sus torres fueron forjadas con cristal y tormenta.");
        Console.WriteLine("Encontré una puerta sellada detrás de la fuente lunar.");
        Console.WriteLine("Antes de llegar a la sala del jefe, me desconecté.");
    }
}
```


**Salida de la Terminal:**


```text
Registro de Misiones - Día 27 de la Caída de Brasa
-------------------------------
Una ciudadela flotante surgió sobre el Mar de Cristal.
Sus torres fueron forjadas con cristal y tormenta.
Encontré una puerta sellada detrás de la fuente lunar.
Antes de llegar a la sala del jefe, me desconecté.
```



## 4. Comentarios en C#

Los comentarios son notas escritas dentro del código que el compilador ignora por completo. Ayudan a explicar la lógica a los desarrolladores.

* **Comentarios de Una Línea**: Comienzan con dos barras diagonales (`//`).
* **Comentarios de Varias Líneas**: Se encierran entre `/*` y `*/`.

---


## 5. Ejercicios Adicionales de Práctica


### Ejercicio 4: Rant Nerdy
Usar comentarios de una línea y de varias líneas para documentar una opinión sobre diseño de juegos y su razonamiento.

```csharp
using System;

class NerdyRant
{
    static void Main()
    {
        /* Boss rush mode is the purest expression of skill.
           You only bring one build, so you better know it! */
        // I think the hardest difficulty should unlock after your first clear.
    }
}
```


**Salida de la Terminal:**

_(Nota: Los comentarios no producen salida en la terminal.)_


### Ejercicio 5: Cartel de Reclutamiento

Crear un anuncio personal de gremio usando comentarios y sentencias `Console.WriteLine()` estructuradas.


```csharp
using System;

class RecruitmentPoster
{
    static void Main()
    {
        /* 
        Recruitment poster for a gaming guild
        I wanna find my dream party
        So I made this poster!
        */

        // Headline to grab attention
        Console.WriteLine("¡ÚNETE A MI GREMIO! 🤝");

        // Introduce yourself
        Console.WriteLine("¡Hola, soy Aria!");

        // State your interest
        Console.WriteLine("Me encanta el diseño de juegos y la creación de niveles.");

        // Favorite pastime
        Console.WriteLine("Me gusta hacer speedruns de Hollow Knight y modificar juegos clásicos.");

        // Call to action
        Console.WriteLine("¡Reúnete con tu escuadrón y construyamos mundos geniales juntos! 🚀");
    }
}
```


**Salida de la Terminal:**


```text
¡ÚNETE A MI GREMIO! 🤝
¡Hola, soy Aria!
Me encanta el diseño de juegos y la creación de niveles.
Me gusta hacer speedruns de Hollow Knight y modificar juegos clásicos.
¡Reúnete con tu escuadrón y construyamos mundos geniales juntos! 🚀
```
