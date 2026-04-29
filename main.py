import random


while True:
    print("*** Jogo de adivinhar o número secreto")
    print("Digite um número entre 1-10 para começar a jogar.")
    num_jogador = int(input("Seu número aqui: "))
    num_aleatorio = random.randint(1,10)

    while num_jogador != num_aleatorio:
        pass 



    print("Você terminou a partida, gostaria de jogar novamente? ")
    Nova_partida = input("Digite S para contnuar ou N para sair do jogo: ")

