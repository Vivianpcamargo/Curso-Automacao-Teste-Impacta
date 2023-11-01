def test_passar_valor_raio_devolver_valor_area(calculo):
    assert calculo.calcular_area() == 12.56


def test_passar_valor_altura_devolver_valor_volume(calculo):
    assert calculo.calcular_volume() == 37.68
