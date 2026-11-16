"""Exercici 19: Suma i producte d'una llista.
Solució comentada en Python 3.
"""

def sumar_llista(valors):
    total = 0
    for valor in valors: total += valor
    return total

def multiplicar_llista(valors):
    producte = 1
    for valor in valors: producte *= valor
    return producte

if __name__ == "__main__":
    dades = [1, 2, 3, 4]
    print("Suma:", sumar_llista(dades))
    print("Producte:", multiplicar_llista(dades))
