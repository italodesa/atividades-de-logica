# 30) Escreva um programa que leia um número inteiro e apresenta sua representação no sistema 
# hexadecimal (base 16)
n =int(input("Digite um número: "))
hex = ""
while n > 0:
    res = n % 16
    if(res == 10):
        res = "A"
    elif(res == 11):
        res = "B"
    elif(res == 12):
        res = "C"
    elif(res == 13):
        res = "D"
    elif(res == 14):
        res = "E"
    elif(res == 15):
        res = "F"
    hex = str(res) + hex
    n //= 16

print(hex)