# 24) Um número inteiro é primo se ele tem exatamente dois divisores, um e ele mesmo. O número 
# um não é primo. O número dois é o único número par que é primo. Escreva um programa que 
# lê um número inteiro n e verifica se esse número inteiro é primo ou não.

n = int(input("Digite um número: "))
qnt_div = 0

for i in range(1,n+1):
    if n % i == 0:
        qnt_div += 1

    if qnt_div > 2:
        break

if n == 1:
    print("O número não é primo")
elif qnt_div > 2:
    print("O número não é primo")
else:
    print("O número é primo")