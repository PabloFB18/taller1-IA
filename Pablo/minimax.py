import nodo


def estado_objetivo(estado):
    """
    Define el estado objetivo.
    :return: Verdadero si es un estado objetivo y falso si no lo es.
    """
    if estado == [1, 0, 0] or estado == [0, 1, 0] or estado == [0, 0, 1]:
        return 1
    else:
        return 0


def estado_final(estado):
    """
    Verifica si es un estado en el que el juego termino.
    :return: Verdadero si el juego termino sino retorna falso.
    """
    if estado == [0, 0, 0]:
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


def posicion_ventaja(estado_evaluar):
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
                bin_lista = ['0'] + bin_lista
        for j in range(0, 3):
            sum_bin[j] = sumar(sum_bin[j], int(bin_lista[j]))
    if sum(sum_bin) == 0:
        return 1
    return 0


def suma_lista(estado_evaluar):
    suma = 0
    for elem in estado_evaluar:
        suma += elem
    return suma


def suma_ceros(estado_evaluar):
    sum_ceros = 0
    for elem in estado_evaluar:
        if elem == 0:
            sum_ceros += 1
    return sum_ceros


def suma_unos(estado_evaluar):
    sum_unos = 0
    for elem in estado_evaluar:
        if elem == 1:
            sum_unos += 1
    return sum_unos


def evaluar_jugada(estado_evaluar):
    """
    Heuristica: si el estado es una posicion de victoria retorna un puntaje 10 sino
    retorna un puntaje de acuerdo a la mayor cantidad de palitos a sacar en una fila.
    :param estado_evaluar: Estado que se evaluara con la funcion heuristica.
    :return: Valor entregado por la funcion heuristica.
    """
    if estado_objetivo(estado_evaluar):
        return -50
    if estado_final(estado_evaluar):
        return 50
    if suma_ceros(estado_evaluar) == 2:
        return -45
    if suma_unos(estado_evaluar) == 2:
        return -45
    if suma_unos(estado_evaluar) == 3:
        return 45
    if posicion_ventaja(estado_evaluar):
        return 40 - suma_lista(estado_evaluar)
    return suma_lista(estado_evaluar)


def obtener_sucesores(estado_actual):
    """
    Obtiene los sucesores.
    Reglas:
    -
    :param estado_actual: Estado actual del cual obtendra los sucesores.
    :return: Tupla con los sucesores.
    """
    sucesores = []

    # obtener solo el maximo y el minimo
    min_heuristica = 100
    min_nodo = nodo.Nodo([0, 0, 0])
    max_heuristica = -100
    max_nodo = nodo.Nodo([0, 0, 0])

    for indice, elem_max in enumerate(estado_actual):
        for elem_new in xrange(elem_max):
            # Creo una copia del estado actual
            estado_aux = estado_actual[:]
            estado_aux[indice] = elem_new

            # Calcular heuristica.
            heuristica = evaluar_jugada(estado_aux)

            # Guardar el menor de los sucesores para el minimo.
            if heuristica < min_heuristica:
                min_heuristica = heuristica
                min_nodo = nodo.Nodo(estado_aux, evaluar_jugada(estado_aux))

            # Guardar el mayor de los sucesores para el maximo.
            if heuristica > max_heuristica:
                max_heuristica = heuristica
                max_nodo = nodo.Nodo(estado_aux, evaluar_jugada(estado_aux))

    sucesores.append(min_nodo)
    sucesores.append(max_nodo)
    return sucesores


def jugar(estado_actual):
    """
    Inicia el turno de la IA
    :param estado_actual: Es el estado actual
    :return: Jugada a realizar
    """
    jugadas = [[0, 0, 0]]
    maximo(estado_actual, jugadas)
    return jugadas[0]


def maximo(estado_actual, jugadas):
    if estado_actual.estado_objetivo():
        return estado_actual.heuristica
    if estado_actual.estado_final():
        return estado_actual.heuristica
    valor_max = -100
    aux = nodo.Nodo([0, 0, 0])
    for sucesor in obtener_sucesores(estado_actual.estado):
        valor = minimo(sucesor, jugadas)
        if valor >= valor_max:
            aux = sucesor
            valor_max = valor
    jugadas[0] = aux.estado
    return valor_max


def minimo(estado_actual, jugadas):
    if estado_actual.estado_objetivo():
        return estado_actual.heuristica * -1
    if estado_actual.estado_final():
        return estado_actual.heuristica * -1
    valor_min = 100
    aux = nodo.Nodo([0, 0, 0])
    for sucesor in obtener_sucesores(estado_actual.estado):
        valor = maximo(sucesor, jugadas)
        if valor <= valor_min:
            aux = sucesor
            valor_min = valor
    jugadas[0] = aux.estado
    return valor_min
