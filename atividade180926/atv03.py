# 3) Escreva um programa que lê um inteiro N e imprime a soma dos N primeiros números inteiros
n = int(input("Digite o ultimo numero de um intervalo e mostraremos a soma: "))
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)