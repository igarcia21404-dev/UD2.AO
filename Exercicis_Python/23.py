"""Exercici 23: Crear caràcters repetits.
Solució comentada en Python 3.
"""

def crear_repetits(nombre, caracter):
    """Repeteix un caràcter un nombre determinat de vegades."""
    if nombre < 0 or len(caracter) != 1:
        raise ValueError("Cal un nombre positiu i un únic caràcter")
    return caracter * nombre

if __name__ == "__main__":
    print(crear_repetits(5, "a"))
