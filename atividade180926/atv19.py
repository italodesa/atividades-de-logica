# Escreva um programa que lê um número e calcula e escreve quantos divisores ele possui.
n = int(input("Digite um numero:"))
quantidade_de_divisores = 0
for i in range(1,n+1):
    if n % i == 0:
        quantidade_de_divisores += 1

print(quantidade_de_divisores)