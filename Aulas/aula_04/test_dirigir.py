from dirigir import dirigir


def teste_pode_dirigir():
    assert dirigir(18, 's') == 'Pode dirigir'


def teste_nao_pode_dirigir():
    assert dirigir(2, 's') == 'Não pode dirigir'


def teste_nao_pode_dirigir2():
    assert dirigir(25, 'n') == 'Não pode dirigir'
