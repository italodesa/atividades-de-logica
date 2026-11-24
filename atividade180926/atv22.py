# 22) Escreva um programa que lê um número não determinado de valores para m, todos inteiros e
# positivos, um de cada vez. Se m for par, verificar quantos divisores possui e escrever esta
# informação. Se m for ímpar e menor do que 12 calcular e escrever o fatorial de m. Se m for
# ímpar e maior ou igual a 12 calcular e escrever a soma dos inteiros de 1 até m

while True:
    print("digite -1 para sair")
    m = int(input("Digite um numero: "))
    if m == -1:
        break

    if m % 2 == 0:
        qntd_div = 0
        for i in range(1,m//2+1):
            if m % i == 0:
                qntd_div += 1
        print(f"quantidade de divisores: {qntd_div}")

    elif  m < 12:
        fat = 1
        for i in range(1,m+1):
            fat *= i
        print(f"fatorial de {m} é {fat}")

    else:
        sum = 0
        for i in range(1,m+1):
            sum += i
        print(f"Somatorio dos inteiros: {sum}")
    