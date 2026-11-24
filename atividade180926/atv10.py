# 10) Escreva um programa que leia uma sequência de números inteiros terminada por 0 e imprima
# na tela o maior e o menor número lido. Obs: o valor 0 é somente um terminador e não deve
# ser considerado nos cálculos

maior_numero = 0
menor_numero = 0
loop = 0
while True:
    print("Digite 0 para sair")
    n = int(input("Digite um numero: "))
    if (n == 0):
        break
    if (loop == 0):
        menor_numero = n
        maior_numero = n
        loop = 1

    if (n > maior_numero):
        maior_numero = n

    if (n < menor_numero):
        menor_numero = n

print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")