import random


while True:
    print("*** Jogo de adivinhar o número secreto")
    print("Digite um número entre 1-10 para começar a jogar.")
    num_aleatorio = random.randint(1,10)
    tentativas = 0
    num_jogador = 0

    while num_jogador != num_aleatorio:
        num_jogador = int(input("Seu número aqui: "))

        if num_jogador < num_aleatorio:
            print(f"Você quase acertou.. Uma dica: o número secreto é maior que {num_jogador}")
            tentativas = tentativas + 1
        elif num_jogador > num_aleatorio:
             print(f"Você quase acertou.. Uma dica: o número secreto é menor que {num_jogador}")
             tentativas = tentativas + 1
        


    print("Você terminou a partida, gostaria de jogar novamente? ")
    Nova_partida = input("Digite S para contnuar ou N para sair do jogo: ")

