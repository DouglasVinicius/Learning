import sys
sys.path.insert(0, '..')

from dominio import Usuario, Leilao
from excecoes import LanceInvalido
import pytest

@pytest.fixture
def usuario():
    return Usuario("Vinicius", 100.0)

@pytest.fixture
def leilao():
    return Leilao("Fones de ouvidos")

def test_verifica_se_subtrai_valor_do_lance_do_usuario(usuario, leilao):
    
    usuario.propoem_lance(leilao, 50.0)
    assert usuario.carteira == 50.0

def test_permite_lance_quando_ha_saldo_suficiente_na_carteira(usuario, leilao):
    
    usuario.propoem_lance(leilao, 5.0)
    assert usuario.carteira == 95.0

def test_nao_permite_lance_quando_eh_maior_que_o_valor_da_carteira(usuario, leilao):

    with pytest.raises(LanceInvalido):
        usuario.propoem_lance(leilao, 150.0)