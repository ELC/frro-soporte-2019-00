# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


def mas_larga(xs):
    return sorted(xs, key=len, reverse=True)[0] if xs else []

# Testing

def test_empty():
    assert mas_larga([]) == []

def test_one_element_list():
    assert mas_larga(["hola"]) == "hola"

def test_several_element_list():
    assert mas_larga(["h", "hola", "esternocleidomastoideo", "adios"]) == "esternocleidomastoideo"