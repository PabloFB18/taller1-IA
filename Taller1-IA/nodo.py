class Nodo:
    """
    Nodo para el arbol del minimax y poda alfa-beta.
    """
    def __init__(self, estado, heuristica=0):
        """
        Constructor del nodo.
        :param estado: Estado de los palitos, representados por una lista.
        :param heuristica: Valor asociado a la posicion de los palitos
        """
        self.estado = estado
        self.heuristica = heuristica

    def estado_objetivo(self):
        """
        Define el estado objetivo.
        :return: Verdadero si es un estado objetivo y falso si no lo es.
        """
        if self.estado == [1, 0, 0] or self.estado == [0, 1, 0] or self.estado == [0, 0, 1]:
            return 1
        else:
            return 0

    def estado_final(self):
        """
        Verifica si es un estado en el que el juego termino.
        :return: Verdadero si el juego termino sino retorna falso.
        """
        if self.estado == [0, 0, 0]:
            return 1
        else:
            return 0
