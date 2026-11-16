"""Exercici 13: Calculadora.
Solució comentada en Python 3.
"""

def calcular(a, op, b):
    """Executa una operació aritmètica bàsica."""
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/":
        if b == 0: raise ZeroDivisionError("No es pot dividir per zero")
        return a / b
    if op == "//":
        if b == 0: raise ZeroDivisionError("No es pot dividir per zero")
        return a // b
    if op == "%":
        if b == 0: raise ZeroDivisionError("No es pot dividir per zero")
        return a % b
    if op == "**": return a ** b
    raise ValueError("Operador no vàlid")

if __name__ == "__main__":
    a = float(input("Primer número: "))
    op = input("Operació (+, -, *, /, //, %, **): ")
    b = float(input("Segon número: "))
    try: print("Resultat:", calcular(a, op, b))
    except (ValueError, ZeroDivisionError) as error: print("Error:", error)
