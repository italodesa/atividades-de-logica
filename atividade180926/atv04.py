# 4) Escreva um programa que lê um inteiro N e imprime os N primeiros inteiros negativos.
n = int(input("informe um numero inteiro n, e imprimimos os primeiros n negativos:"))
for i in range(n, 0, -1):
    print(-i)