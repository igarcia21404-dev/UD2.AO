"""Exercici 12: Majoria d'edat.
Solució comentada en Python 3.
"""

def classificar_edat(edat):
    """Retorna si és menor, major o té exactament 18 anys."""
    if edat < 18:
        return "No és major d'edat"
    if edat == 18:
        return "Té exactament 18 anys"
    return "És major d'edat"

if __name__ == "__main__":
    edat = int(input("Edat: "))
    print(classificar_edat(edat))
# La funció també es pot importar des d'un altre programa amb:
# from exercici_12 import classificar_edat
