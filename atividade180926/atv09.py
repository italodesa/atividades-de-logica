# 9) Escreva um programa que leia uma sequência de números inteiros terminada por 0 e imprima
# na tela a soma e a média aritmética destes números. Obs: o valor 0 é somente um terminador
# e não deve ser considerado nos cálculos

sum = 0
quantidade = 0

while True:
    print("Digite 0 para sair")
    n = int(input("Digite um número: "))
    if(n == 0):
        break
    sum += n
    quantidade += 1

media = sum / quantidade
print(f"Soma: {sum}")
print(f"Média aritmetica: {media}")