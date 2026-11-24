# 29) Escreva um programa que leia um número inteiro e apresenta sua representação no sistema 
# binário (base 2)

n = int(input("digite um número: "))
value = n
bin = ""
while n > 0:
    bin = str(n % 2) + bin
    n = n // 2

print(f"{value} em bínario é: {"0b"+bin}")