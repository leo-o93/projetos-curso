import random

numero = random.randint(1, 100)
tentativas = 0

print("Adivinhe o número entre 1 e 100")

while True:
    palpite = int(input("Seu palpite: "))
    tentativas += 1

    if palpite < numero:
        print("Muito baixo!")
    elif palpite > numero:
        print("Muito alto!")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
