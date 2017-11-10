# -*- coding: utf-8 -*-import controlador
from time import time
import controlador
import validaciones


def realizar_jugada(estado_actual):
    """
    Recibe la jugada por pantalla.
    :param estado_actual: Estado previo a recibir la nueva jugada.
    :return: Reorna la juada recibida.
    """
    # Recibir jugada.
    jugada = list(raw_input('Realice una jugada: ').replace(',', ''))

    # Validacion jugada invalida.
    while not controlador.jugada_valida(jugada, estado_actual):
        print 'Jugada invalida'
        jugada = list(raw_input('Realice una jugada: ').replace(',', ''))

    return jugada


def instrucciones():
    """
    Instruciones del juego.
    :return: void.
    """
    print ' '
    print 'Instrucciones:'
    print '- El juego consiste en alinear 15 palos de fósforos en tres filas.'
    print '  La primera fila esta compuesta por 7 palos de fósforos,'
    print '  la segunda fila de 5 y la tercera fila de 3.'
    print '- Los adversarios juegan por turnos.'
    print '- Cada jugador puede sacar la cantidad de palos de fósforos que quiera'
    print '  pero siemprede una misma fila.'
    print '- El jugador que saque el último palo de fósforo pierde.'
    print '- Si uno de los jugadores se demora más de 30 segundos en sacar los'
    print '  palos de fósforo pierde.'
    print '- Los palos estan representados por numeros de cada fila, '
    print '  por ejemplo [7,5,3].'
    print '- Para realizar una jugada se debe ingresar los palos de fosforo'
    print '  con el formato "a,b,c"'
    print ' '


def mensaje_derrota():
    """
    Mensaje de derrota.
    :return: void.
    """
    print ' '
    print 'Has sido derrotado'
    print ' '


def mensaje_victoria():
    """
    Mensaje de victoria.
    :return: void.
    """
    print ' '
    print 'Has ganado'
    print ' '


