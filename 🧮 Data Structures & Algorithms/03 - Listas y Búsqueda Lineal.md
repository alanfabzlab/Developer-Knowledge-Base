
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
bolsa_botin = ['Poción de Salud', 'Espada de Hierro', 'Runa de Bomba', 'Pergamino de Teletransporte', 'Llave Dorada', 'Piel de Monstruo']

# Indexación
print(bolsa_botin[0])  # Salida: Poción de Salud
print(bolsa_botin[2])  # Salida: Runa de Bomba

# Rebanado
zonas = ['Bosque de Cenizas', 'Cascadas Luminosas', 'Pico de Brasa', 'Breva del Ocaso', 'Everest', 'Puerta de Escarcha', 'Puente Dorado']
print(zonas[1:4])  # Salida: ['Cascadas Luminosas', 'Pico de Brasa', 'Breva del Ocaso']
```


### Métodos Comunes de Lista

- `.append(item)`: Agrega un elemento al final de la lista.
    
- `.insert(index, item)`: Inserta un elemento en un índice específico.
    
- `.pop(index)`: Elimina y retorna un elemento de un índice específico (elimina el último elemento si no se pasa ningún índice).
    
- `len(list)`: Retorna el número total de elementos de la lista.
    


Python

```python
pendientes = ['Fabricar una poción de salud', 'Explorar el Bosque de Cenizas', 'Subir de nivel en la hoguera']

pendientes.append('Limpiar la Fortaleza Hundida')
pendientes.insert(2, 'Reclutar a un miembro del grupo')
pendientes.pop(4)

print(len(pendientes))  # Salida: 4
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
def linear_search(lista_entrada, valor_objetivo):
    for elemento in lista_entrada:
        if elemento == valor_objetivo:
            return True
    return False

lista_gremio = [
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

print(linear_search(lista_gremio, 'nyx@arcanist.gg'))   # Salida: True
print(linear_search(lista_gremio, 'mark.scout@gg.gg'))  # Salida: False
```


## 3. Eficiencia Algorítmica

- **Mejor Caso — $O(1)$:** El elemento objetivo está justo al principio de la lista. La búsqueda termina de inmediato en 1 paso.
    
- **Peor Caso — $O(N)$:** El elemento objetivo está al final de la lista o no está presente en ella. El algoritmo debe revisar cada elemento ($N$ operaciones) antes de concluir.
