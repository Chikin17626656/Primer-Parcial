# NotaFácil

Gestor de notas por consola para el Instituto Horizonte. Permite cargar los
alumnos de un curso con sus notas de dos parciales y ver al instante el
listado, las estadísticas, el ranking y más, sin hacer cuentas a mano.

## Cómo ejecutarlo

Requiere **Python 3.10 o superior** (el menú usa `match-case`). No hace falta
instalar nada extra.

```
python main.py
```

## Qué hace

Al iniciar muestra un menú que se repite hasta elegir `0`:

| Opción | Acción |
|---|---|
| 1 | Cargar alumnos (cantidad de 1 a 30, nombre y notas de los parciales 1 y 2) |
| 2 | Mostrar el listado en el orden de carga |
| 3 | Mostrar estadísticas del curso |
| 4 | Ver el ranking, del mejor al peor promedio |
| 5 | Buscar un alumno por su nombre |
| 6 | Juegos con un nombre: cuenta las vocales y lo muestra invertido |
| 0 | Salir |

Las opciones 2 a 5 necesitan que primero se hayan cargado alumnos.

**Validaciones:** todos los datos se piden de nuevo hasta que sean válidos.
El nombre debe tener al menos 5 caracteres y solo letras (a-z, A-Z) y
espacios. Las notas son enteros de 0 a 10.

**Estadísticas:** promedio general del curso, mejor y peor promedio (con el
nombre del alumno) y cantidad de alumnos que promocionan (promedio >= 6),
aprueban (>= 4 y < 6) y desaprueban (< 4).

## Organización del proyecto

| Archivo | Contenido |
|---|---|
| `main.py` | El menú principal y el flujo del programa |
| `validaciones.py` | Funciones que validan nombre, notas y cantidad de alumnos |
| `procesamiento.py` | Promedios, estadísticas, ordenamiento burbuja, búsqueda y funciones sobre cadenas |
