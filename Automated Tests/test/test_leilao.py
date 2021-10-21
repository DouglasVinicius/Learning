import sys
sys.path.insert(0, '..')

from unittest import TestCase
from dominio import Usuario, Lance, Leilao
from excecoes import LanceInvalido

class TestLeilao(TestCase):

    def setUp(self):
        self.usuario1 = Usuario("Gustavo", 5000.0)
        lance_usuario1 = Lance(self.usuario1, 1250.0)
        self.leilao = Leilao("Celular")
        self.leilao.propoem(lance_usuario1)

    def test_avalia_valor_unico(self):
        menor_esperado = 1250.0
        maior_esperado = 1250.0
        self.assertEqual([menor_esperado, maior_esperado], [self.leilao.menor_valor, self.leilao.maior_valor])

    def test_avalia_valores_em_ordem_crescente(self):
        usuario2 = Usuario("Rafael", 5000.0)
        lance_usuario2 = Lance(usuario2, 1500.0)
        self.leilao.propoem(lance_usuario2)

        menor_esperado = 1250.0
        maior_esperado = 1500.0
        self.assertEqual([menor_esperado, maior_esperado], [self.leilao.menor_valor, self.leilao.maior_valor])

    def test_nao_permite_inserir_valores_menores(self):
        with self.assertRaises(LanceInvalido):
            usuario2 = Usuario("Rafael", 5000.0)
            lance_usuario2 = Lance(usuario2, 850.0)
            self.leilao.propoem(lance_usuario2)

    def test_permite_inserir_valores_maiores(self):
        usuario2 = Usuario("Rafael", 5000.0)
        lance_usuario2 = Lance(usuario2, 1500.0)
        self.leilao.propoem(lance_usuario2)

        quantidade_de_lances_atuais = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances_atuais)

    def test_permitir_lance_caso_nao_haja_nenhum(self):    
        quantidade_de_lances_atuais = len(self.leilao.lances)

        self.assertEqual(1, quantidade_de_lances_atuais)

    def test_permitir_lance_caso_ultimo_usuario_seja_diferente(self):
        usuario2 = Usuario("Rafael", 5000.0)
        lance_usuario2 = Lance(usuario2, 1500.0)
        self.leilao.propoem(lance_usuario2)

        quantidade_de_lances_atuais = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances_atuais)

    def test_nao_permitir_lance_caso_ultimo_usuario_seja_igual(self):
        with self.assertRaises(LanceInvalido):
            lance2_usuario1 = Lance(self.usuario1, 1500.0)
            self.leilao.propoem(lance2_usuario1)