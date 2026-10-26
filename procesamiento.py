"""Procesamiento de datos de NotaFacil.

Responde a la pregunta: que hacemos con los alumnos? Promedios,
estadisticas, ordenamiento burbuja, busqueda y funciones sobre cadenas.
Ninguna funciin usa variables globales: todo entra por parimetros y
sale por return (o se modifica la lista recibida, que es mutable).
"""

PROMEDIO_PROMOCION = 6
PROMEDIO_APROBACION = 4
NO_ENCONTRADO = -1
VOCALES = "aeiouAEIOU"


def crear_lista(cantidad: int, valor_inicial) -> list:
    """Devuelve una lista con 'cantidad' lugares, todos iguales."""
    lista = []
    for i in range(cantidad):
        lista = lista + [valor_inicial]
    return lista


def calcular_promedio_alumno(nota_1: int, nota_2: int) -> float:
    """Devuelve el promedio de las dos notas de un alumno."""
    return (nota_1 + nota_2) / 2


def calcular_promedios(notas_1: list, notas_2: list) -> list:
    """Devuelve una lista nueva con el promedio de cada alumno."""
    promedios = []
    for i in range(len(notas_1)):
        promedio = calcular_promedio_alumno(notas_1[i], notas_2[i])
        promedios = promedios + [promedio]
    return promedios


def calcular_promedio_general(promedios: list) -> float:
    """Devuelve el promedio general del curso (acumulador)."""
    acumulador = 0
    for i in range(len(promedios)):
        acumulador = acumulador + promedios[i]
    return acumulador / len(promedios)


def buscar_indice_mejor_promedio(promedios: list) -> int:
    """Devuelve la posicion del mayor promedio (maximo).

    Se parte del primer elemento y no de 0, asi funciona con
    cualquier valor. Requiere una lista con al menos un elemento.
    """
    indice_maximo = 0
    for i in range(1, len(promedios)):
        if promedios[i] > promedios[indice_maximo]:
            indice_maximo = i
    return indice_maximo


def buscar_indice_peor_promedio(promedios: list) -> int:
    """Devuelve la posicion del menor promedio (minimo).

    Mismo esquema que el maximo, con el operador invertido.
    """
    indice_minimo = 0
    for i in range(1, len(promedios)):
        if promedios[i] < promedios[indice_minimo]:
            indice_minimo = i
    return indice_minimo


def contar_promocionan(promedios: list) -> int:
    """Devuelve cuantos alumnos promocionan: promedio >= 6 (contador)."""
    cantidad = 0
    for i in range(len(promedios)):
        if promedios[i] >= PROMEDIO_PROMOCION:
            cantidad = cantidad + 1
    return cantidad


def contar_aprueban(promedios: list) -> int:
    """Devuelve cuantos alumnos aprueban: promedio >= 4 y < 6."""
    cantidad = 0
    for i in range(len(promedios)):
        if (promedios[i] >= PROMEDIO_APROBACION
                and promedios[i] < PROMEDIO_PROMOCION):
            cantidad = cantidad + 1
    return cantidad


def contar_desaprueban(promedios: list) -> int:
    """Devuelve cuantos alumnos desaprueban: promedio < 4."""
    cantidad = 0
    for i in range(len(promedios)):
        if promedios[i] < PROMEDIO_APROBACION:
            cantidad = cantidad + 1
    return cantidad


def copiar_lista(lista: list) -> list:
    """Devuelve una copia independiente, armada elemento por elemento."""
    copia = []
    for i in range(len(lista)):
        copia = copia + [lista[i]]
    return copia


def ordenar_burbuja(nombres: list, notas_1: list, notas_2: list,
                    promedios: list) -> None:
    """Ordena las cuatro listas de mejor a peor promedio (burbuja).

    Modifica las listas recibidas y no devuelve nada. Cada intercambio
    mueve juntos nombre, notas y promedio, para que los datos de un
    alumno no se mezclen con los de otro.
    """
    cantidad = len(promedios)
    for pasada in range(cantidad - 1):
        hubo_intercambio = False
        for i in range(cantidad - 1 - pasada):
            if promedios[i] < promedios[i + 1]:
                auxiliar = promedios[i]
                promedios[i] = promedios[i + 1]
                promedios[i + 1] = auxiliar

                auxiliar = nombres[i]
                nombres[i] = nombres[i + 1]
                nombres[i + 1] = auxiliar

                auxiliar = notas_1[i]
                notas_1[i] = notas_1[i + 1]
                notas_1[i + 1] = auxiliar

                auxiliar = notas_2[i]
                notas_2[i] = notas_2[i + 1]
                notas_2[i + 1] = auxiliar

                hubo_intercambio = True
        # Si una pasada completa no intercambió nada, ya está ordenado
        if not hubo_intercambio:
            break


def buscar_alumno(nombres: list, nombre_buscado: str) -> int:
    """Devuelve la posición del alumno, o -1 si no existe."""
    for i in range(len(nombres)):
        if nombres[i] == nombre_buscado:
            return i
    return NO_ENCONTRADO


def es_vocal(caracter: str) -> bool:
    """Devuelve True si el caracter es una vocal (con o sin tilde)."""
    for i in range(len(VOCALES)):
        if caracter == VOCALES[i]:
            return True
    return False


def contar_vocales(texto: str) -> int:
    """Devuelve la cantidad de vocales del texto (contador)."""
    cantidad = 0
    for i in range(len(texto)):
        if es_vocal(texto[i]):
            cantidad = cantidad + 1
    return cantidad


def invertir_cadena(texto: str) -> str:
    """Devuelve el texto escrito de atrás para adelante."""
    invertido = ""
    for i in range(len(texto) - 1, -1, -1):
        invertido = invertido + texto[i]
    return invertido


def formatear_decimales(numero: float) -> str:
    """Devuelve el numero (>= 0) como texto con dos decimales.

    Redondea a centesimas usando solo aritmetica: 7.5 se muestra "7.50".
    """
    centesimas = int(numero * 100 + 0.5)
    parte_entera = centesimas // 100
    parte_decimal = centesimas % 100
    texto_decimal = str(parte_decimal)
    if parte_decimal < 10:
        texto_decimal = "0" + texto_decimal
    return str(parte_entera) + "." + texto_decimal
