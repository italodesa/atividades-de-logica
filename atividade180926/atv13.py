# 13) Escreva um programa que lê um inteiro n, calcule e imprima o valor da seguinte soma: 
# Soma o numerador aumenta e o denominador diminui

n = int(input("Digite um número: "))
sum = 0
for i in range(0,n+1):
    sum += n/(i+1)
    n -= 1 
