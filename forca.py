alavra = "PYTHON"
palavra_oculta = ["_", "_", "_", "_", "_", "_"]
erros = 0

while erros < 6 and "_" in palavra_oculta:

    print("\n=== JOGO DE ADIVINHAÇÃO ===")
    print("Palavra:", " ".join(palavra_oculta))
    print("Erros:", erros)

    letra = input("Digite uma letra: ").upper()

    if letra in palavra:
        print("Você acertou!")

        for i in range(6):
            if palavra[i] == letra:
                palavra_oculta[i] = letra

    else:
        erros = erros + 1
        print("Você errou!")

    print("Palavra:", " ".join(palavra_oculta))


if "_" not in palavra_oculta:
    print("\nParabéns! Você venceu!")
else:
    print("\nVocê perdeu!")

print("A palavra era:", palavra)
