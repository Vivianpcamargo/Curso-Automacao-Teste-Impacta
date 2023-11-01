from pytest import fixture
from src.calcular_area import Calcular_area
from src.medidas import Medida


@fixture
def medida():
    return Medida(2, 3)


@fixture
def calculo():
    raio = Medida(2, 3)
    calculo = Calcular_area('area', raio)
    return calculo
