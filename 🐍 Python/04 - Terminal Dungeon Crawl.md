

# 04. Terminal Dungeon Crawl (`terminal_game.py`)

**Course:** Python
**Topic:** Terminal Dungeon Crawl, Control Flow, Game Loop & State Management
**Tags:** `#python` `#project` `#cli` `#game-dev` `#control-flow`


A text-based mini-dungeon crawler built in the terminal as a Checkpoint Project, integrating fundamental Python concepts: variables, conditional logic, loops, and the `random` module.

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />


## 🎯 Project Requirements

* **File Name:** `terminal_game.py`
* **Core Logic:** Guide the hero through an interactive dungeon where each step presents at least 2 choices.
* **Key Mechanics:** Use control flow (`if`/`elif`/`else`), loops (`while`/`for`), input handling (`input()`), and optional random outcomes using `import random`.

---


## 💡 Implementation (`terminal_game.py`)

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


## 🛠️ Concepts Applied

- **Input & Parsing:** Capturing player selections via standard terminal input.
    
- **State Management:** Tracking player variables like `hp` and inventory flags (`has_key`).
    
- **Game Loop:** Keeping the game active with a `while` loop until a win/loss condition is triggered.
    
- **Randomization:** Using `random.randint()` to generate unexpected dungeon events.
