import controlador
import nodo


def main():

    estado = nodo.Nodo([7, 5, 3])
    estado.estado = controlador.jugar_minimax(estado)
    print 'jugada'
    print estado.estado

    # print 'Hola'
    # opcion = 0
    # # menu
    # while opcion != 3:
    #     # preguntar por la opcion
    #     print 'Opciones: jugar primero[1], jugar segundo[2], salir[3]'
    #     opcion = input()
    #     # verificar opcion valida
    #     while opcion != 1 and opcion != 2 and opcion != 3:
    #         print 'Opciones: jugar primero[1], jugar segundo[2], salir[3]'
    #         opcion = input()
    #
    #     if opcion == 1:
    #         estado_actual = logica.estado_inicial()
    #
    #         while estado_actual != [0, 0, 0]:
    #             print estado_actual.estado
    #             print 'Realice una jugada: columna, cantidad'
    #             jugada = input()
    #             jugada_columna = int(jugada[0])
    #             jugada_cantidad = int(jugada[1])
    #
    #             # falta validacion jugada invalida
    #
    #             estado_actual.estado[jugada_columna - 1] = jugada_cantidad
    #
    #             print estado_actual.estado
    #
    #             estado_actual.estado = logica.jugar(estado_actual)
    #
    #             print estado_actual.estado
    #
    # print 'Chao'


if __name__ == '__main__':
    main()
