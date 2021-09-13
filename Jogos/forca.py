def jogar():
    print("***********************************************")
    print("**********Bem vindo ao jogo de Forca!**********")
    print("***********************************************", end="\n\n")

    palavra_adivinhar = "palavra".lower()
    palavra_na_tela = []
    for i in range(0, len(palavra_adivinhar)):
        palavra_na_tela.append('_')

    enforcou = False
    acertou = False
    palavra_descoberta = False
    rodada = 0
    letras_anteriores = []

    while((not enforcou) and (not palavra_descoberta)):
        try:
            letra_repetida = False
            rodada += 1
            letras_faltando = palavra_na_tela.count('_')

            print("Palavra secreta até o momento: ")
            for i in palavra_na_tela:
                print(i, end=' ')
            print("\nVocê acertou {} de {} letras da palavra secreta!".format(len(palavra_na_tela)-letras_faltando, len(palavra_na_tela)))
            letra_usuario = input("\n\nDigite sua letra de A a Z (não há distinção entre letras minúsculas e maiúsculas), ou '0' para sair: ").lower().replace(" ", "")

            try:
                sair = (int(letra_usuario) == 0)
            except:
                sair = False

            if(not sair):
                if(ord(letra_usuario) < 97 or ord(letra_usuario) > 122):
                    rodada -= 1
                    print("Valor inválido, por favor digite uma letra de A a Z, ou '0'!", end="\n\n")
                    continue

            print("Tentativas anteriores:", end=" [")
            for anteriores in letras_anteriores:
                if(anteriores == letra_usuario):
                    letra_repetida = True           
                print(anteriores, end=", ")
            print("]")

            if(letra_repetida):
                rodada -= 1
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
                    for letra in palavra_na_tela:
                        if(letra != '_'):
                            palavra_descoberta = True
                        else:
                            palavra_descoberta = False
                            break
                else:
                    print("Que pena, a letra escolhida não está contida na palavra secreta!", "Tente denovo", sep="\n")


                acertou = False
                letras_anteriores.append(letra_usuario)
        except:
            rodada -= 1
            print("Valor inválido, por favor digite uma letra de A a Z, ou '0'!", end="\n\n")

    if(enforcou):
        print("\nSuas tentativas terminaram e o personagem foi enforcado!", "A palavra secreta era a '{}'.".format(palavra_adivinhar),"Obrigado por jogar, mais sorte da próxima vez!", sep="\n")
    else:
        print("Parabéns, você adivinhou toda a palavra e conseguiu ganhar o jogo!")

if(__name__ == "__main__"):
    jogar()