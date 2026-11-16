"""Exercici 29: Comptar majúscules.
Solució comentada en Python 3.
"""

def comptar_majuscules(text):
    return sum(1 for caracter in text if caracter.isupper())

if __name__ == "__main__":
    print(comptar_majuscules("Hola MÓN"))
