"""Exercici 28: Filtrar paraules.
Solució comentada en Python 3.
"""

def filtrar_paraules(paraules, x):
    """Retorna les paraules amb més de x caràcters."""
    return [p for p in paraules if len(p) > x]

if __name__ == "__main__":
    print(filtrar_paraules(["sol", "casa", "ordinador"], 3))
