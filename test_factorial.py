"""Pruebas unitarias para la función factorial."""
import pytest
from practica_factorial.factorial import factorial

def test_factorial_cero():
    """El factorial de 0 debe ser 1."""
    assert factorial(0) == 1

def test_factorial_positivo():
    """El factorial de 5 debe ser 120."""
    assert factorial(5) == 120

def test_factorial_error_negativo():
    """Debe lanzar ValueError con números negativos."""
    with pytest.raises(ValueError):
        factorial(-1)