"""Exercici 14: Calculadora i bases.
Solució comentada en Python 3.
"""

def convertir(numero, base):
    """Converteix un enter decimal a la base indicada."""
    if base == 2: return bin(numero)
    if base == 8: return oct(numero)
    if base == 10: return str(numero)
    if base == 16: return hex(numero)
    raise ValueError("La base ha de ser 2, 8, 10 o 16")

if __name__ == "__main__":
    numero = int(input("Enter decimal: "))
    base = int(input("Base de sortida (2, 8, 10, 16): "))
    print(convertir(numero, base))
