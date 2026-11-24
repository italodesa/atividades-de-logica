# 28) Em uma competição de ginástica olímpica a nota é determinada por um painel de seis juízes. 
# Cada um dos juízes atribui uma nota entre zero e dez para o desempenho do atleta. Para 
# calcular a nota final, a nota mais alta e a nota mais baixa são descartadas e é calculado a 
# média das quatro restantes. Escreva um programa que leia seis notas entre zero e dez e 
# calcule a média após o descarte da maior e da menor nota.

j1 = int(input("Digite a nota 1: "))

maior = j1
menor = j1

j2 = int(input("Digite a nota 2: "))

if (j2 > maior):
    maior = j2
elif (j2 < menor):
    menor = j2

j3 = int(input("Digite a nota 3: "))

if (j3 > maior):
    maior = j3
elif (j3 < menor):
    menor = j3

j4 = int(input("Digite a nota 4: "))

if (j4 > maior):
    maior = j4
elif (j4 < menor):
    menor = j4

j5 = int(input("Digite a nota 5: "))

if (j5 > maior):
    maior = j5
elif (j5 < menor):
    menor = j5

j6 = int(input("Digite a nota 6: "))

if (j6 > maior):
    maior = j6
elif (j6 < menor):
    menor = j6

media = ((j1 + j2 + j3 + j4 + j5 + j6) - maior - menor) / 4
print(f"Media: {media}")