# Implementar la función es_palindromo(), que devuelva un booleano en base a
# si palabra se lee igual de corrido como al revés.


# Ejemplos: arenera, radar, ojo, oso, salas.
# Resolver sin utilizar loops (for/while), sino con slicing.
def generar_n_caracteres(n, char):
    return char * n

# Testing

def test_zero():
    assert generar_n_caracteres("h", 0) == ""

def test_one():
    assert generar_n_caracteres("h", 1) == "h"

def test_greater_than_one():
    assert generar_n_caracteres("h", 2) == "hh"