# Implementar la función es_vocal, que reciba un carácter y
# devuelva un booleano en base a si letra es una vocal o no.


from functools import reduce

def multip(xs):
    return reduce(lambda x, y: x * y, xs, 1)

# Testing

# Classical

def test_non_empty_list():
    assert multip([1, 2, 3, 4, 5]) == 120


# Property Testing

from hypothesis import given, example
import hypothesis.strategies as st

@given(st.lists(st.integers()))
def test_power(l):
    assert multip(l + l) == multip(l) ** 2

@given(st.lists(st.integers()), st.integers(min_value=1, max_value=100))
def test_n_power(l, n):
    assert multip(l * n) == multip(l) ** n