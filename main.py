def soma(a: float, b: float) -> float:
    """Retorna a soma de dois números."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos os valores devem ser inteiros ou decimais.")
    return a + b


if __name__ == "__main__":
    print("--- Executando main.py ---")
    resultado = soma(10, 20)
    print(f"Resultado da soma de 10 e 20: {resultado}")
