import random

nomes = []

quantidade = int(input("Quantas pessoas compraram a rifa? "))

for i in range(quantidade):
    nome = input("Digite o nome: ")
    nomes = nomes + [nome]

sorteio = random.randint(0, quantidade - 1)

print("O ganhador foi:", nomes[sorteio])
