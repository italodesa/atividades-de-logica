# 4) Escreva um programa que lê uma string S e inteiros não-negativos I e J e imprima o segmento 
# S[I..J]. Não use slice (fatiamento).

s = input("Escreva um texto: ")
i = int(input("Começo: "))
j = int(input("Fim(inclusive): "))

while i <= j:
    print(s[i],end="")
    i += 1