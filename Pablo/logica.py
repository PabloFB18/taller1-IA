from Pablo import nodo


def estado_inicial():
    """
    Define el estado inicial.
    :return: Tupla con el estado inicial.
    """
    return nodo.nodo([7, 5, 3], 0)


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
            sucesores.append(nodo.nodo(estado_aux, evaluar_jugada(estado_aux)))
    return sucesores


def estado_objetivo(estado_consulta):
    """
    Define el estado objetivo.
    :param estado_consulta: Estado que se desea evaluar con el estado objetivo.
    :return: Verdadero si es un estado objetivo y falso si no lo es.
    """
    if estado_consulta == [1, 0, 0] or estado_consulta == [0, 1, 0] or estado_consulta == [0, 0, 1]:
        return 1
    else:
        return 0


def sumar(bin_1, bin_2):
    """
    Suma binaria de un digito.
    :param bin_1: Numero a sumar..
    :param bin_2: Numero a sumar.
    :return: Resultado
    """
    if bin_1 == bin_2:
        return 0
    else:
        return 1


def winning_position(estado_evaluar):
    """
    Determina si el estado a evaluar se encuentra en una pocision de victoria.
    :param estado_evaluar: Estado que se desea evaluar
    :return: True si se encuentra en una posicion de victoria sino falso.
    """
    sum_bin = [0, 0, 0]
    for i in range(0, 3):
        bin_str = "{0:b}".format(estado_evaluar[i])
        bin_lista = []
        for j in range(0, len(bin_str)):
            bin_lista.append(bin_str[j])
        if len(bin_lista) < 3:
            while len(bin_lista) < 3:
                bin_lista.append(0)
            reversed(bin_lista)
        for j in range(0, 3):
            sum_bin[j] = sumar(sum_bin[j], int(bin_lista[j]))
    if sum(sum_bin) == 0:
        return 1
    return 0


def evaluar_jugada(estado_evaluar):
    """
    Heuristica: si el estado es una posicion de victoria retorna un puntaje 10 sino
    retorna un puntaje de acuerdo a la mayor cantidad de palitos a sacar en una fila.
    :param estado_evaluar: Estado que se evaluara con la funcion heuristica.
    :return: Valor entregado por la funcion heuristica.
    """
    if estado_objetivo(estado_evaluar):
        return 50
    if estado_final(estado_evaluar):
        return -50
    if winning_position(estado_evaluar):
        return 20 - max(estado_evaluar)
    return max(estado_evaluar)


def jugar(estado_actual):
    """
    Inicia el turno de la IA
    :param estado_actual: Es el estado actual
    :return: Jugada a realizar
    """
    cont = [0]
    jugadas = list()
    jugadas.append([])
    maximo(estado_actual, jugadas, cont)
    return jugadas[0]


def estado_final(estado_evaluar):
    if estado_evaluar == [0, 0, 0]:
        return 1
    else:
        return 0


def maximo(estado_actual, jugadas, cont):
    cont[0] += 1
    # if cont[0] > 1:
    #     cont[0] = 0
    #     return estado_actual.heuristica
    if estado_final(estado_actual.estado):
        cont[0] = 0
        return estado_actual.heuristica
    valor_max = -99
    aux = nodo.nodo([0, 0, 0], 0)
    for sucesor in obtener_sucesores(estado_actual.estado):
        print str(sucesor.estado) + ' ' + str(sucesor.heuristica)
        # valor = minimo(sucesor, jugadas, cont)
        valor = sucesor.heuristica
        if valor > valor_max:
            aux = sucesor
            valor_max = valor
    jugadas[0] = aux.estado
    # print jugadas[0]
    return valor_max


def minimo(estado_actual, jugadas, cont):
    cont[0] += 1
    # if cont[0] > 1:
    #     cont[0] = 0
    #     return estado_actual.heuristica
    if estado_final(estado_actual.estado):
        cont[0] = 0
        return estado_actual.heuristica
    valor_min = 99
    aux = nodo.nodo([0, 0, 0], 0)
    for sucesor in obtener_sucesores(estado_actual.estado):
        print str(sucesor.estado) + ' ' + str(sucesor.heuristica)
        valor = maximo(sucesor, jugadas, cont)
        if valor < valor_min:
            aux = sucesor
            valor_min = valor
    jugadas[0] = aux.estado
    # print jugadas[0]
    return valor_min
