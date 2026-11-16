"""Exercici 21: Palíndrom.
Solució comentada en Python 3.
"""

def es_palindrom(paraula):
    """Comprova el palíndrom ignorant majúscules i espais."""
    neta = "".join(c.lower() for c in paraula if c.isalnum())
    return neta == neta[::-1]

if __name__ == "__main__":
    print(es_palindrom(input("Paraula o frase: ")))
