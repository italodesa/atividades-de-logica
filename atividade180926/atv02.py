# 2) Escreva um programa que imprima os N primeiros números naturais ímpares
n = int(input("Digite o a quantidade de numeros impares em um intervalo: "))
#vai ate n*2 porque se ele digitar 5, deve devolver os 5 primeiros numeros ímpares
for i in range(1,n*2):
    if i % 2 != 0:
        print(i)