import adivinhacao
import forca

def menu_de_jogos():
    print("***********************************************")
    print("**********Bem vindo ao menu de jogos!**********")
    print("***********************************************", end="\n\n")
    
    jogar_novamente = 1
    while(True):
        if(jogar_novamente == 1):
            while(True):
                try:
                    print("Qual das opções abaixo você gostaria de jogar?")
                    print("(1) Adivinhação  (2) Forca  (q) Sair")
                    opcao = input("Digite sua escolha: ")

                    if(opcao == 'q'):
                        print("Até a próxima partida!")
                        break
                    elif(int(opcao) == 1):
                        adivinhacao.jogar()
                        break
                    elif(int(opcao) == 2):
                        forca.jogar()
                        break
                    else:
                        print("Valor inválido, digite novamente!")
                        continue
                except:
                    print("Valor inválido, digite novamente!")

        try:
            jogar_novamente = int(input("\nJogar novamente?\n   1 - Sim\n   2 - Não\n\nResposta: "))
            if(jogar_novamente == 2):
                print("Até a próxima partida!")
                break
            elif(jogar_novamente != 1):
                print("Valor inválido, digite novamente!")
        except:
            jogar_novamente = 0
            print("Valor inválido, digite novamente!")

if(__name__ == "__main__"):
    menu_de_jogos()