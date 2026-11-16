"""Exercici 20: Invertir una cadena.
Solució comentada en Python 3.
"""

def invertir(text):
    """Retorna la cadena escrita al revés."""
    return text[::-1]

if __name__ == "__main__":
    print(invertir(input("Text: ")))
