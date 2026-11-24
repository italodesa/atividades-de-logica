# 18) Escreva um programa que exiba a soma dos números que não são múltiplos de 13 entre 100
# e 200.
sum = 0
for i in range(100,201):
    if i % 13 != 0:
        sum += i
print(sum)