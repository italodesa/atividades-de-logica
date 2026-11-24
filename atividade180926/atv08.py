# 8) Escreva um programa que receba vários números, calcule e mostre:
# a) a soma dos números digitados;
# b) a quantidade de números digitado;
# c) a média dos números digitados;
# d) o maior número digitado;
# e) o menor número digitado;
# f) a média dos números pares

sum = 0
quantidade_de_numeros = 0
maior_numero = 0
menor_numero = 1
sum_pares = 0
quantidade_de_pares = 0
while True:
    print("Digite -1 para sair")
    n = int(input("Digite um número:"))

    if (n == -1):
        break

    #Pegar todos os numeros
    quantidade_de_numeros += 1
    sum += n

    #Pegar os pares
    if (n % 2 == 0):
        quantidade_de_pares += 1
        sum_pares += n

    #Pega o maior numero
    if (n > maior_numero):
        maior_numero = n

    #Pega o menor numero
    if(n < menor_numero):
        menor_numero = n

media_total = sum / quantidade_de_numeros
media_pares = sum_pares / quantidade_de_pares

print(f"a) a soma dos números digitados: {sum}")
print(f"b) a quantidade de números digitado: {quantidade_de_numeros}")
print(f"c) a média dos números digitados: {media_total}")
print(f"d) o maior número digitado: {maior_numero}")
print(f"e) o menor número digitado: {menor_numero}")
print(f"f) a média dos números pares: {media_pares}")
