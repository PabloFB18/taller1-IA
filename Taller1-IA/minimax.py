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
        # Obtiene el numero en binario.
        bin_str = "{0:b}".format(estado_evaluar[i])
        bin_lista = []
        # Guarda el numero binario como una lista.
        for j in range(0, len(bin_str)):
            bin_lista.append(bin_str[j])
        # Rellena con ceros si es necesario.
        if len(bin_lista) < 3:
            while len(bin_lista) < 3:
                bin_lista = ['0'] + bin_lista
        # Suma los numeros binarios sin acarreo
        for j in range(0, 3):
            sum_bin[j] = sumar(sum_bin[j], int(bin_lista[j]))
    # Si resultado de la suma es igual a cero
    if sum(sum_bin) == 0:
        return 1
    return 0


def suma_lista(estado_evaluar):
    """
    Suma de los elementos de la lista.
    :param estado_evaluar: Lista de enteros a sumar.
    :return: Resultado de la suma.
    """
    suma = 0
    for elem in estado_evaluar:
        suma += elem
    return suma


def suma_ceros(estado_evaluar):
    """
    Calcula la cantidad de ceros en un estado.
    :param estado_evaluar: Lista con el estado.
    :return: Cantidad de ceros.
    """
    sum_ceros = 0
    for elem in estado_evaluar:
        if elem == 0:
            sum_ceros += 1
    return sum_ceros


def suma_unos(estado_evaluar):
    """
    Calcula la cantidad de unos en un estado.
    :param estado_evaluar: Lista con el estado.
    :return: Cantidad de unos.
    """
    sum_unos = 0
    for elem in estado_evaluar:
        if elem == 1:
            sum_unos += 1
    return sum_unos


def evaluar_jugada(estado_evaluar):
    """
    Heuristica: Retorna un valor de acuerdo a lo buena que es la posicion evaluada.
    :param estado_evaluar: Estado que se evaluara con la funcion heuristica.
    :return: Valor entregado por la funcion heuristica.
    """
    # Caso especial que lleva una victoria.
    if estado_objetivo(estado_evaluar):
        return -50
    # Caso especial que lleva una derrota.
    if estado_final(estado_evaluar):
        return 50
    # Caso especial que lleva una derrota.
    if suma_ceros(estado_evaluar) == 2:
        return -45
    # Caso especial que lleva una derrota.
    if suma_unos(estado_evaluar) == 2:
        return -45
    # Caso especial que lleva una victoria.
    if suma_unos(estado_evaluar) == 3:
        return 45
    # Evaluacion de la jugada.
    if posicion_ventaja(estado_evaluar):
        # Jugada que lleva a una victoria.
        return 40 - suma_lista(estado_evaluar)
    # Jugada que lleva a una derrota.
    return suma_lista(estado_evaluar)


def obtener_sucesores(estado_actual):
    """
    Obtiene los sucesores.
    Reglas:
    - Se conservan solo los sucesores con el mayor y menor valor de la heuristica.
    :param estado_actual: Estado actual del cual obtendra los sucesores.
    :return: Lista con los sucesores.
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

    # Guardar los sucesores.
    sucesores.append(min_nodo)
    sucesores.append(max_nodo)
    return sucesores


def jugar(estado_actual):
    """
    Inicia el turno de la IA.
    :param estado_actual: Es el estado actual a evaluar.
    :return: Jugada que se debe realizar.
    """
    # Variable donde se guarda la jugada a realizar, se pasa al max y min como corresponda.
    jugadas = [[0, 0, 0]]
    maximo(estado_actual, jugadas)
    return jugadas[0]


def maximo(estado_actual, jugadas):
    """
    Retorna la jugada con mayor valor de la heuristica.
    :param estado_actual: Jugada a evaluar.
    :param jugadas: Variable donde se guarda la jugada a realizar.
    :return: Valor de laheuristica.
    """
    if estado_actual.estado_objetivo():
        return estado_actual.heuristica
    if estado_actual.estado_final():
        return estado_actual.heuristica
    # Obtener los sucesores.
    valor_max = -100
    aux = nodo.Nodo([0, 0, 0])
    for sucesor in obtener_sucesores(estado_actual.estado):
        valor = minimo(sucesor, jugadas)
        # Guardar la mejor jugada.
        if valor >= valor_max:
            aux = sucesor
            valor_max = valor
    # Guardar la posible jugada a realizar.
    jugadas[0] = aux.estado
    return valor_max


def minimo(estado_actual, jugadas):
    """
    Reorna la jugada con menor valor de la heuristica.
    :param estado_actual: Jugada a evaluar.
    :param jugadas: Variable donde se guarda la jugada a realizar.
    :return: Valor de laheuristica.
    """
    if estado_actual.estado_objetivo():
        return estado_actual.heuristica * -1
    if estado_actual.estado_final():
        return estado_actual.heuristica * -1
    # Obtener los sucesores.
    valor_min = 100
    aux = nodo.Nodo([0, 0, 0])
    for sucesor in obtener_sucesores(estado_actual.estado):
        # Guardar la peor jugada.
        valor = maximo(sucesor, jugadas)
        if valor <= valor_min:
            aux = sucesor
            valor_min = valor
    # Guardar la posible jugada a realizar.
    jugadas[0] = aux.estado
    return valor_min
