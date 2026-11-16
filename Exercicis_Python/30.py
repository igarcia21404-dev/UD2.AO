"""Exercici 30: Binari a enter.
Solució comentada en Python 3.
"""

def binari_a_enter(text):
    """Converteix una cadena binària a enter decimal."""
    if not text or any(c not in "01" for c in text):
        raise ValueError("Introdueix només 0 i 1")
    return int(text, 2)

if __name__ == "__main__":
    print(binari_a_enter(input("Número binari: ")))
