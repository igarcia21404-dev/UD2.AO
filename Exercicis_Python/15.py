"""Exercici 15: Major de dos números.
Solució comentada en Python 3.
"""

def gran(a, b):
    """Retorna el més gran dels dos números."""
    return a if a >= b else b

if __name__ == "__main__":
    print(gran(8, 3), gran(-2, 4), gran(5, 5))
