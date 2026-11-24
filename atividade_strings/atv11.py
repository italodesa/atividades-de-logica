# Escreva um programa que leia um valor real (float) e exiba-o na tela com milhares separados 
# por ponto ('.') e as casas decimais separadas por vírgula (','). Por exemplo, para o número 
# 8387932.701 o programa deve exibir "8.387.932,701".

n = float(input("Escreva um número float: "))
#8387932.701
n_resto = str(round(n % 1,3))[2:]
n_int = int(n)
n_str = str(n_int)
s = ""

i = len(n_str) - 1
j = 1
s = ""

while i >= 0:
    s = n_str[i] + s

    if j % 3 == 0 and i != 0:
        s = "." + s

    i -= 1
    j += 1

s = s + "," + n_resto
print(s)