# 11) Escreva um programa que leia uma sequência de números inteiros terminada por 0. Ao final,
# o programa deve exibir: a) a quantidade de números digitada; b) o percentual de números
# positivos digitados e c) o percentual de números negativos digitados.

quantidade_de_numeros = 0
quantidade_positivo = 0
quantidade_negativo = 0

while True:
    print("Digite 0 para sair.")
    n = int(input("Digite um número(positivo ou negativo): "))

    if (n == 0):
        break

    quantidade_de_numeros += 1
    if (n > 0):
        quantidade_positivo += 1
    else:
        quantidade_negativo += 1

porcentual_positivo = (quantidade_positivo / quantidade_de_numeros) * 100
porcentual_negativo = (quantidade_negativo / quantidade_de_numeros) * 100

print(f"Quantidade de números digitados: {quantidade_de_numeros}")
print(f"Porcentual de números positivos: {porcentual_positivo:.2f}%")
print(f"Porcentual de números negativos: {porcentual_negativo:.2f}%")

