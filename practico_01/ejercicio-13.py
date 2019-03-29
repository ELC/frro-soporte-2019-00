def es_primo(m):
    if m <= 2:
        return True
    
    limit = int(m ** 0.5 + 1)

    return not any(m % i == 0 for i in range(3, limit, 2))

# Testing

def test_one():
    assert es_primo(1) is True

def test_prime():
    assert es_primo(17) is True

def test_non_prime():
    assert es_primo(18) is False