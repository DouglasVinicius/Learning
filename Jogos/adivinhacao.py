import random

def jogar():
    print("***********************************************")
    print("*******Bem vindo ao jogo de adivinhação!*******")
    print("***********************************************", end="\n\n")

    numero_adivinhar = random.randrange(1, 101)
    quantidade_de_tentativas_iniciais = 0
    numeros_anteriores = []
    rodada = 0
    restam_tentativas = True
    
    while(True):
        try:
            print("Antes de iniciarmos, qual dificuldade você deseja para o jogo?")
            print("(1) Muito fácil  (2) Fácil  (3) Médio  (4) Difícil  (5) Impossível")
            dificuldade = int(input("Digite sua escolha: "))

            if(dificuldade == 1):
                quantidade_de_tentativas_iniciais = 50
            elif(dificuldade == 2):
                quantidade_de_tentativas_iniciais = 30
            elif(dificuldade == 3):
                quantidade_de_tentativas_iniciais = 15
            elif(dificuldade == 4):
                quantidade_de_tentativas_iniciais = 8
            elif(dificuldade == 5):
                quantidade_de_tentativas_iniciais = 3
            else:
                print("Escolha incorreta, por favor digite uma opção válida!")
                continue
            break
        except:
            print("Escolha incorreta, por favor digite uma opção válida!")

    while(restam_tentativas):
        try:
            numero_repetido = False

            rodada += 1
            restam_tentativas = (rodada < quantidade_de_tentativas_iniciais)
            print("---------------------------------------------------------------")
            print(f"Tentativa {rodada} de {quantidade_de_tentativas_iniciais}: ")

            numero_usuario = input("\nDigite seu número de 1 a 100, ou 'q' para sair: ")
            sair = (numero_usuario == 'q')
            
            if(not sair):
                if(int(numero_usuario) < 1 or int(numero_usuario) > 100):
                    rodada -= 1
                    print("Valor inválido, por favor digite um valor de 1 a 100, ou 'q'!", end="\n\n")
                    continue

            print("Tentativas anteriores:", end=" [")
            for i in numeros_anteriores:
                if(i == numero_usuario):
                    numero_repetido = True
                print(i, end=", ")
            print("]")

            if(numero_repetido):
                rodada -= 1
                print("\nEsse número já foi escolhido, por favor tente escolher novos número!", end="\n\n")
            else:
                if(sair):
                    print("O número secreto era o {}.".format(numero_adivinhar), "\nObrigado por jogar, mais sorte da próxima vez!")
                    return
                else:
                    acertou = (numero_adivinhar == int(numero_usuario))
                    maior = (numero_adivinhar < int(numero_usuario))
                    if(acertou):
                        rodada -= 1
                        pontuacao_final = float(((quantidade_de_tentativas_iniciais-rodada)*100)/quantidade_de_tentativas_iniciais)
                        str_pontuacao = "Sua pontuação final é: {:5.2f} de 100.00".format(pontuacao_final)
                        print("\nParabéns, você acertou o número!", str_pontuacao, sep="\n")
                        return
                    elif(restam_tentativas):
                        if(maior):
                            print("\nQue pena, você errou!", "\nDica: o número que você digitou é maior que o número secreto!!!", end="\n\n")
                        else:
                            print("\nQue pena, você errou!", "\nDica: o número que você digitou é menor que o número secreto!!!", end="\n\n")
                numeros_anteriores.append(numero_usuario)
        except:
            rodada -= 1
            print("Valor inválido, por favor digite um valor de 1 a 100, ou 'q'!", end="\n\n")

    print("\nSuas tentativas terminaram!", "O número secreto era o {}.".format(numero_adivinhar),"Obrigado por jogar, mais sorte da próxima vez!", sep="\n")

if(__name__ == "__main__"):
    jogar()