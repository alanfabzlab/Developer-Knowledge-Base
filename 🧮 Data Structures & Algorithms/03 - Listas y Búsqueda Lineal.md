
# 03. Listas y Búsqueda Lineal

**Versión original en inglés:** [03 - Lists & Linear Search.md](03%20-%20Lists%20&%20Linear%20Search.md)

**Curso:** Estructuras de Datos y Algoritmos
**Tema:** Listas, Indexación, Rebanado, Métodos de Lista y Búsqueda Lineal
**Etiquetas:** `#dsa` `#lists` `#linear-search`



## 1. Repaso Rápido: Listas en Python

Una **Lista** es una colección ordenada de elementos almacenados en una sola variable. Los elementos van encerrados entre corchetes `[]` y separados por comas.

### Indexación y Rebanado
- **Indexación:** Accede a elementos individuales usando índices que empiezan en cero.
- **Rebanado:** Extrae subsegmentos usando `list[start:end]`, donde `start` es inclusivo y `end` es exclusivo.

Python

```python
loot_bag = ['Health Potion', 'Iron Sword', 'Bomb Rune', 'Teleport Scroll', 'Golden Key', 'Monster Pelt']

# Indexing
print(loot_bag[0])  # Output: Health Potion
print(loot_bag[2])  # Output: Bomb Rune

# Slicing
zones = ['Ashwood', 'Brightfalls', 'Cinderpeak', 'Duskmoor', 'Everest', 'Frostgate', 'Goldspan']
print(zones[1:4])  # Output: ['Brightfalls', 'Cinderpeak', 'Duskmoor']
```


### Métodos Comunes de Lista

- `.append(item)`: Agrega un elemento al final de la lista.
    
- `.insert(index, item)`: Inserta un elemento en un índice específico.
    
- `.pop(index)`: Elimina y retorna un elemento de un índice específico (elimina el último elemento si no se pasa ningún índice).
    
- `len(list)`: Retorna el número total de elementos de la lista.
    


Python

```python
to_do = ['Craft a health potion', 'Explore the Ashwood', 'Level up at the bonfire']

to_do.append('Clear the Sunken Keep')
to_do.insert(2, 'Recruit a party member')
to_do.pop(4)

print(len(to_do))  # Output: 4
```


## 2. Algoritmo de Búsqueda Lineal

La **Búsqueda Lineal** es la técnica de búsqueda más simple. Inspecciona cada elemento de una colección de forma secuencial, desde el principio hasta el final, hasta que se encuentra un valor coincidente o se alcanza el final de la lista.


### Desglose del Algoritmo

1. **Entrada:** Una lista no ordenada de elementos y un valor objetivo.
    
2. **Proceso:** Recorre todos los elementos de forma secuencial. Compara el elemento actual con el valor objetivo.
    
3. **Salida:** Retorna `True` si se encuentra, o `False` si el bucle termina sin coincidencia.
    


### Implementación en Python


Python

```python
def linear_search(input_list, target_value):
    for item in input_list:
        if item == target_value:
            return True
    return False

guild_roster = [
    'aria@stormborn.gg',
    'kai@vanguard.clan',
    'nyx@arcanist.gg',
    'borin@ranger.gg',
    'dara@shadow.gg',
    'elowen@arcanist.gg',
    'cass@ranger.gg',
    'jorund@vanguard.clan',
    'vex@shadow.gg',
    'rhea@stormborn.gg',
    'soren@ranger.gg',
    'pleaseaddmeplease@gg.gg',
    'lyra@arcanist.gg'
]

print(linear_search(guild_roster, 'nyx@arcanist.gg'))   # Output: True
print(linear_search(guild_roster, 'mark.scout@gg.gg'))  # Output: False
```


## 3. Eficiencia Algorítmica

- **Mejor Caso — $O(1)$:** El elemento objetivo está justo al principio de la lista. La búsqueda termina de inmediato en 1 paso.
    
- **Peor Caso — $O(N)$:** El elemento objetivo está al final de la lista o no está presente en ella. El algoritmo debe revisar cada elemento ($N$ operaciones) antes de concluir.
