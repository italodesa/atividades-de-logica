# 25) Em uma progressão aritmética (PA), o primeiro termo é o valor inicial da sequência, a razão é 
# o valor constante somado a cada termo para formar o termo seguinte, e o número de termos 
# é a quantidade total de elementos. Escreva um programa que imprima os elementos de uma 
# PA e o somatório da mesma, dados o primeiro termo, o número de termos e a razão.

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
quantidade_total = int(input("Digite a quantidade de termos: "))
i = 0
sum = 0
while i < quantidade_total:
    print(primeiro_termo)
    sum += primeiro_termo
    primeiro_termo += razao
    i += 1
print(f"Somatorio: {sum}")