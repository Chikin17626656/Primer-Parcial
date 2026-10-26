"""NotaFacil: gestor de notas por consola para el Instituto Horizonte.

Responde a la pregunta: en que orden hacemos las cosas? Coordina el
menu y la interaccion con el usuario. No sabe como se valida ni como se
calcula nada: le pregunta a validaciones.py y a procesamiento.py.

Se ejecuta con: python main.py
"""

import validaciones
import procesamiento


def pedir_cantidad_alumnos() -> int:
    """Pide la cantidad de alumnos (1 a 30) hasta que sea valida."""
    texto = input("Cantidad de alumnos (1 a 30): ")
    while not validaciones.es_cantidad_valida(texto):
        print("Error: ingresa un numero entero entre 1 y 30.")
        texto = input("Cantidad de alumnos (1 a 30): ")
    return int(texto)


def pedir_nombre(numero_alumno: int) -> str:
    """Pide el nombre de un alumno hasta que sea válido."""
    mensaje = "Nombre del alumno " + str(numero_alumno) + ": "
    nombre = input(mensaje)
    while not validaciones.es_nombre_valido(nombre):
        print("Error: minimo 5 caracteres, solo letras y espacios.")
        nombre = input(mensaje)
    return nombre


def pedir_nota(descripcion: str) -> int:
    """Pide una nota entera de 0 a 10 hasta que sea valida."""
    mensaje = "Nota del " + descripcion + " (0 a 10): "
    texto = input(mensaje)
    while not validaciones.es_nota_valida(texto):
        print("Error: ingresa un numero entero entre 0 y 10.")
        texto = input(mensaje)
    return int(texto)


def cargar_alumnos(nombres: list, notas_1: list, notas_2: list) -> None:
    """Pide los datos de cada alumno y los guarda en las listas.

    Las listas llegan con un lugar por alumno. Esta funcion completa
    cada lugar y no devuelve nada: como las listas son mutables, los
    cambios se ven en quien la llamo.
    """
    for i in range(len(nombres)):
        print()
        nombres[i] = pedir_nombre(i + 1)
        notas_1[i] = pedir_nota("parcial 1")
        notas_2[i] = pedir_nota("parcial 2")


def mostrar_menu() -> None:
    """Muestra las opciones del menu principal."""
    print()
    print("===== NOTAFACIL =====")
    print()
    print("1. Cargar alumnos")
    print("2. Mostrar listado")
    print("3. Mostrar estadísticas")
    print("4. Ver ranking (ordenado)")
    print("5. Buscar alumno")
    print("6. Juegos con un nombre")
    print("0. Salir")


def mostrar_alumno(nombre: str, nota_1: int, nota_2: int,
                   promedio: float) -> None:
    """Imprime los datos de un alumno en una línea."""
    texto_promedio = procesamiento.formatear_decimales(promedio)
    print(nombre + " | Parcial 1: " + str(nota_1)
          + " | Parcial 2: " + str(nota_2)
          + " | Promedio: " + texto_promedio)


def mostrar_listado(nombres: list, notas_1: list, notas_2: list,
                    promedios: list) -> None:
    """Muestra todos los alumnos en el orden en que se cargaron."""
    print()
    print("--- Listado de alumnos ---")
    for i in range(len(nombres)):
        mostrar_alumno(nombres[i], notas_1[i], notas_2[i], promedios[i])


def mostrar_estadisticas(nombres: list, promedios: list) -> None:
    """Muestra promedio general, mejor y peor promedio y condiciones."""
    promedio_general = procesamiento.calcular_promedio_general(promedios)
    indice_mejor = procesamiento.buscar_indice_mejor_promedio(promedios)
    indice_peor = procesamiento.buscar_indice_peor_promedio(promedios)
    promocionan = procesamiento.contar_promocionan(promedios)
    aprueban = procesamiento.contar_aprueban(promedios)
    desaprueban = procesamiento.contar_desaprueban(promedios)
    texto_general = procesamiento.formatear_decimales(promedio_general)
    texto_mejor = procesamiento.formatear_decimales(promedios[indice_mejor])
    texto_peor = procesamiento.formatear_decimales(promedios[indice_peor])
    print()
    print("--- Estadisticas del curso ---")
    print("Promedio general: " + texto_general)
    print("Mejor promedio: " + texto_mejor
          + " (" + nombres[indice_mejor] + ")")
    print("Peor promedio: " + texto_peor
          + " (" + nombres[indice_peor] + ")")
    print("Promocionan (promedio >= 6): " + str(promocionan))
    print("Aprueban (promedio >= 4 y < 6): " + str(aprueban))
    print("Desaprueban (promedio < 4): " + str(desaprueban))


