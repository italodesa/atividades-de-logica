# 34) Elaborar um programa que leia do teclado uma altura 
# (h > 2) em número de linhas e desenhe um "x" como 
# nos exemplos ao lado.

#   x  x   1
#    xx    2
#    xx    3
#   x  x   4


h = int(input("Digite uma altura (h > 2): "))
e = 0
d = h // 2

for i in range(h):
    print((" " * e) + "X",end="")
    print((" " * d) + "X" + (" " * d))

    d -= 1
    e += 1

print("------------------Solução do chat gpt-------------------------------")

for i in range(h):
    esquerda = i
    direita = h - 1 - i

    for j in range(h):
        if j == esquerda or j == direita:
            print("X", end="")
        else:
            print(" ", end="")

    print()