# Uma  progressão aritmética  é  uma  sequência  de  números  em  que cada  termo,  a  partir  do 
# segundo, é obtido multiplicando o termo anterior por um valor fixo. Em uma PG o primeiro 
# termo é o valor inicial da sequência, o número de termos é a quantidade de elementos que 
# compõem a sequência. Se a sequência for limitada, o número de termos é finito; se não tiver 
# fim, ela é infinita, e a razão é o valor constante pelo qual multiplicamos um termo para achar o 
# seguinte.  Descobrimos  a  razão  dividindo  qualquer  termo  (exceto  o  primeiro)  pelo  seu 
# antecessor. Escreva um programa que imprima os elementos de uma PG e o somatório da 
# mesma, dados o primeiro termo, o número de termos e a razão

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
quantidade_total = int(input("Digite a quantidade de termos: "))
i = 0
sum = 0

while i < quantidade_total:
    print(primeiro_termo)
    sum += primeiro_termo
    primeiro_termo *= razao
    i += 1
print(f"Somatorio: {sum}")

