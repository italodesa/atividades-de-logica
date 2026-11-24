# Um número perfeito é um inteiro positivo tal que a soma dos seus divisores próprios é igual ao
# número. Por exemplo, 28 = 1 + 2 + 4 + 7 + 14 é um número perfeito. Se a soma dos divisores
# é menor que o número ele é deficiente. Se a soma é maior que o número ele é abundante.
# Faça um programa que leia um número inteiro positivo n e imprima uma mensagem indicando
# se o número é perfeito, deficiente ou abundante

n = int(input("informe um numero: "))
sum = 0

for i in range(1,n+1):
    if n % i == 0:
        sum += i

if sum == n:
    print("É um número perfeito")
elif sum < n:
    print("O número é deficiente")
else:
    print("O número é abudante")