import random

def jogar():
    print("***********************************************")
    print("**********Bem vindo ao jogo de Forca!**********")
    print("***********************************************", end="\n\n")

    with open("palavras_forca.txt", "r") as arquivo:
        opcoes_palavras = arquivo.readlines()
    palavra_sorteada = random.randrange(0, len(opcoes_palavras))

    palavra_adivinhar = opcoes_palavras[palavra_sorteada].lower().strip()
    palavra_na_tela = ["_" for letra in palavra_adivinhar]

    enforcou = False
    acertou = False
    palavra_descoberta = False
    erros = 0
    quantidade_de_tentativas = 0
    letras_anteriores = []

    while(True):
        try:
            print("Antes de iniciarmos, qual dificuldade você deseja para o jogo?")
            print("(1) Muito fácil  (2) Fácil  (3) Médio  (4) Difícil  (5) Impossível")
            index_dificuldade = int(input("Digite sua escolha: "))
            dificuldades = (12, 9, 6, 4, 2)

            if(index_dificuldade >= 1 and index_dificuldade <= 5):
                quantidade_de_tentativas = dificuldades[index_dificuldade-1]
            else:
                print("Escolha incorreta, por favor digite uma opção válida!")
                continue
            break
        except:
            print("Escolha incorreta, por favor digite uma opção válida!")

    while((not enforcou) and (not palavra_descoberta)):
        try:
            letra_repetida = False
            letras_faltando = palavra_na_tela.count('_')

            print("Palavra secreta até o momento: ")
            for i in palavra_na_tela:
                print(i, end=' ')
            print("\nVocê acertou {} de {} letras da palavra secreta e errou {} de {} vezes!".format(len(palavra_na_tela)-letras_faltando, len(palavra_na_tela), erros, quantidade_de_tentativas))

            letra_usuario = input("\n\nDigite sua letra de A a Z (não há distinção entre letras minúsculas e maiúsculas), ou '0' para sair: ").lower().replace(" ", "")
            try:
                sair = (int(letra_usuario) == 0)
            except:
                sair = False

            if(not sair):
                if(ord(letra_usuario) < 97 or ord(letra_usuario) > 122):
                    print("Valor inválido, por favor digite uma letra de A a Z, ou '0'!", end="\n\n")
                    continue

            print("Tentativas anteriores:", end=" [")
            for anteriores in letras_anteriores:
                if(anteriores == letra_usuario):
                    letra_repetida = True           
                print(anteriores, end=", ")
            print("]")

            if(letra_repetida):
                print("\nEssa letra já foi escolhida, por favor tente escolher novas letras!", "Lembre-se que letras maiúsculas e minúsculas são interpretadas da mesma forma!", sep="\n", end="\n\n")
            else:
                if(sair):
                    print("A palavra secreta era a '{}'.".format(palavra_adivinhar),"Obrigado por jogar, mais sorte da próxima vez!")
                    return
                for index in range (0, len(palavra_adivinhar)):
                    if(palavra_adivinhar[index] == letra_usuario):
                        palavra_na_tela[index] = letra_usuario
                        acertou = True       

                if(acertou):
                    print("\nParabéns, a letra escolhida está contida na palavra!")
                    palavra_descoberta = "_" not in palavra_na_tela
                else:
                    erros += 1
                    print("Que pena, a letra escolhida não está contida na palavra secreta!", "Tente denovo", sep="\n")

                enforcou = erros == quantidade_de_tentativas
                acertou = False
                letras_anteriores.append(letra_usuario)
        except:
            print("Valor inválido, por favor digite uma letra de A a Z, ou '0'!", end="\n\n")

    if(enforcou):
        print("\nSuas tentativas terminaram e o personagem foi enforcado!", "A palavra secreta era a '{}'.".format(palavra_adivinhar),"Obrigado por jogar, mais sorte da próxima vez!", sep="\n")
    else:
        print("Parabéns, você adivinhou toda a palavra e conseguiu ganhar o jogo!")

if(__name__ == "__main__"):
    jogar()