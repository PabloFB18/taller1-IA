import nodo
import controlador
import re

import minimax


def opcion_valida(opcion):
    if opcion is None:
        return 1
    pattern = re.compile("^[1-3]$")
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
    jugada = list(raw_input('Realice una jugada: a,b,c: ').replace(',', ''))

    # Validacion jugada invalida.
    while not controlador.jugada_valida(jugada, estado_actual):
        print 'Jugada invalida'
        jugada = list(raw_input('Realice una jugada: a,b,c: ').replace(',', ''))

    return jugada


def opcion_valida_orden(opcion_orden):
    if opcion_orden is None:
        return 1
    pattern = re.compile("^[1-2]$")
    if not pattern.match(opcion_orden):
        return 1
    return 0


def main():

    print 'Hola'
    opcion_principal = 0
    # menu
    while opcion_principal != 3:

        # Preguntar por la opcion.
        opcion_principal = raw_input('Opciones: minimax[1], poda alfa-beta[2], salir[3]: ')
        # Verificar opcion valida.
        while opcion_valida(opcion_principal):
            print 'Opcion invalida'

            opcion_principal = raw_input('Opciones: minimax[1], poda alfa-beta[2], salir[3]: ')
        opcion_principal = int(opcion_principal)

        # Opcion 1: minimax.
        if opcion_principal == 1:

            # Preguntar quien juega primero.
            opcion_orden = raw_input('Opciones: jugar primero[1], jugar segundo[2]: ')
            # Verificar opcion valida.
            while opcion_valida_orden(opcion_orden):
                print 'Opcion invalida'

                opcion_orden = raw_input('Opciones: jugar primero[1], jugar segundo[2]: ')
            opcion_orden = int(opcion_orden)

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
                        print 'Has sido derrotado'
                        break

                    print 'Pensando...'

                    # Jugada IA.
                    estado_actual.estado = controlador.jugar_minimax(estado_actual)

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        # Imprimir el estado del juego.
                        print estado_actual.estado
                        print 'Has ganado'
                        break

                print 'juego terminado'

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
                        print 'Has ganado'
                        break

                    # Imprimir el estado del juego.
                    print estado_actual.estado

                    # Pociciones [a, b, c] del juego.
                    # Jugada persona
                    estado_actual.estado = realizar_jugada(estado_actual)

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        print 'Has sido derrotado'
                        break

                print 'juego terminado'

        # Jugar poda alfa-beta
        if opcion_principal == 2:

            # Preguntar quien juega primero.
            opcion_orden = raw_input('Opciones: jugar primero[1], jugar segundo[2]: ')
            # Verificar opcion valida.
            while opcion_valida_orden(opcion_orden):
                print 'Opcion invalida'

                opcion_orden = raw_input('Opciones: jugar primero[1], jugar segundo[2]: ')
            opcion_orden = int(opcion_orden)

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
                        print 'Has sido derrotado'
                        break

                    print 'Pensando...'

                    # Jugada IA.
                    estado_actual.estado = controlador.jugar_alpha_beta(estado_actual)

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        # Imprimir el estado del juego.
                        print estado_actual.estado
                        print 'Has ganado'
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
                        print 'Has ganado'
                        break

                    # Imprimir el estado del juego.
                    print estado_actual.estado

                    # Pociciones [a, b, c] del juego.
                    # Jugada persona
                    estado_actual.estado = realizar_jugada(estado_actual)

                    # Termino de la partida.
                    if estado_actual.estado_final():
                        print 'Has sido derrotado'
                        break

                print 'juego terminado'

    print 'Chao'


if __name__ == '__main__':
    main()
