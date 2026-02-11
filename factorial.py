"""Módulo para calcular el factorial de un número."""

def factorial(n: int) -> int:
    """Calcula el factorial de un número entero no negativo."""
    if n < 0:
        raise ValueError("El número debe ser no negativo")
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado