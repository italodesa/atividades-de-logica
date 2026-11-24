# 21) Escreva um programa que gere os números de 1000 a 1999 e exiba aqueles que divididos
# por 11 dão um resto igual a 5.

for i in range(1000,2000):
    if i % 11 == 5:
        print(i)