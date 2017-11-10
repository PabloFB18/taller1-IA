import re
import minimax
import nodo
import alphaBeta


def jugar_minimax(estado):
    """
    Llama la funcion jugar de minimax
    :param estado: Recibe la jugada que debe maximisar.
    :return: Entrega la jugada que se debe realizar.
    """
    return minimax.jugar(estado)


def jugar_alpha_beta(estado):
    """
    Llama la funcion jugar de poda alfa-beta
    :param estado: Recibe la jugada que debe maximisar.
    :return: Entrega la jugada que se debe realizar.
    """
    return alphaBeta.jugar(estado)


def estado_inicial():
    """
    Define el estado inicial.
    :return: Instancia del nodo con el estado inicial.
    """
    return nodo.Nodo([7, 5, 3])


def jugada_valida(jugada, estado_actual):
    """
    Validacion de la jugada ingresada.
    :param jugada: La nueva jugada.
    :param estado_actual: El estado previo a realizarse la jugada.
    :return: Verdadero si la jugada es valida y falso si no lo es
    """
    if jugada is None:
        return 0
    # Definicion expresion regular para validar que la jugada cmpe el formato
    pattern = re.compile("^\['[0-7]', '[0-5]', '[0-3]'\]$")

    if not pattern.match(str(jugada)):
        return 0

    # Pasar datos de la lista de string a entero.
    for indice in range(0, len(jugada)):
        jugada[indice] = int(jugada[indice])

    # Verificar jugada valida
    if jugada[0] < estado_actual.estado[0]:
        if jugada[1] == estado_actual.estado[1] and jugada[2] == estado_actual.estado[2]:
            return 1
    if jugada[1] < estado_actual.estado[1]:
        if jugada[0] == estado_actual.estado[0] and jugada[2] == estado_actual.estado[2]:
            return 1
    if jugada[2] < estado_actual.estado[2]:
        if jugada[1] == estado_actual.estado[1] and jugada[0] == estado_actual.estado[0]:
            return 1
    return 0
