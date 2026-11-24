# 15) Um valor aproximado de cos(x) pode ser calculado pela série abaixo. Escreva um programa
# que lê um ângulo x e calcula seu cos(x) pela soma dos 100 primeiros termos da série abaixo.

def fatorial(n):
    fat = 1
    for i in range(n, 1, -1):
        fat *= i
    return fat
    

angulo = int(input("Digite um ângulo: "))

count = 2
sum = 1
for i in range(2,101,2):
    if count % 2 == 0:
        sum -= angulo**i / fatorial(i)
        count += 1
        continue

    sum += angulo**i / fatorial(i)
    count += 1

print(sum)