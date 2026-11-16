"""Exercici 18: Vocal.
Solució comentada en Python 3.
"""

def es_vocal(caracter):
    """Indica si el caràcter és una vocal."""
    return len(caracter) == 1 and caracter.lower() in "aeiouàèéíïòóúü"

if __name__ == "__main__":
    lletra = input("Introdueix un caràcter: ")
    print(es_vocal(lletra))
