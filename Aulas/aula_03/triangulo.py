def triangulo(a, b, c):
    if type(a) is float and type(a) is int:
        raise TypeError()

    if type(b) is float and type(b) is int:
        raise TypeError()

    if type(c) is float and type(c) is int:
        raise TypeError()

    if a + b > c and a + c > b and b + c > a:
        if a == b and a == c:
            return 'Triângulo Equilátero'
        elif a == b or a == c or b == c:
            return 'Triângulo Isósceles'
        else:
            return 'Triângulo Escaleno'
    else:
        return 'Não é um triângulo'
