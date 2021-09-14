import random

class Forca:
    def __init__(self):
        self.enforcou = False
        self.acertou = False
        self.palavra_descoberta = False
        self.erros = 0
        self.quantidade_de_tentativas = 0
        self.letras_anteriores = []

    def escolhe_palavra(self):
        with open("palavras_forca.txt", "r") as arquivo:
            opcoes_palavras = arquivo.readlines()
        palavra_sorteada = random.randrange(0, len(opcoes_palavras))

        return opcoes_palavras[palavra_sorteada].lower().strip()

    def escolhe_dificuldade(self):
        while(True):
            try:
                print("Antes de iniciarmos, qual dificuldade você deseja para o jogo?")
                print("(1) Muito fácil  (2) Fácil  (3) Médio  (4) Difícil  (5) Impossível")
                index_dificuldade = int(input("Digite sua escolha: "))
                dificuldades = (12, 9, 6, 4, 2)

                if(index_dificuldade >= 1 and index_dificuldade <= 5):
                    self.quantidade_de_tentativas = dificuldades[index_dificuldade-1]
                else:
                    print("Escolha incorreta, por favor digite uma opção válida!")
                    continue
                break
            except:
                print("Escolha incorreta, por favor digite uma opção válida!")

    def verifica_imprime_repeticoes(self, letra_usuario):
        letra_repetida = False
        print("Tentativas anteriores:", end=" [")
        for anteriores in self.letras_anteriores:
            if(anteriores == letra_usuario):
                letra_repetida = True           
            print(anteriores, end=", ")
        print("]")

        if(letra_repetida):
            print("\nEssa letra já foi escolhida, por favor tente escolher novas letras!", "Lembre-se que letras maiúsculas e minúsculas são interpretadas da mesma forma!", sep="\n", end="\n\n")

    def informa_jogador(self, palavra):
        letras_faltando = palavra.count('_')

        print("Palavra secreta até o momento: ")
        for i in palavra:
            print(i, end=' ')
        print("\nVocê acertou {} de {} letras da palavra secreta e errou {} de {} vezes!".format(len(palavra)-letras_faltando, len(palavra), self.erros, self.quantidade_de_tentativas))

    def coleta_entrada(self):
        return input("\n\nDigite sua letra de A a Z (não há distinção entre letras minúsculas e maiúsculas), ou '0' para sair: ").lower().replace(" ", "")

    def verifica_saida(self, letra_usuario):
        try:
            sair = (int(letra_usuario) == 0)
        except:
            sair = False

        return sair

    def main_loop(self, palavra_adivinhar, palavra_na_tela):
        while((not self.enforcou) and (not self.palavra_descoberta)):
            try:
                self.informa_jogador(palavra_na_tela)
                letra_usuario = self.coleta_entrada()

                sair = self.verifica_saida(letra_usuario)
                self.verifica_imprime_repeticoes(letra_usuario)

                if(sair):
                    print("A palavra secreta era a '{}'.".format(palavra_adivinhar),"Obrigado por jogar, mais sorte da próxima vez!")
                    return
                else:
                    if(ord(letra_usuario) < 97 or ord(letra_usuario) > 122):
                        print("Valor inválido, por favor digite uma letra de A a Z, ou '0'!", end="\n\n")
                        continue

                for index in range (0, len(palavra_adivinhar)):
                    if(palavra_adivinhar[index] == letra_usuario):
                        palavra_na_tela[index] = letra_usuario
                        self.acertou = True       

                if(self.acertou):
                    print("\nParabéns, a letra escolhida está contida na palavra!")
                    self.palavra_descoberta = "_" not in palavra_na_tela
                else:
                    self.erros += 1
                    print("Que pena, a letra escolhida não está contida na palavra secreta!", "Tente denovo", sep="\n")

                self.enforcou = self.erros == self.quantidade_de_tentativas
                self.acertou = False
                self.letras_anteriores.append(letra_usuario)
            except:
                print("Valor inválido, por favor digite uma letra de A a Z, ou '0'!", end="\n\n")

    def resultado(self, palavra_adivinhar):
        if(self.enforcou):
            print("\nSuas tentativas terminaram e o personagem foi enforcado!", "A palavra secreta era a '{}'.".format(palavra_adivinhar),"Obrigado por jogar, mais sorte da próxima vez!", sep="\n")
        else:
            print("Parabéns, você adivinhou toda a palavra e conseguiu ganhar o jogo!")

    def jogar(self):
        print("***********************************************")
        print("**********Bem vindo ao jogo de Forca!**********")
        print("***********************************************", end="\n\n")

        palavra_adivinhar = self.escolhe_palavra()
        palavra_na_tela = ["_" for letra in palavra_adivinhar]
        self.__init__()

        self.escolhe_dificuldade()
        self.main_loop(palavra_adivinhar, palavra_na_tela)
        self.resultado(palavra_adivinhar)