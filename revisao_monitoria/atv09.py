# 9. Solicite ao usuário um número inteiro e utilize uma estrutura for para apresentar sua tabuada de 1
# até 10.

def tabuada(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

n = int(input("Digite um número em que queira saber a tabuada"))
tabuada(n)