import random

class Adivinhacao:
    def __init__(self):
        self.numero_adivinhar = random.randrange(1, 101)
        self.quantidade_de_tentativas_iniciais = 0
        self.numeros_anteriores = []
        self.rodada = 0
        self.restam_tentativas = True

    def escolhe_dificuldade(self):
        while(True):
            try:
                print("Antes de iniciarmos, qual dificuldade você deseja para o jogo?")
                print("(1) Muito fácil  (2) Fácil  (3) Médio  (4) Difícil  (5) Impossível")
                index_dificuldade = int(input("Digite sua escolha: "))
                dificuldades = (20, 15, 10, 6, 3)

                if(index_dificuldade >= 1 and index_dificuldade <= 5):
                    self.quantidade_de_tentativas_iniciais = dificuldades[index_dificuldade-1]
                else:
                    print("Escolha incorreta, por favor digite uma opção válida!")
                    continue
                break
            except:
                print("Escolha incorreta, por favor digite uma opção válida!")

    def verifica_imprime_repeticoes(self, numero_usuario):
        numero_repetido = False
        print("Tentativas anteriores:", end=" [")
        for i in self.numeros_anteriores:
            if(i == numero_usuario):
                numero_repetido = True
            print(i, end=", ")
        print("]")

        return numero_repetido

    def main_loop(self):
        while(self.restam_tentativas):
            try:
                self.rodada += 1
                self.restam_tentativas = (self.rodada < self.quantidade_de_tentativas_iniciais)
                print("---------------------------------------------------------------")
                print(f"Tentativa {self.rodada} de {self.quantidade_de_tentativas_iniciais}: ")

                numero_usuario = input("\nDigite seu número de 1 a 100, ou 'q' para sair: ")
                sair = (numero_usuario == 'q')
                
                if(not sair):
                    if(int(numero_usuario) < 1 or int(numero_usuario) > 100):
                        self.rodada -= 1
                        print("Valor inválido, por favor digite um valor de 1 a 100, ou 'q'!", end="\n\n")
                        continue

                numero_repetido = self.verifica_imprime_repeticoes(numero_usuario)

                if(numero_repetido):
                    self.rodada -= 1
                    print("\nEsse número já foi escolhido, por favor tente escolher novos número!", end="\n\n")
                else:
                    if(sair):
                        print("O número secreto era o {}.".format(self.numero_adivinhar), "\nObrigado por jogar, mais sorte da próxima vez!")
                        return
                    else:
                        acertou = (self.numero_adivinhar == int(numero_usuario))
                        maior = (self.numero_adivinhar < int(numero_usuario))
                        if(acertou):
                            self.rodada -= 1
                            pontuacao_final = float(((self.quantidade_de_tentativas_iniciais-self.rodada)*100)/self.quantidade_de_tentativas_iniciais)
                            str_pontuacao = "Sua pontuação final é: {:5.2f} de 100.00".format(pontuacao_final)
                            print("\nParabéns, você acertou o número!", str_pontuacao, sep="\n")
                            return 1
                        elif(self.restam_tentativas):
                            if(maior):
                                print("\nQue pena, você errou!", "\nDica: o número que você digitou é maior que o número secreto!!!", end="\n\n")
                            else:
                                print("\nQue pena, você errou!", "\nDica: o número que você digitou é menor que o número secreto!!!", end="\n\n")
                    self.numeros_anteriores.append(numero_usuario)
            except:
                self.rodada -= 1
                print("Valor inválido, por favor digite um valor de 1 a 100, ou 'q'!", end="\n\n")
        return 0

    def jogar(self):
        print("***********************************************")
        print("*******Bem vindo ao jogo de adivinhação!*******")
        print("***********************************************", end="\n\n")

        self.__init__()
        self.escolhe_dificuldade()
        resultado = self.main_loop()

        if(resultado == 0):
            print("\nSuas tentativas terminaram!", "O número secreto era o {}.".format(self.numero_adivinhar),"Obrigado por jogar, mais sorte da próxima vez!", sep="\n")