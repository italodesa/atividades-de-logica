# 7) Escreva um programa que lê um número não determinados de valores n, todos inteiros e
# positivos, um de cada vez, e calcule e escreva a média aritmética dos valores lidos, a
# quantidade de valores pares, a quantidade de valores ímpares, a percentagem de valores
# pares e a percentagem de valores ímpares

quantidade_de_numeros = 0
quantidade_de_pares = 0
quantidade_de_impares = 0
sum = 0

while True:
    print("Digite -1 para sair")
    n = int(input("Digite um inteiro N:"))
    if (n == -1):
        break
    if (n % 2 == 0):
        quantidade_de_pares += 1
    else:
        quantidade_de_impares += 1

    quantidade_de_numeros += 1
    sum += n

media = sum / quantidade_de_numeros
porcentagem_pares = (quantidade_de_pares / quantidade_de_numeros) * 100
porcentagem_impares = (quantidade_de_impares / quantidade_de_numeros) * 100

print(f"media aritmetica: {media}")
print(f"quantidade de pares: {quantidade_de_pares}")
print(f"quantidade de impares: {quantidade_de_impares}")
print(f"porcentagem de valores pares: {porcentagem_pares}%")
print(f"porcentagem de valores ímpares: {porcentagem_impares}")