def mostrar_ranking(nombres: list, notas_1: list, notas_2: list,
                    promedios: list) -> None:
    """Muestra el ranking sin alterar el orden original de la carga."""
    # Las listas son mutables: se ordenan copias para no pisar las
    # originales, que se siguen mostrando en orden de carga.
    nombres_ord = procesamiento.copiar_lista(nombres)
    notas_1_ord = procesamiento.copiar_lista(notas_1)
    notas_2_ord = procesamiento.copiar_lista(notas_2)
    promedios_ord = procesamiento.copiar_lista(promedios)
    procesamiento.ordenar_burbuja(
        nombres=nombres_ord,
        notas_1=notas_1_ord,
        notas_2=notas_2_ord,
        promedios=promedios_ord,
    )
    print()
    print("--- Ranking: del mejor al peor promedio ---")
    for i in range(len(nombres_ord)):
        texto_promedio = procesamiento.formatear_decimales(promedios_ord[i])
        print(str(i + 1) + ". " + nombres_ord[i]
              + " - Promedio: " + texto_promedio)


def buscar_alumno_por_nombre(nombres: list, notas_1: list,
                             notas_2: list, promedios: list) -> None:
    """Pide un nombre y muestra las notas del alumno si existe."""
    nombre_buscado = input("Nombre del alumno a buscar: ")
    indice = procesamiento.buscar_alumno(nombres, nombre_buscado)
    print()
    if indice == procesamiento.NO_ENCONTRADO:
        print("El alumno \"" + nombre_buscado + "\" no existe.")
    else:
        mostrar_alumno(nombres[indice], notas_1[indice],
                       notas_2[indice], promedios[indice])


def jugar_con_nombre() -> None:
    """Pide un nombre y muestra sus vocales y el nombre invertido."""
    nombre = input("Nombre del alumno: ")
    print()
    print("Vocales: " + str(procesamiento.contar_vocales(nombre)))
    print("Invertido: " + procesamiento.invertir_cadena(nombre))


def main() -> None:
    """Ejecuta el menú principal hasta que se elige salir."""
    nombres = []
    notas_1 = []
    notas_2 = []
    promedios = []
    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Elegi una opcion: ")
        match opcion:
            case "2" | "3" | "4" | "5" if len(nombres) == 0:
                # Guard: estas opciones necesitan alumnos cargados
                print("Primero tenes que cargar alumnos (opcion 1).")
            case "1":
                cantidad = pedir_cantidad_alumnos()
                nombres = procesamiento.crear_lista(cantidad, "")
                notas_1 = procesamiento.crear_lista(cantidad, 0)
                notas_2 = procesamiento.crear_lista(cantidad, 0)
                cargar_alumnos(nombres, notas_1, notas_2)
                promedios = procesamiento.calcular_promedios(
                    notas_1, notas_2
                )
                print()
                print("Se cargaron " + str(cantidad) + " alumnos.")
            case "2":
                mostrar_listado(nombres, notas_1, notas_2, promedios)
            case "3":
                mostrar_estadisticas(nombres, promedios)
            case "4":
                mostrar_ranking(nombres, notas_1, notas_2, promedios)
            case "5":
                buscar_alumno_por_nombre(nombres, notas_1, notas_2,
                                         promedios)
            case "6":
                jugar_con_nombre()
            case "0":
                print("Hasta luego!")
            case _:
                print("Opcion invalida. Elegi un numero del menu.")


main()
