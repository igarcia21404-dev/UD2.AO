"""Exercici 27: Paraula més llarga.
Solució comentada en Python 3.
"""

def paraula_mes_llarga(paraules):
    if not paraules: return ""
    return max(paraules, key=len)

if __name__ == "__main__":
    print(paraula_mes_llarga(["Hola", "Ramis", "IES", "Paraula"]))
