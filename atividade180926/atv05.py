# 5) Escreva um programa que lê um inteiro N e uma sequência de N números inteiros, e imprime a
# soma dos números pares da sequência lida

n = int(input("Digite um inteiro N: "))
sum = 0

for i in range(1,n+1):
    if i % 2 == 0:
        sum += i

print(sum)