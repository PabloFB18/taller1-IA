import minimax

import nodo
import alphaBeta


def jugar_minimax(estado):
    return minimax.jugar(estado)


def jugar_alpha_beta(estado):
    return alphaBeta.jugar(estado)


# def jugar_mejor_jugada(estado):
#     return mejorJugada.jugar(estado)


def estado_inicial():
    """
    Define el estado inicial.
    :return: Tupla con el estado inicial.
    """
    return nodo.nodo([7, 5, 3], 0)
