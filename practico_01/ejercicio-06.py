# Implementar la función multiplicar() que devuelva el producto de todos los números de una lista.


def inversa(string):
    return string[::-1]

# Testing

# Classical

def test_one_character():
    assert inversa("a") == "a"

def test_even_characters():
    assert inversa("ho") == "oh"

def test_odd_characters():
    assert inversa("hol") == "loh"

# Property Testing

from hypothesis import given
import hypothesis.strategies as st

@given(st.text())
def test_identity(text):
    assert inversa(inversa(text)) == text
