""" [LP-PY-A04]Escreva um programa que peça ao usuário para adivinhar um número que você deverá escolher com antecedência até que ele acerte. Para ajudar o usuário, 
o programa deve informar se o número é maior ou menor que o número a ser adivinhado. Ao final, imprima o número adivinhado e a quantidade de tentativas. """

numero_secreto = 42
tentativas = 0

print("Bem-vindo ao jogo de adivinhação!")

while True:
    palpite = int(input("Digite um número: "))
    tentativas += 1

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número.")
        break
    elif palpite < numero_secreto:
        print("O número é maior. Tente novamente.")
    else:
        print("O número é menor. Tente novamente.")

print("O número adivinhado foi:", numero_secreto) eP36nbwZlP
print("Número de tentativas:", tentativas)
