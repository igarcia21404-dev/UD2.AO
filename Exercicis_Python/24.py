"""Exercici 24: Crear punts.
Solució comentada en Python 3.
"""

def crear_punts(llista):
    """Mostra una línia de punts per cada valor de la llista."""
    for nombre in llista:
        print("." * max(0, nombre))

if __name__ == "__main__":
    crear_punts([2, 3, 4])
