"""
Your module description
"""
from funciones import sumar
from funciones import esPrimo

def test_sumar():
    assert sumar(2, 4) == 6
    assert sumar(-2, 2) == 0
    assert sumar(2, 2) == 4

def test_esPrimo():
    assert esPrimo(8) is False
    assert esPrimo(7) is True
    