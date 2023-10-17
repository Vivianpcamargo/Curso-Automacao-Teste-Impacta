import pytest
from triangulo import triangulo


def teste_Triangulo_Escaleno():
    assert triangulo(2, 5, 4) == 'Triângulo Escaleno'


def teste_Triangulo_Isosceles():
    assert triangulo(4, 5, 4) == 'Triângulo Isósceles'


def teste_Triangulo_Equilatero():
    assert triangulo(4, 4, 4) == 'Triângulo Equilátero'


def teste_Triangulo_NaoTriangulo():
    assert triangulo(0, 4, 4) == 'Não é um triângulo'


def teste_Triangulo_TypeError():
    with pytest.raises(TypeError):
        triangulo(2, 5, '4')
