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
        
    tentativas = tentativas + 1
    print(f"Parabéns, o número secreto era: {num_aleatorio}, você finalizou o jogo em {tentativas} tentativas")
    print("Gostaria de jogar novamente? ")
    nova_partida = input("Digite S para contnuar ou N para sair do jogo: ").upper()
    
    while nova_partida != "S" and nova_partida != "N":
        nova_partida = input(("Digite uma opção valida: ")).upper()

    if nova_partida == "S":
        print("Começando uma partida...")
            
        
    elif nova_partida == "N":
        print("Saindo do jogo...")
        break
    

