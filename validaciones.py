"""Validaciones de NotaFacil.

Responde una sola pregunta: el dato es valido? Todas las funciones
reciben el dato tal como lo escribio el usuario (texto) y devuelven
True o False. No usan input ni print: quien pide y avisa es main.py.
"""

CANTIDAD_MINIMA = 1
CANTIDAD_MAXIMA = 30
NOTA_MINIMA = 0
NOTA_MAXIMA = 10
LARGO_MINIMO_NOMBRE = 5


def es_letra(caracter: str) -> bool:
    """Devuelve True si el caracter es una letra de a-z o A-Z."""
    return ("a" <= caracter <= "z") or ("A" <= caracter <= "Z")


def es_digito(caracter: str) -> bool:
    """Devuelve True si el caracter es un digito de 0 a 9."""
    return "0" <= caracter <= "9"


def es_entero(texto: str) -> bool:
    """Devuelve True si el texto no está vacío y son todos dígitos."""
    if len(texto) == 0:
        return False
    for i in range(len(texto)):
        if not es_digito(texto[i]):
            return False
    return True


def es_cantidad_valida(texto: str) -> bool:
    """Devuelve True si el texto es un entero entre 1 y 30."""
    if not es_entero(texto):
        return False
    return CANTIDAD_MINIMA <= int(texto) <= CANTIDAD_MAXIMA


def es_nota_valida(texto: str) -> bool:
    """Devuelve True si el texto es un entero entre 0 y 10."""
    if not es_entero(texto):
        return False
    return NOTA_MINIMA <= int(texto) <= NOTA_MAXIMA


def es_nombre_valido(nombre: str) -> bool:
    """Devuelve True si el nombre es válido.

    Condiciones: al menos 5 caracteres, y solo letras (a-z, A-Z) y
    espacios. Un nombre hecho solo de espacios no se acepta.
    """
    if len(nombre) < LARGO_MINIMO_NOMBRE:
        return False
    hay_letra = False
    for i in range(len(nombre)):
        if es_letra(nombre[i]):
            hay_letra = True
        elif nombre[i] != " ":
            return False
    return hay_letra
