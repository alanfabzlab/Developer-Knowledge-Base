---
course: Python
chapter: Terminal Adventure Game
topic: Checkpoint Project, Control Flow & CLI Logic
tags:
  - python
  - project
  - cli
  - game-dev
  - control-flow
---


# 04. Terminal Adventure Game (`terminal_game.py`)

A text-based mini-adventure game built in the terminal as a Checkpoint Project, integrating fundamental Python concepts: variables, conditional logic, loops, and the `random` module.

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />


## 🎯 Project Requirements

* **File Name:** `terminal_game.py`
* **Core Logic:** Guide the player through an interactive story where each step presents at least 2 choices.
* **Key Mechanics:** Use control flow (`if`/`elif`/`else`), loops (`while`/`for`), input handling (`input()`), and optional random outcomes using `import random`.

---


## 💡 Implementation (`terminal_game.py`)

```python
# terminal_game.py
import random

print("=================================")
print("  🌲 SNOWY FOREST SURVIVAL 🌲    ")
print("=================================\n")

hp = 100
has_key = False

print("You wake up near an abandoned cabin in a snowy forest.")
print("Your main objective is to survive and find a way inside.\n")

while hp > 0:
    print(f"Current HP: {hp}")
    print("What do you want to do?")
    print("1. Explore the woods")
    print("2. Try to open the cabin door")
    print("3. Rest by the campfire")
    
    choice = input("Enter your choice (1-3): ")
    print()

    if choice == '1':
        print("You venture into the deep snow...")
        event = random.randint(1, 3)
        if event == 1:
            print("You found an old rusty key under a pine tree! 🔑")
            has_key = True
        elif event == 2:
            print("A sudden snowstorm hits! You take 15 cold damage. ❄️")
            hp -= 15
        else:
            print("You found nothing, but the woods are quiet.")
            
    elif choice == '2':
        if has_key:
            print("You unlock the cabin door with the rusty key and step inside safely.")
            print("🎉 VICTORY! You survived the wilderness!")
            break
        else:
            print("The door is locked tight. You need to find a key first!")
            
    elif choice == '3':
        print("You rest near the campfire and recover 10 HP. 🔥")
        hp = min(100, hp + 10)
        
    else:
        print("Invalid choice. Please pick 1, 2, or 3.")
        
    print("-" * 40)

if hp <= 0:
    print("\n💀 Game Over! You succumbed to the cold environment.")
```


## 🛠️ Concepts Applied

- **Input & Parsing:** Capturing user selections via standard terminal input.
    
- **State Management:** Tracking player variables like `hp` and inventory flags (`has_key`).
    
- **Game Loop:** Keeping the game active with a `while` loop until a win/loss condition is triggered.
    
- **Randomization:** Using `random.randint()` to generate unexpected wilderness events.
