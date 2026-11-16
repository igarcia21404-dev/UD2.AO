"""Exercici 22: Superposició de llistes.
Solució comentada en Python 3.
"""

def superposicio(llista1, llista2):
    """Retorna True si les llistes comparteixen algun element."""
    return any(element in llista2 for element in llista1)

if __name__ == "__main__":
    print(superposicio([1, 2, 3], [5, 3, 8]))
