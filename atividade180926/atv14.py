# 14) Escreva um programa que lê um inteiro n, calcule e imprima o valor da seguinte soma:
# Soma alternada de 1 - 1/2 + 1/3 ... 1/n

n = int(input("Digite um número: "))
sum = 0
count = 1
for i in range(1,n+1):
    if i % 2 == 0:
        sum -= 1/i
        continue
    sum += 1/i

print(sum)