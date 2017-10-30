import nodo


def obtener_sucesores(estado_actual):
    """
    Obtiene los sucesores.
    :param estado_actual: Estado actual del cual obtendra los sucesores.
    :return: Tupla con los sucesores.
    """
    sucesores = []
    for indice, elem_max in enumerate(estado_actual):
        for elem_new in xrange(elem_max):
            # Creo una copia del estado actual
            estado_aux = estado_actual[:]
            estado_aux[indice] = elem_new
            sucesores.append(nodo.Nodo(estado_aux))
    return sucesores


def jugar(estado_actual):
    """
    Inicia el turno de la IA
    :param estado_actual: Es el estado actual
    :return: Jugada a realizar
    """
    jugadas = [[]]
    alfa = -99
    beta = 99
    maximo(estado_actual, alfa, beta, jugadas)
    return jugadas[0]


def maximo(estado_actual, alfa, beta, jugadas):
    if estado_actual.estado_objetivo():
        return 0
    if estado_actual.estado_final():
        return 1
    valor_max = -10
    aux = nodo.Nodo([0, 0, 0])
    for sucesor in obtener_sucesores(estado_actual.estado):
        valor = minimo(sucesor, alfa, beta, jugadas)
        # Guardar el maximo de los sucesores para saber cual camino seguir.
        if valor > valor_max:
            aux = sucesor
            valor_max = valor
        # Verificar si se debe modificar el valor de alfa
        if valor > alfa:
            alfa = valor
        # Verificar si se debe hacer poda.
        if valor >= beta:
            break
    jugadas[0] = aux.estado
    return valor_max


def minimo(estado_actual, alfa, beta, jugadas):
    if estado_actual.estado_objetivo():
        return 1
    if estado_actual.estado_final():
        return 0
    valor_min = 10
    aux = nodo.Nodo([0, 0, 0])
    for sucesor in obtener_sucesores(estado_actual.estado):
        valor = maximo(sucesor, alfa, beta, jugadas)
        # Guardar el minimo de los sucesores para saber cual camino seguir.
        if valor < valor_min:
            aux = sucesor
            valor_min = valor
            # Verificar si se debe modificar el valor de alfa
            if valor < beta:
                beta = valor
            # Verificar si se debe hacer poda.
            if valor <= alfa:
                break
    jugadas[0] = aux.estado
    return valor_min
