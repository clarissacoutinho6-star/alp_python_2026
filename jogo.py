import random

while True:

    print("=== JOGO DE ADIVINHAÇÃO ===")
    print("1 - Fácil (1 a 10)")
    print("2 - Médio (1 a 20)")
    print("3 - Difícil (1 a 30)")

    nivel = int(input("Escolha o nível: "))

    if nivel == 1:
        numero = random.randint(1, 10)
    elif nivel == 2:
        numero = random.randint(1, 20)
    else:
        numero = random.randint(1, 30)

    acertou = False

    for tentativa in range(1, 4):

        chute = int(input("Digite um número: "))

        if chute == numero:
            print("Parabéns, você acertou!")
            acertou = True
            break

        else:
            print("Você errou!")

            if chute > numero:
                print("Tente um número menor")
            else:
                print("Tente um número maior")

    if acertou == False:
        print("Você perdeu! Fim de jogo.")
        print("O número sorteado era:", numero)

    jogar = input("Quer jogar novamente? (s/n): ")

    if jogar != "s":
        print("Fim de jogo!")
        break
