"""Exercici 26: Major d'una llista.
Solució comentada en Python 3.
"""

def gran_llista(numeros):
    if not numeros: raise ValueError("La llista no pot ser buida")
    major = numeros[0]
    for numero in numeros[1:]:
        if numero > major: major = numero
    return major

if __name__ == "__main__":
    print(gran_llista([3, 4, 2, 3, 10]))
