import adivinhacao
import forca

escolha = 0

print("**********************************************")
print("Olá! Seja bem vinda ou bem vindo.")
print("Escolha um jogo!")

while(escolha != 1 and escolha != 2):
    escolha = int(input("(1)Adivinhacao - (2)Forca\nEscolha:"))
    print("**********************************************")

    if(escolha == 1):
        adivinhacao.jogar()
    elif(escolha == 2):
        forca.jogar()
    else:
        print("Número incorreto! Por favor, selecione o numero do jogo corretamente.")

if(__name__ == "__main__"):
    jogar()