class Medida():
    def __init__(self, raio, altura):
        self.__raio = raio
        self.__altura = altura

    def get_raio(self) -> int:
        return self.__raio

    def get_altura(self) -> int:
        return self.__altura
