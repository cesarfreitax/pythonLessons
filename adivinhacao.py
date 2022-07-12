import random

def jogar():

    print("**********************************************")
    print("Bem vinda ou bem vindo ao jogo de adivinhacao!")
    print("**********************************************")

    numero_secreto = random.randrange(1, 11)
    tentativa = 1
    numero_de_tentativas = 0
    dificuldade = 0
    pontos = 1000

    while(dificuldade != 1 and dificuldade != 2 and dificuldade != 3):

        print("(1)Fácil | (2)Médio | (3)Difícil")
        dificuldade = int(input("Defina a dificuldade:"))

        if(dificuldade == 1):
            numero_de_tentativas = 10
            print("Modo fácil ativado! Vamos lá...")
        elif(dificuldade == 2):
            numero_de_tentativas = 5
            print("Modo médio ativado! Vamos lá...")
        elif(dificuldade == 3):
            numero_de_tentativas = 3
            print("Modo difícil ativado! Vamos lá...")
        else:
            print("Digite um nível de dificuldade de 1 até 3!!!")

        print("**********************************************")

        for tentativa in range(1, numero_de_tentativas +1):
            print("Tentativa {} de {}".format(tentativa, numero_de_tentativas))
            chute = int(input("Digite o seu número entre 1 a 10: "))
            acertou = numero_secreto == chute
            maior   = numero_secreto > chute
            menor   = numero_secreto < chute

            if(chute > 10 or chute < 1):
                print("Vc precisa digitar um número entre 1 a 10!!! Tente de novo.")
                continue

            print("Voce digitou o numero", chute, ".")

            if(acertou):
                print("Vc acertou!")
                print("A sua pontuacao foi de {} pontos!!!".format(pontos))
                break
            else:
                if(maior):
                    print("O numero é maior, tente novamente.")
                    pontuacao_perdida = abs(numero_secreto - chute)
                    pontos = pontos - pontuacao_perdida
                elif(menor):
                    print("O numero é menor, tente novamente.")
                    pontuacao_perdida = abs(numero_secreto - chute)
                    pontos = pontos - pontuacao_perdida

            print("**********************************************")

if(__name__ == "__main__"):
    jogar()