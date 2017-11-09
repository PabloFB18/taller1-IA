# -*- coding: utf-8 -*-import controlador
import re

import controlador


def opcion_valida(opcion):
    if opcion is None:
        return 1
    pattern = re.compile('^[1-4]$')
    if not pattern.match(opcion):
        return 1
    return 0
    # else:
    #     opcion = int(opcion)
    # if opcion == 1:
    #     return 0
    # if opcion == 2:
    #     return 0
    # if opcion == 3:
    #     return 0
    # return 1


def realizar_jugada(estado_actual):
    # Recibir jugada.
    jugada = list(raw_input('Realice una jugada: ').replace(',', ''))

    # Validacion jugada invalida.
    while not controlador.jugada_valida(jugada, estado_actual):
        print 'Jugada invalida'
        jugada = list(raw_input('Realice una jugada: ').replace(',', ''))

    return jugada


def opcion_valida_orden(opcion_orden):
    if opcion_orden is None:
        return 1
    pattern = re.compile('^[1-2]$')
    if not pattern.match(opcion_orden):
        return 1
    return 0


def instrucciones():
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


def main():

    print ' '
    print 'Bienvenido al juego de NIM'
    print ' '

    opcion_principal = 0
    # menu
    while opcion_principal != 4:

        # Preguntar por la opcion.
        opcion_principal = raw_input('Opciones: minimax[1], poda alfa-beta[2], intrucciones[3], salir[4]: ')
        # Verificar opcion valida.
        while opcion_valida(opcion_principal):
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
            while opcion_valida_orden(opcion_orden):
                print 'Opcion invalida'

                opcion_orden = raw_input('Opciones: jugar primero[1], jugar segundo[2]: ')
            opcion_orden = int(opcion_orden)

            print ' '

            # Jugar primero.
            if opcion_orden == 1:

                # Crear el juego.
                estado_actual = controlador.estado_inicial()

                while 1:
                    # Imprimir el estado del juego.
                    print estado_actual.estado

                    # Pociciones [a, b, c] del juego.
                    # Jugada persona
                    estado_actual.estado = realizar_jugada(estado_actual)

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        print ' '
                        print 'Has sido derrotado'
                        print ' '
                        break

                    print 'Pensando...'

                    # Jugada IA.
                    estado_actual.estado = controlador.jugar_minimax(estado_actual)

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        # Imprimir el estado del juego.
                        print estado_actual.estado
                        print ' '
                        print 'Has ganado'
                        print ' '
                        break

            # Jugar segundo.
            else:

                # Crear el juego.
                estado_actual = controlador.estado_inicial()

                while 1:

                    print 'Pensando...'

                    # Jugada IA.
                    estado_actual.estado = controlador.jugar_minimax(estado_actual)

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        # Imprimir el estado del juego.
                        print estado_actual.estado
                        print ' '
                        print 'Has ganado'
                        print ' '
                        break

                    # Imprimir el estado del juego.
                    print estado_actual.estado

                    # Pociciones [a, b, c] del juego.
                    # Jugada persona
                    estado_actual.estado = realizar_jugada(estado_actual)

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        print ' '
                        print 'Has sido derrotado'
                        print ' '
                        break

        # Jugar poda alfa-beta
        if opcion_principal == 2:

            # Preguntar quien juega primero.
            opcion_orden = raw_input('Opciones: jugar primero[1], jugar segundo[2]: ')
            # Verificar opcion valida.
            while opcion_valida_orden(opcion_orden):
                print 'Opcion invalida'

                opcion_orden = raw_input('Opciones: jugar primero[1], jugar segundo[2]: ')
            opcion_orden = int(opcion_orden)

            print ' '

            # Jugar primero.
            if opcion_orden == 1:

                # Crear el juego.
                estado_actual = controlador.estado_inicial()

                while 1:
                    # Imprimir el estado del juego.
                    print estado_actual.estado

                    # Pociciones [a, b, c] del juego.
                    # Jugada persona
                    estado_actual.estado = realizar_jugada(estado_actual)

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        print ' '
                        print 'Has sido derrotado'
                        print ' '
                        break

                    print 'Pensando...'

                    # Jugada IA.
                    estado_actual.estado = controlador.jugar_alpha_beta(estado_actual)

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        # Imprimir el estado del juego.
                        print estado_actual.estado
                        print ' '
                        print 'Has ganado'
                        print ' '
                        break

                print 'juego terminado'

            # Jugar segundo.
            else:

                # Crear el juego.
                estado_actual = controlador.estado_inicial()

                while 1:

                    print 'Pensando...'

                    # Jugada IA.
                    estado_actual.estado = controlador.jugar_alpha_beta(estado_actual)

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        # Imprimir el estado del juego.
                        print estado_actual.estado
                        print ' '
                        print 'Has ganado'
                        print ' '
                        break

                    # Imprimir el estado del juego.
                    print estado_actual.estado

                    # Pociciones [a, b, c] del juego.
                    # Jugada persona
                    estado_actual.estado = realizar_jugada(estado_actual)

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        print ' '
                        print 'Has sido derrotado'
                        print ' '
                        break

    print 'Adios'
    print 'Adios'


if __name__ == '__main__':
    main()
