


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
print("  🏰 SUNKEN VAULT HEIST 🏰       ")
print("=================================\n")

hp = 100
has_key = False

print("You drop through a grate into a flooded sunken vault.")
print("Your main objective is to escape with the Golden Key.\n")

while hp > 0:
    print(f"Current HP: {hp}")
    print("What do you want to do?")
    print("1. Search the flooded halls")
    print("2. Try to open the vault door")
    print("3. Rest by a burning torch")
    
    choice = input("Enter your choice (1-3): ")
    print()

    if choice == '1':
        print("You wade through the dark water...")
        event = random.randint(1, 3)
        if event == 1:
            print("You pry a rusted Golden Key off a skeleton! 🔑")
            has_key = True
        elif event == 2:
            print("A trap springs! You take 15 trap damage. ❄️")
            hp -= 15
        else:
            print("You find nothing, but the vault is silent.")
            
    elif choice == '2':
        if has_key:
            print("You unlock the vault door with the Golden Key and escape into the night.")
            print("🎉 VICTORY! You looted the Sunken Vault!")
            break
        else:
            print("The door is sealed tight. You need to find a key first!")
            
    elif choice == '3':
        print("You rest by the torch and recover 10 HP. 🔥")
        hp = min(100, hp + 10)
        
    else:
        print("Invalid choice. Please pick 1, 2, or 3.")
        
    print("-" * 40)

if hp <= 0:
    print("\n💀 Game Over! The vault claimed another treasure hunter.")
```


## 🛠️ Conceptos Aplicados

- **Entrada e Interpretación:** Capturar las selecciones del jugador mediante la entrada estándar de la terminal.
    
- **Gestión de Estado:** Seguir variables del jugador como `hp` y banderas de inventario (`has_key`).
    
- **Bucle de Juego:** Mantener el juego activo con un bucle `while` hasta que se dispare una condición de victoria o derrota.
    
- **Aleatorización:** Usar `random.randint()` para generar eventos inesperados dentro de la mazmorra.
