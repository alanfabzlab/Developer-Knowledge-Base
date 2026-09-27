
# 04. Flujo Avanzado y PRs

**Versión original en inglés:** [04 - Advanced Workflow & PRs.md](./04%20-%20Advanced%20Workflow%20&%20PRs.md)

**Curso:** Git & GitHub
**Tema:** Merge, resolución de conflictos y pull requests (PR)
**Etiquetas:** `#git` `#pull-requests` `#merging`



## 1. Merge de Ramas y Gestión de Conflictos

El merge combina los cambios de una rama en otra (por ejemplo, traer las actualizaciones de `main` a una rama de funcionalidad o viceversa)[cite: 70, 71].

Bash

```bash
# Bring updates from main into your current working branch
git checkout main
git pull
git checkout <your-feature-branch>
git merge main
```


### Conflictos de Merge

Ocurren cuando se realizan cambios en la misma parte de un archivo en diferentes ramas, o cuando una rama elimina un archivo que otra rama modificó. Los editores de código ofrecen opciones para resolverlos:

- **Accept Incoming Changes:** Sobrescribe los cambios locales con los de la rama que se está fusionando.
    
- **Accept Current Changes:** Conserva los cambios de la rama local e ignora los cambios fusionados.
    
- **Accept Both Changes:** Conserva ambas versiones del código modificado.
    


Después de resolver los conflictos, prepara y confirma el código fusionado:

Bash

```bash
git add .
git commit -m "fix(combat): resuelve conflictos de merge en el estado del jefe"
git push origin <your-feature-branch>
```


## 2. Pull Requests (PRs) y Revisión de Código

Un **Pull Request (PR)** propone fusionar el código de una rama/repositorio en otro, lo que permite la revisión del equipo, la discusión y verificaciones automatizadas antes de integrar el código.

### Lista de Verificación para PRs

1. **Traer los Últimos Cambios:** Actualiza el código local (`git pull origin main`).
    
2. **Probar:** Verifica que el juego compile y que la funcionalidad se ejecute sin errores.
    
3. **Revisar:** Limpia el código temporal, los registros de depuración y los archivos innecesarios.
    
4. **Resolver Conflictos:** Asegúrate de que no queden conflictos de merge abiertos.
    


## 3. Flujo de Contribución a Código Abierto

Proceso estándar para contribuir a repositorios externos de motores de videojuegos o de equipos:

1. **Haz fork** del repositorio original a tu cuenta de GitHub.
    
2. **Clona** tu fork localmente: `git clone <fork-url>`.
    
3. **Crea una rama** para los cambios: `git switch -c feature-name`.
    
4. **Haz commit y push** de las actualizaciones a tu fork.
    
5. **Abre un Pull Request** contra la rama `main` del proyecto original.

