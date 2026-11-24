# 12) Escreva um programa que lê um  inteiro n, calcule e imprima o valor da seguinte soma:
# 1 + 1/1 + 1/2 ... 1/N

n = int(input("Digite um número N: "))
sum = 1

for i in range(2,n+1):
    sum += 1/i

print(sum)