def main():
    """
    Menu del juego con todas las posibles opciones.
    :return: void.
    """
    print ' '
    print 'Bienvenido al juego de NIM'
    print ' '

    opcion_principal = 0
    # menu
    while opcion_principal != 4:

        # Preguntar por la opcion.
        opcion_principal = raw_input('Opciones: minimax[1], poda alfa-beta[2], intrucciones[3], salir[4]: ')
        # Verificar opcion valida.
        while validaciones.opcion_valida(opcion_principal):
            print 'Opcion invalida'

            opcion_principal = raw_input('Opciones: minimax[1], poda alfa-beta[2], instrucciones[3], salir[4]: ')
        opcion_principal = int(opcion_principal)

        # Desplegar instrucciones.
        if opcion_principal == 3:
            instrucciones()

        # Opcion 1: minimax.
        if opcion_principal == 1:

            # Preguntar quien juega primero.
            opcion_orden = raw_input('Opciones: jugar primero[1], jugar segundo[2]: ')
            # Verificar opcion valida.
            while validaciones.opcion_valida_orden(opcion_orden):
                print 'Opcion invalida'
                opcion_orden = raw_input('Opciones: jugar primero[1], jugar segundo[2]: ')

            opcion_orden = int(opcion_orden)

            print ' '

            # Jugar primero.
            if opcion_orden == 1:

                # Crear el juego.
                estado_actual = controlador.estado_inicial()

                # Imprimir el estado del juego.
                print estado_actual.estado

                while 1:

                    # Obtener el tiempo antes de que juegue la persona.
                    tiempo_inicio_jugador = time()

                    # Jugada persona
                    estado_actual.estado = realizar_jugada(estado_actual)

                    # Obtener el tiempo despues de que juegue la persona.
                    tiempo_termino_jugador = time()

                    # En caso de que la jugada demore mas de 30 segundos.
                    if tiempo_termino_jugador - tiempo_inicio_jugador > 30:
                        print ' '
                        print 'Has pasado los 30 segundos, perdiste.'
                        print ' '
                        break

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        mensaje_derrota()
                        break

                    print 'Pensando...'

                    # Obtener el tiempo antes de ejecutar algoritmo.
                    tiempo_inicio_maquina = time()

                    # Jugada IA.
                    estado_actual.estado = controlador.jugar_minimax(estado_actual)

                    # Obtener el tiempo despues de ejecutar algoritmo.
                    tiempo_termino_maquina = time()

                    # En caso de que la jugada demore mas de 30 segundos.
                    if tiempo_termino_maquina - tiempo_inicio_maquina > 30:
                        print ' '
                        print 'Han pasado 30 segundos, ganaste.'
                        print ' '
                        break

                    # Imprimir el estado del juego.
                    print estado_actual.estado

                    print 'La jugada demoro: ' + str(tiempo_termino_maquina - tiempo_inicio_maquina) + ' segundos.'

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        mensaje_victoria()
                        break

            # Jugar segundo.
            else:

                # Crear el juego.
                estado_actual = controlador.estado_inicial()

                while 1:

                    print 'Pensando...'

                    # Obtener el tiempo antes de ejecutar algoritmo.
                    tiempo_inicio_maquina = time()

                    # Jugada IA.
                    estado_actual.estado = controlador.jugar_minimax(estado_actual)

                    # Obtener el tiempo despues de ejecutar algoritmo.
                    tiempo_termino_maquina = time()

                    # En caso de que la jugada demore mas de 30 segundos.
                    if tiempo_termino_maquina - tiempo_inicio_maquina > 30:
                        print ' '
                        print 'Han pasado 30 segundos, ganaste.'
                        print ' '
                        break

                    # Imprimir el estado del juego.
                    print estado_actual.estado

                    print 'La jugada demoro: ' + str(tiempo_termino_maquina - tiempo_inicio_maquina) + ' segundos.'

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        mensaje_victoria()
                        break

                    # Obtener el tiempo antes de que juegue la persona.
                    tiempo_inicio_jugador = time()

                    # Jugada persona
                    estado_actual.estado = realizar_jugada(estado_actual)

                    # Obtener el tiempo despues de que juegue la persona.
                    tiempo_termino_jugador = time()

                    # En caso de que la jugada demore mas de 30 segundos.
                    if tiempo_termino_jugador - tiempo_inicio_jugador > 30:
                        print ' '
                        print 'Has pasado los 30 segundos, perdiste.'
                        print ' '
                        break

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        mensaje_derrota()
                        break

        # Jugar poda alfa-beta
        if opcion_principal == 2:

            # Preguntar quien juega primero.
            opcion_orden = raw_input('Opciones: jugar primero[1], jugar segundo[2]: ')
            # Verificar opcion valida.
            while validaciones.opcion_valida_orden(opcion_orden):
                print 'Opcion invalida'

                opcion_orden = raw_input('Opciones: jugar primero[1], jugar segundo[2]: ')
            opcion_orden = int(opcion_orden)

            print ' '

            # Jugar primero.
            if opcion_orden == 1:

                # Crear el juego.
                estado_actual = controlador.estado_inicial()

                # Imprimir el estado del juego.
                print estado_actual.estado

                while 1:

                    # Obtener el tiempo antes de que juegue la persona.
                    tiempo_inicio_jugador = time()

                    # Jugada persona
                    estado_actual.estado = realizar_jugada(estado_actual)

                    # Obtener el tiempo despues de que juegue la persona.
                    tiempo_termino_jugador = time()

                    # En caso de que la jugada demore mas de 30 segundos.
                    if tiempo_termino_jugador - tiempo_inicio_jugador > 30:
                        print ' '
                        print 'Has pasado los 30 segundos, perdiste.'
                        print ' '
                        break

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        mensaje_derrota()
                        break

                    print 'Pensando...'

                    # Obtener el tiempo antes de ejecutar algoritmo.
                    tiempo_inicio_maquina = time()

                    # Jugada IA.
                    estado_actual.estado = controlador.jugar_alpha_beta(estado_actual)

                    # Obtener el tiempo despues de ejecutar algoritmo.
                    tiempo_termino_maquina = time()

                    # En caso de que la jugada demore mas de 30 segundos.
                    if tiempo_termino_maquina - tiempo_inicio_maquina > 30:
                        print ' '
                        print 'Han pasado 30 segundos, ganaste.'
                        print ' '
                        break

                    # Imprimir el estado del juego.
                    print estado_actual.estado

                    print 'La jugada demoro: ' + str(tiempo_termino_maquina - tiempo_inicio_maquina) + ' segundos.'

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        mensaje_victoria()
                        break

            # Jugar segundo.
            else:

                # Crear el juego.
                estado_actual = controlador.estado_inicial()

                while 1:

                    print 'Pensando...'

                    # Obtener el tiempo antes de ejecutar algoritmo.
                    tiempo_inicio_maquina = time()

                    # Jugada IA.
                    estado_actual.estado = controlador.jugar_alpha_beta(estado_actual)

                    # Obtener el tiempo despues de ejecutar algoritmo.
                    tiempo_termino_maquina = time()

                    # En caso de que la jugada demore mas de 30 segundos.
                    if tiempo_termino_maquina - tiempo_inicio_maquina > 30:
                        print ' '
                        print 'Han pasado 30 segundos, ganaste.'
                        print ' '
                        break

                    # Imprimir el estado del juego.
                    print estado_actual.estado

                    print 'La jugada demoro: ' + str(tiempo_termino_maquina - tiempo_inicio_maquina) + ' segundos.'

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        mensaje_victoria()
                        break

                    # Obtener el tiempo antes de que juegue la persona.
                    tiempo_inicio_jugador = time()

                    # Jugada persona
                    estado_actual.estado = realizar_jugada(estado_actual)

                    # Obtener el tiempo despues de que juegue la persona.
                    tiempo_termino_jugador = time()

                    # En caso de que la jugada demore mas de 30 segundos.
                    if tiempo_termino_jugador - tiempo_inicio_jugador > 30:
                        print ' '
                        print 'Has pasado los 30 segundos, perdiste.'
                        print ' '
                        break

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        mensaje_derrota()
                        break

    print ' '
    print 'Adios'


if __name__ == '__main__':
    main()
