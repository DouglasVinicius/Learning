from excecoes import LanceInvalido

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propoem_lance(self, leilao, valor):
        if(self.valor_eh_valido(valor)):
            lance = Lance(self.__nome, valor)
            leilao.propoem(lance)
            self.__carteira -= valor
        else:
            raise LanceInvalido("Saldo na carteira insuficiente para lance!")

    def valor_eh_valido(self, valor):
        return valor <= self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao: str):
        self.descricao = descricao
        self.__lances = []

    @property
    def lances(self):
        return self.__lances[:]

    def propoem(self, lance: Lance):
        if(self.lance_eh_valido(lance)):
            if(not self.tem_lances()):
                self.menor_valor = lance.valor
            self.maior_valor = lance.valor

            self.__lances.append(lance)

    def lance_eh_valido(self, lance):
        return (
            (not self.tem_lances()) or 
            (self.usuario_diferente_do_anterior(lance) and self.lance_maior_que_anterior(lance))
        )
        
    def tem_lances(self):
        return self.__lances

    def usuario_diferente_do_anterior(self, lance):
        if(self.__lances[-1].usuario != lance.usuario):
            return True
        raise LanceInvalido("O mesmo usuario nao pode dar dois lances seguidos!")

    def lance_maior_que_anterior(self, lance):
        if(self.__lances[-1].valor < lance.valor):
            return True
        raise LanceInvalido("Nao pode dar um lance menor que lances passados!")