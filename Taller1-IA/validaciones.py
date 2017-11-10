import re


def opcion_valida(opcion):
    """
    Validacion de la opcion principal el menu.
    :param opcion: Opcion selecionada.
    :return: Verdadero si opcion es invalida y falso si es valida.
    """
    if opcion is None:
        return 1
    # Definicion expresion regular para validacion
    pattern = re.compile('^[1-4]$')
    if not pattern.match(opcion):
        return 1
    return 0


def opcion_valida_orden(opcion_orden):
    """
    Validacion de la opcion de quien juega primero del menu.
    :param opcion_orden: Opcion selecionada.
    :return: Verdadero si opcion es invalida y falso si es valida.
    """
    if opcion_orden is None:
        return 1
    # Definicion expresion regular para validacion
    pattern = re.compile('^[1-2]$')
    if not pattern.match(opcion_orden):
        return 1
    return 0
