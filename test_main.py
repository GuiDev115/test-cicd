import pytest
from main import soma

# Teste 1: Valida resultados corretos da soma
def test_soma_valores_validos():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(2.5, 2.5) == 5.0

# Teste 2: Valida se lança TypeError ao receber tipos inválidos
def test_soma_tipo_invalido():
    with pytest.raises(TypeError):
        soma("texto", 5)
