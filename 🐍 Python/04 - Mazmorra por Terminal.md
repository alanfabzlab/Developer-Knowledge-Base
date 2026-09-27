


# 04. Mazmorra por Terminal (`terminal_game.py`)

**Versión original en inglés:** [04 - Terminal Dungeon Crawl.md](./04%20-%20Terminal%20Dungeon%20Crawl.md)

**Curso:** Python
**Tema:** Mazmorra por terminal, control de flujo, bucle de juego y gestión de estado
**Etiquetas:** `#python` `#project` `#cli` `#game-dev` `#control-flow`


Un mini crawler de mazmorras basado en texto, creado en la terminal como Proyecto de Hito, integrando conceptos fundamentales de Python: variables, lógica condicional, bucles y el módulo `random`.

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />


## 🎯 Requisitos del Proyecto

* **Nombre del archivo:** `terminal_game.py`
* **Lógica principal:** Guía al héroe a través de una mazmorra interactiva donde cada paso presenta al menos 2 opciones.
* **Mecánicas clave:** Usa control de flujo (`if`/`elif`/`else`), bucles (`while`/`for`), manejo de la entrada (`input()`) y resultados aleatorios opcionales con `import random`.

---


## 💡 Implementación (`terminal_game.py`)

```python
# terminal_game.py
import random

print("=================================")
print("  🏰 ASALTO A LA BÓVEDA HUNDIDA 🏰       ")
print("=================================\n")

hp = 100
tiene_llave = False

print("Caes por una rejilla hasta una bóveda hundida e inundada.")
print("Tu objetivo principal es escapar con la Llave Dorada.\n")

while hp > 0:
    print(f"HP Actual: {hp}")
    print("¿Qué quieres hacer?")
    print("1. Explorar los pasillos inundados")
    print("2. Intentar abrir la puerta de la bóveda")
    print("3. Descansar junto a una antorcha ardiendo")
    
    eleccion = input("Introduce tu elección (1-3): ")
    print()

    if eleccion == '1':
        print("Caminas por el agua oscura...")
        evento = random.randint(1, 3)
        if evento == 1:
            print("¡Arrancas una Llave Dorada oxidada del esqueleto! 🔑")
            tiene_llave = True
        elif evento == 2:
            print("¡Se dispara una trampa! Recibes 15 de daño. ❄️")
            hp -= 15
        else:
            print("No encuentras nada, pero la bóveda está en silencio.")
            
    elif eleccion == '2':
        if tiene_llave:
            print("Desbloqueas la puerta de la bóveda con la Llave Dorada y escapas hacia la noche.")
            print("🎉 ¡VICTORIA! ¡Has saqueado la Bóveda Hundida!")
            break
        else:
            print("¡La puerta está sellada! Primero necesitas encontrar una llave.")
            
    elif eleccion == '3':
        print("Descansas junto a la antorcha y recuperas 10 HP. 🔥")
        hp = min(100, hp + 10)
        
    else:
        print("Elección no válida. Elige 1, 2 o 3.")
        
    print("-" * 40)

if hp <= 0:
    print("\n💀 ¡Fin del Juego! La bóveda reclamó a otro cazador de tesoros.")
```


## 🛠️ Conceptos Aplicados

- **Entrada e Interpretación:** Capturar las selecciones del jugador mediante la entrada estándar de la terminal.
    
- **Gestión de Estado:** Seguir variables del jugador como `hp` y banderas de inventario (`has_key`).
    
- **Bucle de Juego:** Mantener el juego activo con un bucle `while` hasta que se dispare una condición de victoria o derrota.
    
- **Aleatorización:** Usar `random.randint()` para generar eventos inesperados dentro de la mazmorra.
