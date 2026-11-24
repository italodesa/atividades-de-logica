# 17) Escreva um programa que exiba a soma dos números múltiplos de 7 entre 100 e 200
sum = 0
for i in range(100,201):
    if i % 7 == 0:
        sum += i
print(sum)