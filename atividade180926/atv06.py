# 6) Produza duas versões de um programa que escreva n ≥ 0 asteriscos em uma linha sendo o
# valor n fornecido pelo usuário. A primeira versão deve utilizar o comando for e a segunda o
# comando while. Compare as duas versões

n = int(input("Digite uma quantidade N de asteriscos: "))
count = 0
# Usando for
print("Usando o for:")
for i in range(n):
    print("*",end=" ")

print()
print("-" * 25)

# Usando while
print("Usando o while")
while count < n:
    print("*",end=" ")
    count += 1